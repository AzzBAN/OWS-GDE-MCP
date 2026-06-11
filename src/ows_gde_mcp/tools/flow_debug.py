"""Flow debugging tools for OWS service chains.

Three tools for tracing and auditing service-to-service call chains and
the RunScripts that glue them together:

- `walk_service_chain` — recursively follow `InvokeService` steps from
  a starting service and return a flattened call tree.
- `diff_service_io` — compare a caller's payload preparation against the
  callee's input schema, surface field-level mismatches.
- `lint_service_script` — static analysis of a RunScript body for known
  anti-patterns (empty catch, hardcoded UUIDs, null-deref reads).

These compose with the existing tools (`get_service`, `get_service_script`,
`search_service_logs`) to power the `ows-flow-debug` skill — the agent
no longer needs to walk a 5-deep call tree by hand.
"""

from __future__ import annotations

import re
from typing import Any

from ows_gde_mcp.tools.live import get_service
from ows_gde_mcp.tools.scripts import get_service_script

# Step types that invoke another service. Discovered from real flow JSON
# (`type` field on each step). The set covers both the legacy
# `invoke_service` and the modern `invokeService` casings observed.
_INVOKE_STEP_TYPES = frozenset({"invokeService", "invoke_service", "invoke"})

# Step types that run inline JS — these carry the failure-prone glue logic.
_RUNSCRIPT_STEP_TYPES = frozenset({"runScript", "run_script", "script"})

# Step types that touch a Model (read or write).
_MODEL_STEP_TYPES = frozenset(
    {
        "modelInstanceGetList",
        "modelInstanceGet",
        "modelInstanceCreate",
        "modelInstanceUpdate",
        "modelInstanceDelete",
        "modelInstanceQuery",
        "queryByTql",
    }
)

# UUID regex (canonical 8-4-4-4-12 lowercase hex).
_UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")

# Common service URI prefixes — used to parse out (project, module, service)
# from a `service_rest_uri` value found inside an InvokeService step.
_SERVICE_URI_PREFIXES = (
    "/adc-service/web/rest/v1/services/",
    "/adc-service/rest/v1/services/",
)


def _parse_service_uri(uri: str) -> tuple[str, str, str] | None:
    """Parse `(project, module, service)` from any known service URI form.

    Accepts:
    - `/adc-service/rest/v1/services/<p>/<m>/<s>`
    - `/adc-service/web/rest/v1/services/<p>/<m>/<s>`
    - `/<p>/<m>/<s>` (canonical)

    Returns `None` if the URI is malformed.
    """
    if not isinstance(uri, str) or not uri:
        return None
    rel = uri
    for prefix in _SERVICE_URI_PREFIXES:
        if rel.startswith(prefix):
            rel = rel[len(prefix) :]
            break
    else:
        rel = rel.lstrip("/")
    parts = rel.split("/")
    if len(parts) >= 3 and all(parts[:3]):
        return parts[0], parts[1], parts[2]
    return None


def _classify_step(step: dict[str, Any]) -> str:
    """Bucket a flow step into a coarse category for the call tree."""
    t = (step.get("type") or "").strip()
    if t in _INVOKE_STEP_TYPES:
        return "invoke_service"
    if t in _RUNSCRIPT_STEP_TYPES:
        return "run_script"
    if t in _MODEL_STEP_TYPES:
        return "model"
    if t in ("input", "output"):
        return t
    if t in ("condition", "branch", "switch"):
        return "branch"
    return t or "unknown"


def _extract_invoke_target(step: dict[str, Any]) -> str | None:
    """Pull the target service URI out of an InvokeService step."""
    for key in ("service_rest_uri", "service_uri", "serviceUri", "serviceRestUri"):
        v = step.get(key)
        if isinstance(v, str) and v:
            return v
    # Some flow shapes nest it under `parameters` or `properties`.
    nested = step.get("parameters") or step.get("properties") or {}
    if isinstance(nested, dict):
        for key in ("service_rest_uri", "service_uri", "serviceUri", "serviceRestUri"):
            v = nested.get(key)
            if isinstance(v, str) and v:
                return v
    return None


def _extract_script_name(step: dict[str, Any]) -> str | None:
    """Pull the script name out of a RunScript step."""
    for key in ("script_name", "scriptName", "name"):
        v = step.get(key)
        if isinstance(v, str) and v and key != "name":
            return v
    nested = step.get("parameters") or step.get("properties") or {}
    if isinstance(nested, dict):
        for key in ("script_name", "scriptName"):
            v = nested.get(key)
            if isinstance(v, str) and v:
                return v
    return None


