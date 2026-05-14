"""FastMCP server entrypoint.

Phase 0: ships `status` (no auth) and `whoami` (real OWS call) so we can
prove the auth pipeline end-to-end before adding artifact introspection
tools (Phase 1+).
"""

from __future__ import annotations

import argparse
import sys

from mcp.server.fastmcp import FastMCP

from ows_gde_mcp import __version__
from ows_gde_mcp.client import OwsApiError, OwsClient
from ows_gde_mcp.config import Tenant, settings
from ows_gde_mcp.tools import live as _live
from ows_gde_mcp.tools import packages as _pkgs

mcp = FastMCP("ows-gde-mcp")


# Register offline `.gpk` introspection tools. These do not require auth.
mcp.tool()(_pkgs.list_app_packages)
mcp.tool()(_pkgs.get_app_package_info)
mcp.tool()(_pkgs.list_app_artifacts)
mcp.tool()(_pkgs.get_app_artifact)
mcp.tool()(_pkgs.search_app_artifacts)

# Register live OWS introspection tools. Require OWS_<TENANT>_SESSION_COOKIE.
mcp.tool()(_live.list_live_menus)
mcp.tool()(_live.list_live_apps)
mcp.tool()(_live.get_favorite_menus)
mcp.tool()(_live.get_model_fields)
mcp.tool()(_live.call_ows_api)
# Studio (design-state) — projects, modules, models
mcp.tool()(_live.list_studio_projects)
mcp.tool()(_live.get_studio_project)
mcp.tool()(_live.list_project_modules)
mcp.tool()(_live.get_studio_module)
mcp.tool()(_live.list_models)
mcp.tool()(_live.get_model)


@mcp.tool()
def status() -> dict:
    """Report MCP server status & which tenants have URLs/secrets configured."""
    return {
        "version": __version__,
        "phase": "0-discovery",
        "tenants": {
            Tenant.TESTBED.value: {
                "studio_url": str(settings.OWS_TESTBED_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_TESTBED_RUNTIME_URL or ""),
                "has_session_cookie": bool(settings.OWS_TESTBED_SESSION_COOKIE),
                "has_csrf_token": bool(settings.OWS_TESTBED_CSRF_TOKEN),
            },
            Tenant.PROD.value: {
                "studio_url": str(settings.OWS_PROD_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_PROD_RUNTIME_URL or ""),
                "has_session_cookie": bool(settings.OWS_PROD_SESSION_COOKIE),
                "has_csrf_token": bool(settings.OWS_PROD_CSRF_TOKEN),
                "write_enabled": settings.OWS_PROD_WRITE_ENABLED,
            },
        },
    }


@mcp.tool()
async def whoami(tenant: str) -> dict:
    """Return the logged-in user profile for the given tenant.

    Args:
        tenant: "prod" or "testbed".

    Returns:
        Parsed `/portal/web/rest/v1/user/my-info` payload (userId, userName,
        userAccount, tenantId, roles, time zone, etc.). Includes a small
        `_session_alive` boolean confirming `/portal/web/rest/sso/check`.
    """
    t = Tenant(tenant)
    async with OwsClient.for_tenant(t, settings) as client:
        try:
            me = await client.get("/portal/web/rest/v1/user/my-info")
            alive = await client.get("/portal/web/rest/sso/check")
        except OwsApiError as e:
            return {
                "error": {
                    "status": e.status,
                    "code": e.code,
                    "message": e.message,
                    "path": e.path,
                },
                "hint": (
                    "If code is ADC.COMM.SDK.03240001, the session cookie is "
                    "missing or expired. Re-capture it (see README → 'Capturing "
                    f"the session cookie') and update OWS_{t.value.upper()}_SESSION_COOKIE."
                ),
            }
        return {
            "tenant": t.value,
            "userId": me.get("userId"),
            "userAccount": me.get("userAccount"),
            "userName": me.get("userName"),
            "tenantId": me.get("tenantId"),
            "timeZone": me.get("timeZone"),
            "roles": [r.get("roleName") for r in (me.get("role") or [])],
            "_session_alive": bool(alive),
        }


def cli() -> None:
    parser = argparse.ArgumentParser(prog="ows-gde-mcp")
    sub = parser.add_subparsers(dest="cmd", required=True)
    serve = sub.add_parser("serve", help="Run the MCP server.")
    serve.add_argument(
        "--http",
        action="store_true",
        help="Run as Streamable HTTP server instead of stdio.",
    )
    serve.add_argument(
        "--port",
        type=int,
        default=settings.OWS_MCP_HTTP_PORT,
        help=f"HTTP port (default {settings.OWS_MCP_HTTP_PORT}).",
    )
    args = parser.parse_args()

    if args.cmd == "serve":
        if args.http:
            mcp.settings.port = args.port
            mcp.run(transport="streamable-http")
        else:
            mcp.run()
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    cli()
