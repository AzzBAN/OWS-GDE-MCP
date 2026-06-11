"""Tests for the script tools in `tools/scripts.py`.

Covers three categories of OWS scripts:
- Service-bundled scripts (RunScript / ScriptLib / Translator / Validator)
  via `POST /adc-studio-service/web/rest/v1/app/service/script/query-all`.
- Page scripts via `GET /adc-studio-ui/web/rest/v1/page-core/page/{id}`,
  projecting `content.js` + `content.js_content` into a flat list.

Endpoint shapes verified against testbed `centralized_inquiry_tracker` on
2026-05-18 — see the discovery transcript in this PR for the captured
request/response samples.
"""

from __future__ import annotations

import json
import re

import pytest

from ows_gde_mcp.config import Settings
from ows_gde_mcp.tools import scripts as _scripts


@pytest.fixture
def fake_settings(monkeypatch: pytest.MonkeyPatch) -> Settings:
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
    # _studio_post is imported into tools.scripts from tools.live, so the
    # `settings` symbol that matters is the one inside tools.live.
    monkeypatch.setattr("ows_gde_mcp.tools.live.settings", s)
    return s


_SCRIPT_QUERY_URL = re.compile(
    r"^https://testbed\.example\.com"
    r"/adc-studio-service/web/rest/v1/app/service/script/query-all$"
)
_PAGE_DETAIL_URL = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page/\d+$"
)
_PAGE_SCRIPT_LIST_URL = re.compile(
    r"^https://testbed\.example\.com/adc-studio-ui/web/rest/v1/page-core/page-script/"
    r"[a-z_]+/[a-z_]+(\?.*)?$"
)


# ---------------- list_service_scripts ----------------


async def test_list_service_scripts_happy_path(
    fake_settings: Settings, httpx_mock
) -> None:
    """Brief listing returns summarized rows; JS body intentionally omitted."""
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        json={
            "content": [
                {
                    "id": 36379,
                    "project_name": "centralized_inquiry_tracker",
                    "module_name": "centralized_inquiry_tracker",
                    "script_name": "runScript_um_handling",
                    "language": "JavaScript",
                    "interp_name": "Rhino2",
                    "version": "2.1",
                    "script_type": "RunScript",
                    "content": None,
                    "active": True,
                    "updated_by": "test-user",
                    "updated_time": "2025-11-26T11:18:55.000+00:00",
                    "created_by": "test-user",
                    "created_time": "2024-11-17T13:03:08.000+00:00",
                    "description": None,
                },
            ],
            "totalElements": 76,
            "totalPages": 8,
            "number": 0,
            "size": 100,
        },
    )
    out = await _scripts.list_service_scripts(
        "testbed",
        "centralized_inquiry_tracker",
        "centralized_inquiry_tracker",
    )
    assert out["total"] == 76
    assert len(out["scripts"]) == 1
    row = out["scripts"][0]
    assert row["script_name"] == "runScript_um_handling"
    assert row["script_type"] == "RunScript"
    assert row["language"] == "JavaScript"
    # content body must NOT bleed into the summary.
    assert "content" not in row


async def test_list_service_scripts_sends_brief_true(
    fake_settings: Settings, httpx_mock
) -> None:
    """The request body must include `brief: true` so the server omits JS bodies."""
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        json={"content": [], "totalElements": 0, "number": 0, "size": 100},
    )
    await _scripts.list_service_scripts(
        "testbed", "p", "m", script_type="RunScript", limit=50
    )
    sent = httpx_mock.get_request()
    assert sent is not None
    body = json.loads(sent.content)
    assert body["brief"] is True
    assert body["script_type"] == "RunScript"
    assert body["project_name"] == "p"
    assert body["module_name"] == "m"
    assert body["limit"] == 50


async def test_list_service_scripts_error_returns_error_dict(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        status_code=500,
        json={"error": {"code": "ADC.X", "message": "boom"}},
    )
    out = await _scripts.list_service_scripts("testbed", "p", "m")
    assert "error" in out
    assert out["error"]["code"] == "ADC.X"


# ---------------- get_service_script ----------------


