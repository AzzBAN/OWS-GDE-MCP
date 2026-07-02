---
tags: [platform, findings, utilities]
---
# Platform Utility Functions

The platform-provided globals available to a RunScript (no `require`/`import` — they are
ambient Rhino globals). This note catalogs the ones **actually exercised** in `src/phase1-sfo`,
with exact signatures and the gotchas found in use. Model-store specifics live in
[[ServiceInvoker and Model API]]; this note covers the wider utility surface.

> **Provenance / scope:** the `MultiPart` + file-token findings were harvested from
> `sfo_attachment_create.js`, which is otherwise excluded from deep documentation per the
> vault brief. They are recorded here as **reusable platform capabilities** (any binary
> upload would use them), not as attachment-feature docs.

## `ServiceInvoker` — the workhorse (37× post, 4× invoke, 2× get)

| Call | Signature | Notes |
|---|---|---|
| `ServiceInvoker.post(uri, body)` | returns parsed JSON | the default for model + service calls |
| `ServiceInvoker.get(uri)` | returns parsed JSON | e.g. processing-task-info, find-by-id |
| `ServiceInvoker.invoke(...)` | — | **not called by us directly**; BPM scripts call it *internally* (e.g. `createTicketScript`), which is the source of the opaque `"Invoke service failed"` throw — see [[BPM Services]] and the catch-the-throw pattern in `sfo_new_forecast.js` / `sfo_reforecast.js` |

Every call gets its **own** try/catch — ADC errors carry no context. See [[ServiceInvoker and Model API]].

## The `cse://` internal-service scheme

Most calls use relative paths (`/adc-model/rest/...`, `/adc-service/rest/...`, `/adc-bpm/rest/...`).
The `adc-file` service is instead addressed with the **`cse://`** scheme (Cloud Service Engine
internal routing) rather than a relative path:

```
cse://adc-file/rest/v1/file-token/new-file-token
cse://adc-file/rest/v1/file-token/upload?file_token={file_token}
```

`{placeholder}` segments in a `cse://` URL are substituted from a params object (see `MultiPart.post` below).

## `MultiPart` — multipart/form-data uploads

`MultiPart` (capital **P** — `Multipart` will not resolve) is the only way to send a
multipart body. Four-argument form:

```javascript
MultiPart.post(
  "cse://adc-file/rest/v1/file-token/upload?file_token={file_token}", // 1: URI w/ {placeholders}
  { file: base64Data },                                               // 2: body parts (key → value)
  ["file"],                                                           // 3: which keys are file parts
  { file_token: token }                                              // 4: values substituted into {…} in the URI
);
```

| Arg | Meaning |
|---|---|
| 1 | target URI; `{name}` tokens are filled from arg 4 |
| 2 | parts object — `{ partKey: value }` |
| 3 | array of part keys to treat as **file** parts (vs plain form fields) |
| 4 | path/query substitution params for the URI placeholders |

## adc-file file-token flow (two steps)

1. **Mint a token** — `ServiceInvoker.post("cse://adc-file/rest/v1/file-token/new-file-token", {})`.
   ⚠️ The token **is the entire `result` string**, not a `result.file_token` key:
   ```javascript
   var token = (tokRes && tokRes.result) ? tokRes.result : null;
   ```
2. **Upload against the token** — `MultiPart.post(.../upload?file_token={file_token}, { file: base64 }, ["file"], { file_token: token })`.

**B-05 (open):** the upload step fails with `"Invalid file token length"`. Because base64 in
the model is the durable source of truth, the upload is treated as **best-effort / soft-fail** —
`attemptUpload()` never throws; on any token/upload error it returns
`{ file_token: "", upload_status: "stored" }` and the create proceeds. See [[Blockers]].

## `ApplicationEnvironment.getVariable(name)` — credentials & URLs

The sanctioned way to read ADC environment variables (endpoints, credentials) — **never
hardcode secrets in source**. Guard the global, as it may be absent in some contexts:

```javascript
var url = (typeof ApplicationEnvironment !== "undefined")
  ? ApplicationEnvironment.getVariable("SF_CALLBACK_URL")
  : null;
```

Used today in `callback_sfo.js`; the [[callback_sfo]] rewrite plan sources the outbound
endpoint + Basic-auth header this way (`SF_UPDATE_FORECAST_URL` / `_AUTH`).

## `console.log` — the only logging facility (212×)

No structured logger, no levels. Everything observable goes through `console.log`. Convention:
prefix each line with the function name — `console.log("[fnName] …")` — since that prefix is
the only way to trace which function emitted a line in the flat ADC log. `JSON.stringify`
(no native pretty-printer guarantee) is used to dump payloads/responses.

## Standard JS built-ins

`JSON.parse` / `JSON.stringify` and `new Date()` are available (date handling per the WIB
rules in [[ADC RunScript Constraints]]). The forbidden array methods and the top-level
`return` requirement also live in [[ADC RunScript Constraints]].
