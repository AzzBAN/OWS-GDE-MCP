"""Cross-reference analysis for OWS artifacts.

These tools scan live OWS artifact bodies for references to a target asset
URI, so an agent can answer "what calls service X?" or "which services
in this module are unused?" without manually trawling Studio.

Reference scanning is *static*: it reads the JSON definition of each
source artifact and substring-matches against the target's
`<project>/<module>/<name>` segment. The match catches all observed URI
forms in OWS:
- canonical: `/<project>/<module>/<name>` (services, models, redirect button location)
- service runtime: `/adc-service/rest/v1/services/<project>/<module>/<name>`
- service web runtime: `/adc-service/web/rest/v1/services/<project>/<module>/<name>`
- bare path (no leading slash, e.g. in `templates` arrays)
- inline JS strings inside a page's `js_content` block (e.g.
  `MessageProcessor.process({serviceId: "/adc-service/rest/v1/services/..."})`)

References are classified as:
- `strong` - the value is held in a known typed-URI field
  (`model_uri`, `bind_model_uri`, `service_uri`, `service_rest_uri`,
  `service_id`, `serviceId`, `serviceName`, `page_uri`, `script_uri`,
  `asset_uri`, `location`).
- `weak`   - the URI appears as a substring elsewhere (description,
  expression, embedded script body, `js_content`, ...). Useful but
  lower-confidence.

Coverage in this release (PR2.5):
- Source artifacts scanned: **services** (full flow JSON via
  `list_services(include_flow=True)`) and **pages** (full content tree
  via `get_page_detail`, fetched in parallel for every listed page).
  Pages contribute three reference surfaces: component props/propsBind,
  inline scripts in the `js_content` blocks (page tab "Script"), and
  inline CSS in `css_content`.
- Source artifacts NOT yet scanned: triggers, workflows. A target
  referenced *only* from one of these will appear unused. Surfaced in
  `warnings` on every response.
- Search scope: same (project, module) as the target by default.
- Target types: any artifact with a canonical
  `/<project>/<module>/<name>` URI (service, model, page, script).

`from_package` is reserved for offline `.gpk` scanning and currently
raises `NotImplementedError` - live only for now.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Iterator
from typing import Any

# Field names whose values are typed URI references. A match in any of
# these is a strong reference. Discovered by inspecting real service flow
# JSON (modelInstance steps, invoke steps) and page content trees
# (component props, propsBind, eventSource, js_content blocks).
_STRONG_URI_FIELDS = frozenset(
    {
        # service flow fields
        "model_uri",
        "bind_model_uri",
        "service_uri",
        "service_rest_uri",
        "page_uri",
        "script_uri",
        "asset_uri",
        # page content tree fields (component props)
        "serviceName",
        "serviceId",
        "service_id",
        "location",
    }
)

# OWS service runtime URI prefixes we recognise during normalization.
# Page content can use either prefix and we substring-match against the
# relative `<project>/<module>/<name>` segment to catch all variants.
_SERVICE_RUNTIME_PREFIXES = (
    "/adc-service/rest/v1/services",
    "/adc-service/web/rest/v1/services",
)


def _normalize_target_uri(target: str) -> str:
    """Normalize a target reference to canonical form.

    Accepts:
    - canonical 3-segment `/proj/mod/name`
    - service-runtime `/adc-service/rest/v1/services/proj/mod/name`
    - service-web-runtime `/adc-service/web/rest/v1/services/proj/mod/name`
    - virtual RunScript URI `/proj/mod/_RunScript/script_name` — bundled JS
      file under SERVICE/RunScript. Virtual because RunScripts aren't
      top-level artifacts; this form lets `find_artifact_references`
      answer "what runs script X?" by returning the parent service.
    - virtual ScriptLib URI `/proj/mod/_ScriptLib/script_name` — same idea
      for shared script libraries.

    Bare names (no slash) are rejected - they're ambiguous without
    project/module context.
    """
    s = (target or "").strip()
    if not s.startswith("/"):
        raise ValueError(
            "target_uri must start with '/' and resolve to a canonical asset URI "
            f"like '/<project>/<module>/<name>'. Got: {target!r}"
        )
    for prefix in _SERVICE_RUNTIME_PREFIXES:
        if s.startswith(prefix):
            s = s[len(prefix) :]
            break
    parts = [p for p in s.split("/") if p]
    # Virtual RunScript/ScriptLib URIs have 4 segments; canonical artifacts have 3.
    if len(parts) == 4 and parts[2] in _VIRTUAL_BUCKETS:
        return "/" + "/".join(parts)
    if len(parts) != 3:
        raise ValueError(
            "target_uri must resolve to '/<project>/<module>/<name>' (3 segments) "
            "or virtual '/<project>/<module>/_RunScript|_ScriptLib/<name>' "
            f"(4 segments). After normalization got: '/{'/'.join(parts)}'"
        )
    return "/" + "/".join(parts)


# Virtual third-segment buckets for artifacts that live *inside* a SERVICE
# rather than as standalone top-level artifacts (RunScript JS files,
# ScriptLib shared functions). The reference scanner builds canonical URIs
# of the form `/<project>/<module>/<bucket>/<script_name>` for these so
# find_artifact_references can answer "what runs script X?".
_VIRTUAL_BUCKETS = frozenset({"_RunScript", "_ScriptLib"})

# Step types that reference a bundled-script asset by bare name. The scanner
# treats their `script_name` field as a strong reference to the virtual
# canonical URI `/<project>/<module>/<bucket>/<script_name>`.
_BUNDLED_SCRIPT_STEPS: dict[str, str] = {
    "runScript": "_RunScript",
    "runScriptLib": "_ScriptLib",
}


def _bundled_scripts_for(service_flow: Any) -> list[str]:
    """Return every bundled `script_name` referenced inside a service flow.

    Walks `flow.steps.<step>.script_name` for every step whose `type` is
    in `_BUNDLED_SCRIPT_STEPS`. Used to bridge the audit-confidence gap
    described in `docs/audit-confidence.md`: Log Analysis records
    `element_name=<script_name>` rather than the parent service name, so
    correlating runtime hits requires probing the script names too.

    Returns an empty list for non-dict input or services with no
    bundled-script steps.
    """
    if not isinstance(service_flow, dict):
        return []
    steps = service_flow.get("steps") or {}
    if not isinstance(steps, dict):
        return []
    out: list[str] = []
    for step in steps.values():
        if not isinstance(step, dict):
            continue
        if step.get("type") in _BUNDLED_SCRIPT_STEPS:
            name = step.get("script_name")
            if isinstance(name, str) and name:
                out.append(name)
    return out


def _walk(obj: Any, parent_key: str = "") -> Iterator[tuple[str, str, Any]]:
    """Yield (leaf_field_name, dotted_key_path, value) for every leaf in a JSON tree."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            yield from _walk(v, new_key)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            new_key = f"{parent_key}[{i}]"
            yield from _walk(item, new_key)
    else:
        leaf = parent_key.rsplit(".", 1)[-1] if parent_key else ""
        # Strip array-index suffix from the leaf so '[3]' doesn't become the field name.
        leaf = leaf.split("[", 1)[0]
        yield (leaf, parent_key, obj)


