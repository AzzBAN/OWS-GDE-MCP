# Plan — `ows-gde-mcp`

Authoritative phasing & scope for this repo. See README.md for context and
AGENTS.md for hard rules.

> AGENTS.md is the working plan; this file is being aligned with it. Phase 1
> in this repo is artifact introspection, not the process-orchestration tools
> originally drafted below.

## Decisions (frozen)

| Area | Choice |
|---|---|
| Language / runtime | Python + FastMCP (`mcp[cli]`) |
| HTTP client | `httpx` async |
| Tenant model | Per-tool argument (`tenant: "prod" \| "testbed"`) |
| Transport | stdio (default) **and** Streamable HTTP supported |
| Discovery method | Playwright MCP, headed browser, interactive login |
| Production safety | `OWS_PROD_WRITE_ENABLED=1` env + `confirm=true` arg |
| Path validation | Reject absolute URLs and `..` traversal at OwsClient.request layer |
| Write-gate placement | Enforced in OwsClient.request for all non-GET prod requests; per-tool gating no longer required |
| Session refresh | Headless CAS auto-relogin in `auth_login.py`, triggered by 302→`/dspcas/login` and pre-warmed at server startup. Optional `[login]` extra (`playwright`). |
| Auth cache | Per-process `AuthContext` cache keyed by tenant — refreshed cookies survive across tool calls (cleared on MCP restart). |
| Default payload size | List/get tools return summary by default; full data behind `include_*` / `*_only` opt-ins. |

## Phase 0 — Discovery & scaffolding *(complete)*

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

- Exit criterion met: `whoami` returns the user profile from testbed via
  captured auth.

## Phase 1 — Artifact introspection (Studio + offline `.gpk`) *(complete)*

The shipped v1 surface for "what is X in our OWS?" — Studio metadata via the
live API, plus offline `.gpk` package introspection that needs no auth.

| Tool | Source | R/W |
|---|---|---|
| `list_app_packages`, `get_app_package_info`, `list_app_artifacts`, `get_app_artifact`, `search_app_artifacts` | offline `.gpk` | R |
| `list_live_menus`, `list_live_apps`, `get_favorite_menus` | live portal | R |
| `list_studio_projects`, `get_studio_project`, `list_project_modules`, `get_studio_module`, `list_studio_element_types` | live Studio mgmt | R |
| `list_models`, `get_model`, `get_model_fields` | live Studio Model | R |
| `list_services`, `get_service` | live Studio Service | R |
| `list_pages`, `get_page`, `get_page_detail` | live Studio Page | R |
| `list_scripts` | live Studio MCP-Script | R |
| `list_triggers`, `get_trigger` | live Studio Trigger | R |
| `call_ows_api` | escape hatch | R/W (gated) |

**Exit criteria:** All common artifact types covered by `list_*` / `get_*`
plus the studio element-type catalogue.

## PR2/PR2.5/PR3 — Cross-reference + audit *(complete, 2026-05-16)*

Cross-reference analysis combining static refs (services + pages + triggers)
with runtime log evidence to answer "is this artifact actually used?".

| Tool | Sources scanned |
|---|---|
| `find_artifact_references(target_uri)` | services flow + pages content + triggers |
| `find_unused_artifacts(project, module, type)` | same |
| `audit_artifact_usage(project, module, type)` | static refs + runtime logs (3-day window) |
| `search_service_logs`, `get_log_trace`, `count_service_invocations` | Log Analysis service |

Confidence ratings on `audit_artifact_usage` candidates:
`low` (services + pages only), `medium` (+ triggers; current default),
`high` (+ workflows; reaches `high` after workflow scanning lands).

See `docs/audit-confidence.md` for what the ratings mean.

**Open coverage gaps (future PRs):**
- Workflow BPMN scanning — activities inside a workflow that invoke
  services don't surface as static refs yet.
- TQL dot-notation refs — `modelInstanceTqlQuery.tql` strings that
  reference models via `<project>.<module>.<name>` (vs slash form).
- External callers (other tenants, REST API consumers, RPA bots) — by
  nature invisible to static analysis; documented as a permanent caveat.
- `from_package` offline-mode for the audit/reference tools — currently
  raises `NotImplementedError`; live-only for now.

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
| `invoke_service(service_id, payload, confirm?)` | W (depends) |
| `list_service_runs(service_id, filters)` | R |
| `get_service_run(run_id)` | R |

Studio-side `list_services`/`get_service` already shipped in Phase 1; this
phase covers runtime invocation/observability.

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

## Future — Process runtime (was Phase 1, deferred)

Runtime orchestration of business processes — distinct from Studio-side
introspection of process *definitions*. Not part of v1.

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

## Risks (carry-forward)

- API surface is observed, not documented — pin behaviors in tests.
- SSO / CAPTCHA in login path; mitigate with persistent Playwright profile or
  manual cookie paste.
- Sensitive data in responses — opt-in `include_sensitive=true`.
- Rate limits unknown — surface 429s with retry-after.