async def test_get_service_script_returns_full_body(
    fake_settings: Settings, httpx_mock
) -> None:
    body_js = "/* RunScript */\nconsole.log('hi');\n"
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        json={
            "content": [
                {
                    "id": 36379,
                    "script_name": "runScript_um_handling",
                    "project_name": "p",
                    "module_name": "m",
                    "script_type": "RunScript",
                    "content": body_js,
                    "language": "JavaScript",
                    "interp_name": "Rhino2",
                    "version": "2.1",
                    "active": True,
                }
            ],
            "totalElements": 1,
            "number": 0,
            "size": 100,
        },
    )
    row = await _scripts.get_service_script(
        "testbed", "p", "m", "runScript_um_handling"
    )
    assert row["script_name"] == "runScript_um_handling"
    assert row["content"] == body_js
    assert row["language"] == "JavaScript"


async def test_get_service_script_not_found(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        json={"content": [], "totalElements": 0, "number": 0, "size": 100},
    )
    out = await _scripts.get_service_script("testbed", "p", "m", "missing")
    assert "error" in out
    assert "missing" in out["error"]


async def test_get_service_script_request_omits_brief(
    fake_settings: Settings, httpx_mock
) -> None:
    """For detail fetches, `brief` must NOT be set so the server returns content."""
    httpx_mock.add_response(
        url=_SCRIPT_QUERY_URL,
        method="POST",
        json={"content": [], "totalElements": 0, "number": 0, "size": 100},
    )
    await _scripts.get_service_script("testbed", "p", "m", "anything")
    sent = httpx_mock.get_request()
    assert sent is not None
    body = json.loads(sent.content)
    assert "brief" not in body or body["brief"] is False
    assert body["script_name"] == "anything"


# ---------------- get_page_scripts ----------------


_PAGE_CONTENT_FIXTURE = {
    "id": "page",
    "name": "page",
    "children": [],
    "js": [
        {
            "type": "lib",
            "projectName": "centralized_inquiry_tracker",
            "moduleName": "centralized_inquiry_tracker",
            "lib": "init",
            "inline": False,
            "openLevel": "protected",
            "name": "script_1",
        },
        {
            "type": "lib",
            "projectName": "usage_app_log",
            "moduleName": "usage_app_log",
            "lib": "main_js_clone",
            "inline": False,
            "openLevel": "protected",
            "name": "script_5",
        },
    ],
    "css": [
        {
            "type": "lib",
            "projectName": "centralized_inquiry_tracker",
            "moduleName": "centralized_inquiry_tracker",
            "lib": "customization",
            "inline": False,
            "openLevel": "private",
        }
    ],
    "js_content": {
        "centralized_inquiry_tracker/centralized_inquiry_tracker/init": "function init(){}",
        "usage_app_log/usage_app_log/main_js_clone": "function clone(){}",
    },
    "css_content": {
        "centralized_inquiry_tracker/centralized_inquiry_tracker/customization": ".x{color:red;}"
    },
}


async def test_get_page_scripts_happy_path(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_PAGE_DETAIL_URL,
        method="GET",
        json={
            "id": "1447727760177532928",
            "name": "CIT_Query_v2",
            "project_name": "centralized_inquiry_tracker",
            "module_name": "centralized_inquiry_tracker",
            "type": "responsive-web",
            "content": json.dumps(_PAGE_CONTENT_FIXTURE),
        },
    )
    out = await _scripts.get_page_scripts("testbed", "1447727760177532928")
    assert out["page_name"] == "CIT_Query_v2"
    assert len(out["js"]) == 2
    init_script = next(s for s in out["js"] if s["lib"] == "init")
    assert init_script["has_content"] is True
    assert init_script["content"] == "function init(){}"
    # External-module imports come fully inlined.
    cross = next(s for s in out["js"] if s["lib"] == "main_js_clone")
    assert cross["project"] == "usage_app_log"
    assert cross["content"] == "function clone(){}"
    # CSS by default is included.
    assert len(out["css"]) == 1
    assert out["css"][0]["lib"] == "customization"


