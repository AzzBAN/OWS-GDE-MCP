---
tags: [platform, findings, model-api]
---
# ServiceInvoker and Model API

Model instances are read/written via `ServiceInvoker.post()` against `/adc-model/rest/` endpoints. Model URIs: `/projectName/moduleName/modelName`, always as a query-string parameter.

## The try/catch rule (non-negotiable)

**Every `ServiceInvoker` call gets its own try/catch.** ADC throws a generic `"Invoke service failed"` with zero context — without a granular catch logging the TQL/endpoint, the failure is unrecoverable from logs.

```javascript
var res;
try {
    res = ServiceInvoker.post("/adc-model/rest/v1/...", payload);
} catch (e) {
    console.log("[fnName] ServiceInvoker failed: " + (e.message || String(e)));
    console.log("[fnName] TQL: " + payload.tql);
    throw e;
}
```

## Endpoint cheat sheet

| Operation | Endpoint | Field access in response |
|---|---|---|
| Filtered find | `POST /v1/model-instances/base-instances/find?modelUri=…` | `instance.property_values.field` |
| Full SELECT / cross-project | `POST /v1/model-instances/query-by-tql` | `row.field` (**flat**, top-level) |
| By id / keycode | `GET /v1/model-instances/find-by-id` / `find-by-keycode` | `result.property_values.field` |
| Create | `POST /v2/model-instances/batch-create?uri=…` | `result.result` → new id array |
| Update by TQL | `POST /v2/model-instances/batch-update-tql?uri=…` | `result.successCount` |
| Update by id | `POST /v2/model-instances/batch-update?modelUri=…` | 200 no body = success |

## query-by-tql response-shape finding

The correct endpoint is **v1** (not v2), and the response is `{ results: [...], total: N }` — **not a flat array**. `total` is unreliable (may be `-1`). Always:

```javascript
var rows = (res && res.results) ? res.results : [];
```

Pagination: stop on `rows.length < PAGE_SIZE` — see [[TQL Findings]].

## Write conventions

- `base_instance_parameter: { enable_trigger: false }` on creates/updates — suppresses downstream triggers; set `true` only deliberately.
- **CPQ rule: no delete.** The batch-delete-tql endpoint exists but must never be used in CPQ scripts.
- Ticket creation does **not** use these endpoints at all — it goes through [[BPM Services]].

## CMDB model URIs

```
/datahub/cmdb/cmdb_site
/datahub/cmdb/cmdb_device
/datahub/cmdb/cmdb_fm_office     — tower provider (owner)
/datahub/cmdb/cmdb_ne_type
/datahub/cmdb/cmdb_power         — ⚠ B-04: unverified, see [[Blockers]]
```
