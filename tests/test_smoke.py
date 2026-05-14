"""Smoke test — package imports and config loads."""

from __future__ import annotations


def test_package_imports() -> None:
    import ows_gde_mcp

    assert ows_gde_mcp.__version__


def test_config_loads() -> None:
    from ows_gde_mcp.config import Tenant, settings

    assert Tenant.PROD.value == "prod"
    assert Tenant.TESTBED.value == "testbed"
    # Defaults are safe.
    assert settings.OWS_PROD_WRITE_ENABLED is False
    assert settings.OWS_MCP_TRANSPORT == "stdio"


def test_status_tool_smoke() -> None:
    from ows_gde_mcp.server import status

    out = status()
    assert out["phase"].startswith("0")
    assert "testbed" in out["tenants"]
    assert "prod" in out["tenants"]
    # Each tenant reports auth-readiness booleans.
    assert "has_session_cookie" in out["tenants"]["testbed"]
    assert "has_csrf_token" in out["tenants"]["testbed"]
