---
name: ows-flow-debug
description: Trace and debug end-to-end flows in OWS — page → service, service → service, and page → page navigation. TRIGGER when the user asks "why is X failing", "what's wrong with this page/service", "trace the flow of Y", "audit the call chain", or describes broken behavior in an OWS app. Inspects flow steps, RunScript bodies, input/output schemas, log traces, and reference graph; identifies bad code patterns (silent catch, hardcoded IDs, missing validation), schema mismatches (caller passes X but service expects Y), and dead branches; reports findings with concrete file/step/line locations and recommended fixes.
---

# OWS Flow Debug Skill

Use when something in an OWS app is broken or behaving unexpectedly and you need to trace the full call chain to find root cause.

## Quick Start: I have a service error message

If you already have a specific error (stack trace, error code, failed service name), skip the broad flow tracing and go straight:

1. `search_service_logs(service_name=..., log_level="ERROR", content_preview_chars=0)` — find the failing call; use `content_preview_chars=0` for full stack traces.
2. `get_log_trace(trace_id=...)` — pull the cross-service trace from the error's `trace_id`.
3. `get_service(..., flow_only=True)` — read the failing service's flow steps.
4. `get_service_script(...)` — read the RunScript body if the error points at a script step.
5. `invoke_service(..., payload={...})` — reproduce on testbed (`confirm=True` on prod), mirroring the flow's input schema.

Then resume the full Steps below if the root cause spans callers/callees.

**Common error patterns:**
- `NullPointerException` in RunScript → input field mapping, a required field is null
- `TQL compile failed` → field name mismatch, verify with `get_model_fields`
- `403 / permission denied` → service `open_level` mismatch or missing role
- `timeout` → downstream service slow, check `duration_ms` across the trace

## Delegate to a subagent when possible

This skill walks call chains across pages, services, scripts, and logs — the payloads add up fast and a single trace can blow past the 32MB context limit. If the `Agent` tool is available, dispatch the trace to a subagent (general-purpose):

- Brief it with the four anchors from Step 1 (entry point, trigger, observed, expected)
- Ask it to walk the chain using the steps below
- Have it return only the report from Step 5 (root cause, evidence, call chain, fix, confidence)
- It must NOT return raw flow JSON, full SPL trees, or full log bodies

If `Agent` is unavailable (you are already a subagent), follow the skill directly and use lean variants: `get_service(flow_only=True)`, `get_page_detail(parsed=True)`, `find_artifact_references(with_excerpts=False)`, `search_service_logs(content_preview_chars=200)`.

Three flavors:

- **Page → Service** — a button or load action calls a service and the response is wrong
- **Service → Service** — an orchestration service calls a downstream service that fails
- **Page → Page** — navigation from one page to another loses context or shows wrong data

## Step 1: Frame the failure

Before opening any tool, get from the user (or infer from context):

- **What page / service is the entry point?** (e.g. `CIT_Query_v2`, `centralize_inquiry_ticket_get_list_datagrid`)
- **What does the user click / what triggers the failure?** (page load, button click, row click, save)
- **What is the observed behavior?** (error toast, empty grid, wrong field, slow, hang)
- **What is the expected behavior?**
- **Is it always reproducible, or only for certain inputs?**

Without these four anchors, the trace becomes a fishing expedition. Ask if any are missing.

## Step 2: Build the call graph

### Page → Service entry point

1. `get_page_detail(page_id, parsed=True)` — find every `service_refs[]` wired to the page
2. `get_page_scripts(page_id, include_content=True)` — read `init`, `events`, `utils` JS to see which service the failing action actually invokes (SPL has the *list*, scripts pick *which one runs when*)
3. `get_service(project, module, service_name, flow_only=True)` — open the flow

### Service → Service hop

For each service in the chain:

1. `get_service(flow_only=True)` — find every `InvokeService` step's `service_rest_uri`
2. `get_service_script(script_name)` for any `RunScript` step in between — these often transform input/output and are the most common failure points
3. Build the call tree mentally:
   ```
   svc_A
   ├─ RunScript: validate_input
   ├─ InvokeService: svc_B
   │   ├─ QueryModel: tt_troubleticket
   │   └─ RunScript: format_output
   └─ RunScript: merge_response
   ```

### Page → Page navigation

1. `get_page_detail(parsed=True)` on the source page — find `redirectButton`, `linkColumn`, or scripts using `$page.navigate` / `window.location`
2. Identify what context (IDs, params) the source passes
3. `get_page_detail(parsed=True)` on the destination page → look at its `init` script
4. Verify the destination's `init` reads the same param names the source sets

## Step 3: Confirm with logs

For each suspicious service:

- `search_service_logs(service_name=X, log_level="ERROR", content_preview_chars=0)` — full stack traces, last 3 days
- If you find a hit, grab the `trace_id` and run `get_log_trace(trace_id)` to see the entire request chain in chronological order
- Cross-reference each log step with the flow step to identify exactly where the chain broke

If logs are silent, the failure is either pre-API (page-script bug, never sent the request) or older than 3 days (retention).

## Step 4: Audit code patterns

When reading flow steps and RunScripts, watch for these failure-prone patterns:

### Bad: silent catch
```javascript
try {
    var x = input.get("foo").bar;
    output.put("result", x);
} catch (e) {
    // swallowed — caller never knows
}
```
**Why it breaks:** caller sees success, downstream gets `null`.
**Fix:** rethrow or set an explicit error field.

