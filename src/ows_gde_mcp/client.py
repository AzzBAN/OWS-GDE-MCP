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
from ows_gde_mcp.auth_login import login as _cas_login
from ows_gde_mcp.config import Settings, Surface, Tenant


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


# Per-process AuthContext cache, keyed by tenant. Lets refreshed cookies
# survive across tool calls (each call creates a new OwsClient) and be reused
# across surfaces (one CAS session covers both Studio and Runtime of the same
# tenant). The cache lives only for the lifetime of this process — restarting
# the MCP (or reconnecting via /mcp) clears it and re-reads .env.
_auth_cache: dict[Tenant, AuthContext] = {}

# Per-tenant relogin lock + last-relogin timestamp. Module-level so concurrent
# OwsClient instances (and concurrent callers from log_analysis.py) all
# serialise through one lock. Fixes the bug where 66 concurrent log probes
# each launched their own headless Chromium because the lock was per-client.
_relogin_locks: dict[Tenant, asyncio.Lock] = {}
_last_relogin_at: dict[Tenant, float] = {}


def _relogin_lock(tenant: Tenant) -> asyncio.Lock:
    """Return the per-tenant relogin lock, creating it lazily."""
    lock = _relogin_locks.get(tenant)
    if lock is None:
        lock = asyncio.Lock()
        _relogin_locks[tenant] = lock
    return lock


async def refresh_tenant_session(tenant: Tenant, settings: Settings) -> None:
    """Run CAS login for `tenant` (serialised, deduplicated).

    Module-level entry point any code path can call (the OwsClient request
    loop, log_analysis.py, prewarm, etc.) and be guaranteed exactly one
    Playwright session ever runs concurrently. If another caller refreshed
    within the last 5 seconds, this is a no-op — the in-memory auth is
    already current.
    """
    async with _relogin_lock(tenant):
        if time.monotonic() - _last_relogin_at.get(tenant, 0.0) < 5.0:
            return
        cookie, csrf = await _cas_login(tenant, settings)
        auth = _auth_cache.get(tenant)
        if auth is None:
            # Should never happen — _auth_for_tenant was called before any
            # request that could 302. Defensive: build one in place.
            auth = AuthContext(cookie=cookie, csrf_token=csrf)
            _auth_cache[tenant] = auth
        else:
            auth.cookie = cookie
            auth.csrf_token = csrf
        _last_relogin_at[tenant] = time.monotonic()


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


def _auth_for_tenant(tenant: Tenant, settings: Settings) -> AuthContext:
    """Return the cached AuthContext for a tenant, building one if missing.

    The cookie/CSRF live on the AuthContext; the URL the request gets sent to
    is decided by the OwsClient that wraps it.
    """
    cached = _auth_cache.get(tenant)
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
                f"No session cookie configured for tenant '{tenant.value}' and no "
                f"OWS_{tenant.value.upper()}_USERNAME / _PASSWORD for auto-relogin. "
                f"Set OWS_{tenant.value.upper()}_SESSION_COOKIE in .env, or set "
                "credentials to enable auto-login. See README.md."
            )
        cookie = "_placeholder_=1"
    auth = AuthContext(cookie=cookie, csrf_token=csrf)
    _auth_cache[tenant] = auth
    return auth


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
        auth = _auth_for_tenant(tenant, settings)
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
        """Delegate to the module-level `refresh_tenant_session`.

        Kept as a method for backward compatibility with existing tests
        that monkeypatch `_cas_login` and call this directly. The real
        deduplication lives in `refresh_tenant_session` so that callers
        outside the OwsClient request loop (e.g. `log_analysis._fetch_csrf`)
        share the same lock.
        """
        await refresh_tenant_session(self._tenant, self._settings)

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

    Picks whichever surface is configured (runtime preferred — login server
    typically lives on the same host on both surfaces, and runtime is the
    surface that's most reliably present).

    Returns a short status string for logging, or None if neither surface nor
    creds are configured (silent skip — startup must not fail when
    auto-relogin is optional). Never raises.
    """
    surfaces = settings.configured_surfaces(tenant)
    if not surfaces:
        return None
    surface = surfaces[0]  # runtime preferred (configured_surfaces orders it first)
    try:
        client = OwsClient.for_surface(tenant, surface, settings)
    except RuntimeError:
        return None
    try:
        async with client:
            await client._refresh_session()
        return f"prewarmed {tenant.value} ({surface.value})"
    except RuntimeError as e:
        # Most likely: missing creds, or playwright not installed. Don't
        # break startup — the first tool call will surface the same error
        # with full context.
        return f"prewarm skipped for {tenant.value}: {e}"