def _extract_model_uri(step: dict[str, Any]) -> str | None:
    """Pull the model URI out of a model-touching step."""
    for key in ("model_uri", "modelUri", "asset_uri"):
        v = step.get(key)
        if isinstance(v, str) and v:
            return v
    return None


def _summarize_step(step: dict[str, Any]) -> dict[str, Any]:
    """One step's compact representation for the call tree."""
    kind = _classify_step(step)
    out: dict[str, Any] = {
        "name": step.get("name"),
        "type": step.get("type"),
        "kind": kind,
    }
    if kind == "invoke_service":
        out["target_uri"] = _extract_invoke_target(step)
    elif kind == "run_script":
        out["script_name"] = _extract_script_name(step)
    elif kind == "model":
        out["model_uri"] = _extract_model_uri(step)
        if step.get("query_condition"):
            out["query_condition"] = step["query_condition"]
    if step.get("ignore_exception"):
        out["ignore_exception"] = True
    if step.get("next"):
        out["next"] = step["next"]
    return out


def _flow_steps(flow: dict[str, Any]) -> list[dict[str, Any]]:
    """Pull steps out of a flow dict in a stable order.

    Flow shapes vary — `steps` may be a dict keyed by step-name (most
    common) or a list. Always returns a list with the step name attached.
    """
    raw = flow.get("steps") if isinstance(flow, dict) else None
    if isinstance(raw, dict):
        out = []
        for name, step in raw.items():
            if isinstance(step, dict):
                merged = {**step}
                if "name" not in merged:
                    merged["name"] = name
                out.append(merged)
        return out
    if isinstance(raw, list):
        return [s for s in raw if isinstance(s, dict)]
    return []


async def walk_service_chain(
    tenant: str,
    project_name: str,
    module_name: str,
    service_name: str,
    *,
    max_depth: int = 5,
    include_scripts: bool = False,
) -> dict[str, Any]:
    """Recursively follow `InvokeService` steps and return a call tree.

    Walks every reachable downstream service from the entry point up to
    `max_depth` hops. For each visited service, captures the flat list
    of its flow steps with kind classification (invoke_service /
    run_script / model / branch / input / output / unknown) plus the
    target URI / script name / model URI per step. Cycles are detected
    via a visited set keyed on `<project>/<module>/<service>`.

    Args:
        tenant: "prod" or "testbed". Studio surface required (the
            underlying `get_service` call hits Studio).
        project_name / module_name / service_name: locate the entry-point
            service.
        max_depth: cap the recursion. Default 5. Set to 1 to inspect
            only the entry-point service without following hops.
        include_scripts: if True, also fetch each RunScript's full JS
            body via `get_service_script` and embed it under
            `script_body`. Off by default — bodies inflate the response
            substantially.

    Returns:
        ```
        {
            "entry": "<p>/<m>/<s>",
            "depth": int,            # actual depth reached
            "service_count": int,
            "services": {
                "<p>/<m>/<s>": {
                    "steps": [{name, type, kind, target_uri?, ...}],
                    "depth": int,
                    "errors": [...]  # if get_service / script fetch failed
                }
            },
            "edges": [{"from": "<p>/<m>/<s>", "to": "<p>/<m>/<s>", "step": <name>}],
            "warnings": [...]
        }
        ```
    """
    entry_key = f"{project_name}/{module_name}/{service_name}"
    services: dict[str, Any] = {}
    edges: list[dict[str, Any]] = []
    warnings: list[str] = []
    queue: list[tuple[str, str, str, int]] = [(project_name, module_name, service_name, 0)]
    actual_depth = 0

    while queue:
        proj, mod, svc, depth = queue.pop(0)
        key = f"{proj}/{mod}/{svc}"
        if key in services:
            continue
        if depth > max_depth:
            warnings.append(f"depth limit reached before {key}")
            continue
        actual_depth = max(actual_depth, depth)

        try:
            res = await get_service(tenant, proj, mod, svc, flow_only=True)
        except Exception as e:  # noqa: BLE001 — surface, don't crash
            services[key] = {"depth": depth, "steps": [], "errors": [f"fetch: {e}"]}
            continue
        if not isinstance(res, dict) or "error" in res:
            services[key] = {
                "depth": depth,
                "steps": [],
                "errors": [res.get("error") if isinstance(res, dict) else "no-data"],
            }
            continue

        flow = res.get("flow") or {}
        steps = _flow_steps(flow)
        summarized = [_summarize_step(s) for s in steps]
        services[key] = {"depth": depth, "steps": summarized, "errors": []}

        # Optionally fetch script bodies for each RunScript step
        if include_scripts:
            for step_summary in summarized:
                if step_summary["kind"] != "run_script":
                    continue
                sname = step_summary.get("script_name")
                if not sname:
                    continue
                try:
                    body = await get_service_script(tenant, proj, mod, sname)
                except Exception as e:  # noqa: BLE001
                    step_summary["script_error"] = str(e)
                    continue
                if isinstance(body, dict):
                    step_summary["script_body"] = body.get("content")

        # Enqueue downstream services
        for step_summary in summarized:
            if step_summary["kind"] != "invoke_service":
                continue
            target = step_summary.get("target_uri")
            if not target:
                continue
            parsed = _parse_service_uri(target)
            if not parsed:
                warnings.append(f"unparseable target_uri at {key}/{step_summary['name']}: {target}")
                continue
            tp, tm, ts = parsed
            target_key = f"{tp}/{tm}/{ts}"
            edges.append({"from": key, "to": target_key, "step": step_summary["name"]})
            if target_key not in services and depth + 1 <= max_depth:
                queue.append((tp, tm, ts, depth + 1))

    return {
        "entry": entry_key,
        "depth": actual_depth,
        "service_count": len(services),
        "services": services,
        "edges": edges,
        "warnings": warnings,
    }


