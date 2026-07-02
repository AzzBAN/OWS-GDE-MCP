---
tags: [platform, findings, tql]
---
# TQL Findings

TQL (Top Query Language) is ADC's SQL-like model query language. Two forms with different rules — mixing them up produces silent empty results.

| Form | Used in | Syntax |
|---|---|---|
| **Data-filtering TQL** | V1 `condition_tql`, trigger conditions | WHERE body only |
| **Complete TQL** | `query-by-tql` | Full `SELECT … FROM … WHERE …` |

## The string-quoting trap (production-confirmed)

In **complete TQL**, string parameters in equality conditions **must be single-quoted** — bare `$param` compiles but silently returns no rows:

```sql
where orderid = $orderid     -- WRONG: zero rows, no error
where orderid = '$orderid'   -- CORRECT
```

Data-filtering TQL does **not** want quotes — use bare `$param` there.

## Optional parameters

- `$!varName` — **self-erasing**: if null/empty/missing, the whole containing condition drops out. Use for optional filters.
- `ifmissing($author, 'ignore')` / `ifempty($author, 'value', 'Unknown')` — same idea for data-filtering TQL.

## COUNT syntax (GaussDB)

- `count('*')` — single-quoted asterisk; bare `count(*)` is a runtime error.
- Conditional counting: `SUM(CASE WHEN … THEN 1 ELSE 0 END)`, not `COUNT(CASE WHEN …)`.

## NOW() arithmetic is in seconds

```sql
(NOW() - create_time) / 3600 as aging_hours      -- CORRECT
(NOW() - create_time) / 3600000 as aging_hours   -- WRONG: near-zero result
```

## Pagination

- Default 1000 rows, **hard cap 5000** regardless of `limit`.
- **Never trust `result.total`** (may be `-1`, may be stale mid-pagination). Stop on `page.length < PAGE_SIZE` only.
- Always pair `ORDER BY` with `START…LIMIT` for stable page boundaries.

## Other rules

- Column aliases can't be referenced in WHERE — repeat the expression.
- GROUP BY must list every non-aggregated SELECT column.
- Cross-project models in FROM need the full URI in **double quotes**: `from "/cmdb-project/network/sites"`.
- Filter option fields by `keycode`, never display label (and remember the `BusinessStatusResovled` typo).

Related: [[ServiceInvoker and Model API]] · [[ADC RunScript Constraints]]
