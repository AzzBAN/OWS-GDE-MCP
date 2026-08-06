"""FastMCP server entrypoint.

Phase 0: ships `status` (no auth) and `whoami` (real OWS call) so we can
prove the auth pipeline end-to-end before adding artifact introspection
tools (Phase 1+).
"""

from __future__ import annotations

import argparse
import asyncio
import sys

from mcp.server.fastmcp import FastMCP

from ows_gde_mcp import __version__
from ows_gde_mcp.client import OwsApiError, OwsClient, prewarm_session
from ows_gde_mcp.config import Surface, Tenant, settings
from ows_gde_mcp.tools import files as _files
from ows_gde_mcp.tools import flow_debug as _flow
from ows_gde_mcp.tools import help as _help
from ows_gde_mcp.tools import live as _live
from ows_gde_mcp.tools import log_analysis as _logs
from ows_gde_mcp.tools import packages as _pkgs
from ows_gde_mcp.tools import pages as _pages
from ows_gde_mcp.tools import processes as _procs
from ows_gde_mcp.tools import references as _refs
from ows_gde_mcp.tools import scripts as _scripts

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
mcp.tool()(_live.list_studio_element_types)
mcp.tool()(_live.list_models)
mcp.tool()(_live.get_model)
mcp.tool()(_live.get_model_schema)
mcp.tool()(_live.list_services)
mcp.tool()(_live.get_service)
# Studio (design-state) — pages
mcp.tool()(_pages.list_pages)
mcp.tool()(_pages.get_page)
mcp.tool()(_pages.get_page_detail)
mcp.tool()(_pages.save_page_content)
mcp.tool()(_pages.create_page)
mcp.tool()(_pages.add_page_component)
mcp.tool()(_pages.update_page_component_props)
mcp.tool()(_pages.remove_page_component)
mcp.tool()(_live.list_scripts)
mcp.tool()(_live.list_triggers)
mcp.tool()(_live.get_trigger)
# Execution — invoke a Service / run a TQL model query
mcp.tool()(_live.invoke_service)
mcp.tool()(_live.query_model_data)

# BPM process catalog — discover ticket-prefix → model mapping (cached locally).
mcp.tool()(_procs.list_processes)
mcp.tool()(_procs.get_process)
mcp.tool()(_procs.resolve_process_by_prefix)
mcp.tool()(_procs.refresh_process_cache)

# Service-bundled scripts (RunScript / ScriptLib / Translator / Validator) and page scripts.
# Verified against testbed Studio on 2026-05-18 — see tools/scripts.py.
mcp.tool()(_scripts.list_service_scripts)
mcp.tool()(_scripts.get_service_script)
mcp.tool()(_scripts.create_service_script)
mcp.tool()(_scripts.update_service_script)
mcp.tool()(_scripts.get_page_scripts)
mcp.tool()(_scripts.list_page_scripts)

# File attachments — list/download files behind a `mateinfo-file-token`.
# Verified against prod 2026-05-27 — see tools/files.py.
mcp.tool()(_files.list_file_attachments)
mcp.tool()(_files.download_file_attachment)

# OWS knowledge vault — local Obsidian vault (populate via
# `scripts/import_help_corpus.py`). get_help_home returns the curated MOC;
# search_help ranks curated findings above the reference corpus;
# add_help_finding lets the end user grow the vault.
mcp.tool()(_help.get_help_home)
mcp.tool()(_help.list_help_topics)
mcp.tool()(_help.get_help_topic)
mcp.tool()(_help.search_help)
mcp.tool()(_help.add_help_finding)

# Cross-reference analysis (live OWS only for now; from_package = PR2.5)
mcp.tool()(_refs.find_artifact_references)
mcp.tool()(_refs.find_unused_artifacts)
mcp.tool()(_refs.audit_artifact_usage)

# Log Analysis (runtime log search) — separate auth scheme; see log_analysis.py.
mcp.tool()(_logs.search_service_logs)
mcp.tool()(_logs.get_log_trace)
mcp.tool()(_logs.count_service_invocations)

# Flow debugging — recursively walk service chains, diff caller/callee schemas,
# and lint RunScript bodies for known anti-patterns.
mcp.tool()(_flow.walk_service_chain)
mcp.tool()(_flow.diff_service_io)
mcp.tool()(_flow.lint_service_script)


@mcp.tool()
async def refresh_session(tenant: str) -> dict:
    """Force a CAS re-login for the given tenant. Returns the userId on success.

    One CAS login covers both Studio and Runtime surfaces of the tenant — the
    cookie is shared. Use this when tools start failing with redirect errors
    and you'd rather refresh manually than wait for auto-relogin to fire on
    the next call. Requires `OWS_<TENANT>_USERNAME` and
    `OWS_<TENANT>_PASSWORD` in `.env`, plus the optional `login` extra
    installed (`uv pip install -e '.[login]'` and `playwright install chromium`).
    """
    t = Tenant(tenant)
    surfaces = settings.configured_surfaces(t)
    if not surfaces:
        return {
            "tenant": t.value,
            "refreshed": False,
            "error": (
                f"No studio or runtime URL configured for tenant '{t.value}'. "
                f"Set OWS_{t.value.upper()}_RUNTIME_URL or "
                f"OWS_{t.value.upper()}_STUDIO_URL in .env."
            ),
        }
    surface = surfaces[0]
    async with OwsClient.for_surface(t, surface, settings) as client:
        await client._refresh_session()
        me = await client.get("/portal/web/rest/v1/user/my-info")
        return {
            "tenant": t.value,
            "surface_used": surface.value,
            "refreshed": True,
            "userId": me.get("userId") if isinstance(me, dict) else None,
        }


