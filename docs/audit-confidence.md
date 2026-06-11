# Audit confidence ratings

`audit_artifact_usage` returns each candidate-unused artifact with a
`confidence` rating (`low` / `medium` / `high` / `n/a`) and a list of
`caveats`. This file explains what each rating actually means so users
don't delete a service that's only quiet for the moment.

## Why we don't say "definitely_unused"

Even with zero static references AND zero log hits, an artifact might
still be in active use:

1. **Log retention is ~3 days on this tenant.** A service called weekly
   via a scheduled job will show no log hits in our window.
2. **Workflow BPMN scanning is not implemented yet.** Activities inside
   a workflow that invoke services don't show up as static refs.
3. **External callers are invisible.** Other tenants, REST API consumers,
   RPA bots, off-tenant integrations — none surface in static analysis.
4. **TQL dot-notation refs are not yet caught.** Services that reference
   models via `<project>.<module>.<name>` (vs `/proj/mod/name`) inside
   `modelInstanceTqlQuery.tql` strings are missed.

## How log evidence maps to services

`count_service_invocations` and `audit_artifact_usage` filter Log
Analysis by `element_name`. Two probe paths now correlate hits to a
service:

1. **Direct match** — `element_name=<service-name>` (e.g. top-level
   workflows, services whose RunScript is named identically to the
   parent).
2. **Bundled-script match** — for every `runScript` / `runScriptLib`
   step in the service flow, we additionally probe
   `element_name=<script_name>` and roll the hits up to the parent
   service.

The second probe path closes the historic gap where a service like
`tts_check_faultlevel` looked unused because the log entries record
`element_name=runScript_check_faultlevel` (the bundled RunScript), not
the parent service name. With both probe paths in place, `runtime_hits`
on a service is now a meaningful negative signal.

**Remaining caveat:** A service that triggers another service via
`invokeService` and never runs its own bundled script will still show
zero direct hits. The downstream service's hits won't roll up here —
they belong to the downstream service. That matches the audit's intent
(per-service usage), but be aware when interpreting `runtime_hits=0` on
an `invokeService`-only orchestration node.

## Confidence rules

| Rating | Static refs | Log hits | Sources scanned (out of: triggers, workflows, bundled-scripts) |
|--------|-------------|----------|-----------------------------------------------------------|
| `high` | 0 | 0 | all three |
| `medium` | 0 | 0 | two of three |
| `low` | 0 | 0 | one or fewer |
| `n/a` | ≥1 OR ≥1 | — | the artifact is in `definitely_used.*` |

Today: triggers + bundled-script correlation are scanned, workflows are
not — so the default for clean candidates is **`medium`**. The rating
will lift to **`high`** once workflow BPMN scanning lands.

## What "high" still doesn't mean

Even `high` is *high confidence the artifact has zero in-tenant refs*.
It does NOT prove:
- No external system calls it.
- No scheduled job longer than the log retention window calls it.
- No future code generates a URI to it dynamically.

So the audit tool's job is to surface candidates with as much context as
possible — humans (or higher-level agents) make the deletion call.

## Caveats list

Every `likely_unused_candidates` row carries a `caveats` array. The
contents are static and only reflect *known* gaps in our coverage:

```
"Tenant log retention is ~3 days. A service called weekly via a
 scheduled job may show zero log hits without being unused."
"Workflow BPMN artifacts are NOT yet scanned. Activities inside a
 workflow that invoke services won't surface as static refs."
"External callers (other tenants, REST API consumers, RPA bots) are
 invisible to static analysis."
```

Future PRs that close coverage gaps will remove the corresponding caveat
and (when applicable) bump the confidence rating.
