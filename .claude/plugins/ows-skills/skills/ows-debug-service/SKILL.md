---
name: ows-debug-service
description: Debug a failing or misbehaving OWS service — search logs, trace execution, walk flow steps. Use when a service returns unexpected results or errors.
---

# OWS Debug Service Skill

## Delegate to a subagent when possible

If the `Agent` tool is available, dispatch the log + flow reads to a subagent (general-purpose). Logs and flow blobs are payload-heavy and stay in the transcript verbatim — keep them in the subagent.

Brief it with the failing service, expected vs observed, and ask it to return: root cause, evidence (file:step or log timestamp), and the recommended fix. Not raw logs or flow JSON.

If `Agent` is unavailable, follow the steps below directly and use `content_preview_chars=200` on `search_service_logs` unless you are specifically grepping a stack trace.

## Steps

1. **Search recent logs** — use `search_service_logs(tenant, project_name, module_name, service_name, log_level="ERROR")`.
   - Default window is last 3 days
   - Look for `trace_id` in the results — you'll need it for step 2

2. **Get the full trace** — use `get_log_trace(tenant, trace_id)` to see the complete call chain in chronological order.
   - Shows every service invoked in the request, in order
   - Identifies exactly which step failed and what the error was

3. **Inspect the service flow** — use `get_service(tenant, project_name, module_name, service_name, flow_only=True)`.
   - Walk the `flow` steps to understand the logic
   - Cross-reference with the failing step from the trace

4. **Check scripts** — if a RunScript step is failing, use `get_service_script(tenant, project_name, module_name, script_name)` to read the JS body.

5. **Test the service** — use `invoke_service(tenant, project_name, module_name, service_name, payload={...})` to reproduce the issue.
   - On testbed only unless `confirm=True` on prod
   - Mirror the input shape from the flow's input schema

## Reading Logs

| Field | Meaning |
|-------|---------|
| `log_level` | ERROR / WARN / INFO |
| `trace_id` | Correlates all logs from one request |
| `element_name` | The service that logged this |
| `duration_ms` | How long this step took |
| `log_content` | The actual error message / stack trace |

## Common Error Patterns

- `NullPointerException` in RunScript → check input field mapping, a required field is null
- `TQL compile failed` → field name mismatch, use `get_model_fields` to verify
- `403 / permission denied` → service `open_level` mismatch or missing role
- `timeout` → downstream service slow, check `duration_ms` across the trace

## Notes

- Always start with logs before reading code — the trace tells you exactly where it broke
- `content_preview_chars=0` on `search_service_logs` to get full error messages when the default 200 chars truncates the stack trace
