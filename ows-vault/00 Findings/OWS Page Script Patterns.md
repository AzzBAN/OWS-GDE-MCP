---
tags: [platform, findings, page-scripts]
---
# OWS Page Script Patterns

Browser-side rules for scripts bound via `Nf.ready(...)` on OWS form phases. All discovered from live production debugging of the SFO forecast workflow. Distinct runtime from [[ADC RunScript Constraints]].

## Core API

```javascript
Nf.ready(function () {
  S("componentId").getValue() / .setValue(v) / .show() / .hide() / .setReadOnly(true);
});
Spl.EventBus.register("componentId", "ValueChange", handler);
S("gridId").setCellValue(rowIndex, "columnName", value);
```

## safeGet — `S()` returns `undefined` for absent components

If a component isn't on the current phase's form layout, `S(id)` is `undefined` and `.getValue()` crashes the entire page script. Always guard cross-phase reads:

```javascript
function safeGet(fieldId) {
  var comp = S(fieldId);
  if (!comp) return null;
  return comp.getValue();
}
```

Log a boot warning when required fields are missing so the developer knows what to add in the form designer.

## Dual event names — handlers can fire twice

OWS fires both `"ValueChange"` and `"value-change"` for one user interaction on some components. Registering both = double execution of API calls and field writes. **Rule:** handlers with side effects register `"ValueChange"` only.

## Phase-to-phase data carry needs bound components

Model column values persist on the ticket, but a page script can only read a column if a **form component bound to it exists on that phase's layout**. Downstream phases (Validate / CapCheck / Confirm) need hidden read-only bound components for: `bandwidth`, `new_bandwith`, `existing_bw_mbps`, `order_type`, `new_forecast_type`, `reforecast_reason`. Without them, `commitBW()` silently no-ops.

## applyResultData cascade — delete trigger fields first

Loading an SFO record and applying it can re-fire handlers bound to fields in the result (e.g. a reforecast ticket's own `reference_existing_sfo_id` re-triggers the load handler and overwrites the operator's selection with an older ticket's data):

```javascript
delete response.result.reference_existing_sfo_id;  // strip before applying
applyResultData(response.result);
```

## circuit_path grid rules

- `afteredit`: always guard `if (rowIndex < 0 || !path) return;` before touching the row.
- `.toFixed(2)` on every numeric cell write (floating-point noise).
- Guard `bwCap > 0` before any utilization division.
- `utilization` (= total_bandwidth/capacity) and `utilization_existing` (= throughput/capacity) are **different columns** — never write both from one formula.
- Status roll-up: write `path.<field>` **in memory** as well as via `setCellValue` before calling `autoStatus`, or it reads stale values. Call order: NE → utilization → port → roll-up.

## autoSet transport thresholds

Transport dropdown keycode is `"IP"` — the old script's `"IP MPLS"` never matched, leaving IP thresholds silently dead. Thresholds: IP > 85%, MW > 75%, DWDM/GPON/SDH/FO Cable > 100%, empty → NA.

## commitBW — terminal phase exits only

Writes committed BW into `existing_bw_mbps` so the **next** reforecast can read the pre-change value. Three commit points: Validate (`operation_executor="close"`), CapEsc (`operation_escalation="accept"`), Confirm (`operation_submitter="Close"`). Post-normalization it's scenario-agnostic — see [[BW Field Normalization]].

## Form designer notes

- Static default visibility is applied **before** `Nf.ready` — fields that should start hidden must default to "hidden" in the designer, or they flicker. Don't hack around it in JS.

## Phase script map

| Phase | Script |
|---|---|
| Create / Reforecast | `create_phase_page_script.js` |
| Validate Order | `validate_phase_page_script.js` |
| Capacity Escalation | `capacity_check_phase_page_script.js` |
| Confirm Order | `confirm_phase_page_script.js` |

Refactored versions: `reference/refactored/`. They appear in the code graph (`graph/graph.canvas`).
