# AGENTS.md — context for future agents working in this repo

## What this repo is
Python FastMCP server that exposes Huawei OWS / GDE (Operation Web Services /
General Digital Engine) **as a programmable introspection surface** for AI
agents and developer tooling. Scope is *every artifact a developer can build
in OWS Development State Studio* — Models, Pages, Services, Scripts, Processes,
Jobs, Triggers, Events, RPA, AI Models, Agents, etc. (~50 types).

Two tenants the user has access to (same account):

- **Testbed:** `https://1057-sg-studio.teleows.com/` (Studio + Runtime co-hosted)
- **Production:** `https://1057-sg.teleows.com/` (Runtime; Studio URL TBD)

## Hard rules
1. **Never commit credentials.** `.env` is gitignored. The OWS password the user
   originally pasted in chat must be considered compromised — the user has been
   asked to rotate it.
2. **Production is read-mostly.** Any tool that mutates prod state must check
   both `OWS_PROD_WRITE_ENABLED=1` (env) and `confirm: true` (call arg) before
   acting. Testbed has no such gate.
3. **Tenant is always explicit.** Every tool takes `tenant: "prod" | "testbed"`.
   No implicit defaults.
4. **Discovery before code.** No tool ships until there is a captured request +
   response in `docs/discovery/<tenant>/` proving the endpoint shape.
5. **Capture dumps may be sensitive.** `docs/discovery/raw/` and
   `docs/discovery/**/*.json` are gitignored except sanitized samples under
   `docs/discovery/examples/`.

## Toolchain
- `uv` for Python env + scripts.
- `mcp[cli]` (FastMCP) for the server.
- `httpx` (async) for the OWS HTTP client.
- `pydantic` + `pydantic-settings` for models / config.
- `pytest` + `pytest-httpx` for tests.
- `ruff` for lint/format.

## Phase order (revised — artifact-introspection focused)
0. **Discovery & scaffolding** (current). Auth scheme reverse-engineered;
   `whoami` works end-to-end. Pending: parse a sample app export + Studio walk.
1. **Core introspection** — `list_apps`, `list_artifacts`, `get_artifact`,
   `search_artifacts`, plus a generic `call_ows_api` escape hatch. Common
   artifact types first (Model, Page, Service, Script, Business Process).
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
- Auth scheme: cookie? bearer token? CSRF header? Refresh strategy?
- Are there separate API base paths for Studio vs Runtime, or one gateway?