def _has_word_boundary(value: str, needle: str) -> bool:
    """True if `needle` appears in `value` with non-identifier neighbours.

    Used to verify a relative-form match (`proj/mod/name`) hasn't matched a
    longer URI like `proj/mod/name_extra`. Anchors at start, '/', or any
    non-identifier character.
    """
    i = 0
    while True:
        i = value.find(needle, i)
        if i < 0:
            return False
        end = i + len(needle)
        left_ok = i == 0 or (not value[i - 1].isalnum() and value[i - 1] != "_")
        right_ok = end >= len(value) or (not value[end].isalnum() and value[end] != "_")
        if left_ok and right_ok:
            return True
        i = end


def _scan_body_for_refs(body: Any, target_uri: str) -> list[dict[str, Any]]:
    """Return every reference to `target_uri` found inside `body`.

    Matches against both the canonical form (`/proj/mod/name`) and the
    bare relative form (`proj/mod/name`) so URIs embedded in `templates`
    arrays without leading slashes are caught. The relative form is
    word-boundary-checked to avoid colliding with `proj/mod/name_extra`.
    """
    canonical = target_uri  # `/proj/mod/name`
    relative = target_uri.lstrip("/")  # `proj/mod/name`
    refs: list[dict[str, Any]] = []
    for field_name, key_path, value in _walk(body):
        if not isinstance(value, str):
            continue
        if canonical in value:
            pass  # canonical match always counts
        elif relative in value and _has_word_boundary(value, relative):
            pass  # relative match with clean boundary
        else:
            continue
        kind = "strong" if field_name in _STRONG_URI_FIELDS else "weak"
        excerpt = value if len(value) <= 200 else value[:200] + "..."
        refs.append(
            {
                "kind": kind,
                "field": field_name,
                "path": key_path,
                "excerpt": excerpt,
            }
        )
    return refs


def _is_self_reference(
    src_name: str | None,
    src_project: str | None,
    src_module: str | None,
    target_canonical: str,
) -> bool:
    """True if `src_*` IS the target - used to skip an artifact's own URI."""
    if not (src_name and src_project and src_module):
        return False
    return f"/{src_project}/{src_module}/{src_name}" == target_canonical


async def _fetch_services_with_flow(
    tenant: str, project_name: str, module_name: str
) -> list[dict[str, Any]]:
    """Page through `list_services(include_flow=True)` and return every row.

    Heavy: each row carries the full flow JSON. On a 313-service module
    this is ~1 MB. Caller should call once and reuse.
    """
    from ows_gde_mcp.tools.live import list_services

    out: list[dict[str, Any]] = []
    start = 0
    page_size = 200
    while True:
        res = await list_services(
            tenant,
            project_name,
            module_name,
            start=start,
            limit=page_size,
            include_flow=True,
        )
        if not isinstance(res, dict):
            break
        services = res.get("services") or []
        out.extend(services)
        total = res.get("total", 0) or 0
        if not services or start + page_size >= total:
            break
        start += page_size
    return out


