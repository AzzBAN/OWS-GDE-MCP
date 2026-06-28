"""Smoke test — package imports and config loads."""

from __future__ import annotations


def test_package_imports() -> None:
    import ows_gde_mcp

    assert ows_gde_mcp.__version__


def test_config_loads() -> None:
    from ows_gde_mcp.config import Settings, Tenant

    assert Tenant.PROD.value == "prod"
    assert Tenant.TESTBED.value == "testbed"
    # Defaults are safe — build a fresh Settings ignoring any host .env so a
    # developer's local prod-write flag can't flip this assertion.
    defaults = Settings(_env_file=None)
    assert defaults.OWS_PROD_WRITE_ENABLED is False
    assert defaults.OWS_MCP_TRANSPORT == "stdio"


def test_status_tool_smoke() -> None:
    from ows_gde_mcp.server import status

    out = status()
    assert out["phase"].startswith("0")
    assert "testbed" in out["tenants"]
    assert "prod" in out["tenants"]
    # Each tenant reports auth-readiness booleans.
    assert "has_session_cookie" in out["tenants"]["testbed"]
    assert "has_csrf_token" in out["tenants"]["testbed"]
