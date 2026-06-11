"""Tests for the Studio artifact tools (`list_pages`, `get_page`, `list_scripts`).

The Page and Script endpoints used by these tools are inferred from the
already-verified `list_services` / `list_models` patterns and have not yet
been confirmed against discovery captures, so the tools are written to
degrade gracefully when the controller surface differs. These tests
exercise both the happy path and the error-path branches that gracefully
degrade.

Style follows `tests/test_client_security.py`: a `Settings` fixture with
both tenants configured and `monkeypatch.setattr` swapping the global
`settings` referenced inside `ows_gde_mcp.tools.live` so the live tool
helpers route through `pytest-httpx`.
"""

from __future__ import annotations

import re

import pytest

from ows_gde_mcp.config import Settings
from ows_gde_mcp.tools import live as _live

# ---------------- fixtures ----------------


@pytest.fixture
def fake_settings(monkeypatch: pytest.MonkeyPatch) -> Settings:
    """Settings with the testbed tenant fully configured.

    Mirrors `tests/test_client_security.py` — explicit `delenv` calls keep
    the developer's host env from leaking in via pydantic-settings.
    """
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
        OWS_TESTBED_STUDIO_URL="https://testbed.example.com",
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="csrf-testbed",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=False,
    )
    # `_studio_post` / `_runtime_post` inside live.py captures the
    # module-level `settings` symbol; patch that single binding so
    # OwsClient.for_surface sees the fixture.
    monkeypatch.setattr("ows_gde_mcp.tools.live.settings", s)
    return s


# ---------------- list_pages ----------------
#
# Endpoint verified against live testbed Studio: a GET against
# `/adc-studio-ui/web/rest/v1/page-core/page/{project}/{module}` with
# camelCase query params (`projectName`, `moduleName`, `pageSize`, ...)
# and a `{"data": [...], "total", "totalPage", "page", "pageSize"}` shape.
# Per-row fields are `name`/`type`/`creator`/`updater`/`update_time`,
# *not* the `page_name`/`page_type`/`created_by` shape we previously
# inferred.


PAGE_LIST_URL_RE = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/"
    r"tt_app/[a-z_]+(\?.*)?$"
)


async def test_list_pages_happy_path(fake_settings: Settings, httpx_mock) -> None:
    """Live shape: `{"data": [...], "total", "totalPage", "page",
    "pageSize"}`. Each row carries `name`, `type`, `creator`, `updater`,
    `create_time`, `update_time`. The tool maps these to its summary keys."""
    httpx_mock.add_response(
        url=PAGE_LIST_URL_RE,
        method="GET",
        json={
            "data": [
                {
                    "id": "1",
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
                },
                {
                    "id": "2",
                    "name": "user_detail",
                    "type": "responsive-web",
                    "display_name": "User Detail",
                    "project_name": "tt_app",
                    "module_name": "user_module",
                    "active": True,
                },
            ],
            "total": 2,
            "totalPage": 1,
            "page": 0,
            "pageSize": 50,
        },
    )
    out = await _live.list_pages("testbed", "tt_app", "user_module")
    assert set(out.keys()) >= {"total", "pages", "totalPage", "page", "pageSize"}
    assert out["total"] == 2
    assert len(out["pages"]) == 2
    first = out["pages"][0]
    assert first["page_name"] == "user_list"
    assert first["display_name"] == "User List"
    assert first["page_type"] == "responsive-web"
    assert first["creator"] == "alice"


async def test_list_pages_error_returns_error_dict(fake_settings: Settings, httpx_mock) -> None:
    """A structured OWS error body must be caught and surfaced under
    `error`, not propagate as an exception."""
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
    out = await _live.list_pages("testbed", "tt_app", "missing_module")
    assert "error" in out
    assert out["error"]["code"] == "ADC.STUDIO.PAGE.404"
    assert out["error"]["status"] == 500


# ---------------- get_page ----------------


async def test_get_page_not_found_returns_error_string(fake_settings: Settings, httpx_mock) -> None:
    """Empty result set → tool returns a not-found `{"error": "..."}` dict
    matching the `get_service` style."""
    httpx_mock.add_response(
        url=PAGE_LIST_URL_RE,
        method="GET",
        json={"data": [], "total": 0, "totalPage": 0, "page": 0, "pageSize": 50},
    )
    out = await _live.get_page("testbed", "tt_app", "user_module", "no_such_page")
    assert "error" in out
    assert "no_such_page" in out["error"]
    assert "tt_app/user_module" in out["error"]