# ============================================================
# diff_service_io — compare a caller's payload prep vs callee schema
# ============================================================


def _input_schema_fields(flow: dict[str, Any]) -> dict[str, str]:
    """Extract `{field_name: type}` from a service's input_node schema."""
    steps = _flow_steps(flow)
    for step in steps:
        if step.get("type") != "input":
            continue
        inp = step.get("input") or {}
        props = inp.get("properties") or []
        return {
            p.get("name"): p.get("type", "")
            for p in props
            if isinstance(p, dict) and p.get("name")
        }
    return {}


def _find_invoke_step(flow: dict[str, Any], callee_uri: str) -> dict[str, Any] | None:
    """Find the InvokeService step in `flow` whose target matches `callee_uri`.

    Substring-matches the canonical `<project>/<module>/<name>` segment
    against the step's target URI to handle prefix variants.
    """
    callee_seg = callee_uri.lstrip("/")
    for prefix in _SERVICE_URI_PREFIXES:
        if callee_uri.startswith(prefix):
            callee_seg = callee_uri[len(prefix) :].lstrip("/")
            break
    for step in _flow_steps(flow):
        if _classify_step(step) != "invoke_service":
            continue
        target = _extract_invoke_target(step) or ""
        if callee_seg in target.lstrip("/"):
            return step
    return None


def _invoke_payload_fields(step: dict[str, Any]) -> dict[str, Any]:
    """Pull the payload-property names the caller sets on an InvokeService.

    OWS InvokeService steps describe the outbound payload either via
    a `parameters.properties` array (recent shape) or a `request_body`
    dict (older shape). Returns `{field_name: type|"unknown"}`.
    """
    out: dict[str, Any] = {}
    nested = step.get("parameters") or {}
    props = nested.get("properties") if isinstance(nested, dict) else None
    if isinstance(props, list):
        for p in props:
            if isinstance(p, dict) and p.get("name"):
                out[p["name"]] = p.get("type", "unknown")
    rb = step.get("request_body") or step.get("requestBody")
    if isinstance(rb, dict):
        for k in rb.keys():
            out.setdefault(k, "unknown")
    return out


