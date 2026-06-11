"""Tests for `invoke_service` and `query_model_data`.

Both endpoints were captured from a live Studio session on 2026-05-18:
- `invoke_service` (testbed) -> `POST /adc-studio-service/web/rest/v1/app/service/test/<p>/<m>/<s>`
- `invoke_service` (prod)    -> `POST /adc-app-ops/web/rest/v1/service/test`
- `query_model_data` -> `POST /adc-app-ops/web/rest/v1/model-data-management/queryByTql`
  (optionally pre-flighted via `.../tqlTranslateCheck`).

Mocking style mirrors `tests/tools/test_studio_artifacts.py`: a `Settings`
fixture with both tenants configured, `monkeypatch.setattr` swapping the
module-level `settings` symbol inside `ows_gde_mcp.tools.live`, and
`pytest-httpx` for the network layer.
"""

from __future__ import annotations

import pytest

from ows_gde_mcp.config import Settings
from ows_gde_mcp.tools import live as _live


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
        OWS_PROD_STUDIO_URL="https://prod.example.com",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=False,
    )
    monkeypatch.setattr("ows_gde_mcp.tools.live.settings", s)
    return s


@pytest.fixture
def prod_writable(monkeypatch: pytest.MonkeyPatch) -> Settings:
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
        OWS_PROD_STUDIO_URL="https://prod.example.com",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=True,
    )
    monkeypatch.setattr("ows_gde_mcp.tools.live.settings", s)
    return s


# ---------------- invoke_service ----------------


async def test_invoke_service_testbed_happy_path(
    fake_settings: Settings, httpx_mock
) -> None:
    """Testbed uses Studio playground endpoint."""
    httpx_mock.add_response(
        url=(
            "https://testbed.example.com/adc-studio-service/web/rest/v1/app/service/"
            "test/centralized_inquiry_tracker/centralized_inquiry_tracker/centralize_um_handling"
        ),
        method="POST",
        json={"result": "ok", "data": [{"id": 1}]},
    )
    out = await _live.invoke_service(
        "testbed",
        "centralized_inquiry_tracker",
        "centralized_inquiry_tracker",
        "centralize_um_handling",
        {"account": "test"},
    )
    assert out == {"result": "ok", "data": [{"id": 1}]}


async def test_invoke_service_testbed_empty_payload_defaults_to_empty_dict(
    fake_settings: Settings, httpx_mock
) -> None:
    """Caller can omit `payload` for services that take no input (testbed)."""
    httpx_mock.add_response(
        url=(
            "https://testbed.example.com/adc-studio-service/web/rest/v1/app/service/"
            "test/p/m/s"
        ),
        method="POST",
        match_json={},
        json={"ok": True},
    )
    out = await _live.invoke_service("testbed", "p", "m", "s")
    assert out == {"ok": True}


async def test_invoke_service_prod_uses_runtime_apops_endpoint(
    prod_writable: Settings, httpx_mock
) -> None:
    """Prod uses the runtime app-ops endpoint, not Studio."""
    httpx_mock.add_response(
        url="https://prod.example.com/adc-app-ops/web/rest/v1/service/test",
        method="POST",
        match_json={
            "request_string": "/adc-service/rest/v1/services/tt_improvement/tt_rma/tt_rma_inc_batch_cancel",
            "raw_body": {"inc_ids": ["INC-001", "INC-002"]},
        },
        json={"traceId": "abc123", "success": True, "result": {"debug_output": {"result": "ok"}}},
    )
    out = await _live.invoke_service(
        "prod",
        "tt_improvement",
        "tt_rma",
        "tt_rma_inc_batch_cancel",
        {"inc_ids": ["INC-001", "INC-002"]},
        confirm=True,
    )
    assert out["success"] is True
    assert out["traceId"] == "abc123"


async def test_invoke_service_prod_without_confirm_raises(
    prod_writable: Settings,
) -> None:
    """Prod still requires confirm=True even with OWS_PROD_WRITE_ENABLED."""
    with pytest.raises(ValueError, match="confirm=True"):
        await _live.invoke_service("prod", "p", "m", "s", {})


