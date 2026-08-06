"""GDE Page layout query and mutation tools.

Provides capabilities for:
- Listing and querying studio pages (metadata & full layout tree).
- Saving modifications to the page layout structure.
- Spinning up new empty responsive pages.
- Adding, updating, and removing component nodes directly inside the page's SPL JSON AST.
"""

from __future__ import annotations

import json
from typing import Any

from ows_gde_mcp.client import OwsApiError, OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings


# Helper functions to avoid circular imports with live.py
async def _studio_get(tenant: str, path: str, **kwargs: Any) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.STUDIO, settings) as client:
        return await client.get(path, **kwargs)


async def _studio_post(
    tenant: str,
    path: str,
    json_data: Any = None,
    *,
    confirm: bool = False,
    **kwargs: Any,
) -> Any:
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.STUDIO, settings) as client:
        return await client.post(path, json=json_data, confirm=confirm, **kwargs)

# Page-tree fields whose values typically hold a service reference.
_PAGE_SERVICE_REF_FIELDS = {"serviceName", "serviceId", "location", "serviceUri"}


def _summarize_page(p: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": p.get("id"),
        "page_name": p.get("name"),
        "display_name": p.get("display_name"),
        "page_type": p.get("type"),
        "project_name": p.get("project_name"),
        "module_name": p.get("module_name"),
        "model_name": p.get("model_name"),
        "active": p.get("active"),
        "open_level": p.get("open_level"),
        "manifest_version": p.get("manifest_version"),
        "creator": p.get("creator"),
        "updater": p.get("updater"),
        "create_time": p.get("create_time"),
        "update_time": p.get("update_time"),
        "tag_id": p.get("tag_id"),
        "customizable": p.get("customizable"),
    }


