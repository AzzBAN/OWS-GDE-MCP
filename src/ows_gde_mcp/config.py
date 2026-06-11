"""Settings & tenant resolution.

OWS has two independent axes:

- **Tenant** — `prod` or `testbed`. Each tenant is a separate environment with
  its own user accounts, session cookies, and CAS server.
- **Surface** — `studio` (design-time authoring) or `runtime` (deployed apps
  for end users / preview / production traffic).

A given tenant can have either, both, or neither surface configured. On the
testbed used for discovery, the same host serves both surfaces; in production
the developer-facing Studio is typically unavailable so only `runtime` is set.

Auth values + base URLs live in env (or .env). See .env.example.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BeforeValidator, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def _empty_to_none(v: object) -> object:
    """Treat an empty string in .env as 'unset' (so HttpUrl validation skips it)."""
    if isinstance(v, str) and not v.strip():
        return None
    return v


OptionalUrl = Annotated[HttpUrl | None, BeforeValidator(_empty_to_none)]
OptionalStr = Annotated[str | None, BeforeValidator(_empty_to_none)]


class Tenant(StrEnum):
    PROD = "prod"
    TESTBED = "testbed"


class Surface(StrEnum):
    STUDIO = "studio"
    RUNTIME = "runtime"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # (tenant, surface) base URLs — set whichever apply, blanks raise on use.
    OWS_TESTBED_STUDIO_URL: OptionalUrl = None
    OWS_TESTBED_RUNTIME_URL: OptionalUrl = None
    OWS_PROD_STUDIO_URL: OptionalUrl = None
    OWS_PROD_RUNTIME_URL: OptionalUrl = None

    # Session cookies (raw `Cookie:` header value) captured from a logged-in
    # browser. One per tenant — the same CAS session works against both
    # surfaces of that tenant. Required for the MCP to make authenticated
    # requests.
    OWS_TESTBED_SESSION_COOKIE: OptionalStr = None
    OWS_PROD_SESSION_COOKIE: OptionalStr = None

    # CSRF tokens — `window.csrfToken` / `localStorage.csrfTokens[].csrfToken`
    # from a logged-in browser. Required for non-GET requests only. Per-tenant.
    OWS_TESTBED_CSRF_TOKEN: OptionalStr = None
    OWS_PROD_CSRF_TOKEN: OptionalStr = None

    # Credentials for auto-relogin when the captured session cookie expires.
    # Per-tenant. Optional: if unset, expired-session requests fail with a
    # clear error instead of being retried.
    OWS_TESTBED_USERNAME: OptionalStr = None
    OWS_TESTBED_PASSWORD: OptionalStr = None
    OWS_PROD_USERNAME: OptionalStr = None
    OWS_PROD_PASSWORD: OptionalStr = None

    # Production safety gate.
    OWS_PROD_WRITE_ENABLED: bool = False

    # Server transport.
    OWS_MCP_TRANSPORT: str = "stdio"  # "stdio" | "http"
    OWS_MCP_HTTP_PORT: int = 8765

    def base_url(self, tenant: Tenant, surface: Surface) -> str:
        """Resolve the base URL for one (tenant, surface) cell.

        No fallback between surfaces — if the requested surface isn't
        configured for the tenant, raise a clear error naming the env var
        the user needs to set.
        """
        match (tenant, surface):
            case (Tenant.TESTBED, Surface.STUDIO):
                url = self.OWS_TESTBED_STUDIO_URL
            case (Tenant.TESTBED, Surface.RUNTIME):
                url = self.OWS_TESTBED_RUNTIME_URL
            case (Tenant.PROD, Surface.STUDIO):
                url = self.OWS_PROD_STUDIO_URL
            case (Tenant.PROD, Surface.RUNTIME):
                url = self.OWS_PROD_RUNTIME_URL
            case _:  # pragma: no cover — exhaustive over the enums
                raise ValueError(f"unknown (tenant, surface): ({tenant!r}, {surface!r})")
        if not url:
            env_var = f"OWS_{tenant.value.upper()}_{surface.value.upper()}_URL"
            raise RuntimeError(
                f"No {surface.value} URL configured for tenant '{tenant.value}'. "
                f"Set {env_var} in .env. "
                "Note: the studio surface is design-time authoring; the runtime "
                "surface is deployed apps. They are independent — a tenant may "
                "have one, both, or neither."
            )
        return str(url).rstrip("/")

    def configured_surfaces(self, tenant: Tenant) -> list[Surface]:
        """Return the surfaces that have a URL configured for a tenant."""
        out: list[Surface] = []
        for s in (Surface.RUNTIME, Surface.STUDIO):
            try:
                self.base_url(tenant, s)
                out.append(s)
            except RuntimeError:
                pass
        return out

    def assert_prod_write_allowed(self, tenant: Tenant, *, confirm: bool) -> None:
        """Call from any tool that mutates state. Raises on prod misuse."""
        if tenant != Tenant.PROD:
            return
        if not self.OWS_PROD_WRITE_ENABLED:
            raise PermissionError(
                "Production writes are disabled. Set OWS_PROD_WRITE_ENABLED=1 in .env to allow."
            )
        if not confirm:
            raise ValueError(
                "Production mutation requires confirm=True. "
                "Re-issue the call with confirm=true once you're sure."
            )


settings = Settings()
