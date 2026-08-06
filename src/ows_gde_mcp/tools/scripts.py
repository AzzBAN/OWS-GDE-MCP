"""MCP tools for OWS scripts — three categories under one surface.

OWS exposes JavaScript / scripting code in three different places, each with
a different storage shape and endpoint. This module wraps the two that were
not yet covered by the MCP, on top of the existing surfaces:

| Category | Storage | Endpoint | Wrapper |
|---|---|---|---|
| 1. Service RunScript / ScriptLib / Translator / Validator | bundled inside SERVICE artifacts | `POST /adc-studio-service/web/rest/v1/app/service/script/query-all` | `list_service_scripts`, `get_service_script` |
| 2a. Page scripts wired to a specific page | embedded in the page-detail payload | `GET /adc-studio-ui/web/rest/v1/page-core/page/{page_id}` | `get_page_scripts` |
| 2b. Page-script module catalog (the Page → Script Manage tab) | dedicated endpoint | `GET /adc-studio-ui/web/rest/v1/page-core/page-script/{project}/{module}` | `list_page_scripts` |
| 3. MCP scripts (top-level Studio Script artifact) | separate MCP artifact | `GET /adc-studio-mcp/web/rest/v1/scriptmgt/scripts` | `list_scripts` (already in `tools/live.py`) |

Endpoint shapes were captured by driving Studio in Playwright on
2026-05-18 against the testbed `centralized_inquiry_tracker` project.

## script_type values observed

`RunScript`, `ScriptLib`, `Translator`, `Validator` for service scripts.
`js`, `jsinline`, `cssinline` (and presumably `css`) for page scripts.
The catalogue is maintained server-side and may grow; pass `None` /
empty filters to enumerate all types.

## Page scripts: two shapes, two endpoints

`get_page_scripts(page_id)` returns scripts WIRED TO ONE PAGE. The data
rides along inside `get_page_detail`'s `content.js` / `content.js_content`
fields — there's no dedicated per-page endpoint.

`list_page_scripts(project, module)` returns ALL page-namespace scripts
in the module — both reusable libs (`type=js`) and per-page inline
scripts (`type=jsinline` / `cssinline`). It hits a separate dedicated
catalog endpoint that the Studio "Page Script Manage" UI fires.
"""

from __future__ import annotations

import json
from typing import Any

from ows_gde_mcp.client import OwsApiError
from ows_gde_mcp.tools.live import _studio_get, _studio_post

_SERVICE_SCRIPT_PATH = "/adc-studio-service/web/rest/v1/app/service/script/query-all"
_PAGE_DETAIL_PATH = "/adc-studio-ui/web/rest/v1/page-core/page/{page_id}"
_PAGE_SCRIPT_LIST_PATH = (
    "/adc-studio-ui/web/rest/v1/page-core/page-script/{project_name}/{module_name}"
)


def _summarize_service_script(row: dict[str, Any]) -> dict[str, Any]:
    """Slim a service-script row for listing — drops the JS body."""
    return {
        "id": row.get("id"),
        "script_name": row.get("script_name"),
        "script_type": row.get("script_type"),
        "language": row.get("language"),
        "interp_name": row.get("interp_name"),
        "version": row.get("version"),
        "active": row.get("active"),
        "project_name": row.get("project_name"),
        "module_name": row.get("module_name"),
        "description": row.get("description"),
        "created_by": row.get("created_by"),
        "updated_by": row.get("updated_by"),
        "created_time": row.get("created_time"),
        "updated_time": row.get("updated_time"),
    }


async def list_service_scripts(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    script_type: str = "",
    script_name: str = "",
    start: int = 0,
    limit: int = 100,
    confirm: bool = False,
) -> dict[str, Any]:
    """List the bundled scripts (RunScript, ScriptLib, Translator, Validator) in a module.

    Calls `POST /adc-studio-service/web/rest/v1/app/service/script/query-all`
    with `brief=true`, which omits the JS body from each row.

    These scripts live INSIDE service artifacts (under
    `SERVICE/RunScript/JavaScript/Rhino2/<name>.js` etc) and were not
    visible to `list_scripts`, which covers the separate top-level
    "MCP-Script" artifact category. On a typical app the count is high
    — `centralized_inquiry_tracker` has 76 of these vs. 0 surfaced by
    `list_scripts`.

    Args:
        tenant: "prod" or "testbed".
        project_name: Studio project (typically same as module).
        module_name: Studio module hosting the SERVICE artifacts.
        script_type: filter `"RunScript" | "ScriptLib" | "Translator" |
            "Validator"`. Empty string = all types.
        script_name: substring filter on script_name. Empty string = all.
        start: row offset (default 0).
        limit: max rows per page (default 100).
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.

    Returns:
        `{"total", "page", "page_size", "scripts": [{id, script_name,
          script_type, language, interp_name, version, active,
          project_name, module_name, description, created_by, updated_by,
          created_time, updated_time}]}`
    """
    body: dict[str, Any] = {
        "project_name": project_name,
        "module_name": module_name,
        "script_type": script_type,
        "brief": True,
        "sort_by": "updateTime",
        "start": start,
        "limit": limit,
    }
    if script_name:
        body["script_name"] = script_name
    try:
        res = await _studio_post(
            tenant, _SERVICE_SCRIPT_PATH, json=body, confirm=confirm, read_only=True
        )
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": e.message,
                "path": e.path,
            }
        }

    if not isinstance(res, dict):
        return {"total": 0, "scripts": [], "raw": res}

    rows = res.get("content") or []
    return {
        "total": res.get("totalElements", len(rows)),
        "page": res.get("number", 0),
        "page_size": res.get("size", limit),
        "scripts": [
            _summarize_service_script(r) for r in rows if isinstance(r, dict)
        ],
    }


