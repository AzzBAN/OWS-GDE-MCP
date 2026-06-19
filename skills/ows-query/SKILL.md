---
name: ows-query
description: Query OWS model data — resolves process prefix, discovers fields, builds and runs TQL. Use when asked about tickets, CMs, INCs, BOTs, or any process data.
---

# OWS Query Skill

## Steps

1. **Resolve the process** — use `resolve_process_by_prefix` with the ticket prefix (CM, INC, BOT, TTS, etc.) to get `tickets_uri`.

2. **Discover fields** — if the query needs a field you're unsure about, use `get_model_fields(asset_uri=tickets_uri)` to find the exact field name. Field names are snake_case and may differ from their display labels (e.g. `createtime` not `createTime`).

3. **Build TQL** — use this syntax:
   ```
   select * from "<tickets_uri>" as t where <conditions> order by t.<field> desc limit <N>
   ```
   - Always quote the asset URI with double quotes
   - Always alias the model (e.g. `as t`)
   - Use `t.<fieldname>` for ordering and filtering

4. **Run the query** — use `query_model_data(tenant, tql)`. It validates before executing.

5. **Present results** — extract and show only the relevant fields in a table. Don't dump all 200+ fields.

## Common Fields

| Field | Meaning |
|-------|---------|
| `createtime` | When the ticket was created |
| `lastupdatetime` | Last update |
| `ticketstatus` | running / closed / aborted |
| `task_status` | dispatched / accepted / completed |
| `orderidview` | Human-readable ticket ID |
| `title` | Ticket title |
| `region` | Geographic region |
| `site_id_name` | Site ID |
| `assign_to_fme_full` | Assigned engineer name |
| `fault_type` | Wireless / Transmission / Power |

## Notes

- Always use `tenant: "prod"` for real data unless the user says testbed
- If TQL fails with "field not recognized", re-check field name via `get_model_fields`
- For top-N newest, use `order by t.createtime desc limit N`
- For filtering by date: `t.createtime >= '2026-05-20 00:00:00'`
