# ows-gde-mcp

A Model Context Protocol (MCP) server that turns Huawei **OWS / GDE**
(Operation Web Services / General Digital Engine) into a programmable surface
for any AI agent or developer tooling. The MCP introspects everything you can
build in **Development State Studio** — Models, Pages, Services, Scripts,
Processes, Jobs, Triggers, Events, RPA Scripts, AI Models, Agents, and ~40
more artifact types — so an agent can answer "what is X in our OWS?" without
you copy-pasting from the portal.

> **Disclaimer:** This is an independent integration. Not affiliated with,
> endorsed by, or sponsored by Huawei. Use only against tenants you have
> authorization to access; review your tenant's terms of service before
> running automated calls. See `LICENSE` (Apache-2.0) and `NOTICE`.

## Tools

**📄 Full reference: [`docs/tools.md`](docs/tools.md)** — auto-generated from
the live MCP server, lists every tool with its signature and description.

Regenerate after adding/changing a tool:

```bash
uv run python scripts/gen_tools_md.py
```

47 tools across these categories:

- **Diagnostics & session:** `status`, `whoami`, `refresh_session`.
- **Live OWS — Studio introspection (auth required):** `list_studio_projects`,
  `get_studio_project`, `list_project_modules`, `get_studio_module`,
  `list_studio_element_types`, `list_models`, `get_model`,
  `get_model_fields`, `query_model_data`, `list_services`, `get_service`,
  `invoke_service`, `list_service_scripts`, `get_service_script`,
  `list_pages`, `get_page`, `get_page_detail`, `get_page_scripts`,
  `list_page_scripts`, `list_scripts`, `list_triggers`, `get_trigger`,
  `list_live_menus`, `list_live_apps`, `get_favorite_menus`,
  `call_ows_api` (generic escape hatch).
- **Cross-reference + audit (live, static + runtime):**
  `find_artifact_references`, `find_unused_artifacts`,
  `audit_artifact_usage`. See `docs/audit-confidence.md` for what
  the confidence ratings mean.
- **Runtime log search:** `search_service_logs`, `get_log_trace`,
  `count_service_invocations` (Log Analysis service; ~3-day retention).
- **BPM processes:** `list_processes`, `get_process`,
  `resolve_process_by_prefix`, `refresh_process_cache`.
- **Help docs (offline cache):** `list_help_topics`, `get_help_topic`,
  `search_help`.
- **Offline `.gpk` introspection (no auth):** `list_app_packages`,
  `get_app_package_info`, `list_app_artifacts`, `get_app_artifact`,
  `search_app_artifacts`.

## What this wraps

OWS has two independent axes that each tool routes through:

- **Tenant** — `prod` or `testbed`. Separate environments with their own
  accounts and CAS servers.
- **Surface** — `studio` (design-time authoring) or `runtime` (deployed
  apps for end users / preview / production traffic).

| Tenant   | Studio (design-time)                           | Runtime (deployed apps)                         |
|----------|------------------------------------------------|-------------------------------------------------|
| Testbed  | `https://<tenant>-studio.example.com/`         | `https://<tenant>-studio.example.com/` (same host on this testbed) |
| Prod     | _typically unavailable to developers_          | `https://<tenant>.example.com/`                  |

Typical workflow: author in testbed studio → preview on testbed runtime →
deploy to prod runtime. A tenant can have either, both, or neither surface
configured; tools that target an unconfigured surface fail fast with a clear
error naming the env var to set. There is no automatic fallback between
surfaces.

Each tool internally picks the right surface for the API it's calling:

- **Studio surface** (`/adc-studio-*/...`) — `list_studio_projects`,
  `list_models`, `list_services`, `list_pages`, `list_scripts`, etc.
- **Runtime surface** (`/portal/...`, `/adc-model/...`, `/adc-service/...`) —
  `whoami`, `list_live_menus`, `list_live_apps`, `get_favorite_menus`,
  `get_model_fields`, etc.

`call_ows_api` accepts an explicit `surface` parameter (default `runtime`)
for paths the typed tools don't yet wrap.