async def get_service_script(
    tenant: str,
    project_name: str,
    module_name: str,
    script_name: str,
    *,
    script_type: str = "",
    confirm: bool = False,
) -> dict[str, Any]:
    """Fetch a service script's full JS body and metadata.

    Calls `POST /adc-studio-service/web/rest/v1/app/service/script/query-all`
    with `script_name=<name>` and `brief=false` (default), so each row
    carries the full `content` field with the JS body.

    The endpoint is shared with `list_service_scripts` — the difference is
    that here `brief` is omitted and `script_name` is supplied as an exact
    filter. If multiple types share the name (rare), pass `script_type` to
    disambiguate.

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name: where the script lives.
        script_name: exact `script_name` to fetch (e.g. `runScript_um_handling`).
        script_type: optional `RunScript | ScriptLib | Translator |
            Validator` to disambiguate. Empty string = match any.
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.

    Returns:
        Single script row including `content` (the full JS body):
        `{id, script_name, script_type, language, interp_name, version,
          script_type, content, active, ...}`. If not found, returns
        `{"error": "..."}`.
    """
    body: dict[str, Any] = {
        "project_name": project_name,
        "module_name": module_name,
        "script_type": script_type,
        "script_name": script_name,
        "start": 0,
        "limit": 100,
    }
    try:
        res = await _studio_post(
            tenant, _SERVICE_SCRIPT_PATH, json=body, confirm=confirm, read_only=True
        )
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": e.message,
                "path": e.path,
            }
        }

    rows = res.get("content") if isinstance(res, dict) else None
    if not rows:
        return {
            "error": (
                f"Script {script_name!r} not found in "
                f"{project_name}/{module_name}"
            )
        }

    # The server already filters by exact `script_name`, but be defensive.
    for row in rows:
        if isinstance(row, dict) and row.get("script_name") == script_name:
            return row
    return {
        "error": (
            f"Script {script_name!r} not found in "
            f"{project_name}/{module_name} (server returned {len(rows)} unrelated rows)"
        )
    }


def _project_page_scripts(
    content: dict[str, Any], *, include_content: bool, kind: str = "js"
) -> list[dict[str, Any]]:
    """Project page-script references + bodies out of a parsed SPL tree.

    Args:
        content: parsed `content` dict (already JSON-decoded).
        include_content: if True, attach the matching JS/CSS body from
            `<kind>_content` to each reference. Bodies of other-module libs
            this page imports are included verbatim.
        kind: `"js"` or `"css"` — picks which keys we project.

    Returns:
        list of `{name, project, module, lib, type, inline, open_level,
                  has_content, content?}`
    """
    refs = content.get(kind) or []
    bodies = content.get(f"{kind}_content") or {}
    out = []
    for ref in refs:
        if not isinstance(ref, dict):
            continue
        proj = ref.get("projectName")
        mod = ref.get("moduleName")
        lib = ref.get("lib")
        body_key = f"{proj}/{mod}/{lib}" if (proj and mod and lib) else None
        body = bodies.get(body_key) if body_key else None
        item: dict[str, Any] = {
            "name": ref.get("name") or lib,
            "project": proj,
            "module": mod,
            "lib": lib,
            "type": ref.get("type"),
            "inline": ref.get("inline"),
            "open_level": ref.get("openLevel"),
            "has_content": body is not None,
        }
        if include_content and isinstance(body, str):
            item["content"] = body
        out.append(item)
    return out


