"""Settings & tenant resolution.

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


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Tenant base URLs — set whichever apply, blanks raise on use.
    OWS_TESTBED_STUDIO_URL: OptionalUrl = None
    OWS_PROD_STUDIO_URL: OptionalUrl = None
    OWS_TESTBED_RUNTIME_URL: OptionalUrl = None
    OWS_PROD_RUNTIME_URL: OptionalUrl = None

    # Session cookies (raw `Cookie:` header value) captured from a logged-in
    # browser. Required for the MCP to make authenticated requests.
    OWS_TESTBED_SESSION_COOKIE: OptionalStr = None
    OWS_PROD_SESSION_COOKIE: OptionalStr = None

    # CSRF tokens — `window.csrfToken` / `localStorage.csrfTokens[].csrfToken`
    # from a logged-in browser. Required for non-GET requests only.
    OWS_TESTBED_CSRF_TOKEN: OptionalStr = None
    OWS_PROD_CSRF_TOKEN: OptionalStr = None

    # Production safety gate.
    OWS_PROD_WRITE_ENABLED: bool = False

    # Server transport.
    OWS_MCP_TRANSPORT: str = "stdio"  # "stdio" | "http"
    OWS_MCP_HTTP_PORT: int = 8765

    def studio_url(self, tenant: Tenant) -> str:
        url = self.OWS_TESTBED_STUDIO_URL if tenant == Tenant.TESTBED else self.OWS_PROD_STUDIO_URL
        if not url:
            raise RuntimeError(
                f"No Studio URL configured for tenant '{tenant}'. "
                f"Set OWS_{tenant.upper()}_STUDIO_URL in .env."
            )
        return str(url).rstrip("/")

    def runtime_url(self, tenant: Tenant) -> str:
        url = (
            self.OWS_TESTBED_RUNTIME_URL if tenant == Tenant.TESTBED else self.OWS_PROD_RUNTIME_URL
        )
        if not url:
            raise RuntimeError(
                f"No Runtime URL configured for tenant '{tenant}'. "
                f"Set OWS_{tenant.upper()}_RUNTIME_URL in .env."
            )
        return str(url).rstrip("/")

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