Same-origin services discovered (and gated by the same auth scheme):
`/dspcas/`, `/portal/web/rest/v1/`, `/adc-ui/web/rest/v1/`,
`/adc-service/web/rest/v1/services|legacy/services/`,
`/adc-model/web/rest/v1/`, `/adc-agent/web/rest/v1/`,
`/adc-studio-project-mgt/web/rest/`, `/adc-static/`.

See `docs/discovery.md` for the full, sourced API map and
`docs/plan.md` for phase-by-phase tool plan.

## Safety model

- **Per-tool tenant arg.** Every tool requires `tenant: "prod" | "testbed"`.
- **Per-tool surface routing.** Tools route to the right surface (studio vs
  runtime) for their API. Calling an unconfigured surface fails with a
  clear error naming the env var to set — no silent fallback.
- **One CAS session per tenant.** A single login covers both surfaces of
  the same tenant; cookies/CSRF are stored per-tenant, not per-surface.
- **Production is read-mostly.** Mutations against `prod` are gated centrally
  in `OwsClient.request`: any non-GET request requires both
  `OWS_PROD_WRITE_ENABLED=1` in env and `confirm: true` at call time. New
  tools inherit the gate automatically.
- **SSRF guard.** Every request path is validated before I/O — absolute URLs,
  protocol-relative paths (`//host/...`), and `..` traversal segments
  (including percent-encoded) are rejected.
- **No credentials in code.** Auth values live in `.env` (gitignored). Either
  a captured session cookie or username/password (for auto-relogin); never
  committed.

## Quickstart

```bash
# 1. Install core dependencies (this is all most users need)
uv sync                       # or: pip install -r requirements.txt
                              # installs httpx, pydantic, cryptography, ... —
                              # cryptography powers the pure-HTTP CAS login.
                              # Dependencies are NOT auto-installed at runtime;
                              # a missing core dep fails at import with ModuleNotFoundError.

# 1b. OPTIONAL: only if HTTP login can't clear a host (captcha / MFA),
#     install the Playwright fallback. Skip this unless you hit that error.
uv pip install -e '.[login]'
playwright install chromium

# 2. Configure
cp .env.example .env
$EDITOR .env   # set the (tenant × surface) URLs you have access to,
               # then set OWS_<TENANT>_USERNAME / _PASSWORD (primary path),
               # or paste a session cookie + CSRF token as a manual override.

# 3. Smoke test
uv run python -c "
import asyncio
from ows_gde_mcp.server import whoami
print(asyncio.run(whoami('testbed')))
"

# 4. Run the MCP
uv run ows-gde-mcp serve              # stdio (default)
uv run ows-gde-mcp serve --http       # Streamable HTTP for multi-client
uv run ows-gde-mcp serve --no-prewarm # skip the startup CAS login
```

On startup the server pre-warms a CAS login for every tenant that has
credentials configured, so the first tool call doesn't pay the relogin cost.
When a session expires mid-batch, `OwsClient.request` detects the 302→CAS
redirect, relogs in (under an `asyncio.Lock`, so concurrent calls share one
login), and retries the original request once. Use `refresh_session(tenant)`
to force a re-auth on demand.

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

## Claude Code plugin (skills + MCP + knowledge vault)

This repo is also a **Claude Code plugin marketplace**. Installing the plugin
brings, in one step: the MCP server (run via `uv`), the guidance skills, an
evolving knowledge vault, and a SessionStart hook that surfaces curated
findings into context.

### Install from GitHub

```bash
# 1. Add this repo as a marketplace
claude plugin marketplace add AzzBAN/OWS-GDE-MCP

# 2. Install the plugin (skills + MCP + hook)
claude plugin install ows-gde-mcp@ows-gde
```

`uv` must be on your PATH — the bundled MCP runs as
`uv run --project ${CLAUDE_PLUGIN_ROOT} ows-gde-mcp serve` and syncs its deps on
first launch. Set your `OWS_*` credentials (see `.env.example`) in the project
where you use it. Skills are namespaced under the plugin, e.g.
`/ows-gde-mcp:ows-query`, and also trigger automatically by description.

> Prefer to wire the MCP yourself instead of bundling? Skip the plugin and add
> the `mcpServers` config above; the skills can still be installed standalone.

### Where the code actually runs

These two setups are **not the same server**, and you can have both active
in the same session (they show up as separate tool namespaces,
`mcp__ows-gde__*` vs `mcp__plugin_ows-gde-mcp_ows-gde__*`):