@mcp.tool()
def status() -> dict:
    """Report MCP server status & which (tenant, surface) cells have URLs/secrets configured."""
    return {
        "version": __version__,
        "phase": "0-discovery",
        "tenants": {
            Tenant.TESTBED.value: {
                "studio_url": str(settings.OWS_TESTBED_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_TESTBED_RUNTIME_URL or ""),
                "configured_surfaces": [
                    s.value for s in settings.configured_surfaces(Tenant.TESTBED)
                ],
                "has_session_cookie": bool(settings.OWS_TESTBED_SESSION_COOKIE),
                "has_csrf_token": bool(settings.OWS_TESTBED_CSRF_TOKEN),
            },
            Tenant.PROD.value: {
                "studio_url": str(settings.OWS_PROD_STUDIO_URL or ""),
                "runtime_url": str(settings.OWS_PROD_RUNTIME_URL or ""),
                "configured_surfaces": [s.value for s in settings.configured_surfaces(Tenant.PROD)],
                "has_session_cookie": bool(settings.OWS_PROD_SESSION_COOKIE),
                "has_csrf_token": bool(settings.OWS_PROD_CSRF_TOKEN),
                "write_enabled": settings.OWS_PROD_WRITE_ENABLED,
            },
        },
    }


@mcp.tool()
async def whoami(tenant: str) -> dict:
    """Return the logged-in user profile for the given tenant.

    Routes through the **runtime** surface (the portal user-info endpoint
    only exists on runtime). The tenant must have a runtime URL configured.

    Args:
        tenant: "prod" or "testbed".

    Returns:
        Parsed `/portal/web/rest/v1/user/my-info` payload (userId, userName,
        userAccount, tenantId, roles, time zone, etc.). Includes a small
        `_session_alive` boolean confirming `/portal/web/rest/sso/check`.
    """
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.RUNTIME, settings) as client:
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
    serve.add_argument(
        "--no-prewarm",
        action="store_true",
        help="Skip the startup CAS login. By default the server logs in for "
        "every tenant with credentials configured so the first tool call "
        "doesn't pay the relogin cost.",
    )
    findings = sub.add_parser(
        "findings",
        help="Print the knowledge-vault home + curated findings (for the "
        "SessionStart hook). Reads the vault resolved from OWS_VAULT_DIR or "
        "./ows-vault; never makes network calls.",
    )
    findings.add_argument(
        "--hook",
        action="store_true",
        help="Emit a Claude Code SessionStart hook JSON object "
        "({hookSpecificOutput.additionalContext}) instead of plain text.",
    )
    args = parser.parse_args()

    if args.cmd == "serve":
        if not args.no_prewarm:
            asyncio.run(_prewarm_all())
        if args.http:
            mcp.settings.port = args.port
            mcp.run(transport="streamable-http")
        else:
            mcp.run()
    elif args.cmd == "findings":
        _emit_findings(hook=args.hook)
    else:
        parser.print_help()
        sys.exit(2)


def _emit_findings(*, hook: bool) -> None:
    """Print the vault MOC + curated findings; for the SessionStart hook.

    Best-effort: if no vault/findings exist, emits nothing (exit 0) so a fresh
    project doesn't get a noisy hook error.
    """
    import json as _json

    home = _help.get_help_home()
    if "error" in home:
        return  # no vault yet — stay quiet
    parts = [f"# OWS knowledge vault\n\n{home.get('text', '')}".strip()]
    for f in home.get("findings", []):
        topic = _help.get_help_topic(f["local"])
        if "error" not in topic:
            parts.append(topic.get("text", "").strip())
    context = "\n\n---\n\n".join(p for p in parts if p)
    if not context.strip():
        return
    if hook:
        print(
            _json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "SessionStart",
                        "additionalContext": (
                            "OWS knowledge vault — curated findings (read these "
                            "before searching the corpus):\n\n" + context
                        ),
                    }
                }
            )
        )
    else:
        print(context)


async def _prewarm_all() -> None:
    """Pre-login any tenant that has creds configured. Best-effort, never raises."""
    tasks = []
    if settings.OWS_TESTBED_USERNAME and settings.OWS_TESTBED_PASSWORD:
        tasks.append(prewarm_session(Tenant.TESTBED, settings))
    if settings.OWS_PROD_USERNAME and settings.OWS_PROD_PASSWORD:
        tasks.append(prewarm_session(Tenant.PROD, settings))
    if not tasks:
        return
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        # stderr so it doesn't interfere with stdio MCP framing on stdout.
        if isinstance(r, Exception):
            print(f"[ows-gde-mcp] prewarm error: {r}", file=sys.stderr)
        elif r:
            print(f"[ows-gde-mcp] {r}", file=sys.stderr)


if __name__ == "__main__":
    cli()
