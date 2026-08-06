"""MCP tools that hit the **live** OWS API.

All tools take an explicit `tenant: "prod" | "testbed"` argument. Each tool
internally routes to the correct **surface** for the API it's calling:

- **Studio surface** (`/adc-studio-*/...`) — design-time authoring APIs.
  Used by `list_studio_projects`, `list_models`, `list_services`,
  `list_pages`, `list_scripts`, etc.
- **Runtime surface** (`/portal/...`, `/adc-model/...`, `/adc-service/...`) —
  deployed-app APIs. Used by `list_live_menus`, `list_live_apps`,
  `get_favorite_menus`, `get_model_fields`, etc.

A tenant must have the matching surface URL configured in `.env`, otherwise
the tool raises a clear "no <surface> URL configured for <tenant>" error.

Auth (cookie + CSRF + page-token headers) is supplied by `OwsClient` and
shared across surfaces of the same tenant.
"""

from __future__ import annotations

from typing import Any

from ows_gde_mcp.client import OwsApiError, OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings
from ows_gde_mcp.service_guard import is_write_service
from ows_gde_mcp.tools.pages import get_page, get_page_detail, list_pages

# ---------------- internal helpers ----------------


async def _runtime_get(tenant: str, path: str, **kwargs: Any) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.RUNTIME, settings) as client:
        return await client.get(path, **kwargs)


async def _runtime_post(
    tenant: str,
    path: str,
    json: Any = None,
    *,
    confirm: bool = False,
    **kwargs: Any,
) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.RUNTIME, settings) as client:
        return await client.post(path, json=json, confirm=confirm, **kwargs)


async def _studio_get(tenant: str, path: str, **kwargs: Any) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.STUDIO, settings) as client:
        return await client.get(path, **kwargs)


async def _studio_post(
    tenant: str,
    path: str,
    json: Any = None,
    *,
    confirm: bool = False,
    read_only: bool = False,
    **kwargs: Any,
) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.STUDIO, settings) as client:
        return await client.post(
            path, json=json, confirm=confirm, read_only=read_only, **kwargs
        )


def _flatten_menu(node: dict, *, parents: tuple[str, ...] = ()) -> list[dict]:
    """Flatten the nested 'getGranted' menu tree into a flat list."""
    out: list[dict] = []
    name = node.get("name") or node.get("text") or ""
    item = {
        "name": name,
        "text": node.get("text"),
        "type": node.get("type"),
        "module": node.get("module"),
        "url": node.get("url"),
        "permission_code": node.get("permission_code"),
        "parent_path": "/".join(parents) if parents else None,
        "active": node.get("active"),
    }
    out.append(item)
    for child in node.get("child") or []:
        out.extend(_flatten_menu(child, parents=(*parents, name)))
    return out


# ---------------- public MCP tools ----------------


async def list_live_menus(
    tenant: str,
    *,
    flatten: bool = False,
    only_with_url: bool = False,
) -> list[dict]:
    """List the menu tree granted to the current user.

    Calls `GET /portal/web/rest/v1/menu/manage/app/getGranted?granted=true`.

    Args:
        tenant: "prod" or "testbed".
        flatten: If true, returns a flat list of every node with its
                 parent_path. If false, returns the hierarchical tree.
        only_with_url: If flattening, drop nodes that don't have a URL
                 (i.e. keep only clickable leaf entries).
    """
    tree = await _runtime_get(
        tenant,
        "/portal/web/rest/v1/menu/manage/app/getGranted",
        params={"granted": "true"},
    )
    if not isinstance(tree, list):
        return tree  # surface unexpected shape
    if not flatten:
        return tree
    items: list[dict] = []
    for root in tree:
        items.extend(_flatten_menu(root))
    if only_with_url:
        items = [i for i in items if i.get("url")]
    return items


async def list_live_apps(tenant: str) -> list[dict]:
    """List unique OWS apps the current user has access to.

    Derived from the granted-menu tree's `module` field, which uses
    `project.module` dot notation (e.g. `thirdparty_dashboard.flp_tt_tracker`).

    Returns a list of `{project, module, menu_count, sample_text}` rows
    aggregated across the menu tree.
    """
    flat = await list_live_menus(tenant, flatten=True)
    counts: dict[tuple[str, str], dict[str, Any]] = {}
    for item in flat:
        mod = item.get("module")
        if not mod or not isinstance(mod, str):
            continue
        if "." in mod:
            project, module = mod.split(".", 1)
        else:
            project, module = mod, ""
        key = (project, module)
        if key not in counts:
            counts[key] = {
                "project": project,
                "module": module,
                "menu_count": 0,
                "sample_text": item.get("text"),
            }
        counts[key]["menu_count"] += 1
    return sorted(counts.values(), key=lambda x: (x["project"], x["module"]))