- **Installed plugin** (`claude plugin install`) — `${CLAUDE_PLUGIN_ROOT}`
  points at `~/.claude/plugins/cache/<marketplace>/ows-gde-mcp/<version>/`, a
  snapshot synced from a full clone of the marketplace repo
  (`~/.claude/plugins/marketplaces/<marketplace>`), pinned to whatever commit
  was on the marketplace's default branch at install/update time. Editing
  your local checkout does **nothing** for plugin users — they only pick up
  changes after you push and they run `claude plugin marketplace update` /
  `claude plugin update`.
- **Raw `mcpServers` entry** (the `.mcp.json` in this repo, or one you hand-add
  pointing `--project` at a local path) — runs live against whatever is on
  disk in that directory, uncommitted changes included.

Either way, **`.env` and the knowledge vault (`OWS_VAULT_DIR`, default
`./ows-vault`) resolve relative to the process's current working
directory** — i.e. wherever you launched `claude` from — never relative to
`${CLAUDE_PLUGIN_ROOT}`. A fresh plugin install does not bring your `.env` or
vault findings with it; each project directory needs its own.

### Knowledge vault & findings

The help tools read an Obsidian-standard vault, resolved from `OWS_VAULT_DIR`
(default `./ows-vault` — per project):

- `get_help_home` — the curated Map of Content (read first).
- `search_help` — full-text search; **curated `00 Findings/` rank above** the
  auto-generated `Reference/` corpus.
- `add_help_finding(title, body, tags=[...])` — capture a reusable platform
  finding. Findings are plain markdown in `00 Findings/`, meant to be committed
  and shared. The `ows-capture-finding` skill drives this flow.

Populate the read-only reference corpus (regenerable, gitignored) with:

```bash
uv run python scripts/import_help_corpus.py \
    --vault ~/codes/huaweed/knowledge-helper/vault
```

### Available skills

| Skill | Use when... |
|-------|------------|
| `ows-query` | Querying tickets, CMs, INCs, or any process data |
| `ows-page-analysis` | Explaining, auditing, or modifying a page element |
| `ows-debug-service` | A service is failing or returning unexpected results |
| `ows-new-service` | Building a new service element |
| `ows-new-page` | Building a new page element |
| `ows-mcp-tools` | Deciding which MCP tool to use for a given question |

### Usage

Skills are invoked automatically when the task matches their description, or
explicitly via slash command:

```
/ows-query
/ows-page-analysis
/ows-debug-service
```

## Authentication

Set `OWS_<TENANT>_USERNAME` / `_PASSWORD` in `.env`. The MCP performs a
pure-HTTP CAS login on demand and caches the session **per host** — so prod's
separate studio and runtime hosts each authenticate independently.

If HTTP login can't clear a host (captcha / MFA), install the optional
Playwright fallback:

    uv pip install -e '.[login]' && playwright install chromium

As a last resort you can paste a captured `OWS_<TENANT>_SESSION_COOKIE`
(+ `_CSRF_TOKEN`) from a logged-in browser.

Note: prod studio reads that issue POST (`get_model`, `get_model_schema`)
require `confirm=true`, like other prod write-gated calls.

## Capturing the session cookie (manual fallback)

Skip this section if you've set `OWS_<TENANT>_USERNAME` / `_PASSWORD` —
HTTP auto-login handles it. Use the manual path when you want to operate
without storing the password, or when neither HTTP nor Playwright login
is available.

OWS uses CAS (`/dspcas/login`) for SSO. The **session cookie is HttpOnly**, so
JavaScript can't read it — you'll grab it once via DevTools.

1. Open `https://<your-tenant>-studio.example.com/` in Chrome / Edge / Brave.
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

The cookie typically lasts roughly an hour. When it expires, OWS endpoints
return `403 ADC.COMM.SDK.03240001` (or 302 to `/dspcas/login`). With creds
configured, the MCP re-authenticates itself; without creds, re-capture and
update `.env`.

## Verification

```bash
uv run pytest                        # auth-token verified against live capture samples
uv run ruff check .                  # lint
uv run ruff format .                 # format
```

Once `.env` is set, `whoami("testbed")` should return your tenant ID, user ID,
user name, and roles — confirming the full pipeline works.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
