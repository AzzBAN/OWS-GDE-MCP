# AGENTS.md — context for future agents working in this repo

## What this repo is
Python FastMCP server that exposes Huawei OWS / GDE (Operation Web Services /
General Digital Engine) **as a programmable introspection surface** for AI
agents and developer tooling. Scope is *every artifact a developer can build
in OWS Development State Studio* — Models, Pages, Services, Scripts, Processes,
Jobs, Triggers, Events, RPA, AI Models, Agents, etc. (~50 types).

Tenants follow a `<tenant>-studio.example.com` (testbed/studio + runtime
co-hosted) and `<tenant>.example.com` (prod runtime) shape. Configure real
hostnames in `.env`; nothing tenant-specific should land in the repo.

## Hard rules
1. **Never commit credentials or tenant identifiers.** `.env` is gitignored.
   Treat any captured cookie, CSRF token, username, or tenant hostname as
   sensitive — keep them in `.env`, scrub them out of docs and discovery dumps
   before committing.
2. **Production is read-mostly.** All mutations against prod are gated centrally
   in `OwsClient.request`: non-GET requests require `OWS_PROD_WRITE_ENABLED=1`
   and `confirm=True`. New tools inherit this automatically. Testbed has no
   such gate.
3. **Tenant is always explicit.** Every tool takes `tenant: "prod" | "testbed"`.
   No implicit defaults.
4. **Discovery before code.** No tool ships until there is a captured request +
   response in `docs/discovery/<tenant>/` proving the endpoint shape.
5. **Capture dumps may be sensitive.** `docs/discovery/raw/` and
   `docs/discovery/**/*.json` are gitignored except sanitized samples under
   `docs/discovery/examples/`.
6. **Path validation runs before any I/O.** `OwsClient.request` rejects absolute
   URLs, protocol-relative paths, and `..` traversal segments (including
   percent-encoded). Don't add tools that bypass this.
7. **Auto-relogin is opt-in but transparent.** When `OWS_<TENANT>_USERNAME` /
   `_PASSWORD` are set and the `login` extra is installed, expired sessions
   refresh themselves via headless CAS. Refreshed cookies live only in
   process memory — never write them back to `.env`.

## Toolchain
- `uv` for Python env + scripts.
- `mcp[cli]` (FastMCP) for the server.
- `httpx` (async) for the OWS HTTP client.
- `pydantic` + `pydantic-settings` for models / config.
- `pytest` + `pytest-httpx` for tests.
- `ruff` for lint/format.
- `playwright` (optional, via `[login]` extra) for headless CAS auto-relogin.

## Phase order (revised — artifact-introspection focused)
0. **Discovery & scaffolding** (current). Auth scheme reverse-engineered;
   `whoami` works end-to-end. Pending: parse a sample app export + Studio walk.
1. **Core introspection** (in progress, near complete) — `list_apps`,
   `list_artifacts`, `get_artifact`, `search_artifacts`, plus a generic
   `call_ows_api` escape hatch. Common artifact types first (Model, Page,
   Service, Script, Business Process). Note: pages/scripts shipped with
   inferred endpoints pending discovery verification (see `docs/discovery.md`
   "Endpoints needing live verification").
2. **Data layer** — typed Model tools, TQL queries, Data Process, Data Source.
3. **AI / Agent artifacts** — AI Model, AI Service, Agent, Flow, Prompt, Tool,
   Knowledge Management, etc.
4. **Integration artifacts** — Inbound/Outbound REST/SOAP, Connector, RPA
   Script, Function Service, Trigger, Job.
5. **Runtime ops** — Work orders, alarms, SLA/OLA (only if needed beyond
   introspection).
6. **Help docs ingestion** — wrap the Studio online help so the MCP can
   answer "what does this artifact mean?" with citations.
7. Polish — logging, tests, docs, packaging.

## How discovery works
Playwright MCP is configured at user scope (`~/.config/devin/config.json`)
with `--headed`. The agent:
1. Opens a tenant URL in the visible browser.
2. The user completes login + any SSO/CAPTCHA interactively.
3. The agent navigates each Studio module tab in turn.
4. After each tab, calls `browser_network_requests` and writes the result to
   `docs/discovery/<tenant>/<module>.json`.
5. Summarizes findings (auth scheme, base API paths, sample shapes) into
   `docs/discovery.md`.

Production walk is **read-only** — `GET`-equivalent navigation only, no
Save / Publish / Deploy clicks.

## Common commands
```bash
# Run the MCP locally
uv run ows-gde-mcp serve

# Run tests
uv run pytest

# Lint
uv run ruff check .
uv run ruff format .
```

## Open questions (resolve during Phase 0)
- Does Production also have a `-studio` subdomain? If so, what URL?
- Does Testbed have a separate runtime URL, or is the studio host shared?
- ~~Auth scheme: cookie? bearer token? CSRF header? Refresh strategy?~~
  Resolved: HttpOnly session cookie + `x-gde-csrf-token` + reverse-engineered
  `x-adc-page-token`/`x-adc-page-timestamp` anti-tamper headers (see
  `docs/discovery.md`). Refresh strategy: headless CAS auto-relogin in
  `auth_login.py` triggered on 302→`/dspcas/login`.
- Are there separate API base paths for Studio vs Runtime, or one gateway?
- **Pages / Scripts endpoints** (`/adc-studio-page/.../app/page/query`,
  `/adc-studio-script/.../app/script/query`) are inferred and not yet
  verified by a Studio walk. `list_scripts` returns 404 against the live
  testbed — fix is a discovery walk to find the real path.