async def _fetch_pages_with_content(
    tenant: str, project_name: str, module_name: str, *, concurrency: int = 8
) -> list[dict[str, Any]]:
    """List every page in the module then fetch each detail in parallel.

    Returns rows with `content` populated (still a JSON-encoded string -
    `_scan_pages_for_refs` parses it before walking).

    Cost: 1 list call + N detail calls (N = pages in module). The
    `concurrency` cap keeps OWS from rate-limiting; 8 is comfortable.
    """
    from ows_gde_mcp.tools.live import get_page_detail, list_pages

    summaries: list[dict[str, Any]] = []
    page = 0
    size = 100
    while True:
        res = await list_pages(tenant, project_name, module_name, page=page, page_size=size)
        if not isinstance(res, dict):
            break
        rows = res.get("pages") or []
        summaries.extend(rows)
        total = res.get("total", 0) or 0
        if not rows or (page + 1) * size >= total:
            break
        page += 1

    sem = asyncio.Semaphore(concurrency)

    async def fetch_one(row: dict[str, Any]) -> dict[str, Any]:
        page_id = row.get("id")
        if not page_id:
            return row
        async with sem:
            detail = await get_page_detail(tenant, str(page_id))
        if isinstance(detail, dict) and "error" not in detail:
            return {**row, **detail}
        return row

    return await asyncio.gather(*(fetch_one(r) for r in summaries))


async def _fetch_triggers(tenant: str, project_name: str, module_name: str) -> list[dict[str, Any]]:
    """Page through `list_triggers(active=None)` and return every row.

    `active=None` so dormant triggers (active=false) still surface — the
    URI they reference is still in the design state and matters for
    ref-counting. Each row carries `trigger_activities[]` whose
    `service_rest_uri` field is what we scan for service references.
    """
    from ows_gde_mcp.tools.live import list_triggers

    out: list[dict[str, Any]] = []
    start = 0
    page_size = 200
    while True:
        res = await list_triggers(
            tenant,
            project_name,
            module_name,
            active=None,
            start=start,
            limit=page_size,
        )
        if not isinstance(res, dict):
            break
        triggers = res.get("triggers") or []
        out.extend(triggers)
        total = res.get("total", 0) or 0
        if not triggers or start + page_size >= total:
            break
        start += page_size
    return out


def _scan_triggers_for_refs(
    triggers: list[dict[str, Any]], target_canonical: str
) -> list[dict[str, Any]]:
    """Walk every trigger body and return refs to `target_canonical`.

    A trigger has two URI surfaces:
    - `model_uri` (top-level): which model fires it.
    - `trigger_activities[].service_rest_uri`: which service it runs.
    Both already match in `_STRONG_URI_FIELDS`, so the generic
    `_scan_body_for_refs` walks them correctly.
    """
    refs: list[dict[str, Any]] = []
    for trig in triggers:
        trig_name = trig.get("trigger_name")
        trig_project = trig.get("project_name")
        trig_module = trig.get("module_name")
        if _is_self_reference(trig_name, trig_project, trig_module, target_canonical):
            continue
        for r in _scan_body_for_refs(trig, target_canonical):
            r["in"] = f"/{trig_project}/{trig_module}/{trig_name}"
            r["in_type"] = "trigger"
            refs.append(r)
    return refs


def _scan_pages_for_refs(
    pages: list[dict[str, Any]], target_canonical: str
) -> list[dict[str, Any]]:
    """Walk every page's parsed content tree and return refs to `target_canonical`.

    The page's `content` field is a JSON-encoded string that contains the
    full SPL UI tree, plus `js_content` and `css_content` blocks holding
    inline scripts and styles. We parse it once and walk the resulting
    object so service references in component props, propsBind, the
    page's Script tab (js_content), and inline CSS all surface.
    """
    refs: list[dict[str, Any]] = []
    for page in pages:
        page_name = page.get("name") or page.get("page_name")
        page_project = page.get("project_name")
        page_module = page.get("module_name")
        if _is_self_reference(page_name, page_project, page_module, target_canonical):
            continue
        content_raw = page.get("content")
        body: Any = page
        if isinstance(content_raw, str) and content_raw.strip():
            try:
                body = json.loads(content_raw)
            except json.JSONDecodeError:
                # Malformed content - fall back to substring-matching the
                # raw string only. We deliberately drop the rest of the
                # page row so the same URI doesn't double-match in both
                # `_raw_content` and the original `content` field.
                body = {"_raw_content": content_raw}
        for r in _scan_body_for_refs(body, target_canonical):
            r["in"] = f"/{page_project}/{page_module}/{page_name}"
            r["in_type"] = "page"
            refs.append(r)
    return refs


