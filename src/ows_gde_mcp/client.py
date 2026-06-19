"""Async HTTP client for one OWS (tenant, surface) cell.

Wraps `httpx.AsyncClient` and injects the anti-tamper + CSRF headers built by
`auth.AuthContext`. One `OwsClient` per (tenant, surface) — auth is shared
across surfaces of the same tenant via a per-tenant `AuthContext` cache, since
a single CAS session covers both Studio and Runtime hosts of that tenant.
"""

from __future__ import annotations

import asyncio
import re
import time
from typing import Any
from urllib.parse import unquote, urlsplit

import httpx

from ows_gde_mcp.auth import AuthContext
from ows_gde_mcp.auth_login import (
    fetch_csrf_via_browser as _fetch_csrf_browser,
)
from ows_gde_mcp.auth_login import (
    login as _cas_login,
)
from ows_gde_mcp.auth_login_http import HttpLoginError
from ows_gde_mcp.auth_login_http import http_login as _http_login
from ows_gde_mcp.config import Settings, Surface, Tenant
from ows_gde_mcp.hosts import host_of


class OwsApiError(RuntimeError):
    """Raised when the OWS controller returns a structured error body."""

    def __init__(
        self,
        *,
        status: int,
        code: str | None,
        message: str | None,
        path: str | None,
        raw: Any,
    ) -> None:
        self.status = status
        self.code = code
        self.message = message
        self.path = path
        self.raw = raw
        super().__init__(f"OWS {status} {code or ''}: {message or raw} (path={path})")


class _NeedsRelogin(Exception):
    """Internal sentinel: OWS bounced us to CAS. Caller should re-auth and retry."""


# Per-process AuthContext cache, keyed by host (netloc). A CAS session cookie
# is bound to the host that issued it: testbed's studio + runtime share one
# host (one login covers both), while prod's studio and runtime are distinct
# hosts (each needs its own login). Lets refreshed cookies survive across tool
# calls (each call creates a new OwsClient) and be reused across surfaces that
# share a host. The cache lives only for the lifetime of this process —
# restarting the MCP (or reconnecting via /mcp) clears it and re-reads .env.
_auth_cache: dict[str, AuthContext] = {}

# Per-host relogin lock + last-relogin timestamp. Module-level so concurrent
# OwsClient instances (and concurrent callers from log_analysis.py) all
# serialise through one lock per host. Fixes the bug where 66 concurrent log
# probes each launched their own headless Chromium because the lock was
# per-client.
_relogin_locks: dict[str, asyncio.Lock] = {}
_last_relogin_at: dict[str, float] = {}


def _relogin_lock(host: str) -> asyncio.Lock:
    """Return the per-host relogin lock, creating it lazily."""
    lock = _relogin_locks.get(host)
    if lock is None:
        lock = asyncio.Lock()
        _relogin_locks[host] = lock
    return lock


async def refresh_host_session(base_url: str, tenant: Tenant, settings: Settings) -> None:
    """Authenticate `base_url`'s host via HTTP->Playwright->error, cache the result.

    Serialised + 5s-debounced per host. First step to yield a live session wins.
    """
    host = host_of(base_url)
    async with _relogin_lock(host):
        if time.monotonic() - _last_relogin_at.get(host, 0.0) < 5.0:
            return
        username, password = _creds_for(tenant, settings)
        if not username or not password:
            raise RuntimeError(
                f"No credentials to authenticate host '{host}'. Set "
                f"OWS_{tenant.value.upper()}_USERNAME and "
                f"OWS_{tenant.value.upper()}_PASSWORD in .env."
            )
        try:
            cookie, csrf = await _http_login(base_url, username, password)
        except HttpLoginError as http_err:
            try:
                cookie, csrf = await _cas_login(tenant, settings, base_url=base_url)
            except RuntimeError as pw_err:
                raise RuntimeError(
                    f"Auto-login failed for '{host}'. HTTP login: {http_err}. "
                    f"Playwright fallback: {pw_err}. Install Playwright with "
                    "`uv pip install -e '.[login]' && playwright install chromium`, "
                    f"or paste a cookie into OWS_{tenant.value.upper()}_SESSION_COOKIE."
                ) from pw_err
        auth = _auth_cache.get(host)
        if auth is None:
            auth = AuthContext(cookie=cookie, csrf_token=csrf)
            _auth_cache[host] = auth
        else:
            auth.cookie = cookie
            if csrf:
                auth.csrf_token = csrf
        # CSRF often comes only from the browser SPA (localStorage.csrfTokens).
        # If login gave us a cookie but no CSRF, capture it so non-GET calls
        # work. Best-effort: skip silently if playwright isn't installed —
        # GET-only workflows still function.
        if not auth.csrf_token:
            try:
                token, header = await _fetch_csrf_browser(base_url)
                auth.csrf_token = token
                auth.csrf_header = header
            except RuntimeError:
                pass
        _last_relogin_at[host] = time.monotonic()


