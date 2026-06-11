# Service flow node-type catalogue

Captured by walking 213 `SERVICE/<name>.json` artifacts across 6 `.gpk`
packages (ICTSM_ChangeRequest, ID_IOH_BO_Helpdesk, c_TroubleTicket,
centralized_inquiry_tracker, thirdparty_dashboard, tt_improvement).

A service flow consists of named **steps** under `flow.steps.<name>`, each
with a `type` field. The reference scanner walks every step looking for
URI-bearing fields. This file catalogues the URI fields per step type so
the scanner can classify matches as `strong` (typed URI field) vs `weak`
(substring match elsewhere).

## Step types observed

| Type                       | URI-bearing fields                                                                 | Count |
|----------------------------|------------------------------------------------------------------------------------|-------|
| `input`                    | `input.bind_model_uri`, `input.properties[...].bind_model_uri` (recursive)         | 210   |
| `output`                   | `output.bind_model_uri`, `output.properties[...].bind_model_uri` (recursive)       | 210   |
| `runScript`                | `script_name` (bundled JS file under `SERVICE/RunScript/.../<name>.js`)            | 63    |
| `modelInstanceGetList`     | `model_uri`                                                                        | 25    |
| `modelInstanceGet`         | `model_uri`                                                                        | 18    |
| `modelInstanceCreate`      | `model_uri`                                                                        | 16    |
| `invokeService`            | `service_uri` (full `/adc-service/rest/v1/services/<proj>/<mod>/<svc>` form)       | 16    |
| `modelInstanceUpdate`      | `model_uri`                                                                        | 15    |
| `modelInstanceBatchDelete` | `model_uri`                                                                        | 15    |
| `modelInstanceBatchUpdate` | `model_uri`                                                                        | 15    |
| `modelInstanceBatchUpsert` | `model_uri`                                                                        | 15    |
| `modelInstanceTqlQuery`    | `tql` (SQL-like text; embeds `<project>.<module>.<model>` dot-form references)     | 7     |
| `modelInstanceUpsert`      | `model_uri`                                                                        | 3     |
| `batchOperation`           | `service_uri`                                                                      | 1     |

## Findings

### Already-handled by the existing `_walk` + `_STRONG_URI_FIELDS`
- `model_uri`, `bind_model_uri`, `service_uri`, `service_rest_uri`,
  `script_uri`, `asset_uri`, `serviceName`, `serviceId`, `service_id`,
  `location` — confirmed working since they are leaf field names regardless
  of nesting depth.
- The recursive `input.properties[...].bind_model_uri` pattern is caught
  because the scanner walks the full tree and matches on the *terminal*
  field name, not the dotted path.

### New strong-URI fields discovered
None — all URI fields observed in this sample use the names already in
`_STRONG_URI_FIELDS`. The scanner is correct for service flows.

### Two patterns the scanner does NOT yet handle correctly

#### 1. `modelInstanceTqlQuery.tql` — TQL strings with dot-notation
Sample:
```
select cmdb_site.site_id, cmdb_site.site_name, ... from cmdb_site
```
The TQL references models via `<table>.<column>` dot-notation, not URI form.
For a model `/<proj>/<mod>/cmdb_site` we'd need to scan TQL strings for the
bare model name `cmdb_site` with a word-boundary check. Not added in PR3a
because it requires knowing the full set of models in the module to avoid
false positives — defer to PR3+ when we have a richer cross-artifact view.

The `tql` field IS still walked by the scanner today, and a *full canonical
URI* embedded in TQL (rare but possible) would be caught as a `weak` ref.
The dot-notation case is the only one we miss.

#### 2. `runScript.script_name` is a bare name, not a URI
Sample: `"script_name": "runScript_check_faultlevel"` references the file
`SERVICE/RunScript/JavaScript/Rhino2/runScript_check_faultlevel.js` bundled
under the same module's SERVICE artifact. There is no canonical URI for
RunScripts — they live under the SERVICE artifact, not as standalone
artifacts.

To make `find_artifact_references` answer "what runs `runScript_check_faultlevel`?",
PR3a-3 introduces a virtual canonical URI:

```
/<project>/<module>/_RunScript/<script_name>
```

When a service flow's `runScript_*` step has `script_name: X`, the scanner
treats it as a strong reference to `/<project>/<module>/_RunScript/X`. The
`find_artifact_references` tool, given that virtual URI, returns the parent
service. This keeps the rest of the reference-scanning code unchanged.

The same pattern applies to `runScriptLib` step types (not yet observed in
this sample, but handled symmetrically).

## Step types we did NOT observe

The Studio designer offers more node types than appear in this sample:
`transform`, `decision` (conditional), `parallel`, `loop`, `stop`,
`callService`, `runScriptLib`, etc. They likely follow the same shape (a
typed URI field per type) but we haven't sampled apps that use them. PR3a
ships with the catalogue above; future apps that exercise unseen types may
surface new strong-URI fields. The scanner remains correct for them — they
just won't get the `kind: strong` upgrade until catalogued.

## Trigger artifact shape

Captured from `tt_improvement_0.0.80.gpk:modules/TTS/general_work/TRIGGER/review_accept_trigger.json`:

```json
{
  "trigger_name": "review_accept_trigger",
  "active": true,
  "model_uri": "/tt_improvement/TTS/tts_data",
  "event_type": "update",
  "before_or_after": "after",
  "condition": "operation_mode = 'Accept'",
  "source": "Page",
  "trigger_activities": [
    {
      "activity_type": "Invoke Service",
      "priority": 100,
      "sync": true,
      "service_rest_uri": "/adc-service/rest/v1/services/tt_improvement/TTS/tts_review_process_order",
      "write_back": true,
      "reference_trans": false
    }
  ]
}
```

URI fields:
- `model_uri` (top-level): which model fires the trigger.
- `trigger_activities[].service_rest_uri`: which service the trigger runs.

Both are already in `_STRONG_URI_FIELDS`. Once PR3b adds trigger artifacts
as a reference *source*, the scanner will walk these correctly without code
changes.

## Confirms a PR2.5 false positive

`tts_review_process_order` — flagged as unused in PR2.5 — is the activity
service of `review_accept_trigger`. Once PR3b ships, it will move into
`definitely_used.static_refs` with `kind: strong, field: service_rest_uri,
in_type: trigger`.