def _scan_services_for_refs(
    services: list[dict[str, Any]], target_canonical: str
) -> list[dict[str, Any]]:
    """Walk every service flow and return refs to `target_canonical`.

    Two scan paths:
    1. Generic: walk the flow body and substring-match URI fields. Catches
       `model_uri`, `service_uri`, `bind_model_uri`, etc.
    2. Bundled-script special case: when `target_canonical` is a virtual
       URI like `/proj/mod/_RunScript/script_name`, look at every
       `runScript` / `runScriptLib` step in the same module and check
       whether its `script_name` matches. Returns a strong ref pointing at
       the parent service.
    """
    refs: list[dict[str, Any]] = []
    target_parts = target_canonical.strip("/").split("/")
    is_virtual = len(target_parts) == 4 and target_parts[2] in _VIRTUAL_BUCKETS
    if is_virtual:
        target_proj, target_mod, target_bucket, target_script = target_parts
    else:
        target_proj = target_mod = target_bucket = target_script = ""

    for src in services:
        src_name = src.get("service_name")
        src_project = src.get("project_name")
        src_module = src.get("module_name")
        if _is_self_reference(src_name, src_project, src_module, target_canonical):
            continue
        body = src.get("flow") or src
        in_uri = f"/{src_project}/{src_module}/{src_name}"

        if is_virtual:
            # Bundled-script lookup: only services in the same module can
            # reference a bundled script (they share the SERVICE/RunScript
            # asset pool with that module).
            if src_project != target_proj or src_module != target_mod:
                continue
            steps = (body.get("steps") or {}) if isinstance(body, dict) else {}
            for step_name, step in steps.items():
                if not isinstance(step, dict):
                    continue
                step_type = step.get("type")
                expected_bucket = _BUNDLED_SCRIPT_STEPS.get(step_type)
                if expected_bucket != target_bucket:
                    continue
                if step.get("script_name") == target_script:
                    refs.append(
                        {
                            "kind": "strong",
                            "field": "script_name",
                            "path": f"flow.steps.{step_name}.script_name",
                            "excerpt": target_script,
                            "in": in_uri,
                            "in_type": "service",
                        }
                    )
            continue  # skip the generic body walk for virtual targets

        for r in _scan_body_for_refs(body, target_canonical):
            r["in"] = in_uri
            r["in_type"] = "service"
            refs.append(r)
    return refs


async def _list_artifact_names(
    tenant: str, project: str, module: str, artifact_type: str
) -> list[dict[str, Any]]:
    """Return `[{"name", ...}]` for every artifact of `artifact_type` in (project, module)."""
    from ows_gde_mcp.tools.live import list_models, list_pages, list_scripts, list_services

    if artifact_type == "service":
        out: list[dict[str, Any]] = []
        start = 0
        while True:
            res = await list_services(
                tenant, project, module, start=start, limit=200, include_flow=False
            )
            rows = res.get("services") or []
            out.extend({"name": r.get("service_name"), **r} for r in rows)
            total = res.get("total", 0) or 0
            if not rows or start + 200 >= total:
                break
            start += 200
        return out

    if artifact_type == "model":
        out2: list[dict[str, Any]] = []
        start = 0
        while True:
            res = await list_models(tenant, project, module, start=start, limit=200)
            rows = res.get("models") or []
            out2.extend({"name": r.get("model_name"), **r} for r in rows)
            total = res.get("total", 0) or 0
            if not rows or start + 200 >= total:
                break
            start += 200
        return out2

    if artifact_type == "page":
        out3: list[dict[str, Any]] = []
        page = 0
        size = 100
        while True:
            res = await list_pages(tenant, project, module, page=page, page_size=size)
            rows = res.get("pages") or []
            out3.extend({"name": r.get("page_name"), **r} for r in rows)
            total = res.get("total", 0) or 0
            if not rows or (page + 1) * size >= total:
                break
            page += 1
        return out3

    if artifact_type == "script":
        out4: list[dict[str, Any]] = []
        start = 0
        while True:
            res = await list_scripts(
                tenant,
                project_name=project,
                module_name=module,
                start=start,
                limit=200,
            )
            rows = res.get("scripts") or []
            out4.extend({"name": r.get("script_name"), **r} for r in rows)
            total = res.get("total", 0) or 0
            if not rows or start + 200 >= total:
                break
            start += 200
        return out4

    raise ValueError(
        f"unsupported artifact_type: {artifact_type!r}. "
        "Expected one of: service, model, page, script."
    )


# ============================================================
# Public MCP tools
# ============================================================


_NOT_IMPLEMENTED_PACKAGE = (
    "from_package offline scanning is reserved for a follow-up. Pass None to scan live OWS."
)
_COVERAGE_WARNINGS = (
    "Sources scanned: services (full flow JSON) + pages (full content tree, "
    "including page-script `js_content` blocks) + triggers (model_uri + "
    "trigger_activities[].service_rest_uri). NOT scanned: workflows. A "
    "target referenced only from a workflow will appear unused.",
)


