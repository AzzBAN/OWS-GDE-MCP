---
tags: [platform, findings, runscript]
---
# ADC RunScript Constraints

All discovered from production failures — treat as hard constraints. Server-side (Rhino2) runtime only; browser-side rules live in [[OWS Page Script Patterns]].

## Return value must be top-level

ADC only captures a **top-level `return`**. A `return` inside an IIFE without an outer `return` is silently discarded — output_node receives `{}`.

```javascript
// WRONG — silently discarded
(function main() { return { success: "true" }; })();

// CORRECT
return (function main() { return { success: "true" }; })();
```

## Forbidden array methods

`.map()`, `.filter()`, `.reduce()`, `.forEach()`, `.find()` — runtime throws on execution. `for` loops only. (Project-wide rule, also applied to page scripts.)

## 20,000,000 JS command quota

Every operation counts (assignments, comparisons, loop increments). On overflow:
```
The script quota [JS Command] reaches [20XXXXXX times] and exceeds the threshold [20000000 times]
```
Strategies: fan out via `ServiceInvoker.post()` (each call gets a fresh 20M budget); single-pass loops; isolate TQL calls into dedicated scripts.

Recommended heavy-work topology: **orchestrator** (fan-out) → **data fetch** (one TQL per invocation) → **aggregation** (pure JS, single-pass).

## Date handling

- Space separator → `Invalid Date`. Always `String(v).trim().replace(" ", "T")` before `new Date()`.
- **WIB (UTC+7)**: no timezone library — offset manually with `WIB_OFFSET_MS = 7*3600*1000`, and **always use `getUTC*()` on shifted dates**, never `getFullYear()`/`getMonth()`.

## Misc hard rules

| Rule | Detail |
|---|---|
| Module format | AMD only — no ES6 `import`/`export` |
| `ServiceInvoker` arity | Exactly 2 arguments; a third throws |
| `_message.start/limit` | `undefined` when invoked standalone — always apply fallbacks before passing to TQL |
| Excel date columns | Declare as `TEXT`, format in translator — `DATETIME` renders `####` |
| Export task fetch | `dir: "DESC"` to get the newest record |
| Dev mode detection | `ApplicationEnvironment.getDomainName() === "1057-sg-studio.teleows.com"` |
| OWS rate limit | 200 req/min; credentials via ADC env vars only |

## Known data quirks

- `BusinessStatusResovled` — platform typo, intentional, use exactly as-is.
- SFO bandwidth unit is **Gbps**; B2B expects Mbps — multiply by 1000.
- `submit_type = "new"` → omit `orderid`; `"resubmit"` → `orderid` required.

Related: [[TQL Findings]] · [[ServiceInvoker and Model API]]
