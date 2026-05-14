# Plan — `ows-gde-mcp`

Authoritative phasing & scope for this repo. See README.md for context and
AGENTS.md for hard rules.

## Decisions (frozen)

| Area | Choice |
|---|---|
| Language / runtime | Python + FastMCP (`mcp[cli]`) |
| HTTP client | `httpx` async |
| Tenant model | Per-tool argument (`tenant: "prod" \| "testbed"`) |
| Transport | stdio (default) **and** Streamable HTTP supported |
| Discovery method | Playwright MCP, headed browser, interactive login |
| Production safety | `OWS_PROD_WRITE_ENABLED=1` env + `confirm=true` arg |

## Phase 0 — Discovery & scaffolding *(current)*

Goal: capture enough of the OWS API surface that subsequent phases write typed
wrappers, not guesses.

1. Add Playwright MCP at user scope (DONE).
2. Scaffold repo: `pyproject.toml`, src layout, gitignore, env example,
   docs structure (DONE).
3. Browser walk against **Testbed** Studio:
   - login (interactive)
   - capture: Process, UI/Form, Data orchestration, Service orchestration,
     Asset Store / GDE Store, Data Models, AI orchestration, Python scripts,
     Studio settings/profile.
   - dump per-module XHR/fetch to `docs/discovery/testbed/<module>.json`
4. Browser walk against **Production** (read-only):
   - login, navigate Runtime modules: Work Orders, Alarms, SLA/OLA, Dashboards.
   - dump to `docs/discovery/prod/<module>.json`.
5. Synthesize findings into `docs/discovery.md`:
   auth scheme, base paths per host, sample request/response shapes.
6. Build `auth.py` + `client.py` against testbed; `whoami(tenant)` works.

**Exit criteria:** `uv run ows-gde-mcp serve` returns the logged-in user's
profile from testbed via a single `whoami` tool, using auth captured in step 3.

## Phase 1 — Process orchestration

Tools (all take `tenant`):

| Tool | Read/Write |
|---|---|
| `list_processes(query?, page?)` | R |
| `get_process(process_id, version?)` | R |
| `list_process_versions(process_id)` | R |
| `start_process_instance(process_id, inputs, confirm?)` | W |
| `list_process_instances(filters)` | R |
| `get_process_instance(instance_id)` | R |
| `cancel_process_instance(instance_id, reason, confirm)` | W |
| `list_my_tasks(filters)` | R |
| `complete_task(task_id, form_data, confirm?)` | W |
| `reassign_task(task_id, assignee, confirm)` | W |

**Exit criteria:** start → query → complete a flow on testbed end-to-end.

## Phase 2 — Asset management / GDE Store

| Tool | R/W |
|---|---|
| `list_assets(filters)` | R |
| `get_asset(asset_id, version?)` | R |
| `list_asset_versions(asset_id)` | R |
| `publish_asset(asset_id, version, notes, confirm)` | W |
| `deploy_asset(asset_id, version, target_env, confirm)` | W |
| `download_asset(asset_id, version, dest_path)` | R (local write) |

## Phase 3 — Data model & Data orchestration

| Tool | R/W |
|---|---|
| `list_data_models(filters)` | R |
| `get_data_model(model_id)` | R |
| `query_records(model_id, filter, fields, page)` | R |
| `get_record(model_id, record_id)` | R |
| `create_record(model_id, payload, confirm?)` | W |
| `update_record(model_id, record_id, payload, confirm?)` | W |
| `delete_record(model_id, record_id, confirm)` | W |
| `list_data_flows(filters)` | R |
| `run_data_flow(flow_id, inputs, confirm?)` | W |
| `get_data_flow_run(run_id)` | R |

## Phase 4 — UI / Form metadata (read-only v1)

| Tool | R/W |
|---|---|
| `list_forms(filters)` | R |
| `get_form(form_id, version?)` | R |
| `get_form_for_task(task_id)` | R |

## Phase 5 — Service orchestration / API Fabric

| Tool | R/W |
|---|---|
| `list_services(filters)` | R |
| `get_service(service_id)` | R |
| `invoke_service(service_id, payload, confirm?)` | W (depends) |
| `list_service_runs(service_id, filters)` | R |
| `get_service_run(run_id)` | R |

## Phase 6 — Runtime ops (work orders / alarms / SLA)

| Tool | R/W |
|---|---|
| `list_work_orders(filters)` | R |
| `get_work_order(wo_id)` | R |
| `create_work_order(type, payload, confirm)` | W |
| `transition_work_order(wo_id, action, comment, confirm)` | W |
| `comment_work_order(wo_id, body, confirm?)` | W |
| `list_alarms(filters)` | R |
| `get_alarm(alarm_id)` | R |
| `ack_alarm(alarm_id, comment, confirm?)` | W |
| `dispatch_alarm_to_wo(alarm_id, options, confirm)` | W |
| `list_sla_breaches(filters)` | R |

## Phase 7 — Polish

- Structured logging (request-id, redacted creds).
- Connection pool tuning; retry-with-backoff on 429/5xx.
- `pytest-httpx` recorded fixtures; offline test runs.
- README install + Claude Desktop / Devin / `mcp.json` examples.
- Optional: MCP **resources** for chat-friendly summaries (open tasks, alarms).
- Optional: prompt templates (e.g., "summarize today's testbed alarms").

## Risks (carry-forward)

- API surface is observed, not documented — pin behaviors in tests.
- SSO / CAPTCHA in login path; mitigate with persistent Playwright profile or
  manual cookie paste.
- Sensitive data in responses — opt-in `include_sensitive=true`.
- Rate limits unknown — surface 429s with retry-after.