async def find_artifact_references(
    tenant: str,
    target_uri: str,
    *,
    search_project: str | None = None,
    search_module: str | None = None,
    from_package: str | None = None,
    with_excerpts: bool = False,
) -> dict[str, Any]:
    """Find every artifact in scope that references `target_uri`.

    Args:
        tenant: "prod" or "testbed".
        target_uri: canonical asset URI like "/<project>/<module>/<name>".
            The service-runtime form
            "/adc-service/rest/v1/services/<project>/<module>/<name>" is
            also accepted and normalized.
        search_project: project to search. Defaults to the target's project.
            Must match the target's project for now (cross-project = PR2.5).
        search_module: module to search inside `search_project`. Defaults
            to the target's module. Cross-module scan = PR2.5.
        from_package: reserved for offline .gpk scanning. NotImplementedError.
        with_excerpts: if True, include the `excerpt` field on each row
            (truncated to 200 chars). Default False — count + location
            is what most callers need; excerpts are the bulk of the
            response payload on busy URIs.

    Returns:
        {
          "target": "/<project>/<module>/<name>",
          "scope": {"project", "module"},
          "sources_scanned": {"services": N, "pages": M, "triggers": 0, "workflows": 0},
          "ref_count": int,
          "strong_ref_count": int,
          "weak_ref_count": int,
          "references": [
            {"in": "/<project>/<module>/<artifact>", "in_type": "service|page",
             "kind": "strong|weak", "field": "...", "path": "...",
             "excerpt": "..."  # only when with_excerpts=True
            }
          ],
          "warnings": [...]
        }
    """
    if from_package is not None:
        raise NotImplementedError(_NOT_IMPLEMENTED_PACKAGE)

    canonical = _normalize_target_uri(target_uri)
    parts = canonical.strip("/").split("/")
    target_project, target_module = parts[0], parts[1]

    project = search_project or target_project
    module = search_module or target_module

    services, pages, triggers = await asyncio.gather(
        _fetch_services_with_flow(tenant, project, module),
        _fetch_pages_with_content(tenant, project, module),
        _fetch_triggers(tenant, project, module),
    )

    references = (
        _scan_services_for_refs(services, canonical)
        + _scan_pages_for_refs(pages, canonical)
        + _scan_triggers_for_refs(triggers, canonical)
    )
    if not with_excerpts:
        for r in references:
            r.pop("excerpt", None)
    strong_count = sum(1 for r in references if r["kind"] == "strong")
    weak_count = len(references) - strong_count

    return {
        "target": canonical,
        "scope": {"project": project, "module": module},
        "sources_scanned": {
            "services": len(services),
            "pages": len(pages),
            "triggers": len(triggers),
            "workflows": 0,
        },
        "ref_count": len(references),
        "strong_ref_count": strong_count,
        "weak_ref_count": weak_count,
        "references": references,
        "warnings": list(_COVERAGE_WARNINGS),
    }


async def find_unused_artifacts(
    tenant: str,
    project_name: str,
    module_name: str,
    artifact_type: str = "service",
    *,
    search_project: str | None = None,
    search_module: str | None = None,
    from_package: str | None = None,
) -> dict[str, Any]:
    """List artifacts of `artifact_type` in (project, module) with zero references.

    For each artifact, scans every service flow and page content tree in
    scope for a reference to its canonical URI. Self-references are
    excluded. The result splits into `definitely_unused` (zero refs found)
    and `used_summary` (refs found, ranked by ref count).

    Args:
        tenant: "prod" or "testbed".
        project_name: project hosting the candidate artifacts.
        module_name: module hosting the candidate artifacts.
        artifact_type: one of "service" | "model" | "page" | "script".
        search_project: project to scan for references. Defaults to
            `project_name`. Cross-project = PR2.5.
        search_module: module to scan for references. Defaults to
            `module_name`. Cross-module = PR2.5.
        from_package: reserved for offline .gpk scanning. NotImplementedError.

    Returns:
        {
          "scope": {"project", "module", "artifact_type",
                    "scanned_in": {"project", "module"}},
          "scanned_count": int,
          "sources_scanned": {"services": N, "pages": M, ...},
          "definitely_unused": [{"name", "uri"}],
          "used_summary": {name: ref_count, ...},
          "warnings": [...]
        }
    """
    if from_package is not None:
        raise NotImplementedError(_NOT_IMPLEMENTED_PACKAGE)

    if artifact_type not in {"service", "model", "page", "script"}:
        raise ValueError(
            f"unsupported artifact_type: {artifact_type!r}. "
            "Expected one of: service, model, page, script."
        )

    src_project = search_project or project_name
    src_module = search_module or module_name

    targets, services, pages, triggers = await asyncio.gather(
        _list_artifact_names(tenant, project_name, module_name, artifact_type),
        _fetch_services_with_flow(tenant, src_project, src_module),
        _fetch_pages_with_content(tenant, src_project, src_module),
        _fetch_triggers(tenant, src_project, src_module),
    )

    # Per-service map of bundled script names (RunScript / ScriptLib).
    # Surfaced in the response so `audit_artifact_usage` can probe each
    # script name against Log Analysis without re-fetching service flows.
    # Module-scoped: scripts only matter when the audit target lives in
    # the same module that owns the service flow.
    bundled_scripts: dict[str, list[str]] = {}
    for src in services:
        if src.get("project_name") != project_name or src.get("module_name") != module_name:
            continue
        scripts = _bundled_scripts_for(src.get("flow"))
        if scripts:
            bundled_scripts[src.get("service_name", "")] = scripts

    unused: list[dict[str, Any]] = []
    used: dict[str, int] = {}

    for target in targets:
        target_name = target.get("name")
        if not target_name:
            continue
        canonical = f"/{project_name}/{module_name}/{target_name}"
        ref_count = (
            len(_scan_services_for_refs(services, canonical))
            + len(_scan_pages_for_refs(pages, canonical))
            + len(_scan_triggers_for_refs(triggers, canonical))
        )
        if ref_count == 0:
            unused.append({"name": target_name, "uri": canonical})
        else:
            used[target_name] = ref_count

    return {
        "scope": {
            "project": project_name,
            "module": module_name,
            "artifact_type": artifact_type,
            "scanned_in": {"project": src_project, "module": src_module},
        },
        "scanned_count": len(targets),
        "sources_scanned": {
            "services": len(services),
            "pages": len(pages),
            "triggers": len(triggers),
            "workflows": 0,
        },
        "definitely_unused": unused,
        "used_summary": dict(sorted(used.items(), key=lambda kv: -kv[1])),
        "bundled_scripts": bundled_scripts,
        "warnings": list(_COVERAGE_WARNINGS),
    }