async def get_page_scripts(
    tenant: str,
    page_id: str,
    *,
    include_content: bool = True,
    include_css: bool = True,
) -> dict[str, Any]:
    """Fetch the JS (and optionally CSS) scripts wired to a page.

    Page scripts (the items under Page → Script tab in Studio: `init`,
    `utils`, `query`, `events`, `main_js_clone`, etc) live INSIDE the
    page-detail payload — there is no separate page-script endpoint. This
    tool calls `GET /adc-studio-ui/web/rest/v1/page-core/page/{page_id}`,
    parses `content`, and projects `js` / `js_content` (and `css` /
    `css_content`) into a flat list. Bodies of scripts owned by other
    modules that this page imports are included verbatim.

    Args:
        tenant: "prod" or "testbed".
        page_id: numeric page id (as string). Find via `list_pages` (`row["id"]`).
        include_content: when True (default), each script entry carries
            `content` (the JS body). Pass False to get only the wiring
            metadata (saves a lot of bytes for dense pages).
        include_css: when True (default), also include CSS scripts under
            the `css` key.

    Returns:
        `{"page_id", "page_name", "project_name", "module_name", "page_type",
          "js": [{name, project, module, lib, type, inline, open_level,
                  has_content, content?}, ...],
          "css": [...]   # only when include_css is True
         }`
    """
    try:
        row = await _studio_get(tenant, _PAGE_DETAIL_PATH.format(page_id=page_id))
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": e.message,
                "path": e.path,
            }
        }

    if not isinstance(row, dict):
        return {"error": f"Page {page_id} not found or unexpected payload"}

    raw_content = row.get("content")
    if not isinstance(raw_content, str) or not raw_content:
        return {
            "page_id": row.get("id"),
            "page_name": row.get("name"),
            "project_name": row.get("project_name"),
            "module_name": row.get("module_name"),
            "page_type": row.get("type"),
            "js": [],
            **({"css": []} if include_css else {}),
            "warning": "Page has no content (empty SPL tree).",
        }
    try:
        content = json.loads(raw_content)
    except (ValueError, TypeError) as e:
        return {
            "page_id": row.get("id"),
            "page_name": row.get("name"),
            "error": f"Failed to parse content: {type(e).__name__}: {e}",
        }

    out: dict[str, Any] = {
        "page_id": row.get("id"),
        "page_name": row.get("name"),
        "project_name": row.get("project_name"),
        "module_name": row.get("module_name"),
        "page_type": row.get("type"),
        "js": _project_page_scripts(
            content, include_content=include_content, kind="js"
        ),
    }
    if include_css:
        out["css"] = _project_page_scripts(
            content, include_content=include_content, kind="css"
        )
    return out


def _summarize_page_script(row: dict[str, Any], *, include_body: bool) -> dict[str, Any]:
    """Slim a page-script catalog row.

    `script` (the JS/CSS body) is optional — pass `include_body=False`
    when listing 50+ rows so the response stays under a reasonable size.
    """
    out = {
        "id": row.get("id"),
        "name": row.get("name"),
        "type": row.get("type"),
        "page_name": row.get("page_name"),
        "page_type": row.get("page_type"),
        "open_level": row.get("open_level"),
        "key_code": row.get("key_code"),
        "project_name": row.get("project_name"),
        "module_name": row.get("module_name"),
        "description": row.get("description"),
        "origin_name": row.get("origin_name"),
        "updater": row.get("updater"),
        "update_time": row.get("update_time"),
    }
    if include_body:
        out["script"] = row.get("script")
    else:
        out["script_length"] = len(row.get("script") or "")
    return out


async def list_page_scripts(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    name: str = "",
    page: int = 0,
    page_size: int = 50,
    sort: str = "updateTime",
    direction: str = "DESC",
    include_body: bool = False,
) -> dict[str, Any]:
    """List the page-namespace scripts (the catalog behind Studio's Page → Script Manage tab).

    Calls `GET /adc-studio-ui/web/rest/v1/page-core/page-script/<project>/<module>`.

    This is the module-level catalog of page scripts — every reusable JS
    library and per-page inline script in the module, surfaced in one
    response. It complements `get_page_scripts(page_id)` which returns
    only the scripts wired to a single page.

    The endpoint returns the full `script` body inline for every row.
    Default `include_body=False` strips the body and keeps only metadata
    + `script_length` so the response stays compact when enumerating
    50+ scripts. Pass `include_body=True` when you need the source.

    Each row's `type` is one of:
    - `js` — reusable JavaScript library (the "lib" entries shown on
      `get_page_scripts`).
    - `jsinline` — JS bound to a specific page (e.g. the `header`
      entry visible in the Studio Page Script tab on `CIT_Query_v2`).
    - `cssinline` — CSS bound to a specific page (and presumably `css`
      for reusable CSS libs, though not observed in the sample).

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name: where the scripts live.
        name: substring filter on script name. Empty = all.
        page: zero-indexed page number.
        page_size: rows per page (default 50).
        sort: column to sort by (default `updateTime`).
        direction: `"ASC"` | `"DESC"`.
        include_body: if True, include the full `script` body per row.
            Default False — replace with `script_length`.

    Returns:
        `{"total", "page", "page_size", "totalPage", "scripts": [...]}`
    """
    params: dict[str, Any] = {
        "projectName": project_name,
        "moduleName": module_name,
        "page": page,
        "pageSize": page_size,
        "name": name,
        "sort": sort,
        "dir": direction,
    }
    try:
        res = await _studio_get(
            tenant,
            _PAGE_SCRIPT_LIST_PATH.format(
                project_name=project_name, module_name=module_name
            ),
            params=params,
        )
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": e.message,
                "path": e.path,
            }
        }

    if not isinstance(res, dict):
        return {"total": 0, "scripts": [], "raw": res}

    rows = res.get("data") or []
    return {
        "total": res.get("total", len(rows)),
        "totalPage": res.get("totalPage"),
        "page": res.get("page", page),
        "page_size": res.get("pageSize", page_size),
        "scripts": [
            _summarize_page_script(r, include_body=include_body)
            for r in rows
            if isinstance(r, dict)
        ],
    }