async def test_get_page_scripts_omit_content(
    fake_settings: Settings, httpx_mock
) -> None:
    """`include_content=False` returns wiring metadata only."""
    httpx_mock.add_response(
        url=_PAGE_DETAIL_URL,
        method="GET",
        json={
            "id": "1",
            "name": "p",
            "type": "responsive-web",
            "content": json.dumps(_PAGE_CONTENT_FIXTURE),
        },
    )
    out = await _scripts.get_page_scripts(
        "testbed", "1", include_content=False, include_css=False
    )
    assert "css" not in out
    for s in out["js"]:
        assert "content" not in s
        assert s["has_content"] is True


async def test_get_page_scripts_empty_content(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_PAGE_DETAIL_URL,
        method="GET",
        json={"id": "1", "name": "blank", "type": "responsive-web", "content": ""},
    )
    out = await _scripts.get_page_scripts("testbed", "1")
    assert out["js"] == []
    assert "warning" in out


async def test_get_page_scripts_malformed_content(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_PAGE_DETAIL_URL,
        method="GET",
        json={"id": "1", "name": "p", "content": "{{{not-json"},
    )
    out = await _scripts.get_page_scripts("testbed", "1")
    assert "error" in out
    assert "Failed to parse content" in out["error"]


# ---------------- list_page_scripts ----------------


_PAGE_SCRIPT_LIST_FIXTURE = {
    "data": [
        {
            "id": 7798,
            "name": "init",
            "page_name": None,
            "script": "function init(){}",
            "project_name": "centralized_inquiry_tracker",
            "module_name": "centralized_inquiry_tracker",
            "type": "js",
            "open_level": "protected",
            "updater": "test-user",
            "update_time": "2026-03-31T10:21:42.000+00:00",
            "page_type": None,
            "origin_name": None,
            "description": None,
            "key_code": "centralized_inquiry_tracker/centralized_inquiry_tracker/init",
        },
        {
            "id": 15950,
            "name": "header",
            "page_name": "CIT_Query_v2",
            "script": "// inline header script\nconsole.log('hi');",
            "project_name": "centralized_inquiry_tracker",
            "module_name": "centralized_inquiry_tracker",
            "type": "jsinline",
            "open_level": "protected",
            "updater": "test-user",
            "update_time": "2026-03-31T10:21:42.000+00:00",
            "page_type": "responsive-web",
            "origin_name": None,
            "description": None,
            "key_code": "centralized_inquiry_tracker/centralized_inquiry_tracker/header",
        },
    ],
    "total": 50,
    "totalPage": 5,
    "page": 0,
    "pageSize": 10,
}


async def test_list_page_scripts_default_strips_body(
    fake_settings: Settings, httpx_mock
) -> None:
    """Default path: strip the JS body, keep only metadata + length."""
    httpx_mock.add_response(
        url=_PAGE_SCRIPT_LIST_URL, method="GET", json=_PAGE_SCRIPT_LIST_FIXTURE
    )
    out = await _scripts.list_page_scripts(
        "testbed", "centralized_inquiry_tracker", "centralized_inquiry_tracker"
    )
    assert out["total"] == 50
    assert out["page"] == 0
    assert len(out["scripts"]) == 2
    init_row = out["scripts"][0]
    assert init_row["name"] == "init"
    assert init_row["type"] == "js"
    assert "script" not in init_row
    assert init_row["script_length"] == len("function init(){}")
    header_row = out["scripts"][1]
    assert header_row["type"] == "jsinline"
    assert header_row["page_name"] == "CIT_Query_v2"


async def test_list_page_scripts_with_body(fake_settings: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url=_PAGE_SCRIPT_LIST_URL, method="GET", json=_PAGE_SCRIPT_LIST_FIXTURE
    )
    out = await _scripts.list_page_scripts(
        "testbed",
        "centralized_inquiry_tracker",
        "centralized_inquiry_tracker",
        include_body=True,
    )
    init_row = out["scripts"][0]
    assert init_row["script"] == "function init(){}"
    assert "script_length" not in init_row


async def test_list_page_scripts_error_returns_error_dict(
    fake_settings: Settings, httpx_mock
) -> None:
    httpx_mock.add_response(
        url=_PAGE_SCRIPT_LIST_URL,
        method="GET",
        status_code=500,
        json={"error": {"code": "ADC.X", "message": "boom"}},
    )
    out = await _scripts.list_page_scripts("testbed", "p", "m")
    assert "error" in out
    assert out["error"]["code"] == "ADC.X"