# ============================================================
# audit_artifact_usage — combined static + runtime evidence
# ============================================================


# Buckets the audit tool emits. There is deliberately no `definitely_unused`
# — see the docstring on `audit_artifact_usage` for why.
_AUDIT_BUCKETS = ("static_refs_only", "runtime_calls_only", "both", "likely_unused_candidates")

# Coverage gaps that affect confidence ratings. Updated as PR3b/PR3+ ship.
_UNSCANNED_SOURCES = ("triggers", "workflows")
_AUDIT_CAVEATS_BASE: tuple[str, ...] = (
    "Tenant log retention is ~3 days. A service called weekly via a "
    "scheduled job may show zero log hits without being unused.",
    "Workflow BPMN artifacts are NOT yet scanned. Activities inside a "
    "workflow that invoke services won't surface as static refs.",
    "External callers (other tenants, REST API consumers, RPA bots) are "
    "invisible to static analysis.",
)


def _confidence_for(
    static_refs: int,
    log_hits: int,
    triggers_scanned: bool,
    workflows_scanned: bool,
    bundled_scripts_correlated: bool = False,
) -> str:
    """Pick a confidence level for an artifact's *unused* status.

    Only meaningful when both static_refs == 0 AND log_hits == 0. Higher
    confidence means more sources were scanned and the artifact still
    came up clean.

    `bundled_scripts_correlated=True` means the audit also probed each
    service's bundled `RunScript` / `ScriptLib` names against Log
    Analysis, closing the correlation gap previously documented in
    `docs/audit-confidence.md`. Without it, the runtime signal is weak.
    """
    if static_refs > 0 or log_hits > 0:
        return "n/a"  # not unused
    fully_scanned = (
        triggers_scanned and workflows_scanned and bundled_scripts_correlated
    )
    if fully_scanned:
        return "high"
    sources_covered = sum(
        [triggers_scanned, workflows_scanned, bundled_scripts_correlated]
    )
    if sources_covered >= 2:
        return "medium"
    return "low"