async def diff_service_io(
    tenant: str,
    caller_project: str,
    caller_module: str,
    caller_service: str,
    callee_project: str,
    callee_module: str,
    callee_service: str,
) -> dict[str, Any]:
    """Compare a caller's `InvokeService` payload to the callee's input schema.

    Field-level diff between what the caller is sending and what the
    callee expects. Catches schema drift — the most common failure mode
    when a downstream service is updated without notifying its callers.

    Args:
        tenant: "prod" or "testbed".
        caller_project / caller_module / caller_service: the orchestration
            service that contains the InvokeService step.
        callee_project / callee_module / callee_service: the target
            service being invoked.

    Returns:
        ```
        {
            "caller": "<p>/<m>/<s>",
            "callee": "<p>/<m>/<s>",
            "missing_required": [...],   # callee requires, caller doesn't send
            "extra_unused": [...],       # caller sends, callee ignores
            "type_mismatches": [{field, caller_type, callee_type}],
            "matched": [...],            # both sides agree
            "errors": [...]
        }
        ```
    """
    errors: list[str] = []
    callee_uri = f"/{callee_project}/{callee_module}/{callee_service}"

    # Fetch both flows
    caller_res = await get_service(
        tenant, caller_project, caller_module, caller_service, flow_only=True
    )
    callee_res = await get_service(
        tenant, callee_project, callee_module, callee_service, flow_only=True
    )

    if not isinstance(caller_res, dict) or "error" in caller_res:
        errors.append(f"caller fetch: {caller_res}")
    if not isinstance(callee_res, dict) or "error" in callee_res:
        errors.append(f"callee fetch: {callee_res}")
    if errors:
        return {
            "caller": f"{caller_project}/{caller_module}/{caller_service}",
            "callee": f"{callee_project}/{callee_module}/{callee_service}",
            "errors": errors,
        }

    caller_flow = caller_res.get("flow") or {}
    callee_flow = callee_res.get("flow") or {}

    invoke_step = _find_invoke_step(caller_flow, callee_uri)
    if not invoke_step:
        errors.append(f"caller does not invoke {callee_uri}")
        return {
            "caller": f"{caller_project}/{caller_module}/{caller_service}",
            "callee": f"{callee_project}/{callee_module}/{callee_service}",
            "errors": errors,
        }

    caller_payload = _invoke_payload_fields(invoke_step)
    callee_input = _input_schema_fields(callee_flow)

    # Find required callee fields (need to dig into the input_node again
    # because _input_schema_fields drops the `required` flag).
    required: set[str] = set()
    for step in _flow_steps(callee_flow):
        if step.get("type") != "input":
            continue
        for p in (step.get("input") or {}).get("properties", []):
            if isinstance(p, dict) and p.get("required") and p.get("name"):
                required.add(p["name"])

    caller_keys = set(caller_payload)
    callee_keys = set(callee_input)

    missing_required = sorted(required - caller_keys)
    extra_unused = sorted(caller_keys - callee_keys)
    matched: list[str] = []
    type_mismatches: list[dict[str, str]] = []
    for f in sorted(caller_keys & callee_keys):
        ct = caller_payload[f]
        et = callee_input[f]
        if ct in (et, "unknown") or et == "unknown":
            matched.append(f)
        else:
            type_mismatches.append({"field": f, "caller_type": ct, "callee_type": et})

    return {
        "caller": f"{caller_project}/{caller_module}/{caller_service}",
        "callee": f"{callee_project}/{callee_module}/{callee_service}",
        "invoke_step": invoke_step.get("name"),
        "missing_required": missing_required,
        "extra_unused": extra_unused,
        "type_mismatches": type_mismatches,
        "matched": matched,
        "errors": errors,
    }


# ============================================================
# lint_service_script — static analysis of a RunScript JS body
# ============================================================


# Anti-pattern matchers. Each returns a (severity, message, line_number)
# tuple per finding. Patterns are conservative — they err toward false
# negatives (miss subtle bugs) over false positives (yelling about
# legitimate code).

_EMPTY_CATCH_RE = re.compile(r"catch\s*\([^)]*\)\s*\{\s*\}", re.MULTILINE)
_CATCH_NO_RETHROW_RE = re.compile(
    r"catch\s*\(([^)]+)\)\s*\{([^}]*)\}",
    re.MULTILINE | re.DOTALL,
)
# Console.log on its own — no logger, just `console.log(e)` swallows
_CONSOLE_LOG_ONLY_RE = re.compile(r"^\s*console\.log\(.*\);?\s*$", re.MULTILINE)
# Hardcoded URL with hostname (testbed/prod hosts)
_HARDCODED_URL_RE = re.compile(r'https?://[\w.-]+', re.MULTILINE)