async def list_pages(
    tenant: str,
    project_name: str,
    module_name: str,
    *,
    name: str = "",
    display_name: str = "",
    tag_id: str = "",
    page_type: str = "responsive-web",
    active: str = "true",
    sort: str = "updateTime",
    direction: str = "DESC",
    page: int = 0,
    page_size: int = 50,
    include_raw: bool = False,
) -> dict[str, Any]:
    """List Pages declared in a Studio project module.

    Calls `GET /adc-studio-ui/web/rest/v1/page-core/page/{project}/{module}`.

    Args:
        tenant: "prod" or "testbed".
        project_name: project code.
        module_name: module code.
        name: optional substring filter on the page name.
        display_name: optional substring filter on the display label.
        tag_id: filter by Studio tag id (empty for any).
        page_type: page namespace — `responsive-web` (default), `mobile`, `mateline`.
        active: `"true"` / `"false"` / `""` for any.
        sort: column to sort by (default `updateTime`).
        direction: `"ASC"` or `"DESC"`.
        page: zero-indexed page number.
        page_size: rows per page.
        include_raw: if True, also include the upstream response payload.
    """
    try:
        res = await _studio_get(
            tenant,
            f"/adc-studio-ui/web/rest/v1/page-core/page/{project_name}/{module_name}",
            params={
                "active": active,
                "sort": sort,
                "dir": direction,
                "page": page,
                "pageSize": page_size,
                "moduleName": module_name,
                "projectName": project_name,
                "type": page_type,
                "name": name,
                "tagId": tag_id,
                "displayName": display_name,
            },
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
        return {"total": 0, "pages": [], "raw": res}

    res_data = res.get("data")
    rows: list[Any] = res_data if isinstance(res_data, list) else []
    summary = [_summarize_page(p) for p in rows if isinstance(p, dict)]
    out: dict[str, Any] = {
        "total": res.get("total", len(summary)),
        "totalPage": res.get("totalPage"),
        "page": res.get("page"),
        "pageSize": res.get("pageSize"),
        "pages": summary,
    }
    if include_raw:
        out["raw"] = res
    return out


async def get_page(
    tenant: str,
    project_name: str,
    module_name: str,
    page_name: str,
    *,
    page_type: str = "responsive-web",
) -> dict[str, Any]:
    """Fetch one Page's metadata row by name.

    Calls the same endpoint as `list_pages` with a `name=` filter, then
    finds the exact match. Returns `{"error": "..."}` if no row matches.
    """
    try:
        res = await _studio_get(
            tenant,
            f"/adc-studio-ui/web/rest/v1/page-core/page/{project_name}/{module_name}",
            params={
                "active": "true",
                "sort": "updateTime",
                "dir": "DESC",
                "page": 0,
                "pageSize": 50,
                "moduleName": module_name,
                "projectName": project_name,
                "type": page_type,
                "name": page_name,
                "tagId": "",
                "displayName": "",
            },
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
        return {"error": f"Page {page_name!r} not found in {project_name}/{module_name}"}

    res_data = res.get("data")
    rows: list[Any] = res_data if isinstance(res_data, list) else []
    for p in rows:
        if isinstance(p, dict) and p.get("name") == page_name:
            return p
    return {"error": f"Page {page_name!r} not found in {project_name}/{module_name}"}


def _parse_spl_node(
    node: Any,
    *,
    components: list[dict],
    event_handlers: list[dict],
    prop_bindings: list[dict],
    service_refs: set[str],
    _path: str = "",
) -> None:
    if not isinstance(node, dict):
        return

    name = node.get("name") or node.get("componentName") or ""
    comp_id = (node.get("props") or {}).get("id") or node.get("id") or ""
    is_slot = node.get("isSlotNode", False)
    path = f"{_path}/{name}" if name and not is_slot else _path

    if name and not is_slot and name not in ("page", "page-slot-1"):
        props = node.get("props") or {}
        comp_entry: dict[str, Any] = {
            "type": name,
            "id": comp_id or None,
            "path": path,
        }
        for key in ("label", "placeholder", "title", "text", "visible", "disabled"):
            if key in props:
                comp_entry[key] = props[key]
        components.append(comp_entry)

    events = node.get("events") or {}
    for event_name, handler in events.items():
        if not handler:
            continue
        fn = handler if isinstance(handler, str) else (handler.get("fn") or handler.get("function") or str(handler))
        event_handlers.append({
            "component_id": comp_id or name or path,
            "event": event_name,
            "handler": fn,
            "path": path,
        })

    props_bind = node.get("propsBind") or {}
    for prop_name, binding in props_bind.items():
        if not binding:
            continue
        binding_str = binding if isinstance(binding, str) else str(binding)
        entry: dict[str, Any] = {
            "component_id": comp_id or name or path,
            "prop": prop_name,
            "binding": binding_str,
            "path": path,
        }
        if any(kw in binding_str for kw in ("service", "Service", "/adc-service")):
            entry["is_service_ref"] = True
        prop_bindings.append(entry)

    props = node.get("props") or {}
    for field in _PAGE_SERVICE_REF_FIELDS:
        val = props.get(field)
        if isinstance(val, str) and val:
            service_refs.add(val)

    for child in node.get("children") or []:
        _parse_spl_node(
            child,
            components=components,
            event_handlers=event_handlers,
            prop_bindings=prop_bindings,
            service_refs=service_refs,
            _path=path,
        )


def _parse_page_detail(row: dict[str, Any]) -> dict[str, Any]:
    out = {k: v for k, v in row.items() if k != "content"}
    raw = row.get("content")
    if not isinstance(raw, str) or not raw:
        out["parsed_spl"] = {"error": "no content", "components": [], "event_handlers": [], "prop_bindings": [], "service_refs": []}
        return out

    try:
        tree = json.loads(raw)
    except (ValueError, TypeError) as e:
        out["parsed_spl"] = {"error": f"parse failed: {e}", "components": [], "event_handlers": [], "prop_bindings": [], "service_refs": []}
        return out

    components: list[dict] = []
    event_handlers: list[dict] = []
    prop_bindings: list[dict] = []
    service_refs: set[str] = set()

    from ows_gde_mcp.tools.references import _walk
    for field_name, _key_path, value in _walk(tree):
        if field_name in _PAGE_SERVICE_REF_FIELDS and isinstance(value, str) and value:
            service_refs.add(value)
        elif field_name == "js_content" and isinstance(value, str):
            import re
            for match in re.findall(r"/adc-service/[^\s\"'`,]+", value):
                service_refs.add(match.rstrip(")};,"))

    _parse_spl_node(tree, components=components, event_handlers=event_handlers, prop_bindings=prop_bindings, service_refs=service_refs)

    seen_bindings: set[tuple] = set()
    unique_bindings = []
    for b in prop_bindings:
        key = (b["component_id"], b["prop"])
        if key not in seen_bindings:
            seen_bindings.add(key)
            unique_bindings.append(b)

    out["parsed_spl"] = {
        "stats": {
            "component_count": len(components),
            "event_handler_count": len(event_handlers),
            "prop_binding_count": len(unique_bindings),
            "service_ref_count": len(service_refs),
        },
        "components": components,
        "event_handlers": event_handlers,
        "prop_bindings": unique_bindings,
        "service_refs": sorted(service_refs),
    }
    return out


def _summarize_page_detail(row: dict[str, Any]) -> dict[str, Any]:
    out = {k: v for k, v in row.items() if k != "content"}
    raw = row.get("content")
    if not isinstance(raw, str) or not raw:
        out["summary"] = {
            "component_count": 0,
            "service_refs": [],
            "script_block_count": 0,
        }
        return out
    try:
        tree = json.loads(raw)
    except (ValueError, TypeError) as e:
        out["summary"] = {
            "component_count": 0,
            "service_refs": [],
            "script_block_count": 0,
            "parse_error": f"{type(e).__name__}: {e}",
        }
        return out

    component_count = 0
    script_block_count = 0
    service_refs: set[str] = set()
    from ows_gde_mcp.tools.references import _walk

    for field_name, _key_path, value in _walk(tree):
        if field_name == "componentType" or field_name == "componentName":
            component_count += 1
        elif field_name == "js_content":
            script_block_count += 1
        elif field_name in _PAGE_SERVICE_REF_FIELDS and isinstance(value, str) and value:
            service_refs.add(value)

    out["summary"] = {
        "component_count": component_count,
        "service_refs": sorted(service_refs),
        "script_block_count": script_block_count,
    }
    return out


async def get_page_detail(
    tenant: str,
    page_id: str,
    *,
    summary_only: bool = False,
    parsed: bool = False,
) -> dict[str, Any]:
    """Fetch one Page's full definition by id, including the SPL content tree."""
    try:
        row = await _studio_get(
            tenant,
            f"/adc-studio-ui/web/rest/v1/page-core/page/{page_id}",
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
    if not isinstance(row, dict):
        return row
    if parsed:
        return _parse_page_detail(row)
    if summary_only:
        return _summarize_page_detail(row)
    return row


# ============================================================
# Mutations (Save, Create, Component Mutations)
# ============================================================


async def save_page_content(
    tenant: str,
    page_id: str,
    payload: dict[str, Any],
    *,
    confirm: bool = False,
) -> dict[str, Any]:
    """PUT updated layout content payload to GDE page-core Studio API.

    Args:
        tenant: "prod" or "testbed".
        page_id: numeric page id.
        payload: complete page properties payload (GDE page JSON object).
        confirm: required True to allow writes against production.
    """
    t = Tenant(tenant)
    s = Surface.STUDIO
    url = f"/adc-studio-ui/web/rest/v1/page-core/page/{page_id}"

    # Auto-serialize nested content if passed as a dict/list to keep it robust
    if "content" in payload and isinstance(payload["content"], (dict, list)):
        payload = dict(payload)
        payload["content"] = json.dumps(payload["content"])

    async with OwsClient.for_surface(t, s, settings) as client:
        try:
            res = await client.request("PUT", url, json=payload, confirm=confirm)
            return {"status": "success", "page": res}
        except OwsApiError as e:
            return {
                "error": {
                    "status": e.status,
                    "code": e.code,
                    "message": e.message,
                    "path": e.path,
                }
            }


async def create_page(
    tenant: str,
    project_name: str,
    module_name: str,
    page_name: str,
    display_name: str,
    *,
    page_type: str = "responsive-web",
    open_level: str = "public",
    active: bool = True,
    customizable: str = "1",
    confirm: bool = False,
) -> dict[str, Any]:
    """POST request to GDE page-core Studio API to create a new blank page.

    Args:
        tenant: "prod" or "testbed".
        project_name: target project name.
        module_name: target module name.
        page_name: code name of the page.
        display_name: label/title visible to the user.
        page_type: page context (defaults to "responsive-web").
        open_level: GDE page protection/access type (defaults to "public").
        active: whether the page draft is active.
        customizable: string "1" or "0" representing design customization capacity.
        confirm: required True to allow writes against production.
    """
    t = Tenant(tenant)
    s = Surface.STUDIO
    url = f"/adc-studio-ui/web/rest/v1/page-core/page/{project_name}/{module_name}"

    payload = {
        "page_name": page_name,
        "display_name": display_name,
        "page_type": page_type,
        "active": active,
        "open_level": open_level,
        "customizable": customizable,
        "content": json.dumps({
            "id": "page",
            "name": "page",
            "children": [
                {
                    "id": "page-slot-1",
                    "name": "default",
                    "isSlotNode": True,
                    "slotType": "common",
                    "visible": False,
                    "children": [
                        {
                            "name": "centerPanel",
                            "children": [],
                            "props": {
                                "id": "CenterPanel1"
                            }
                        }
                    ]
                }
            ]
        })
    }

    async with OwsClient.for_surface(t, s, settings) as client:
        try:
            res = await client.request("POST", url, json=payload, confirm=confirm)
            return {"status": "success", "page": res}
        except OwsApiError as e:
            return {
                "error": {
                    "status": e.status,
                    "code": e.code,
                    "message": e.message,
                    "path": e.path,
                }
            }


def _find_and_modify_node(node: Any, target_id: str, action: str, **kwargs: Any) -> bool:
    """Recursively search for a node by id and apply an action.

    Supports actions: 'update_props', 'add_child', 'delete'.
    """
    if not isinstance(node, dict):
        return False

    curr_id = node.get("id") or (node.get("props") or {}).get("id")

    if curr_id == target_id:
        if action == "update_props":
            props_to_update = kwargs.get("props") or {}
            node.setdefault("props", {}).update(props_to_update)
            return True
        elif action == "add_child":
            node.setdefault("children", []).append(kwargs.get("child", {}))
            return True

    # Recurse children
    children = node.get("children", [])
    if isinstance(children, list):
        for idx, child in enumerate(children):
            if isinstance(child, dict):
                child_id = child.get("id") or (child.get("props") or {}).get("id")
                if child_id == target_id and action == "delete":
                    children.pop(idx)
                    return True
                if _find_and_modify_node(child, target_id, action, **kwargs):
                    return True

    return False


async def _update_tree_action(
    tenant: str,
    page_id: str,
    target_id: str,
    action: str,
    *,
    confirm: bool = False,
    **kwargs: Any,
) -> dict[str, Any]:
    """Helper to fetch a page, apply an AST modification, and save it back."""
    # 1. Fetch current detail
    row = await get_page_detail(tenant, page_id)
    if "error" in row:
        return row

    content_str = row.get("content")
    if not content_str:
        return {"error": "Page has no content/layout to modify."}

    try:
        tree = json.loads(content_str)
    except (ValueError, TypeError) as e:
        return {"error": f"Failed to parse page layout: {e}"}

    # 2. Modify tree
    modified = _find_and_modify_node(tree, target_id, action, **kwargs)
    if not modified:
        return {"error": f"Target component with ID {target_id!r} not found in page structure."}

    # 3. Save modified content
    row["content"] = tree
    return await save_page_content(tenant, page_id, row, confirm=confirm)


async def add_page_component(
    tenant: str,
    page_id: str,
    parent_id: str,
    component_name: str,
    component_id: str,
    props: dict[str, Any] | None = None,
    *,
    confirm: bool = False,
) -> dict[str, Any]:
    """Add a component layout node into the specified parent node's children.

    Args:
        tenant: "prod" or "testbed".
        page_id: numeric page id.
        parent_id: id (props.id or layout id) of the parent node to insert into.
        component_name: GDE component type name (e.g. "textInput", "button", "row").
        component_id: unique ID for the new component.
        props: optional dictionary of initial property key-value pairs.
        confirm: required True to allow writes against production.
    """
    new_child = {
        "name": component_name,
        "id": component_id,
        "children": [],
        "props": {
            "id": component_id,
            **(props or {})
        },
        "events": {},
        "propsBind": {}
    }
    return await _update_tree_action(
        tenant,
        page_id,
        target_id=parent_id,
        action="add_child",
        child=new_child,
        confirm=confirm,
    )


async def update_page_component_props(
    tenant: str,
    page_id: str,
    component_id: str,
    props: dict[str, Any],
    *,
    confirm: bool = False,
) -> dict[str, Any]:
    """Modify/merge key properties on a specific page component.

    Args:
        tenant: "prod" or "testbed".
        page_id: numeric page id.
        component_id: component ID to modify.
        props: dict of properties to merge into the component's existing props.
        confirm: required True to allow writes against production.
    """
    return await _update_tree_action(
        tenant,
        page_id,
        target_id=component_id,
        action="update_props",
        props=props,
        confirm=confirm,
    )


async def remove_page_component(
    tenant: str,
    page_id: str,
    component_id: str,
    *,
    confirm: bool = False,
) -> dict[str, Any]:
    """Remove a layout component by ID from the page tree.

    Args:
        tenant: "prod" or "testbed".
        page_id: numeric page id.
        component_id: component ID to delete.
        confirm: required True to allow writes against production.
    """
    return await _update_tree_action(
        tenant,
        page_id,
        target_id=component_id,
        action="delete",
        confirm=confirm,
    )
