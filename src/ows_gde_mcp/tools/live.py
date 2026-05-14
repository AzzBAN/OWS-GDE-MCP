"""MCP tools that hit the **live** OWS API.

All tools take an explicit `tenant: "prod" | "testbed"` argument. Auth
(cookie + CSRF + page-token headers) is supplied by `OwsClient`.

These tools cover the most useful introspection paths discovered during
Phase 0:

- `list_live_menus` / `list_live_apps` — what apps/menus this account has
  access to (parsed from the portal's granted-menu tree).
- `get_model_fields` — TQL queryable-field schema for any data Model.
- `call_ows_api` — generic escape hatch for any endpoint we haven't yet
  given a typed wrapper.
"""

from __future__ import annotations

from typing import Any

from ows_gde_mcp.client import OwsApiError, OwsClient
from ows_gde_mcp.config import Tenant, settings

# ---------------- internal helpers ----------------


async def _get(tenant: str, path: str, **kwargs: Any) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_tenant(t, settings) as client:
        return await client.get(path, **kwargs)


async def _post(tenant: str, path: str, json: Any = None, **kwargs: Any) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_tenant(t, settings) as client:
        return await client.post(path, json=json, **kwargs)


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
    tree = await _get(
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
    res = await _get(tenant, "/portal/web/rest/v1/menu/favorites")
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
    res = await _post(
        tenant,
        "/adc-model/web/rest/v1/app/tql/init",
        params={"asset_uri": asset_uri},
        json={},
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
        body: optional JSON body (for POST/PUT/etc.).
        params: optional query-string parameters.
        confirm: required `True` to allow non-GET methods against `prod`.

    Returns:
        Parsed JSON response (or raw text if not JSON).
    """
    t = Tenant(tenant)
    method_u = method.upper()
    if method_u != "GET":
        settings.assert_prod_write_allowed(t, confirm=confirm)
    async with OwsClient.for_tenant(t, settings) as client:
        try:
            return await client.request(method_u, path, params=params, json=body)
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
) -> dict[str, Any]:
    """List recently-viewed Studio projects with full metadata.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/recent-projects`.

    Returns:
        `{"total", "projects": [{id, name, display_name, scene, creator,
        create_time, updater, update_time, description, ...}]}`
    """
    res = await _get(
        tenant,
        "/adc-studio-project-mgt/web/rest/v1/recent-projects",
        params={"start": start, "limit": limit},
    )
    data = (res or {}).get("data") or {}
    projects = []
    for row in data.get("data") or []:
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
    res = await _get(tenant, path)
    return (res or {}).get("data") or res


async def list_project_modules(tenant: str, project_id: int) -> list[dict[str, Any]]:
    """List modules inside a Studio project.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/project/{project_id}/modules`.
    """
    res = await _get(
        tenant,
        f"/adc-studio-project-mgt/web/rest/v1/project/{project_id}/modules",
    )
    rows = (res or {}).get("data") or []
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


async def get_studio_module(tenant: str, module_id: int) -> dict[str, Any]:
    """Get module detail including which artifact types it supports.

    Calls `GET /adc-studio-project-mgt/web/rest/v1/modules/{module_id}`.

    Returns the module's `items` list — the artifact-type categories enabled
    on that module (MODEL, PAGE, SERVICE, WORKFLOW, etc.).
    """
    res = await _get(
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


async def list_models(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    model_name: str = "",
    model_type: str = "",
    active: str = "",
    start: int = 0,
    limit: int = 50,
) -> dict[str, Any]:
    """List Data Models declared in a Studio project module.

    Calls `POST /adc-studio-model/web/rest/v1/models/query-model-no-prop`.

    Args:
        model_name: optional substring filter on the model name.
        model_type: optional filter (e.g. "datamodel", "proxymodel",
                    "elasticmodel").
        active: "true" / "false" / "" (any).

    Returns:
        `{"total", "models": [{model_id, model_name, display_name,
        model_type, project_name, module_name, active, open_level,
        created_by, updated_by, created_time, updated_time,
        description?, customized}]}`
    """
    res = await _post(
        tenant,
        "/adc-studio-model/web/rest/v1/models/query-model-no-prop",
        json={
            "project_name": project_name,
            "module_name": module_name,
            "model_name": model_name,
            "model_type": model_type,
            "active": active,
            "start": start,
            "limit": limit,
        },
    )
    return {
        "total": (res or {}).get("total", 0),
        "models": (res or {}).get("data", []),
    }


async def get_model(tenant: str, model_id: int) -> dict[str, Any]:
    """Fetch a Data Model's full schema by id (every property + restrictions).

    Calls `POST /adc-studio-model/web/rest/v1/models/query-by-id?model_id=<id>`.

    Use `list_models()` first to find the `model_id`.
    """
    return await _post(
        tenant,
        "/adc-studio-model/web/rest/v1/models/query-by-id",
        params={"model_id": model_id},
    )


__all__ = [
    "call_ows_api",
    "get_favorite_menus",
    "get_model",
    "get_model_fields",
    "get_studio_module",
    "get_studio_project",
    "list_live_apps",
    "list_live_menus",
    "list_models",
    "list_project_modules",
    "list_studio_projects",
]