# ---------------- list_scripts ----------------
#
# Endpoint verified against live testbed Studio: GET on
# `/adc-studio-mcp/web/rest/v1/scriptmgt/scripts` returns
# `{"resultCode": "0", "result": {"results": [...], "total", "start"}}`.
# Rows carry `name, script_type, type, file, project_name, module_name,
# manifest_version, risk_level` — not the inferred `script_name`/
# `script_uri`/`active` shape.


SCRIPT_LIST_URL_RE = re.compile(
    r"^https://testbed\.example\.com/adc-studio-mcp/web/rest/v1/scriptmgt/scripts(\?.*)?$"
)


async def test_list_scripts_happy_path(fake_settings: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url=SCRIPT_LIST_URL_RE,
        method="GET",
        json={
            "resultCode": "0",
            "resultMessage": "Success",
            "result": {
                "results": [
                    {
                        "id": "abcd-1234",
                        "name": "compute_total",
                        "script_type": "python",
                        "type": "common",
                        "file": "compute_total.py",
                        "project_name": "tt_app",
                        "module_name": "billing",
                        "manifest_version": "1.0",
                        "risk_level": "Low",
                    }
                ],
                "start": 0,
                "total": 1,
            },
        },
    )
    out = await _live.list_scripts("testbed", project_name="tt_app", module_name="billing")
    assert out["total"] == 1
    assert len(out["scripts"]) == 1
    row = out["scripts"][0]
    assert row["script_name"] == "compute_total"
    assert row["script_type"] == "python"
    assert row["module_name"] == "billing"
    assert row["file"] == "compute_total.py"
    assert row["risk_level"] == "Low"


# ---------------- payload slimming (list_models / get_model) ----------------


MODEL_QUERY_URL = (
    "https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryBaseModels"
)
MODEL_BY_ID_URL = (
    "https://testbed.example.com/adc-studio-model/web/rest/v1/models/query-by-id?model_id=99"
)


def _basemodel_row() -> dict:
    """A row in the shape returned by /adc-app-ops queryBaseModels with
    brief_query=true. The endpoint does not ship `properties`, `indexes`,
    `behaviors`, or audit fields — those come from `get_model(model_id)`."""
    return {
        "project_name": "tt_app",
        "module_name": "billing",
        "model_name": "tts_data",
        "model_id": 99,
        "display_name": "TTS Data",
        "model_type": "datamodel",
        "open_level": "public",
        "inheritable": True,
    }


async def test_list_models_summarizes_basemodel_row(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=MODEL_QUERY_URL,
        method="POST",
        json={"start": 0, "limit": 10, "total": 1, "data": [_basemodel_row()]},
    )
    out = await _live.list_models(
        "testbed", project_name="tt_app", module_name="billing"
    )
    assert out["total"] == 1
    assert len(out["models"]) == 1
    row = out["models"][0]
    assert row["model_id"] == 99
    assert row["model_name"] == "tts_data"
    assert row["display_name"] == "TTS Data"
    assert row["model_type"] == "datamodel"
    assert row["open_level"] == "public"
    assert row["inheritable"] is True


async def test_list_models_requires_filter_when_scope_empty(
    fake_settings: Settings,
) -> None:
    out = await _live.list_models("testbed")
    assert "error" in out
    assert out["error"]["code"] == "missing_filter"


async def test_get_model_properties_only_drops_extras(fake_settings: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url=MODEL_BY_ID_URL,
        method="POST",
        json={
            "model_id": 99,
            "model_name": "tts_data",
            "properties": [{"name": "p1", "type": "string"}],
            "indexes": [{"name": "idx"}],
            "behaviors": [{"name": "audit"}],
            "validations": [],
        },
    )
    out = await _live.get_model("testbed", 99, properties_only=True)
    assert set(out.keys()) == {"model_id", "model_name", "properties"}
    assert out["model_id"] == 99
    assert out["model_name"] == "tts_data"
    assert out["properties"] == [{"name": "p1", "type": "string"}]


# ---------------- payload slimming (list_services / get_service) ----------------


SERVICE_QUERY_URL = "https://testbed.example.com/adc-studio-service/web/rest/v1/app/service/query"