async def create_service_script(
    tenant: str,
    project_name: str,
    module_name: str,
    script_name: str,
    content: str,
    *,
    script_type: str = "RunScript",
    language: str = "JavaScript",
    interp_name: str = "Rhino2",
    version: str = "1.0",
    confirm: bool = False,
) -> dict[str, Any]:
    """Create a new service script (RunScript, ScriptLib, etc.) in GDE Studio.

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name: where to create the script.
        script_name: name of the new script (e.g. `runScript_calculate`).
        content: JavaScript body content.
        script_type: type of the script (default: `"RunScript"`).
        language: programming language (default: `"JavaScript"`).
        interp_name: runtime engine interpreter (default: `"Rhino2"`).
        version: metadata version string (default: `"1.0"`).
        confirm: required True to allow writes against production.
    """
    body: dict[str, Any] = {
        "project_name": project_name,
        "module_name": module_name,
        "script_name": script_name,
        "script_type": script_type,
        "language": language,
        "interp_name": interp_name,
        "version": version,
        "content": content,
        "active": True,
    }
    try:
        res = await _studio_post(
            tenant,
            "/adc-studio-service/web/rest/v1/app/service/script/create",
            json=body,
            confirm=confirm,
        )
        return {"status": "success", "id": res}
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": e.message,
                "path": e.path,
            }
        }


async def update_service_script(
    tenant: str,
    project_name: str,
    module_name: str,
    script_name: str,
    content: str,
    *,
    script_type: str = "RunScript",
    confirm: bool = False,
) -> dict[str, Any]:
    """Update (save) the content of an existing service/module script in GDE Studio.

    Fetches the existing script record metadata dynamically to obtain ID, version,
    and interpreter settings, replaces the code body, and POSTs to `/update`.

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name: where the script lives.
        script_name: exact script name.
        content: new JavaScript body content to save.
        script_type: script type filter (default: `"RunScript"`).
        confirm: required True to allow writes against production.
    """
    query_body: dict[str, Any] = {
        "project_name": project_name,
        "module_name": module_name,
        "script_name": script_name,
        "script_type": script_type,
        "start": 0,
        "limit": 10,
    }
    try:
        res_list = await _studio_post(
            tenant,
            _SERVICE_SCRIPT_PATH,
            json=query_body,
            confirm=confirm,
            read_only=True,
        )
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": f"Failed to fetch script metadata: {e.message}",
                "path": e.path,
            }
        }

    rows = res_list.get("content") if isinstance(res_list, dict) else None
    if not rows:
        return {
            "error": f"Script {script_name!r} not found in {project_name}/{module_name}"
        }

    target_row = None
    for row in rows:
        if isinstance(row, dict) and row.get("script_name") == script_name:
            target_row = row
            break

    if not target_row:
        return {
            "error": f"Script {script_name!r} metadata lookup failed."
        }

    target_row["content"] = content

    try:
        await _studio_post(
            tenant,
            "/adc-studio-service/web/rest/v1/app/service/script/update",
            json=target_row,
            confirm=confirm,
        )
        return {
            "status": "success",
            "id": target_row.get("id"),
            "script_name": script_name,
            "version": target_row.get("version"),
            "updater": target_row.get("updated_by"),
            "update_time": target_row.get("updated_time"),
        }
    except OwsApiError as e:
        return {
            "error": {
                "status": e.status,
                "code": e.code,
                "message": f"Failed to save script: {e.message}",
                "path": e.path,
            }
        }


__all__ = [
    "create_service_script",
    "get_page_scripts",
    "get_service_script",
    "list_page_scripts",
    "list_service_scripts",
    "update_service_script",
]
