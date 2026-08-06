"""Unit tests for GDE Page layout query and mutation tools.

Style matches the project's mock-testing patterns using pytest-httpx.
"""

from __future__ import annotations

import json
import re
from typing import Any

import pytest
from pytest_httpx import HTTPXMock

from ows_gde_mcp.config import Settings
from ows_gde_mcp.tools import pages as _pages

PAGE_LIST_URL_RE = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/"
    r"tt_app/[a-z_]+(\?.*)?$"
)

PAGE_DETAIL_URL_RE = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/[0-9]+$"
)

PAGE_PROD_DETAIL_URL_RE = re.compile(
    r"^https://prod\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/[0-9]+$"
)


@pytest.fixture
def fake_settings(monkeypatch: pytest.MonkeyPatch) -> Settings:
    """Fixture with testbed & prod tenants configured."""
    for var in (
        "OWS_PROD_WRITE_ENABLED",
        "OWS_TESTBED_STUDIO_URL",
        "OWS_TESTBED_RUNTIME_URL",
        "OWS_PROD_STUDIO_URL",
        "OWS_PROD_RUNTIME_URL",
        "OWS_TESTBED_SESSION_COOKIE",
        "OWS_PROD_SESSION_COOKIE",
        "OWS_TESTBED_CSRF_TOKEN",
        "OWS_PROD_CSRF_TOKEN",
    ):
        monkeypatch.delenv(var, raising=False)
    s = Settings(
        OWS_TESTBED_STUDIO_URL="https://testbed.example.com",  # type: ignore
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",  # type: ignore
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="csrf-testbed",
        OWS_PROD_STUDIO_URL="https://prod.example.com",  # type: ignore
        OWS_PROD_RUNTIME_URL="https://prod.example.com",  # type: ignore
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=False,
    )
    monkeypatch.setattr("ows_gde_mcp.tools.pages.settings", s)
    return s


def _page_list_response() -> dict[str, Any]:
    return {
        "data": [
            {
                "id": "1273",
                "name": "user_list",
                "type": "responsive-web",
                "display_name": "User List",
                "project_name": "tt_app",
                "module_name": "user_module",
                "active": True,
                "open_level": "protected",
                "manifest_version": "26.2.0",
                "creator": "alice",
                "updater": "bob",
                "create_time": "2024-01-01T00:00:00Z",
                "update_time": "2024-02-01T00:00:00Z",
                "tag_id": "",
                "customizable": "0",
            }
        ],
        "total": 1,
        "totalPage": 1,
        "page": 0,
        "pageSize": 50,
    }


def _page_detail_row(page_id: str = "1273") -> dict[str, Any]:
    content = {
        "id": "page",
        "name": "page",
        "componentType": "Container",
        "children": [
            {
                "id": "btn1",
                "name": "dateTimeInput",
                "componentType": "Button",
                "props": {
                    "id": "btn1",
                    "serviceName": "/tt_app/billing/compute_total",
                    "label": "Compute",
                },
            },
            {
                "id": "grid1",
                "componentName": "DataGrid",
                "props": {
                    "id": "grid1",
                    "location": "/tt_app/billing/list_invoices",
                    "serviceName": "/tt_app/billing/compute_total",
                    "label": "My Grid",
                },
            },
        ],
        "scripts": [
            {"js_content": "console.log('hi')"},
        ],
    }
    return {
        "id": page_id,
        "name": "billing_dashboard",
        "display_name": "Billing Dashboard",
        "project_name": "tt_app",
        "module_name": "billing",
        "content": json.dumps(content),
    }


# ============================================================
# Migrated Read Tests
# ============================================================


@pytest.mark.asyncio
async def test_list_pages_happy_path(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url=PAGE_LIST_URL_RE,
        method="GET",
        json=_page_list_response()
    )
    out = await _pages.list_pages("testbed", "tt_app", "user_module")
    assert set(out.keys()) >= {"total", "pages", "totalPage", "page", "pageSize"}
    assert out["total"] == 1
    assert len(out["pages"]) == 1
    first = out["pages"][0]
    assert first["page_name"] == "user_list"
    assert first["display_name"] == "User List"
    assert first["creator"] == "alice"


@pytest.mark.asyncio
async def test_list_pages_error_returns_error_dict(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url=PAGE_LIST_URL_RE,
        method="GET",
        status_code=500,
        json={
            "error": {
                "code": "ADC.STUDIO.PAGE.404",
                "message": "module not found",
                "args": ["/adc-studio-ui/web/rest/v1/page-core/page/tt_app/missing_module"],
            }
        },
    )
    out = await _pages.list_pages("testbed", "tt_app", "missing_module")
    assert "error" in out
    assert out["error"]["code"] == "ADC.STUDIO.PAGE.404"
    assert out["error"]["status"] == 500


@pytest.mark.asyncio
async def test_get_page_not_found_returns_error_string(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url=PAGE_LIST_URL_RE,
        method="GET",
        json={"data": [], "total": 0, "totalPage": 0, "page": 0, "pageSize": 50},
    )
    out = await _pages.get_page("testbed", "tt_app", "user_module", "no_such_page")
    assert "error" in out
    assert "no_such_page" in out["error"]
    assert "tt_app/user_module" in out["error"]


