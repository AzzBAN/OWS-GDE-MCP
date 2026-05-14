"""Async HTTP client for one OWS tenant.

Wraps `httpx.AsyncClient` and injects the anti-tamper + CSRF headers built by
`auth.AuthContext`. One `OwsClient` per tenant (Production / Testbed).
"""

from __future__ import annotations

from typing import Any

import httpx

from ows_gde_mcp.auth import AuthContext
from ows_gde_mcp.config import Settings, Tenant


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


class OwsClient:
    """One client per tenant. Use as an async context manager.

    Example:
        async with OwsClient.for_tenant(Tenant.TESTBED, settings) as client:
            me = await client.get("/portal/web/rest/v1/user/my-info")
    """

    def __init__(self, base_url: str, auth: AuthContext, *, timeout: float = 30.0) -> None:
        self._auth = auth
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            follow_redirects=False,
        )

    @classmethod
    def for_tenant(cls, tenant: Tenant, settings: Settings) -> OwsClient:
        if tenant == Tenant.TESTBED:
            base = settings.studio_url(Tenant.TESTBED)
            cookie = settings.OWS_TESTBED_SESSION_COOKIE
            csrf = settings.OWS_TESTBED_CSRF_TOKEN
        else:
            base = settings.runtime_url(Tenant.PROD)
            cookie = settings.OWS_PROD_SESSION_COOKIE
            csrf = settings.OWS_PROD_CSRF_TOKEN
        if not cookie:
            raise RuntimeError(
                f"No session cookie configured for tenant '{tenant.value}'. "
                f"Set OWS_{tenant.value.upper()}_SESSION_COOKIE in .env. "
                "See README.md → Capturing the session cookie."
            )
        auth = AuthContext(cookie=cookie, csrf_token=csrf)
        return cls(base, auth)

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
    ) -> Any:
        """Make one authenticated request. Returns parsed JSON on success.

        Raises:
            OwsApiError: when the controller responds with a structured
                error body (`{"error": {"code", "message", ...}}`).
            httpx.HTTPStatusError: for other HTTP failures.
        """
        # Need the post-params URL to compute the page token, because the
        # token is over `path` only — but if `params` add to query string,
        # path stays the same.
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
        return self._handle_response(response, path)

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