async def audit_artifact_usage(
    tenant: str,
    project_name: str,
    module_name: str,
    artifact_type: str = "service",
    *,
    search_project: str | None = None,
    search_module: str | None = None,
    include_runtime: bool = True,
    runtime_tenant: str | None = None,
    runtime_since_ms: int | None = None,
    runtime_until_ms: int | None = None,
    include_used: bool = False,
    start: int = 0,
    limit: int = 0,
) -> dict[str, Any]:
    """Audit usage of every artifact of `artifact_type` in (project, module).

    Combines two evidence sources:
    1. **Static refs** from `find_unused_artifacts` (services + pages +
       triggers) — sourced from `tenant` (must have a Studio surface).
    2. **Runtime log hits** from `count_service_invocations` over the last
       3 days — sourced from `runtime_tenant` (defaults to `tenant`).

    The two-tenant split exists because Studio artifacts and runtime logs
    typically live on different tenants:
    - **Static refs** require Studio. On the typical OWS deployment that's
      `testbed` (developers don't have Studio access on `prod`).
    - **Runtime logs** carry actual usage. The interesting question is
      "is this used in *production*?" so `runtime_tenant="prod"` is the
      common case.

    The output deliberately does NOT contain a `definitely_unused` bucket.
    Even with both signals at zero, an artifact might be used via a
    longer-interval scheduled job, an unscanned source (triggers /
    workflows), or an external caller. The strongest negative finding is
    `likely_unused_candidates`, each row tagged with a confidence rating
    (`low|medium|high`) and the caveats that limit certainty.

    Buckets in the response:
    - `definitely_used.both`         — has static refs AND log hits.
    - `definitely_used.static_refs`  — static refs but 0 log hits in window.
    - `definitely_used.runtime_only` — log hits but 0 static refs (likely
      a Trigger or scheduled job; the static gap will close in PR3b).
    - `likely_unused_candidates`     — 0 static refs AND 0 log hits.

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name: the (project, module) hosting the
            candidate artifacts.
        artifact_type: "service" | "model" | "page" | "script". Only
            "service" is currently checked against runtime logs since the
            log_analysis schema is service-centric (`element_name`).
        include_runtime: if False, runtime evidence is skipped and every
            candidate is classified by static signal only. Useful when
            log_analysis isn't reachable.
        runtime_since_ms / runtime_until_ms: epoch ms; defaults to last 3 days.
            Wider windows are clamped (see `log_analysis.search_service_logs`).
        include_used: if True, return the full `definitely_used` dict
            with `both` / `static_refs` / `runtime_only` arrays. Default
            False — only the counts are returned, since callers usually
            want the candidates list. Opt in when you need the per-row
            detail (e.g. ranking by `static_ref_count`).
        start, limit: page through candidate artifacts. `limit=0` (the
            default) audits every artifact in scope. With `limit>0`, only
            artifacts `start..start+limit` are probed for runtime hits
            and surfaced in the response. `pagination.total_in_scope`
            reports how many exist module-wide so callers know if more
            pages remain.

    Returns: see _AUDIT_BUCKETS plus a `warnings` list and a `confidence_legend`.
    """
    if artifact_type not in {"service", "model", "page", "script"}:
        raise ValueError(
            f"unsupported artifact_type: {artifact_type!r}. "
            "Expected one of: service, model, page, script."
        )
    if start < 0:
        raise ValueError(f"start must be >= 0, got {start}")
    if limit < 0:
        raise ValueError(f"limit must be >= 0, got {limit}")

    src_project = search_project or project_name
    src_module = search_module or module_name

    # Static phase reuses the existing scanner end-to-end.
    static = await find_unused_artifacts(
        tenant,
        project_name,
        module_name,
        artifact_type,
        search_project=search_project,
        search_module=search_module,
    )
    static_unused_all = [row["name"] for row in static["definitely_unused"]]
    static_used_all: dict[str, int] = static["used_summary"]
    bundled_scripts_map: dict[str, list[str]] = static.get("bundled_scripts") or {}
    scanned_count: int = static["scanned_count"]

    # Apply pagination to a single ordered list of all artifact names.
    # `find_unused_artifacts` already sorts unused alphabetically and
    # `used_summary` by ref count desc — concatenate (used first, then
    # unused) so a `limit=10` page surfaces the most-used items first.
    all_names_ordered = list(static_used_all.keys()) + static_unused_all
    total_in_scope = len(all_names_ordered)
    if limit > 0:
        page_names = all_names_ordered[start : start + limit]
    else:
        page_names = all_names_ordered
    page_set = set(page_names)
    static_used_counts = {n: static_used_all[n] for n in static_used_all if n in page_set}
    static_unused = {n for n in static_unused_all if n in page_set}

    # Runtime phase. Only services have a clean log signal — for other
    # artifact types we leave runtime_hits at None so the agent doesn't
    # confuse "0 hits" with "we didn't check".
    runtime_hits: dict[str, int | None] = {}
    runtime_warnings: list[str] = []
    bundled_scripts_correlated = False
    if include_runtime and artifact_type == "service":
        from ows_gde_mcp.tools.log_analysis import count_service_invocations

        # Probes go to runtime_tenant (defaults to tenant). When auditing
        # candidates from testbed Studio, the user typically wants to
        # know whether they're used in *prod* — so let them pass
        # runtime_tenant="prod" while keeping static work on testbed.
        log_tenant = runtime_tenant or tenant

        # Cap concurrent log probes. Without a cap, a 313-service module
        # with avg 1+ bundled scripts apiece would fan out 600+ concurrent
        # POSTs — fine for the network but burns CPU on the server. 6 is
        # fast enough and leaves headroom for other in-flight tools.
        sem = asyncio.Semaphore(6)

        # Build the probe set: each service plus every bundled script it
        # owns (RunScript / ScriptLib). Hits on script names roll up to
        # the parent service. This closes the correlation gap documented
        # in docs/audit-confidence.md (the log records element_name as
        # the script name, not the parent service name, so probing only
        # the parent gives false zero hits).
        probe_targets: list[tuple[str, str]] = []  # (service_name, probe_name)
        for name in page_names:
            probe_targets.append((name, name))
            for script_name in bundled_scripts_map.get(name, []):
                probe_targets.append((name, script_name))
        bundled_scripts_correlated = True

        async def probe(probe_name: str) -> dict[str, Any]:
            async with sem:
                return await count_service_invocations(
                    log_tenant,
                    project_name,
                    module_name,
                    probe_name,
                    start_ms=runtime_since_ms,
                    end_ms=runtime_until_ms,
                )

        tasks = [probe(p) for _, p in probe_targets]
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:  # pragma: no cover — gather should never raise
            runtime_warnings.append(f"runtime probe failed: {e}")
            results = []

        # Initialise per-service hit counters so we report 0 (not None)
        # for services we did probe.
        for service_name in page_names:
            runtime_hits[service_name] = 0

        for (service_name, probe_name), res in zip(probe_targets, results, strict=False):
            if isinstance(res, Exception):
                # Don't pretend we know the count when the probe failed;
                # mark the parent as None so the bucket logic treats it
                # as unmeasured.
                runtime_hits[service_name] = None
                runtime_warnings.append(
                    f"runtime probe failed for {probe_name}: {type(res).__name__}: {res}"
                )
                continue
            if runtime_hits.get(service_name) is None:
                # A previous probe for the same service errored — keep
                # the unmeasured signal rather than overwriting with a
                # partial sum.
                continue
            hits = (res or {}).get("total_hits", 0) or 0
            runtime_hits[service_name] = (runtime_hits.get(service_name) or 0) + hits
            for w in (res or {}).get("warnings", []) or []:
                if w not in runtime_warnings:
                    runtime_warnings.append(w)
    else:
        for name in page_names:
            runtime_hits[name] = None

    # Bucketize. `n/a` (None) runtime hits flow through as if they were
    # zero for the bucket-decision so an agent that runs with
    # include_runtime=False still gets useful output, but the per-row
    # `runtime_hits` field stays None so the caller knows it's unmeasured.
    both: list[dict[str, Any]] = []
    static_only: list[dict[str, Any]] = []
    runtime_only: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []

    triggers_scanned = True  # PR3b: triggers scanned via _fetch_triggers
    workflows_scanned = False

    for name in static_used_counts:
        sref = static_used_counts[name]
        rhits = runtime_hits.get(name)
        canonical = f"/{project_name}/{module_name}/{name}"
        row = {
            "name": name,
            "uri": canonical,
            "static_ref_count": sref,
            "runtime_hits": rhits,
        }
        if (rhits or 0) > 0:
            both.append(row)
        else:
            static_only.append(row)

    for name in static_unused:
        rhits = runtime_hits.get(name)
        canonical = f"/{project_name}/{module_name}/{name}"
        row = {
            "name": name,
            "uri": canonical,
            "static_ref_count": 0,
            "runtime_hits": rhits,
        }
        if (rhits or 0) > 0:
            runtime_only.append(row)
        else:
            row["confidence"] = _confidence_for(
                0,
                0,
                triggers_scanned,
                workflows_scanned,
                bundled_scripts_correlated=bundled_scripts_correlated,
            )
            row["caveats"] = list(_AUDIT_CAVEATS_BASE)
            candidates.append(row)

    both.sort(key=lambda r: -(r["static_ref_count"] + (r["runtime_hits"] or 0)))
    static_only.sort(key=lambda r: -r["static_ref_count"])
    runtime_only.sort(key=lambda r: -(r["runtime_hits"] or 0))
    candidates.sort(key=lambda r: r["name"])

    warnings = list(_COVERAGE_WARNINGS) + runtime_warnings
    if not include_runtime:
        warnings.append("include_runtime=False — runtime log evidence not consulted.")

    if include_used:
        definitely_used: dict[str, Any] = {
            "both": both,
            "static_refs": static_only,
            "runtime_only": runtime_only,
        }
    else:
        definitely_used = {
            "both_count": len(both),
            "static_refs_count": len(static_only),
            "runtime_only_count": len(runtime_only),
        }

    return {
        "scope": {
            "project": project_name,
            "module": module_name,
            "artifact_type": artifact_type,
            "scanned_in": {"project": src_project, "module": src_module},
        },
        "scanned_count": scanned_count,
        "pagination": {
            "start": start,
            "limit": limit,
            "total_in_scope": total_in_scope,
            "returned": len(page_names),
        },
        "sources_scanned": {
            **static["sources_scanned"],
            "runtime_logs": "queried" if include_runtime else "skipped",
        },
        "definitely_used": definitely_used,
        "likely_unused_candidates": candidates,
        "confidence_legend": {
            "high": (
                "0 static refs AND 0 log hits AND every reference source "
                "scanned (services, pages, triggers, workflows, bundled scripts)."
            ),
            "medium": (
                "0 static refs AND 0 log hits but at least one reference source "
                "not yet scanned (typically workflows)."
            ),
            "low": (
                "0 static refs AND 0 log hits but multiple reference sources "
                "not yet scanned."
            ),
            "n/a": (
                "Not in `likely_unused_candidates` — the artifact has at least one signal of use."
            ),
        },
        "warnings": warnings,
    }


__all__ = [
    "audit_artifact_usage",
    "find_artifact_references",
    "find_unused_artifacts",
]
