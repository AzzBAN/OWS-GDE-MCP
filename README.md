# ows-gde-mcp

A Model Context Protocol (MCP) server that exposes Huawei **OWS / GDE**
(Operation Web Services / General Digital Engine) capabilities — Studio
(ADC 2.0) and Runtime — as tools you can call from any MCP client.

> **Status:** Phase 0 (discovery). No tools shipped yet.

## What this wraps

Two tenants, both pointing at the same physical OWS deployment from your
account's perspective:

| Tenant    | Studio (design state)                  | Runtime                       |
|-----------|----------------------------------------|-------------------------------|
| Testbed   | `https://1057-sg-studio.teleows.com/`  | TBD (discovery)               |
| Prod      | TBD (discovery)                        | `https://1057-sg.teleows.com/`|

OWS modules planned for tool coverage (in this order):

1. **Process orchestration** (BPMN-style flows, user tasks, gateways)
2. **Asset management / GDE Store** (publish, version, deploy)
3. **Data models & Data orchestration** (business objects, data flows)
4. **UI / Form metadata** (read-only first)
5. **Service orchestration / API Fabric**
6. **Runtime ops** — work orders, alarms, SLA/OLA

See `docs/plan.md` for the full phased plan and `docs/discovery.md` for the
captured API surface.

## Safety model

- **Per-tool tenant arg.** Every tool requires `tenant: "prod" | "testbed"`.
- **Production is read-mostly.** Mutating tools against `prod` require both
  `OWS_PROD_WRITE_ENABLED=1` in env and `confirm: true` at call time.
- **No credentials in code.** Auth is interactive (headed browser) or via
  session cookies pasted into `.env` (gitignored).

## Quickstart (after Phase 0)

```bash
uv sync
cp .env.example .env  # fill in URLs / cookies
uv run ows-gde-mcp serve            # stdio (default)
uv run ows-gde-mcp serve --http     # Streamable HTTP for multi-client
```

Then add to your MCP client config:

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

## Discovery (Phase 0)

Endpoint inventory is captured by driving the OWS portal with **Playwright MCP**
in a headed browser. The agent walks each Studio module while you handle the
SSO login interactively, and dumps every XHR/fetch request to
`docs/discovery/<tenant>/<module>.json`. Production walk is read-only.

## License

Internal / TBD.