async def get_favorite_menus(tenant: str) -> list[dict]:
    """Return the current user's pinned/favorite menu entries.

    Calls `GET /portal/web/rest/v1/menu/favorites`.
    """
    res = await _runtime_get(tenant, "/portal/web/rest/v1/menu/favorites")
    if not isinstance(res, list):
        return res
    out: list[dict] = []
    for fav in res:
        menu = fav.get("menu", {}) if isinstance(fav, dict) else {}
        out.append(
            {
                "id": fav.get("id") if isinstance(fav, dict) else None,
                "name": menu.get("name"),
                "text": menu.get("text"),
                "module": menu.get("module"),
                "url": menu.get("url"),
                "permission_code": menu.get("permission_code"),
            }
        )
    return out


async def get_model_fields(tenant: str, asset_uri: str) -> dict[str, Any]:
    """Return the TQL queryable-field schema for a Model asset.

    Calls `POST /adc-model/web/rest/v1/app/tql/init?asset_uri=<uri>` with
    an empty body — the same call the Studio UI makes when initialising a
    query builder for a model.

    Args:
        tenant: "prod" or "testbed".
        asset_uri: the asset URI (e.g. "mtask_work", or a fully-qualified
                   `/project/module/model_name`).

    Returns:
        `{"asset_uri", "field_count", "fields": [{name, label, type,
        operators, enum_values?, ...}, ...]}`
    """
    res = await _runtime_post(
        tenant,
        "/adc-model/web/rest/v1/app/tql/init",
        params={"asset_uri": asset_uri},
        json={},
        confirm=True,
        read_only=True,
    )
    packages = res.get("packages") if isinstance(res, dict) else None
    if not isinstance(packages, list):
        return {"asset_uri": asset_uri, "raw": res}
    fields = [
        {
            "id": p.get("id"),
            "name": p.get("name"),
            "label": p.get("label"),
            "type": p.get("type"),
            "operators": p.get("operators"),
            "enum_values": p.get("data"),
        }
        for p in packages
        if isinstance(p, dict)
    ]
    return {
        "asset_uri": asset_uri,
        "field_count": len(fields),
        "fields": fields,
    }


async def call_ows_api(
    tenant: str,
    method: str,
    path: str,
    *,
    surface: str = "runtime",
    body: Any = None,
    params: dict[str, Any] | None = None,
    confirm: bool = False,
) -> Any:
    """Generic escape hatch — call any OWS endpoint that we haven't yet
    wrapped with a typed tool.

    All anti-tamper headers + cookies are attached automatically.

    Args:
        tenant: "prod" or "testbed".
        method: HTTP method (case-insensitive). Mutations against `prod`
                additionally require `confirm=True` and
                `OWS_PROD_WRITE_ENABLED=1` (set in `.env`).
        path: starts with `/`, e.g. `/portal/web/rest/v1/user/my-info`.
        surface: which base URL to route through — `"runtime"` (default,
                for `/portal/...`, `/adc-model/...`, `/adc-service/...`)
                or `"studio"` (for `/adc-studio-*/...` design-time APIs).
                Pick by the path mount: studio APIs only exist on the
                studio host.
        body: optional JSON body (for POST/PUT/etc.).
        params: optional query-string parameters.
        confirm: required `True` to allow non-GET methods against `prod`.

    Returns:
        Parsed JSON response (or raw text if not JSON).
    """
    t = Tenant(tenant)
    s = Surface(surface)
    method_u = method.upper()
    # Name-based safety net for the generic escape hatch: block obvious
    # write services on any tenant. Complements the prod write-gate (which
    # only covers the prod tenant). Legitimate writes go through the typed
    # tools or `confirm=True` + `OWS_PROD_WRITE_ENABLED=1` on the prod gate.
    if method_u != "GET":
        last_segment = path.rstrip("/").rsplit("/", 1)[-1].split("?", 1)[0]
        if is_write_service(last_segment):
            return {
                "error": {
                    "code": "write_guard",
                    "message": (
                        f"Path segment {last_segment!r} looks like a write operation. "
                        "Use the typed tool for this operation, or confirm=True against prod."
                    ),
                }
            }
    async with OwsClient.for_surface(t, s, settings) as client:
        try:
            return await client.request(method_u, path, params=params, json=body, confirm=confirm)
        except OwsApiError as e:
            return {
                "error": {
                    "status": e.status,
                    "code": e.code,
                    "message": e.message,
                    "path": e.path,
                }
            }


# ============================================================
# Studio (design-state) — Projects, Modules, Models
# ============================================================


