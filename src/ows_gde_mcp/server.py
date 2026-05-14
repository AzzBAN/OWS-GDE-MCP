"""FastMCP server entrypoint.

Phase 0: only a placeholder tool that reports discovery status. Real tools land
once endpoints are captured under docs/discovery/.
"""

from __future__ import annotations

import argparse
import sys

from mcp.server.fastmcp import FastMCP

from ows_gde_mcp import __version__
from ows_gde_mcp.config import Tenant, settings

mcp = FastMCP("ows-gde-mcp")


@mcp.tool()
def status() -> dict:
    """Report MCP server status & which tenants have URLs configured."""
    return {
        "version": __version__,
        "phase": "0-discovery",
        "tenants": {
            Tenant.TESTBED.value: {
                "studio_url": str(settings.OWS_TESTBED_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_TESTBED_RUNTIME_URL or ""),
                "has_session_cookie": bool(settings.OWS_TESTBED_SESSION_COOKIE),
            },
            Tenant.PROD.value: {
                "studio_url": str(settings.OWS_PROD_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_PROD_RUNTIME_URL or ""),
                "has_session_cookie": bool(settings.OWS_PROD_SESSION_COOKIE),
                "write_enabled": settings.OWS_PROD_WRITE_ENABLED,
            },
        },
        "note": "Phase 0 (discovery). Real tools ship once docs/discovery/ is populated.",
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
            # FastMCP exposes Streamable HTTP via run(transport="streamable-http")
            mcp.settings.port = args.port
            mcp.run(transport="streamable-http")
        else:
            mcp.run()  # stdio
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    cli()