@pytest.mark.asyncio
async def test_get_page_detail_default_keeps_full_content(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _pages.get_page_detail("testbed", "1273")
    assert out["content"] == row["content"]
    assert "summary" not in out


@pytest.mark.asyncio
async def test_get_page_detail_summary_only_drops_content(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _pages.get_page_detail("testbed", "1273", summary_only=True)
    assert "content" not in out
    summary = out["summary"]
    assert summary["component_count"] == 3
    assert summary["script_block_count"] == 1
    assert summary["service_refs"] == [
        "/tt_app/billing/compute_total",
        "/tt_app/billing/list_invoices",
    ]


@pytest.mark.asyncio
async def test_get_page_detail_summary_handles_malformed_content(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = {"id": "1273", "name": "broken", "content": "not-json{"}
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _pages.get_page_detail("testbed", "1273", summary_only=True)
    assert "content" not in out
    assert out["name"] == "broken"
    assert out["summary"]["component_count"] == 0
    assert "parse_error" in out["summary"]


@pytest.mark.asyncio
async def test_get_page_detail_summary_handles_missing_content(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = {"id": "1273", "name": "empty", "content": None}
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _pages.get_page_detail("testbed", "1273", summary_only=True)
    assert out["summary"] == {
        "component_count": 0,
        "service_refs": [],
        "script_block_count": 0,
    }


# ============================================================
# New Mutation & Component Edit Tests
# ============================================================


@pytest.mark.asyncio
async def test_save_page_content_success(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    payload = {"id": "1273", "name": "my_page", "content": {"id": "page", "name": "page"}}
    
    httpx_mock.add_response(
        url=PAGE_DETAIL_URL_RE,
        method="PUT",
        json={"id": "1273", "name": "my_page", "updater": "bob"}
    )
    
    res = await _pages.save_page_content("testbed", "1273", payload)
    assert res["status"] == "success"
    assert res["page"]["updater"] == "bob"


@pytest.mark.asyncio
async def test_save_page_content_prod_gate(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    payload = {"id": "1273", "name": "my_page", "content": {}}
    
    with pytest.raises((PermissionError, ValueError)):
        await _pages.save_page_content("prod", "1273", payload, confirm=False)
        
    httpx_mock.add_response(
        url=PAGE_PROD_DETAIL_URL_RE,
        method="PUT",
        json={"id": "1273", "updater": "prod_user"}
    )
    fake_settings.OWS_PROD_WRITE_ENABLED = True
    fake_settings.OWS_STUDIO_WRITE_ENABLED = True
    res = await _pages.save_page_content("prod", "1273", payload, confirm=True)
    assert res["status"] == "success"


@pytest.mark.asyncio
async def test_create_page_success(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-studio-ui/web/rest/v1/page-core/page/tt_app/user_module",
        method="POST",
        json={"id": "9999", "name": "new_form", "creator": "alice"}
    )
    res = await _pages.create_page("testbed", "tt_app", "user_module", "new_form", "New Page Form")
    assert res["status"] == "success"
    assert res["page"]["id"] == "9999"


@pytest.mark.asyncio
async def test_add_page_component_success(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    # 1. Mock the GET retrieval
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    
    # 2. Mock the PUT modification save
    httpx_mock.add_response(
        url=PAGE_DETAIL_URL_RE,
        method="PUT",
        json={"id": "1273", "status": "saved"}
    )
    
    res = await _pages.add_page_component(
        "testbed", "1273", "grid1", "personSelect", "user_selector", {"label": "Select User"}
    )
    assert res["status"] == "success"
    
    # Verify the PUT request payload
    requests = httpx_mock.get_requests()
    put_reqs = [r for r in requests if r.method == "PUT"]
    assert len(put_reqs) == 1
    
    captured_payload = json.loads(put_reqs[0].read().decode())
    tree = json.loads(captured_payload["content"])
    
    grid_node = None
    for child in tree["children"]:
        if child.get("id") == "grid1":
            grid_node = child
            break
            
    assert grid_node is not None
    assert len(grid_node["children"]) == 1
    new_comp = grid_node["children"][0]
    assert new_comp["name"] == "personSelect"
    assert new_comp["props"]["id"] == "user_selector"
    assert new_comp["props"]["label"] == "Select User"


@pytest.mark.asyncio
async def test_update_page_component_props_success(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    
    httpx_mock.add_response(
        url=PAGE_DETAIL_URL_RE,
        method="PUT",
        json={"id": "1273", "status": "saved"}
    )
    
    res = await _pages.update_page_component_props(
        "testbed", "1273", "btn1", {"label": "New Button Name", "disabled": True}
    )
    assert res["status"] == "success"
    
    requests = httpx_mock.get_requests()
    put_reqs = [r for r in requests if r.method == "PUT"]
    assert len(put_reqs) == 1
    
    captured_payload = json.loads(put_reqs[0].read().decode())
    tree = json.loads(captured_payload["content"])
    btn_node = tree["children"][0]
    assert btn_node["id"] == "btn1"
    assert btn_node["props"]["label"] == "New Button Name"
    assert btn_node["props"]["disabled"] is True


@pytest.mark.asyncio
async def test_remove_page_component_success(fake_settings: Settings, httpx_mock: HTTPXMock) -> None:
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    
    httpx_mock.add_response(
        url=PAGE_DETAIL_URL_RE,
        method="PUT",
        json={"id": "1273", "status": "saved"}
    )
    
    res = await _pages.remove_page_component("testbed", "1273", "grid1")
    assert res["status"] == "success"
    
    requests = httpx_mock.get_requests()
    put_reqs = [r for r in requests if r.method == "PUT"]
    assert len(put_reqs) == 1
    
    captured_payload = json.loads(put_reqs[0].read().decode())
    tree = json.loads(captured_payload["content"])
    assert len(tree["children"]) == 1
    assert tree["children"][0]["id"] == "btn1"