def _line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _find_anti_patterns(content: str) -> list[dict[str, Any]]:
    """Run all anti-pattern checks against a JS body."""
    findings: list[dict[str, Any]] = []

    # 1. Empty catch blocks — silent failure, caller never knows
    for m in _EMPTY_CATCH_RE.finditer(content):
        findings.append(
            {
                "rule": "empty_catch",
                "severity": "high",
                "line": _line_no(content, m.start()),
                "snippet": m.group(0)[:120],
                "message": "Empty catch swallows the error — caller sees success even on failure. Rethrow or set an explicit error field.",
            }
        )

    # 2. Catch that only console.logs and doesn't rethrow / set output
    for m in _CATCH_NO_RETHROW_RE.finditer(content):
        body = m.group(2)
        if not body.strip():
            continue  # already caught by empty_catch
        if "throw" in body or "output.put" in body or "logger" in body:
            continue
        if _CONSOLE_LOG_ONLY_RE.search(body):
            findings.append(
                {
                    "rule": "catch_only_console_log",
                    "severity": "medium",
                    "line": _line_no(content, m.start()),
                    "snippet": m.group(0)[:160],
                    "message": "Catch only writes to console — caller still sees success. Use logger.error and rethrow or set output.put('error', ...).",
                }
            )

    # 3. Hardcoded UUIDs — won't survive promotion testbed → prod
    for m in _UUID_RE.finditer(content):
        findings.append(
            {
                "rule": "hardcoded_uuid",
                "severity": "medium",
                "line": _line_no(content, m.start()),
                "snippet": m.group(0),
                "message": "Hardcoded UUID — looks up may differ between testbed and prod. Look up by name or pass via input.",
            }
        )

    # 4. Hardcoded HTTP URLs
    for m in _HARDCODED_URL_RE.finditer(content):
        url = m.group(0)
        # Skip references inside comments or known doc URLs
        line_start = content.rfind("\n", 0, m.start()) + 1
        line = content[line_start : content.find("\n", m.start())]
        stripped = line.lstrip()
        if stripped.startswith(("//", "*", "#")):
            continue
        findings.append(
            {
                "rule": "hardcoded_url",
                "severity": "medium",
                "line": _line_no(content, m.start()),
                "snippet": url,
                "message": "Hardcoded URL — environment-specific. Move to config or pass via input.",
            }
        )

    # 5. Null-deref: `input.get("x").foo` without intermediate null guard
    for m in re.finditer(
        r'input\.get\(\s*["\']([^"\']+)["\']\s*\)\.([a-zA-Z_]\w*)',
        content,
    ):
        # Look at preceding 200 chars for a `if (...x...)` or `?.` guard
        window = content[max(0, m.start() - 200) : m.start()]
        var = m.group(1)
        if f"!= null" in window or f"!== null" in window or f"if ({var}" in window or "?." in m.group(0):
            continue
        findings.append(
            {
                "rule": "unguarded_input_deref",
                "severity": "high",
                "line": _line_no(content, m.start()),
                "snippet": m.group(0),
                "message": f"Reading `.{m.group(2)}` on `input.get('{var}')` without a null guard — NPE if the field is missing.",
            }
        )

    # 6. Loose `==` instead of `===`
    for m in re.finditer(r"[^=!<>]==[^=]|[^=!<>]!=[^=]", content):
        findings.append(
            {
                "rule": "loose_equality",
                "severity": "low",
                "line": _line_no(content, m.start()),
                "snippet": content[m.start() : m.end()],
                "message": "Loose equality (`==` / `!=`) — type coercion can mask bugs. Prefer `===` / `!==`.",
            }
        )

    return findings


async def lint_service_script(
    tenant: str,
    project_name: str,
    module_name: str,
    script_name: str,
) -> dict[str, Any]:
    """Static analysis of a RunScript body for known anti-patterns.

    Fetches the script via `get_service_script` and applies a fixed set
    of pattern checks. Each finding has a `rule`, `severity`
    (low/medium/high), `line`, `snippet`, and `message`. Conservative —
    err toward missing bugs over false positives.

    Rules currently implemented:
    - `empty_catch` — `catch (e) {}` silent failure (high)
    - `catch_only_console_log` — catch with only console.log, no rethrow (medium)
    - `hardcoded_uuid` — UUID baked into source (medium)
    - `hardcoded_url` — http(s) URL baked into source (medium)
    - `unguarded_input_deref` — `input.get('x').foo` without null guard (high)
    - `loose_equality` — `==` / `!=` instead of `===` / `!==` (low)

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name / script_name: locate the script.

    Returns:
        ```
        {
            "script": "<project>/<module>/<script>",
            "script_type": "RunScript|ScriptLib|...",
            "line_count": int,
            "finding_count": int,
            "findings": [{rule, severity, line, snippet, message}],
            "errors": [...]
        }
        ```
    """
    res = await get_service_script(tenant, project_name, module_name, script_name)
    if not isinstance(res, dict) or "error" in res:
        return {
            "script": f"{project_name}/{module_name}/{script_name}",
            "errors": [res.get("error") if isinstance(res, dict) else "no-data"],
            "findings": [],
        }
    content = res.get("content") or ""
    if not isinstance(content, str):
        return {
            "script": f"{project_name}/{module_name}/{script_name}",
            "errors": ["script body is not a string"],
            "findings": [],
        }

    findings = _find_anti_patterns(content)
    return {
        "script": f"{project_name}/{module_name}/{script_name}",
        "script_type": res.get("script_type"),
        "line_count": content.count("\n") + 1,
        "finding_count": len(findings),
        "findings": findings,
        "errors": [],
    }


__all__ = [
    "diff_service_io",
    "lint_service_script",
    "walk_service_chain",
]