def _creds_for(tenant: Tenant, settings: Settings) -> tuple[str | None, str | None]:
    if tenant == Tenant.TESTBED:
        return settings.OWS_TESTBED_USERNAME, settings.OWS_TESTBED_PASSWORD
    return settings.OWS_PROD_USERNAME, settings.OWS_PROD_PASSWORD


async def refresh_tenant_session(tenant: Tenant, settings: Settings) -> None:
    """Backward-compat: refresh the tenant's runtime host (first configured surface)."""
    surfaces = settings.configured_surfaces(tenant)
    if not surfaces:
        raise RuntimeError(f"No surface configured for tenant '{tenant.value}'.")
    await refresh_host_session(settings.base_url(tenant, surfaces[0]), tenant, settings)


# Path must start with exactly one '/', not '//' (protocol-relative), and must
# not contain a scheme separator. Accept the full set of unreserved + pchar +
# sub-delims + percent-encoded chars + '/' '?' '#' '&' '=' '%' so legitimate
# query strings & encoded chars pass.
_VALID_PATH_RE = re.compile(r"^/(?!/)[A-Za-z0-9\-._~!$&'()*+,;=:@/?#%]*$")


def _validate_path(path: str) -> None:
    """Reject absolute URLs, protocol-relative paths, and path-traversal segments.

    Raises:
        ValueError: with a message naming the offending input.
    """
    if not isinstance(path, str) or not path:
        raise ValueError(f"path must be a non-empty string starting with '/': {path!r}")
    if "://" in path:
        raise ValueError(
            f"path must be a relative path, not an absolute URL: {path!r}. "
            "Tools that proxy to OWS only accept paths under the configured tenant base URL."
        )
    if path.startswith("//"):
        raise ValueError(f"path must not start with '//' (protocol-relative): {path!r}")
    if not path.startswith("/"):
        raise ValueError(f"path must start with '/': {path!r}")
    if not _VALID_PATH_RE.match(path):
        raise ValueError(f"path contains illegal characters: {path!r}")
    # Reject `..` segments after one round of percent-decoding so encoded
    # variants like `/foo/%2e%2e/bar` are also caught.
    decoded = unquote(path)
    path_only = urlsplit(decoded).path
    for segment in path_only.split("/"):
        if segment == "..":
            raise ValueError(f"path traversal segment '..' is not allowed: {path!r}")


def _auth_for_host(base_url: str, tenant: Tenant, settings: Settings) -> AuthContext:
    """Return the cached AuthContext for a host, building one if missing.

    The cookie/CSRF live on the AuthContext; the URL the request gets sent to
    is decided by the OwsClient that wraps it. Seed values come from the
    per-tenant env vars (unchanged source), else a placeholder that the first
    302→CAS relogin replaces.
    """
    host = host_of(base_url)
    cached = _auth_cache.get(host)
    if cached is not None:
        return cached
    if tenant == Tenant.TESTBED:
        cookie = settings.OWS_TESTBED_SESSION_COOKIE
        csrf = settings.OWS_TESTBED_CSRF_TOKEN
        username = settings.OWS_TESTBED_USERNAME
    else:
        cookie = settings.OWS_PROD_SESSION_COOKIE
        csrf = settings.OWS_PROD_CSRF_TOKEN
        username = settings.OWS_PROD_USERNAME
    if not cookie:
        # No captured cookie. If creds are configured, start with a placeholder
        # AuthContext — the first request will 302 to CAS and auto-relogin
        # will populate real values. If no creds either, fail with a clear
        # message.
        if not username:
            raise RuntimeError(
                f"No session cookie configured for host '{host}' and no "
                f"OWS_{tenant.value.upper()}_USERNAME / _PASSWORD for auto-login. "
                f"See README.md."
            )
        cookie = "_placeholder_=1"
    auth = AuthContext(cookie=cookie, csrf_token=csrf)
    _auth_cache[host] = auth
    return auth