async def list_studio_projects(
    tenant: str,
    *,
    start: int = 0,
    limit: int = 50,
    verbose: bool = False,
) -> dict[str, Any]:
    """List recently-viewed Studio projects with full metadata.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/recent-projects`.

    Args:
        verbose: if True, include the upstream raw rows verbatim under
            `projects` instead of the summarised shape. Useful when you
            need fields the summary drops; default is the lean form.

    Returns:
        `{"total", "projects": [{id, name, display_name, scene, creator,
        create_time, updater, update_time, description, ...}]}`
    """
    res = await _studio_get(
        tenant,
        "/adc-studio-project-mgt/web/rest/v1/recent-projects",
        params={"start": start, "limit": limit},
    )
    data = (res or {}).get("data") or {}
    raw_rows = data.get("data") or []
    if verbose:
        return {"total": data.get("total", len(raw_rows)), "projects": raw_rows}
    projects = []
    for row in raw_rows:
        proj = row.get("project") or row
        projects.append(
            {
                "id": proj.get("id"),
                "name": proj.get("name"),
                "display_name": proj.get("display_name"),
                "scene": proj.get("scene"),
                "creator": proj.get("creator"),
                "create_time": proj.get("create_time"),
                "updater": proj.get("updater"),
                "update_time": proj.get("update_time"),
                "description": proj.get("description"),
                "customized": proj.get("customized"),
                "is_legacy_project": proj.get("is_legacy_project"),
                "uuid": proj.get("uuid"),
                "last_visited": row.get("last_time"),
            }
        )
    return {"total": data.get("total", len(projects)), "projects": projects}


async def get_studio_project(tenant: str, project: str | int) -> dict[str, Any]:
    """Get one Studio project by id or by name.

    Args:
        project: numeric project id (int/str of digits) OR project name.
    """
    p = str(project)
    path = (
        f"/adc-studio-project-mgt/web/rest/v1/projects/{p}"
        if p.isdigit()
        else f"/adc-studio-project-mgt/web/rest/v1/projects/name/{p}"
    )
    res = await _studio_get(tenant, path)
    return (res or {}).get("data") or res


async def list_project_modules(
    tenant: str,
    project_id: int,
    *,
    verbose: bool = False,
) -> list[dict[str, Any]]:
    """List modules inside a Studio project.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/project/{project_id}/modules`.

    Args:
        verbose: if True, return the upstream rows unfiltered. Default
            returns the summarised shape (lean by default).
    """
    res = await _studio_get(
        tenant,
        f"/adc-studio-project-mgt/web/rest/v1/project/{project_id}/modules",
    )
    rows = (res or {}).get("data") or []
    if verbose:
        return list(rows)
    return [
        {
            "id": m.get("id"),
            "name": m.get("name"),
            "prefix": m.get("prefix"),
            "project_id": m.get("project_id"),
            "creator": m.get("creator"),
            "create_time": m.get("create_time"),
            "updater": m.get("updater"),
            "update_time": m.get("update_time"),
            "description": m.get("description"),
            "is_customizable": m.get("is_customizable"),
            "customized": m.get("customized"),
            "basic_module": m.get("basic_module"),
            "legacy": m.get("legacy"),
        }
        for m in rows
    ]


async def list_studio_element_types(
    tenant: str,
    *,
    display_only: bool = True,
) -> dict[str, Any]:
    """Catalogue every Studio artifact "element type" (~80 types).

    Calls `GET /adc-studio-project-mgt/web/rest/v1/modules/element-type`.

    The catalogue is the master list behind the Studio resource picker
    (Common, Data Factory, AI Studio, Agent, Openness Integration,
    Interface Package, RPA, OM Events, MCP, Data Package, Automatic
    Diagnosis and Recovery). Each row carries the type id, code, label,
    navigate/locate URLs (the Studio UI it opens for that type), and
    engine_id.

    Args:
        display_only: filter to types where `display=True`. Internal
            housekeeping types (NE_TYPE, AI_RUNTIME variants used only
            for cross-references, etc.) have `display=False` and are
            excluded by default. Pass False to see everything.

    Returns:
        `{"total", "element_types": [{id, item_type, label,
        navigate_uri (parsed dict), locate_uri, engine_id, display}]}`
    """
    import json as _json

    res = await _studio_get(
        tenant,
        "/adc-studio-project-mgt/web/rest/v1/modules/element-type",
    )
    rows: list[Any] = (
        res.get("data") if isinstance(res, dict) and isinstance(res.get("data"), list) else []
    )
    if display_only:
        rows = [r for r in rows if isinstance(r, dict) and r.get("display")]
    out: list[dict[str, Any]] = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        nav_raw = r.get("navigate_uri")
        nav: Any = None
        if isinstance(nav_raw, str) and nav_raw.strip():
            # Upstream double-encodes navigate_uri as a JSON string.
            try:
                nav = _json.loads(nav_raw)
            except Exception:
                nav = nav_raw
        out.append(
            {
                "id": r.get("id"),
                "item_type": r.get("item_type"),
                "label": r.get("label"),
                "navigate_uri": nav,
                "locate_uri": r.get("locate_uri"),
                "engine_id": r.get("engine_id"),
                "display": r.get("display"),
                "display_type": r.get("display_type"),
            }
        )
    return {"total": len(out), "element_types": out}


async def get_studio_module(tenant: str, module_id: int) -> dict[str, Any]:
    """Get module detail including which artifact types it supports.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/modules/{module_id}`.

    Returns the module's `items` list — the artifact-type categories enabled
    on that module (MODEL, PAGE, SERVICE, WORKFLOW, etc.).
    """
    res = await _studio_get(
        tenant,
        f"/adc-studio-project-mgt/web/rest/v1/modules/{module_id}",
    )
    data = (res or {}).get("data") or res or {}
    items = data.get("items") or []
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "prefix": data.get("prefix"),
        "project_id": data.get("project_id"),
        "description": data.get("description"),
        "supported_item_types": [
            {
                "id": it.get("id"),
                "item_type": it.get("item_type"),
                "label": it.get("label"),
                "engine_id": it.get("engine_id"),
            }
            for it in items
        ],
    }


