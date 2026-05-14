# ows-gde-mcp

A Model Context Protocol (MCP) server that turns Huawei **OWS / GDE**
(Operation Web Services / General Digital Engine) into a programmable surface
for any AI agent or developer tooling. The MCP introspects everything you can
build in **Development State Studio** — Models, Pages, Services, Scripts,
Processes, Jobs, Triggers, Events, RPA Scripts, AI Models, Agents, and ~40
more artifact types — so an agent can answer "what is X in our OWS?" without
you copy-pasting from the portal.

> **Status:** Phase 0 → 1. Auth scheme reverse-engineered and verified;
> `whoami` end-to-end works against the live OWS host (once you paste a
> session cookie). Offline `.gpk` package introspection ships in Phase 1
> with 5 tools — no auth needed.

## Tools

**📄 Full reference: [`docs/tools.md`](docs/tools.md)** — auto-generated from
the live MCP server, lists every tool with its signature and description.

Regenerate after adding/changing a tool:

```bash
uv run python scripts/gen_tools_md.py
```

Quick map of what's in each category (currently 20 tools):

- **Diagnostics:** `status`, `whoami`
- **Live OWS — Studio introspection (auth required):** `list_studio_projects`,
  `get_studio_project`, `list_project_modules`, `get_studio_module`,
  `list_models`, `get_model`, `get_model_fields`, `list_services`,
  `get_service`, `list_live_menus`, `list_live_apps`, `get_favorite_menus`,
  `call_ows_api` (generic escape hatch).
- **Offline `.gpk` introspection (no auth):** `list_app_packages`,
  `get_app_package_info`, `list_app_artifacts`, `get_app_artifact`,
  `search_app_artifacts`.

## What this wraps

| Tenant    | Studio (design state)                  | Runtime                       |
|-----------|----------------------------------------|-------------------------------|
| Testbed   | `https://1057-sg-studio.teleows.com/`  | _shared with Studio host_     |
| Prod      | _TBD (discovery)_                      | `https://1057-sg.teleows.com/`|

Same-origin services discovered (and gated by the same auth scheme):
`/dspcas/`, `/portal/web/rest/v1/`, `/adc-ui/web/rest/v1/`,
`/adc-service/web/rest/v1/services|legacy/services/`,
`/adc-model/web/rest/v1/`, `/adc-agent/web/rest/v1/`,
`/adc-studio-project-mgt/web/rest/`, `/adc-static/`.

See `docs/discovery.md` for the full, sourced API map and
`docs/plan.md` for phase-by-phase tool plan.

## Safety model

- **Per-tool tenant arg.** Every tool requires `tenant: "prod" | "testbed"`.
- **Production is read-mostly.** Mutating tools against `prod` require both
  `OWS_PROD_WRITE_ENABLED=1` in env and `confirm: true` at call time.
- **No credentials in code.** Auth is a pasted session cookie + CSRF token,
  loaded from `.env` (gitignored). Never committed.

## Quickstart

```bash
# 1. Install
uv sync

# 2. Configure
cp .env.example .env
$EDITOR .env   # set STUDIO_URL + paste session cookie + CSRF token (steps below)

# 3. Smoke test the auth pipeline
uv run python -c "
import asyncio
from ows_gde_mcp.server import whoami
print(asyncio.run(whoami('testbed')))
"

# 4. Run the MCP
uv run ows-gde-mcp serve            # stdio (default)
uv run ows-gde-mcp serve --http     # Streamable HTTP for multi-client
```

Add to your MCP client config (Claude Desktop, Devin, Windsurf, etc.):

```json
{
  "mcpServers": {
    "ows-gde": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/OWS_MCP", "ows-gde-mcp", "serve"]
    }
  }
}
```

## Capturing the session cookie

OWS uses CAS (`/dspcas/login`) for SSO. The **session cookie is HttpOnly**, so
JavaScript can't read it — you'll grab it once via DevTools.

1. Open `https://1057-sg-studio.teleows.com/` in Chrome / Edge / Brave.
2. Log in normally (with your OWS account).
3. Open **DevTools** (`Cmd+Opt+I` / `Ctrl+Shift+I`) → **Network** tab.
4. Reload the page. Click any XHR request that succeeds (status 200) — for
   example `my-info`, `getGranted`, or `sso/check`.
5. In **Headers** → **Request Headers**, find the **`Cookie:`** line.
   Copy the entire value (everything after `Cookie: `).
6. Paste into `.env`:
   ```ini
   OWS_TESTBED_SESSION_COOKIE=_LOCALE_=en_US; ...; lastestOperationTime=...
   ```
7. From the same DevTools **Console** tab, run:
   ```js
   window.csrfToken
   ```
   Copy the 48-digit string. Paste into `.env` as `OWS_TESTBED_CSRF_TOKEN=`.

The cookie typically lasts the duration of your CAS session (hours). When it
expires, OWS endpoints will return `403 ADC.COMM.SDK.03240001` — re-capture
and update `.env`. (A future MCP version will run an interactive login on
demand to refresh automatically.)

## Verification

```bash
uv run pytest                        # 14 tests, including auth-token verified
                                     # against 3 live capture samples.
uv run ruff check .                  # lint
uv run ruff format .                 # format
```

Once `.env` is set, `whoami("testbed")` should return your tenant ID, user ID,
user name, and roles — confirming the full pipeline works.

## License

Internal / TBD.
