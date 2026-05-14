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


__all__ = [
    "call_ows_api",
    "get_favorite_menus",
    "get_model_fields",
    "list_live_apps",
    "list_live_menus",
]
