import asyncio

import pytest

from ows_gde_mcp.service_guard import assert_read_service, is_write_service
from ows_gde_mcp.tools import live


def test_read_suffix_allowed():
    assert_read_service("cmdb_site_getList")
    assert_read_service("sfo_ticket_query")


def test_write_keyword_blocked():
    with pytest.raises(ValueError, match="write-operation"):
        assert_read_service("sfo_new_forecast_create")


def test_unknown_unsuffixed_blocked():
    with pytest.raises(ValueError, match="read-suffix"):
        assert_read_service("mystery_service")


def test_catalog_service_allowed():
    # A catalog entry is allowed by the guard.
    from ows_gde_mcp.service_catalog import SERVICE_CATALOG  # noqa: F401

    assert_read_service("sfc_service_forecast_order_process_getList")


def test_invalid_chars_blocked():
    with pytest.raises(ValueError, match="invalid characters"):
        assert_read_service("../evil")


def test_is_write_service_helper():
    assert is_write_service("foo_delete") is True
    assert is_write_service("foo_getList") is False


def test_call_ows_api_blocks_write_path_without_optin():
    # No network: the guard returns before any client is built.
    out = asyncio.run(
        live.call_ows_api(
            tenant="testbed",
            method="POST",
            path="/adc-service/web/rest/v1/legacy/services/sfo_order_create",
        )
    )
    assert out["error"]["code"] == "write_guard"


def test_call_ows_api_has_no_allow_write_param():
    # The per-call allow_write skip was removed (it let LLM-sourced args bypass
    # the name-based write guard). The guard now always fires on non-GET.
    import inspect

    sig = inspect.signature(live.call_ows_api)
    assert "allow_write" not in sig.parameters

