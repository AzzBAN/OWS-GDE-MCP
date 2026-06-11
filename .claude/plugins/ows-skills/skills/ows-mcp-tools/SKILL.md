---
name: ows-mcp-tools
description: Decision tree for choosing the right OWS MCP tool. TRIGGER whenever the user asks about OWS, GDE, Huawei tickets, or anything that requires calling an `mcp__ows-gde__*` tool — including queries about tickets (CM, INC, BOT, TTS, CTT), pages, services, models, triggers, scripts, processes, modules, projects, logs, or Studio elements. Use BEFORE making the first MCP call to pick the leanest tool variant and avoid over-fetching.
---

# OWS MCP Tools Decision Tree

## Heavy reads → delegate to subagent

If the `Agent` tool is in your toolbox, dispatch a subagent (general-purpose or Explore) for any of these — the big payload stays in the subagent's context, you get back a summary:

- 3+ services to inspect / `walk_service_chain` past depth 2
- `find_artifact_references` or `audit_artifact_usage` across a module
- `get_page_detail` + `get_page_scripts` for 2+ pages
- `search_service_logs` likely to return 50+ rows
- Any tool result you've previously seen return "too large to include"

Brief the subagent with the exact tool calls and ask it to return only the answer, not raw payloads.

If `Agent` is unavailable (you are already a subagent), proceed directly but be strict about lean variants: `flow_only=True`, `properties_only=True`, `summary_only=True`/`parsed=True`, `with_excerpts=False`, `content_preview_chars=200` (or `0` only when grepping a stack trace).

## "Show me tickets / data"
→ `resolve_process_by_prefix` → `query_model_data`
→ If field unknown: `get_model_fields` first

## "What pages exist in this module?"
→ `list_pages(tenant, project, module)`

## "Explain / analyze this page"
→ `get_page_detail(parsed=True)` — start here, always
→ Then `get_page_scripts` for JS behavior
→ Raw `get_page_detail` only if you need a specific deep node

## "What services does this page call?"
→ `get_page_detail(summary_only=True)` — fastest, returns service_refs[]
→ Or `get_page_detail(parsed=True)` for full context

## "What does this service do?"
→ `get_service(flow_only=True)` — just the flow steps
→ `get_service_script` — for a specific RunScript body

## "Why is this service failing?"
→ `search_service_logs` → `get_log_trace` → `get_service(flow_only=True)`

## "What calls this service?"
→ `find_artifact_references(tenant, target_uri)`

## "Is this service actually used?"
→ `audit_artifact_usage` or `count_service_invocations`

## "What models exist?"
→ `list_models(tenant, project_name, module_name)`
→ `get_model_fields(tenant, asset_uri)` for queryable fields
→ `get_model(model_id)` for full schema

## "What triggers exist?"
→ `list_triggers(tenant, project, module)`

## "Run / test a service"
→ `invoke_service` — testbed only without confirm, prod requires `confirm=True`

## "Search logs"
→ `search_service_logs` — filter by service_name, log_level, time window
→ `get_log_trace` — full trace by trace_id

## Size guidance

| Tool variant | When to use |
|---|---|
| `get_page_detail(summary_only=True)` | Just need component count + service refs |
| `get_page_detail(parsed=True)` | Need to understand structure and wiring |
| `get_page_detail` (raw) | Need to inspect a specific deep node |
| `list_services` (no flow) | Enumerate services in a module |
| `get_service(flow_only=True)` | Understand one service's logic |
| `get_model_fields` | Find correct TQL field names |
| `get_model(properties_only=True)` | Just need field names + types |