def _auth_for_tenant(tenant: Tenant, settings: Settings) -> AuthContext:
    """Backward-compat: AuthContext for the tenant's runtime host."""
    surfaces = settings.configured_surfaces(tenant)
    if not surfaces:
        raise RuntimeError(f"No surface configured for tenant '{tenant.value}'.")
    return _auth_for_host(settings.base_url(tenant, surfaces[0]), tenant, settings)


class OwsClient:
    """One client per (tenant, surface). Use as an async context manager.

    Example:
        async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, settings) as client:
            me = await client.get("/portal/web/rest/v1/user/my-info")
    """

    def __init__(
        self,
        base_url: str,
        auth: AuthContext,
        tenant: Tenant,
        surface: Surface,
        settings: Settings,
        *,
        timeout: float = 30.0,
    ) -> None:
        self._auth = auth
        self._tenant = tenant
        self._surface = surface
        self._settings = settings
        self._base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            follow_redirects=False,
        )

    @classmethod
    def for_surface(cls, tenant: Tenant, surface: Surface, settings: Settings) -> OwsClient:
        """Build a client targeting one (tenant, surface) cell.

        Raises:
            RuntimeError: if no URL is configured for that cell, or if the
                tenant has neither a session cookie nor login credentials.
        """
        base = settings.base_url(tenant, surface)
        auth = _auth_for_host(base, tenant, settings)
        return cls(base, auth, tenant, surface, settings)

    async def __aenter__(self) -> OwsClient:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.aclose()

    # ---------------- core methods ----------------

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        src_page: str | None = None,
        target_app: str | None = None,
        extra_headers: dict[str, str] | None = None,
        confirm: bool = False,
        read_only: bool = False,
        _already_retried: bool = False,
    ) -> Any:
        """Make one authenticated request. Returns parsed JSON on success.

        On 302→/dspcas/login, runs a single auto-relogin and retries once.

        Raises:
            ValueError: if `path` is not a safe relative path under the
                tenant base URL (absolute URLs, protocol-relative, or `..`
                traversal segments are rejected before any I/O).
            PermissionError / ValueError: if a non-GET request targets the
                prod tenant without `OWS_PROD_WRITE_ENABLED=1` and `confirm=True`.
            OwsApiError: when the controller responds with a structured
                error body (`{"error": {"code", "message", ...}}`).
            httpx.HTTPStatusError: for other HTTP failures.
            RuntimeError: if auto-relogin is needed but creds aren't
                configured, or if a second relogin is still rejected.
        """
        # Defence in depth: httpx.AsyncClient(base_url=...) silently honours
        # absolute URLs in `path`, which would let a caller redirect requests
        # (and the tenant session cookie) to an arbitrary host. Reject such
        # paths plus any `..` traversal before issuing the request.
        _validate_path(path)

        # Prod write-gate — enforced at the client layer so every tool that
        # routes through here is covered, not just `call_ows_api`.
        # `read_only=True` opts out for POST endpoints that the server
        # contract guarantees can't mutate (e.g. queryByTql).
        if method.upper() != "GET" and not read_only:
            self._settings.assert_prod_write_allowed(self._tenant, confirm=confirm)

        # CSRF bootstrap — POST/PUT/DELETE need `x-gde-csrf-token`. If the
        # tenant has no token yet (cold start, prod without
        # OWS_PROD_CSRF_TOKEN configured), run a proactive relogin to
        # capture one. The 302→/dspcas relogin path can't fire for POST
        # because `headers_for` raises before any HTTP I/O.
        if (
            method.upper() != "GET"
            and not self._auth.csrf_token
            and not _already_retried
        ):
            await self._refresh_session()

        headers = self._auth.headers_for(
            method,
            path,
            src_page=src_page,
            target_app=target_app,
            extra=extra_headers,
        )
        response = await self._client.request(
            method.upper(),
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        try:
            return self._handle_response(response, path)
        except _NeedsRelogin:
            if _already_retried:
                raise RuntimeError(
                    f"Auto-relogin for tenant '{self._tenant.value}' completed but the "
                    "next request was still redirected to CAS — credentials may be "
                    "wrong, the account may be locked, or the cookie was rejected."
                ) from None
            await self._refresh_session()
            return await self.request(
                method,
                path,
                params=params,
                json=json,
                data=data,
                src_page=src_page,
                target_app=target_app,
                extra_headers=extra_headers,
                confirm=confirm,
                read_only=read_only,
                _already_retried=True,
            )

    async def _refresh_session(self) -> None:
        """Delegate to the module-level `refresh_host_session`.

        Kept as a method for backward compatibility with existing tests
        that monkeypatch `_cas_login` and call this directly. The real
        deduplication lives in `refresh_host_session` so that callers
        outside the OwsClient request loop (e.g. `log_analysis._fetch_csrf`)
        share the same per-host lock.
        """
        await refresh_host_session(self._base_url, self._tenant, self._settings)

    async def get(self, path: str, **kwargs: Any) -> Any:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> Any:
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> Any:
        return await self.request("PUT", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> Any:
        return await self.request("DELETE", path, **kwargs)

    # ---------------- helpers ----------------

    @staticmethod
    def _handle_response(response: httpx.Response, path: str) -> Any:
        # CAS expired-session redirect: surface as an internal sentinel so
        # `request()` can decide whether to relogin and retry.
        if response.status_code in (301, 302, 303, 307, 308):
            location = response.headers.get("location", "") or response.headers.get("Location", "")
            if "/dspcas/login" in location.lower():
                raise _NeedsRelogin()

        ct = response.headers.get("content-type", "")
        if "json" in ct:
            try:
                body = response.json()
            except Exception:
                body = None
        else:
            body = None

        if 200 <= response.status_code < 300:
            return body if body is not None else response.text

        # OWS structured error
        if isinstance(body, dict) and isinstance(body.get("error"), dict):
            err = body["error"]
            raise OwsApiError(
                status=response.status_code,
                code=err.get("code"),
                message=err.get("message"),
                path=(err.get("args") or [path])[0] if err.get("args") else path,
                raw=body,
            )

        # Otherwise let httpx raise its standard error
        response.raise_for_status()
        return body


async def prewarm_session(tenant: Tenant, settings: Settings) -> str | None:
    """Force a fresh CAS login for `tenant` at startup, populating the auth cache.

    Authenticates every configured surface's host so that distinct hosts (e.g.
    prod's separate studio + runtime) each get a live session up front. Hosts
    shared across surfaces (testbed) are deduplicated by `refresh_host_session`'s
    per-host debounce.

    Returns a short status string for logging, or None if neither surface nor
    creds are configured (silent skip — startup must not fail when
    auto-relogin is optional). Never raises.
    """
    surfaces = settings.configured_surfaces(tenant)
    if not surfaces:
        return None
    warmed: list[str] = []
    errors: list[str] = []
    for surface in surfaces:
        try:
            await refresh_host_session(settings.base_url(tenant, surface), tenant, settings)
            warmed.append(surface.value)
        except RuntimeError as e:
            # Most likely: missing creds, or playwright not installed. Don't
            # break startup — the first tool call will surface the same error
            # with full context.
            errors.append(f"{surface.value}: {e}")
    if warmed and not errors:
        return f"prewarmed {tenant.value} ({', '.join(warmed)})"
    if not warmed:
        return f"prewarm skipped for {tenant.value}: {'; '.join(errors)}"
    return f"prewarmed {tenant.value} ({', '.join(warmed)}); skipped {'; '.join(errors)}"