def _summarize_basemodel(m: dict[str, Any]) -> dict[str, Any]:
    return {
        "model_id": m.get("model_id"),
        "model_name": m.get("model_name"),
        "display_name": m.get("display_name"),
        "model_type": m.get("model_type"),
        "project_name": m.get("project_name"),
        "module_name": m.get("module_name"),
        "open_level": m.get("open_level"),
        "inheritable": m.get("inheritable"),
    }


_QUERY_BASE_MODELS_PATH = "/adc-app-ops/web/rest/v1/model-data-management/queryBaseModels"


async def list_models(
    tenant: str,
    *,
    project_name: str = "",
    module_name: str = "",
    model_name: str = "",
    model_type: str = "",
    open_level: str = "",
    start: int = 0,
    limit: int = 10,
    brief_query: bool = True,
) -> dict[str, Any]:
    """List Data Models across one or many projects/modules.

    Calls `POST /adc-app-ops/web/rest/v1/model-data-management/queryBaseModels`
    on the **runtime** surface — same `/adc-app-ops/...` family used by
    `query_model_data`. The endpoint is read-only, so the prod write-gate
    is bypassed internally (`confirm=True, read_only=True`).

    Unlike the earlier Studio-only implementation, `project_name` and
    `module_name` are optional — leave them empty to search across the
    whole tenant by `model_name`. To prevent accidental tenant-wide dumps,
    `model_name` is required when both `project_name` and `module_name`
    are empty.

    Args:
        tenant: "prod" or "testbed".
        project_name: optional project filter (substring match server-side).
        module_name: optional module filter.
        model_name: substring filter on model_name. Required when both
            `project_name` and `module_name` are empty.
        model_type: optional filter, e.g. "datamodel", "proxymodel",
            "elasticmodel".
        open_level: optional filter on open_level (e.g. "public").
        start: row offset (default 0).
        limit: rows per page (default 10 — matches the upstream sample;
            bump for broader scans).
        brief_query: pass-through to the upstream. True (default) returns
            the lean shape this tool summarises.

    Returns:
        `{"total", "start", "limit", "models": [{model_id, model_name,
          display_name, model_type, project_name, module_name, open_level,
          inheritable}]}`. On HTTP error: `{"error": {...}}`.

        **ID space note:** the `model_id` values returned here are
        **runtime IDs** from the `/adc-app-ops/...` catalog. They are
        NOT the same as Studio model IDs and cannot be passed to
        `get_model`. To get the full property schema use
        `get_model_schema(tenant, project_name, module_name, model_name)`
        which resolves by name and uses the Studio surface directly.
    """
    if not project_name and not module_name and not model_name:
        return {
            "error": {
                "code": "missing_filter",
                "message": (
                    "model_name is required when both project_name and "
                    "module_name are empty (refusing tenant-wide dump)."
                ),
            }
        }
    try:
        res = await _runtime_post(
            tenant,
            _QUERY_BASE_MODELS_PATH,
            json={
                "project_name": project_name,
                "module_name": module_name,
                "model_name": model_name,
                "model_type": model_type,
                "open_level": open_level,
                "start": start,
                "limit": limit,
                "brief_query": brief_query,
            },
            confirm=True,
            read_only=True,
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
    rows = (res or {}).get("data") or []
    return {
        "total": (res or {}).get("total", 0),
        "start": (res or {}).get("start", start),
        "limit": (res or {}).get("limit", limit),
        "models": [_summarize_basemodel(m) for m in rows if isinstance(m, dict)],
    }


async def get_model(
    tenant: str,
    model_id: int,
    *,
    properties_only: bool = False,
    confirm: bool = False,
) -> dict[str, Any]:
    """Fetch a Data Model's full schema by Studio model id.

    Calls `POST /adc-studio-model/web/rest/v1/models/query-by-id?model_id=<id>`.

    **IMPORTANT — ID space:** this endpoint requires a **Studio model ID**,
    which is different from the runtime model ID returned by `list_models`.
    Passing a runtime ID here will fail with "Model does not exist".
    Use `get_model_schema(tenant, project_name, module_name, model_name)`
    instead — it resolves by name and never requires a numeric ID.

    Args:
        model_id: Studio model ID (NOT the runtime ID from list_models).
        properties_only: if True, return only `{model_id, model_name,
            properties}` — drops indexes, behaviors, validations, and other
            heavy sections.
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.
    """
    res = await _studio_post(
        tenant,
        "/adc-studio-model/web/rest/v1/models/query-by-id",
        params={"model_id": model_id},
        confirm=confirm,
        read_only=True,
    )
    if not properties_only:
        return res
    if not isinstance(res, dict):
        return {"model_id": model_id, "model_name": None, "properties": []}
    body = res.get("data") if isinstance(res.get("data"), dict) else res
    return {
        "model_id": body.get("model_id", model_id),
        "model_name": body.get("model_name"),
        "properties": body.get("properties") or [],
    }


async def get_model_schema(
    tenant: str,
    project_name: str,
    module_name: str,
    model_name: str = "",
    confirm: bool = False,
) -> dict[str, Any]:
    """Fetch full model schema(s) from Studio by name — no numeric ID needed.

    Calls `POST /adc-studio-model/web/rest/v1/models/query-all` with
    `project_name` + `module_name` as query params. Returns every model in
    the module with its full property list (type, restrictions, primary_key,
    required, default_value, etc.) and Studio metadata.

    This is the **correct tool for full schema discovery**. Unlike `get_model`,
    it uses name-based coordinates so there is no runtime-vs-Studio ID space
    confusion. Unlike `list_models`, it hits the Studio surface and returns
    the complete property schema.

    Args:
        tenant: "prod" or "testbed". Studio surface required — use testbed
            for design-time schema inspection.
        project_name: Studio project name (e.g. "datahub").
        module_name: Studio module name (e.g. "cmdb").
        model_name: exact model name filter (e.g. "cmdb_cell"). Leave empty
            to return all models in the module (can be large).
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.

    Returns:
        If `model_name` is given and found:
            `{model_id, model_name, display_name, model_type, model_uri,
              project_name, module_name, open_level, active, properties[],
              indexes[], inheritable, description, ...}`
        If `model_name` is empty:
            `{"total": N, "models": [...]}`  — one entry per model in module.
        On error: `{"error": {...}}`.

        Each property row: `{property_id, property_name, display_name,
        property_type, primary_key, required, default_value?, description?,
        model_id, restrictions[], customized, self_customized, sort}`.
    """
    try:
        res = await _studio_post(
            tenant,
            "/adc-studio-model/web/rest/v1/models/query-all",
            params={"project_name": project_name, "module_name": module_name},
            json={},
            confirm=confirm,
            read_only=True,
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

    if not isinstance(res, list):
        return {"error": {"message": "Unexpected response shape", "raw": res}}

    if model_name:
        for m in res:
            if isinstance(m, dict) and m.get("model_name") == model_name:
                return m
        return {
            "error": {
                "code": "not_found",
                "message": f"Model {model_name!r} not found in {project_name}/{module_name}",
            }
        }

    return {"total": len(res), "models": res}


# ============================================================
# Studio (design-state) — Services
# ============================================================


async def list_services(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    service_name: str = "",
    start: int = 0,
    limit: int = 50,
    include_flow: bool = False,
    confirm: bool = False,
) -> dict[str, Any]:
    """List Services declared in a Studio project module.

    Calls `POST /adc-studio-service/web/rest/v1/app/service/query`.

    The upstream endpoint always ships the full `flow` JSON (steps,
    transitions, input/output schema) per service over the wire — the
    same shape as `SERVICE/<name>.json` in a `.gpk` export. By default
    this tool returns a per-service summary only; pass
    `include_flow=True` to keep the heavy `flow` field per row. Beware:
    on a 313-service module the flow blob inflates the response by 1+ MB.

    Args:
        include_flow: if True, append `flow` to each summarized row.
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.

    Returns:
        Default: `{"total", "services": [{id, service_name, service_uri,
        ui_api, open_level, active, async, enable_operation_log,
        project_name, module_name, created_by, updated_by, created_time,
        updated_time}]}`
        With `include_flow=True`: each row also carries `flow`.
    """
    res = await _studio_post(
        tenant,
        "/adc-studio-service/web/rest/v1/app/service/query",
        json={
            "project_name": project_name,
            "module_name": module_name,
            "service_name": service_name,
            "start": start,
            "limit": limit,
        },
        confirm=confirm,
        read_only=True,
    )
    instances = (res or {}).get("instances") or []
    summary = []
    for s in instances:
        if not isinstance(s, dict):
            continue
        row = {
            "id": s.get("id"),
            "service_name": s.get("service_name"),
            "service_uri": s.get("service_uri"),
            "ui_api": s.get("ui_api"),
            "open_level": s.get("open_level"),
            "active": s.get("active"),
            "async": s.get("async"),
            "enable_operation_log": s.get("enable_operation_log"),
            "project_name": s.get("project_name"),
            "module_name": s.get("module_name"),
            "created_by": s.get("created_by"),
            "updated_by": s.get("updated_by"),
            "created_time": s.get("created_time"),
            "updated_time": s.get("updated_time"),
        }
        if include_flow:
            row["flow"] = s.get("flow")
        summary.append(row)
    return {
        "total": (res or {}).get("total", len(instances)),
        "services": summary,
    }


async def get_service(
    tenant: str,
    project_name: str,
    module_name: str,
    service_name: str,
    *,
    flow_only: bool = False,
    confirm: bool = False,
) -> dict[str, Any]:
    """Fetch one Service's full definition (including its `flow` steps).

    Implemented as a tightly-filtered `list_services` since the studio API
    surfaces full definitions in the list call. If the exact match returns
    nothing, callers should re-issue `list_services` with a substring.

    Args:
        flow_only: if True, return only `{service_name, flow}` — useful
            when the agent only wants to inspect the flow steps.
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.
    """
    res = await _studio_post(
        tenant,
        "/adc-studio-service/web/rest/v1/app/service/query",
        json={
            "project_name": project_name,
            "module_name": module_name,
            "service_name": service_name,
            "start": 0,
            "limit": 10,
        },
        confirm=confirm,
        read_only=True,
    )
    instances = (res or {}).get("instances") or []
    for s in instances:
        if s.get("service_name") == service_name:
            if flow_only:
                return {"service_name": s.get("service_name"), "flow": s.get("flow")}
            return s
    return {"error": f"Service {service_name!r} not found in {project_name}/{module_name}"}


# ============================================================
# Execution — invoke a Service / run a TQL model query
# ============================================================

# Runtime app-ops service test endpoint — used for prod invocation.
_SERVICE_TEST_RUNTIME_PATH = "/adc-app-ops/web/rest/v1/service/test"

# Studio's "Service Playground" exec endpoint — used for testbed invocation.
_SERVICE_TEST_STUDIO_PATH = "/adc-studio-service/web/rest/v1/app/service/test/{project}/{module}/{service}"

# Studio's "Model Data Query" page calls these two endpoints.
_TQL_TRANSLATE_CHECK_PATH = "/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck"
_TQL_QUERY_PATH = "/adc-app-ops/web/rest/v1/model-data-management/queryByTql"


def _service_invoke_path(project_name: str, module_name: str, service_name: str) -> str:
    """Pick the project-scoped or legacy service-runtime path.

    Legacy services (cmdb_*, shared getters) live at
    `/adc-service/rest/v1/legacy/services/<service>` with no project/module
    segment — pass empty project/module to target them.

    NB: this is the `request_string` consumed by the app-ops
    `/service/test` proxy, which uses the no-`web` `/adc-service/rest/v1/...`
    mount (NOT the browser-facing `/adc-service/web/rest/v1/...` form). Keep
    the project-scoped form byte-identical to the previously shipped prod
    path to avoid a regression.
    """
    if project_name and module_name:
        return f"/adc-service/rest/v1/services/{project_name}/{module_name}/{service_name}"
    return f"/adc-service/rest/v1/legacy/services/{service_name}"


async def invoke_service(
    tenant: str,
    project_name: str,
    module_name: str,
    service_name: str,
    payload: dict[str, Any] | None = None,
    *,
    confirm: bool = False,
    extra_headers: dict[str, str] | None = None,
) -> Any:
    """Execute a Service from the Studio service playground with a JSON payload.

    Routes differ by tenant:

    - **prod**: `POST /adc-app-ops/web/rest/v1/service/test` on the
      **runtime** surface with body
      `{"request_string": "/adc-service/rest/v1/services/<p>/<m>/<s>",
      "raw_body": <payload>}`.
      This endpoint works without Studio access and without
      `OWS_PROD_WRITE_ENABLED`. Requires `confirm=True`.

    - **testbed**: `POST /adc-studio-service/web/rest/v1/app/service/test/<p>/<m>/<s>`
      on the **studio** surface — the same endpoint the "Run" button in
      the Studio service playground fires. No `confirm` required.

    A service can have side effects (writes, third-party calls, queue
    enqueues). Against `prod` the call requires `confirm=True`.

    Args:
        tenant: "prod" or "testbed".
        project_name / module_name / service_name: locate the service.
        payload: JSON body to POST. Pass `{}` (or omit) for services that
            take no input. Mirror the input shape the Studio playground
            shows for that service.
            Pass empty ``project_name``/``module_name`` to invoke a legacy
            service (e.g. ``cmdb_site_getList``) at the /legacy/services/ path.
        confirm: required `True` when `tenant == "prod"`.
        extra_headers: optional headers to merge into the request (e.g.
            ``x-gde-tenant-id`` / ``Referer`` / ``Origin``) when a specific
            endpoint rejects the default header set. Do not hardcode a
            tenant id — it is carried in the session cookie.

    Returns:
        Parsed JSON response from the service. On error returns
        `{"error": {"status", "code", "message", "path"}}`.
    """
    body = payload if payload is not None else {}
    t = Tenant(tenant)

    try:
        if t == Tenant.PROD:
            # prod: runtime app-ops endpoint — no Studio access needed.
            service_uri = _service_invoke_path(project_name, module_name, service_name)
            return await _runtime_post(
                tenant,
                _SERVICE_TEST_RUNTIME_PATH,
                json={"request_string": service_uri, "raw_body": body},
                confirm=confirm,
                extra_headers=extra_headers,
            )
        else:
            # testbed: Studio playground endpoint.
            studio_path = _SERVICE_TEST_STUDIO_PATH.format(
                project=project_name, module=module_name, service=service_name
            )
            return await _studio_post(
                tenant, studio_path, json=body, confirm=confirm, extra_headers=extra_headers
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


async def query_model_data(
    tenant: str,
    tql: str,
    *,
    need_null_value: bool = True,
    validate: bool = True,
) -> Any:
    """Execute a read-only TQL query against a Model and return matching rows.

    Routes through the **runtime** surface — `/adc-app-ops/...` is mounted
    on both runtime and studio hosts, and using runtime means a tenant
    that has `OWS_<TENANT>_RUNTIME_URL` set (no studio URL needed) can
    still query model data. The endpoint accepts only SELECT statements
    (no INSERT/UPDATE/DELETE), so the prod write-gate is bypassed
    internally — `confirm=True` is passed through to the client even
    when the caller didn't supply it.

    TQL syntax (verified against Studio's "Model Data Query" page):

        select * from "<asset_uri>" as <alias> limit <N>

    The `asset_uri` is the canonical `/<project>/<module>/<model>` form
    and MUST be quoted. Bare names or dotted paths are rejected by the
    server-side TQL compiler.

    Args:
        tenant: "prod" or "testbed".
        tql: the TQL statement (any read-only form: select / where /
            group by / order by / aggregates).
        need_null_value: passed through to the upstream — when `True`
            (default), null fields are emitted in each row; when `False`
            they're omitted, which is leaner but loses schema fidelity.
        validate: when `True` (default), pre-flight via
            `tqlTranslateCheck` and surface its `errorCode` / `errorRow`
            / `errorColumn` cleanly when the TQL fails to compile.
            Pass `False` to skip the pre-flight (one fewer round-trip).

    Returns:
        On success: `{"row_count": int, "rows": [...]}`. On compile
        failure (validate=True): `{"error": {"code", "row", "column",
        "message", "args"}}`. On HTTP error: `{"error": {"status",
        "code", "message", "path"}}`.
    """
    if validate:
        try:
            check = await _runtime_post(
                tenant,
                _TQL_TRANSLATE_CHECK_PATH,
                json={"tql": tql},
                confirm=True,
                read_only=True,
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
        if isinstance(check, dict) and not check.get("pass", True):
            return {
                "error": {
                    "code": check.get("errorCode"),
                    "row": check.get("errorRow"),
                    "column": check.get("errorColumn"),
                    "args": check.get("errorArgs"),
                    "message": "TQL compile failed",
                    "path": _TQL_TRANSLATE_CHECK_PATH,
                }
            }

    try:
        rows = await _runtime_post(
            tenant,
            _TQL_QUERY_PATH,
            json={"tql": tql, "need_null_value": need_null_value},
            confirm=True,
            read_only=True,
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

    if isinstance(rows, list):
        return {"row_count": len(rows), "rows": rows}
    # The endpoint occasionally wraps results under `data`/`result`; be tolerant.
    if isinstance(rows, dict):
        for key in ("data", "result", "rows"):
            v = rows.get(key)
            if isinstance(v, list):
                return {"row_count": len(v), "rows": v, "raw": rows}
    return {"row_count": 0, "rows": [], "raw": rows}


__all__ = [
    "call_ows_api",
    "get_favorite_menus",
    "get_model",
    "get_model_fields",
    "get_model_schema",
    "get_page",
    "get_page_detail",
    "get_service",
    "get_studio_module",
    "get_studio_project",
    "get_trigger",
    "invoke_service",
    "list_live_apps",
    "list_live_menus",
    "list_models",
    "list_pages",
    "list_project_modules",
    "list_scripts",
    "list_services",
    "list_studio_element_types",
    "list_studio_projects",
    "list_triggers",
    "query_model_data",
]


# ============================================================
# Studio (design-state) — Triggers
# ============================================================


def _summarize_trigger(t: dict[str, Any]) -> dict[str, Any]:
    """Slim a trigger row for listing.

    `trigger_activities[]` is preserved because it's the field the
    reference scanner walks for `service_rest_uri` matches — dropping it
    would defeat PR3b's whole purpose.
    """
    return {
        "trigger_id": t.get("trigger_id"),
        "trigger_name": t.get("trigger_name"),
        "model_uri": t.get("model_uri"),
        "event_type": t.get("event_type"),
        "before_or_after": t.get("before_or_after"),
        "active": t.get("active"),
        "source": t.get("source"),
        "condition": t.get("condition"),
        "project_name": t.get("project_name"),
        "module_name": t.get("module_name"),
        "trigger_activities": t.get("trigger_activities") or [],
        "created_by": t.get("created_by"),
        "updated_by": t.get("updated_by"),
        "created_time": t.get("created_time"),
        "updated_time": t.get("updated_time"),
    }


async def list_triggers(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    trigger_name: str = "",
    active: bool | None = True,
    start: int = 0,
    limit: int = 50,
    verbose: bool = False,
    confirm: bool = False,
) -> dict[str, Any]:
    """List Triggers declared in a Studio project module.

    Calls `POST /adc-studio-model/web/rest/v1/triggers/page-query-all`.

    A Trigger fires on a model event (`event_type` = create/update/delete,
    `before_or_after` = before/after) and runs one or more activities —
    typically `Invoke Service` activities pointing at a service_rest_uri.
    PR3b's reference scanner walks these to close a major static-refs gap.

    Args:
        active: filter by active status. Pass `None` for any.
        verbose: if True, return upstream trigger rows verbatim (drops
            the `_summarize_trigger` field selection). Lean default
            keeps the curated set.
        confirm: required True on prod — this is a read, but issues POST, which the prod write-gate guards.

    Returns:
        `{"total", "page_size", "triggers": [{trigger_id, trigger_name,
          model_uri, event_type, before_or_after, active, source,
          condition, project_name, module_name, trigger_activities[]}]}`
    """
    body: dict[str, Any] = {
        "project_name": project_name,
        "module_name": module_name,
        "trigger_name": trigger_name,
        "start": start,
        "limit": limit,
    }
    if active is not None:
        body["active"] = active
    try:
        res = await _studio_post(
            tenant,
            "/adc-studio-model/web/rest/v1/triggers/page-query-all",
            json=body,
            confirm=confirm,
            read_only=True,
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
        return {"total": 0, "triggers": [], "raw": res}

    rows = res.get("content") if isinstance(res.get("content"), list) else []
    if verbose:
        triggers: list[dict[str, Any]] = [t for t in rows if isinstance(t, dict)]
    else:
        triggers = [_summarize_trigger(t) for t in rows if isinstance(t, dict)]
    return {
        "total": res.get("totalElements", len(triggers)),
        "page_size": res.get("size", limit),
        "triggers": triggers,
    }


async def get_trigger(
    tenant: str,
    project_name: str,
    module_name: str,
    trigger_name: str,
) -> dict[str, Any]:
    """Fetch one Trigger by name.

    Implemented as a tightly-filtered `list_triggers` call (the upstream
    has no separate by-name endpoint). Returns the full row including
    `trigger_activities[]`. If the name doesn't match any row, returns
    `{"error": "..."}`.
    """
    out = await list_triggers(
        tenant,
        project_name,
        module_name,
        trigger_name=trigger_name,
        active=None,
        start=0,
        limit=50,
    )
    if "error" in out:
        return out
    for t in out.get("triggers") or []:
        if t.get("trigger_name") == trigger_name:
            return t
    return {"error": f"Trigger {trigger_name!r} not found in {project_name}/{module_name}"}


def _summarize_script(s: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": s.get("id"),
        "script_name": s.get("name"),
        "script_type": s.get("script_type"),
        "type": s.get("type"),
        "file": s.get("file"),
        "project_name": s.get("project_name"),
        "module_name": s.get("module_name"),
        "manifest_version": s.get("manifest_version"),
        "risk_level": s.get("risk_level"),
    }


async def list_scripts(
    tenant: str,
    *,
    project_name: str = "",
    module_name: str = "",
    name: str = "",
    script_type: str = "",
    start: int = 0,
    limit: int = 50,
    include_raw: bool = False,
) -> dict[str, Any]:
    """List MCP Scripts (the `Script` tab under Studio's MCP element group).

    Calls `GET /adc-studio-mcp/web/rest/v1/scriptmgt/scripts`.

    Verified against the live testbed Studio (the same call the
    `scriptManage.html` UI fires). Note: this endpoint covers the `SCRIPT`
    artifact category specifically — diagnose/automation scripts surfaced
    in the MCP element group. It does not cover RPA scripts, page scripts,
    or the inline `RunScript`/`ScriptLib` files that live under Service
    artifacts (those ship inside the Service flow).

    Args:
        project_name: filter to one project (empty = all projects you can
            see). Pair with `module_name` to narrow further.
        module_name: filter to one module within `project_name`.
        name: substring filter on the script name.
        script_type: optional filter (e.g. `python`).
        start: row offset (default 0).
        limit: rows per page.
        include_raw: if True, include the upstream response under `raw`.

    Returns:
        `{"total", "start", "scripts": [{id, script_name, script_type,
        type, file, project_name, module_name, manifest_version,
        risk_level}]}`
    """
    params: dict[str, Any] = {"limit": limit, "start": start}
    if name:
        params["name"] = name
    if script_type:
        params["script_type"] = script_type
    if project_name:
        params["project_name"] = project_name
    if module_name:
        params["module_name"] = module_name
    try:
        res = await _studio_get(
            tenant,
            "/adc-studio-mcp/web/rest/v1/scriptmgt/scripts",
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

    # Endpoint wraps the payload under `result` per discovery capture.
    payload = res.get("result") if isinstance(res.get("result"), dict) else res
    rows = payload.get("results") if isinstance(payload.get("results"), list) else []
    summary = [_summarize_script(s) for s in rows if isinstance(s, dict)]
    out: dict[str, Any] = {
        "total": payload.get("total", len(summary)),
        "start": payload.get("start", start),
        "scripts": summary,
    }
    if include_raw:
        out["raw"] = res
    return out