async def test_invoke_service_prod_blocked_when_write_disabled(
    fake_settings: Settings,
) -> None:
    """`OWS_PROD_WRITE_ENABLED` defaults to False — non-GET on prod must
    raise PermissionError before any HTTP call."""
    with pytest.raises(PermissionError, match="OWS_PROD_WRITE_ENABLED"):
        await _live.invoke_service("prod", "p", "m", "s", {}, confirm=True)


# ---------------- query_model_data ----------------


async def test_query_model_data_happy_path(fake_settings: Settings, httpx_mock) -> None:
    """Validate-then-query, two POSTs. Server returns rows as a top-level
    list; tool wraps into `{row_count, rows}`."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={"pass": True, "errorCode": None, "failed": False},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        json=[{"id": "1"}, {"id": "2"}],
    )
    out = await _live.query_model_data(
        "testbed",
        'select * from "/p/m/model" as model limit 2',
    )
    assert out == {"row_count": 2, "rows": [{"id": "1"}, {"id": "2"}]}


async def test_query_model_data_translate_check_failure_short_circuits(
    fake_settings: Settings, httpx_mock
) -> None:
    """When the pre-flight returns `pass=false`, the tool surfaces the
    upstream errorRow/errorColumn cleanly and never calls queryByTql."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={
            "pass": False,
            "errorCode": "00130010",
            "errorRow": 1,
            "errorColumn": 14,
            "errorArgs": ["1", "14"],
            "failed": True,
        },
    )
    out = await _live.query_model_data("testbed", "select * from /bad limit 1")
    assert out == {
        "error": {
            "code": "00130010",
            "row": 1,
            "column": 14,
            "args": ["1", "14"],
            "message": "TQL compile failed",
            "path": "/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        }
    }


async def test_query_model_data_skip_validate(
    fake_settings: Settings, httpx_mock
) -> None:
    """`validate=False` must skip the pre-flight entirely. Only one POST."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        json=[],
    )
    out = await _live.query_model_data(
        "testbed",
        'select * from "/p/m/x" as x limit 1',
        validate=False,
    )
    assert out == {"row_count": 0, "rows": []}


async def test_query_model_data_need_null_value_propagates(
    fake_settings: Settings, httpx_mock
) -> None:
    """The `need_null_value` arg must round-trip into the queryByTql body."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={"pass": True, "failed": False},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        match_json={"tql": "select 1", "need_null_value": False},
        json=[],
    )
    out = await _live.query_model_data(
        "testbed", "select 1", need_null_value=False
    )
    assert out == {"row_count": 0, "rows": []}


async def test_query_model_data_dict_response_unwraps_data_key(
    fake_settings: Settings, httpx_mock
) -> None:
    """Defensive: some flavours of the endpoint wrap rows under a `data`
    key. The tool tolerates this and still surfaces `row_count`/`rows`."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={"pass": True, "failed": False},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        json={"data": [{"id": "x"}], "extra": "metadata"},
    )
    out = await _live.query_model_data("testbed", "select 1")
    assert out["row_count"] == 1
    assert out["rows"] == [{"id": "x"}]
    assert out["raw"] == {"data": [{"id": "x"}], "extra": "metadata"}


async def test_query_model_data_http_error_returns_error_envelope(
    fake_settings: Settings, httpx_mock
) -> None:
    """A 500 from queryByTql must return the standard error envelope, not
    raise."""
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={"pass": True, "failed": False},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        status_code=500,
        json={"error": {"code": "X", "message": "boom"}},
    )
    out = await _live.query_model_data("testbed", "select 1")
    assert "error" in out
    assert out["error"]["status"] == 500


async def test_query_model_data_prod_bypasses_write_gate(
    fake_settings: Settings, httpx_mock
) -> None:
    """`fake_settings` has `OWS_PROD_WRITE_ENABLED=False`. TQL is
    select-only on the server, so the tool internally passes
    `confirm=True` and routes to the prod *runtime* host — the call must
    succeed even with the write-gate flag off."""
    httpx_mock.add_response(
        url="https://prod.example.com/adc-app-ops/web/rest/v1/model-data-management/tqlTranslateCheck",
        method="POST",
        json={"pass": True, "failed": False},
    )
    httpx_mock.add_response(
        url="https://prod.example.com/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
        method="POST",
        json=[{"id": "1"}],
    )
    out = await _live.query_model_data(
        "prod", 'select * from "/p/m/x" as x limit 1'
    )
    assert out == {"row_count": 1, "rows": [{"id": "1"}]}