def _heavy_service_row(name: str = "compute_total") -> dict:
    return {
        "id": 1,
        "service_name": name,
        "service_uri": f"tt_app/billing/{name}",
        "ui_api": False,
        "open_level": "private",
        "active": True,
        "async": False,
        "enable_operation_log": False,
        "project_name": "tt_app",
        "module_name": "billing",
        "created_by": "alice",
        "updated_by": "alice",
        "created_time": "2024-01-01T00:00:00Z",
        "updated_time": "2024-01-15T00:00:00Z",
        "flow": {
            "steps": [{"id": "s1", "type": "start"}, {"id": "s2", "type": "end"}],
            "transitions": [{"from": "s1", "to": "s2"}],
            "input_schema": {"type": "object"},
            "output_schema": {"type": "object"},
        },
    }


async def test_list_services_default_drops_raw_count_and_flow(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=SERVICE_QUERY_URL,
        method="POST",
        json={"total": 1, "instances": [_heavy_service_row()]},
    )
    out = await _live.list_services("testbed", "tt_app", "billing")
    assert "_raw_count" not in out
    assert out["total"] == 1
    row = out["services"][0]
    assert "flow" not in row
    assert row["service_name"] == "compute_total"
    assert row["service_uri"] == "tt_app/billing/compute_total"


async def test_list_services_include_flow_keeps_flow(fake_settings: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url=SERVICE_QUERY_URL,
        method="POST",
        json={"total": 1, "instances": [_heavy_service_row()]},
    )
    out = await _live.list_services("testbed", "tt_app", "billing", include_flow=True)
    assert "_raw_count" not in out
    row = out["services"][0]
    assert "flow" in row
    assert row["flow"]["steps"][0]["id"] == "s1"


async def test_get_service_flow_only_returns_minimal_keys(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=SERVICE_QUERY_URL,
        method="POST",
        json={"total": 1, "instances": [_heavy_service_row("compute_total")]},
    )
    out = await _live.get_service("testbed", "tt_app", "billing", "compute_total", flow_only=True)
    assert set(out.keys()) == {"service_name", "flow"}
    assert out["service_name"] == "compute_total"
    assert out["flow"]["steps"][0]["id"] == "s1"


# ---------------- get_page_detail summary_only ----------------


import json as _json  # noqa: E402

PAGE_DETAIL_URL_RE = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/[0-9]+$"
)


def _page_detail_row(page_id: str = "42") -> dict:
    """Page row with a small but representative SPL `content` tree.

    Two components, one js_content block, two distinct service refs
    (one duplicated to verify dedup).
    """
    content = {
        "componentType": "Container",
        "children": [
            {
                "componentType": "Button",
                "props": {
                    "serviceName": "/tt_app/billing/compute_total",
                    "label": "Compute",
                },
            },
            {
                "componentName": "DataGrid",
                "props": {
                    "location": "/tt_app/billing/list_invoices",
                    "serviceName": "/tt_app/billing/compute_total",
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
        "content": _json.dumps(content),
    }


async def test_get_page_detail_default_keeps_full_content(
    fake_settings: Settings, httpx_mock
) -> None:
    """Default behaviour is unchanged — `content` is preserved as a JSON string."""
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _live.get_page_detail("testbed", "42")
    assert out["content"] == row["content"]
    assert "summary" not in out


async def test_get_page_detail_summary_only_drops_content(
    fake_settings: Settings, httpx_mock
) -> None:
    """`summary_only=True` drops `content` and adds a parsed `summary` dict."""
    row = _page_detail_row()
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _live.get_page_detail("testbed", "42", summary_only=True)
    assert "content" not in out
    assert out["name"] == "billing_dashboard"
    summary = out["summary"]
    assert summary["component_count"] == 3
    assert summary["script_block_count"] == 1
    assert summary["service_refs"] == [
        "/tt_app/billing/compute_total",
        "/tt_app/billing/list_invoices",
    ]


async def test_get_page_detail_summary_handles_malformed_content(
    fake_settings: Settings, httpx_mock
) -> None:
    """Bad JSON in `content` must not raise — caller still gets metadata."""
    row = {"id": "42", "name": "broken", "content": "not-json{"}
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _live.get_page_detail("testbed", "42", summary_only=True)
    assert "content" not in out
    assert out["name"] == "broken"
    assert out["summary"]["component_count"] == 0
    assert "parse_error" in out["summary"]


async def test_get_page_detail_summary_handles_missing_content(
    fake_settings: Settings, httpx_mock
) -> None:
    """A row without `content` (or with null) returns an empty summary."""
    row = {"id": "42", "name": "empty", "content": None}
    httpx_mock.add_response(url=PAGE_DETAIL_URL_RE, method="GET", json=row)
    out = await _live.get_page_detail("testbed", "42", summary_only=True)
    assert out["summary"] == {
        "component_count": 0,
        "service_refs": [],
        "script_block_count": 0,
    }