### Bad: hardcoded IDs that won't survive promotion
```javascript
var siteId = "affaa3ee-3312-11ed-803b-0255ac120083";
```
**Why it breaks:** UUIDs differ between testbed and prod.
**Fix:** look up by name or pass via input.

### Bad: missing required-field validation
```javascript
output.put("ticket_id", input.get("ticket_id").toUpperCase());
```
**Why it breaks:** NPE when `ticket_id` is null.
**Fix:** validate at top, throw with clear message.

### Bad: schema mismatch on InvokeService
- Caller flow input schema says `{order_id: string}`
- Callee service expects `{orderId: string}` (camelCase) or `{order_id_view: string}`
- The Studio playground may auto-fix one path but not the other

**Detection:** compare caller's `RunScript` (the one preparing the InvokeService payload) field-by-field against callee's flow input schema.

### Bad: TQL with the wrong field name
```javascript
var rows = query("select * from \"...\" as t order by t.createTime desc");
// model field is `createtime`, lowercase — TQL fails
```
**Detection:** confirm field name via `get_model_fields(asset_uri)`.

### Bad: dead branches in flow conditionals
A flow has a `Condition` node with paths `success` / `failure`, but the `failure` path has no logging or output mapping — when it fires, the caller gets silence.

### Bad: timing assumption (race conditions)
Service A creates a ticket, then immediately reads it back via TQL. The read can hit a replica before the write replicates → empty result.
**Fix:** use the create response, not a follow-up query.

### Bad: page script reads from response before checking error
```javascript
var res = $service.invoke("svc", payload);
$component.get("grid").setData(res.data);  // res may be {error: ...}
```

## Step 5: Report findings

Format the report so it's actionable:

```
ROOT CAUSE
  <one sentence>

EVIDENCE
  - <file>:<location> — <what you found>
  - log trace <trace_id> at <timestamp> — <what it shows>

CALL CHAIN (where it broke)
  Page CIT_Query_v2 (events.js:42)
    └→ service centralize_inquiry_ticket_get_list_datagrid (flow step 3: RunScript filter_input)
        └→ TQL compile error: "createTime" field not recognized
        └→ caller swallows the 500 in catch block, returns []

WHY THE USER SEES IT
  Empty grid even though data exists.

RECOMMENDED FIX
  1. <concrete change>
  2. <concrete change>

CONFIDENCE
  high / medium / low + reason
```

Always state confidence honestly — if you couldn't read a script (Studio access denied on prod) or logs were stale, say so.

## Helpful MCP tools (current)

- `get_page_detail(parsed=True)` — page structure + service refs
- `get_page_scripts` — JS layer behavior
- `get_service(flow_only=True)` — flow steps
- `get_service_script` — RunScript JS body
- `get_model_fields` — verify TQL field names
- `find_artifact_references` — who else calls this
- `search_service_logs` / `get_log_trace` — runtime evidence
- `query_model_data` — verify data state matches expectation

## Proposed new MCP tools (if these would help)

These don't exist yet but would close gaps the current toolset has for flow debugging:

### 1. `walk_service_chain(tenant, service_uri, max_depth=5)`
Recursively follow `InvokeService` steps and return a flattened call tree with:
- Every service in the chain
- Every RunScript inline body
- Every model touched
- Schema mismatches automatically flagged where caller payload doesn't match callee input schema

**Why:** today we manually call `get_service` per hop. Flows with 5+ services become tedious and error-prone to trace.

### 2. `diff_service_io(tenant, caller_uri, callee_uri)`
Take two services, parse the caller's `InvokeService` payload preparation step, parse the callee's input schema, return field-level diff:
- Fields the caller sends that the callee ignores
- Fields the callee requires that the caller doesn't send
- Type mismatches (`string` vs `number`)

**Why:** schema drift is one of the top failure modes and tedious to spot by eye.

### 3. `lint_service_script(tenant, script_name)`
Static analysis of a RunScript body for known anti-patterns:
- `try {} catch(e) {}` empty catches
- Hardcoded UUIDs / URLs
- Reads on possibly-null inputs without guard
- Missing `output.put` on a path that the flow expects

**Why:** these are the patterns this skill tells Claude to look for; codifying them as a tool means consistent detection without re-reading the code each time.

### 4. `get_page_navigation_graph(tenant, project, module)`
Scan every page in a module, follow `redirectButton`, `linkColumn`, and `$page.navigate` calls, return a directed graph of page → page transitions plus the params each hop carries.

**Why:** debugging "wrong data on the destination page" requires knowing every entry point. Today we'd have to read every page manually.

### 5. `resolve_uuid(tenant, uuid)`
Given a UUID found anywhere (alarm name id, fault level id, region id), return the human-readable label by checking common reference models.

**Why:** ticket records are full of UUIDs (`317cf2d1-b324-11ed-a524-0255ac12038a` for "Critical" fault level). Flow debugging requires translating these constantly.

### 6. `replay_service_call(tenant, trace_id)`
Reconstruct the input payload from a logged trace and re-invoke the service on testbed with the same payload. Useful for reproducing prod failures in testbed without manual data copy.

**Why:** "we have the trace, now reproduce it" is a five-step manual process today.

## Notes

- Always start from the failure symptom and work backward — don't audit the whole module
- Don't propose fixes you can't verify (e.g. don't say "race condition" without log evidence of the timing)
- If two services share a name across modules, name the full URI in the report
- Treat absence of logs as "couldn't verify", not "no problem there"
