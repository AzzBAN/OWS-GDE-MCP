"""Integration tests for the `whoami` MCP tool.

Uses `pytest-httpx` to mock the OWS API endpoints so we can test the
full tool logic without a live network.
"""

from __future__ import annotations

import pytest

import ows_gde_mcp.client as client_mod
from ows_gde_mcp.config import Settings
from ows_gde_mcp.server import whoami


@pytest.fixture(autouse=True)
def _reset() -> None:
    """Reset per-process auth state between tests."""
    client_mod._auth_cache.clear()
    client_mod._relogin_locks.clear()
    client_mod._last_relogin_at.clear()


class TestWhoamiTool:
    """Smoke tests for the `whoami` tool.

    The tool calls two runtime endpoints:
    - GET /portal/web/rest/v1/user/my-info  → user profile
    - GET /portal/web/rest/sso/check        → session liveness

    We mock both with `pytest-httpx` to cover the happy path and the
    error path.
    """

    async def test_whoami_returns_user_info(
        self, httpx_mock, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Happy path: both endpoints return 200."""
        test_settings = Settings(
            OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
            OWS_TESTBED_SESSION_COOKIE="k=v",
            OWS_TESTBED_CSRF_TOKEN="csrf-test",
            OWS_PROD_RUNTIME_URL="https://prod.example.com",
            OWS_PROD_SESSION_COOKIE="k=v",
            OWS_PROD_CSRF_TOKEN="csrf-prod",
            OWS_PROD_WRITE_ENABLED=True,
        )
        # Patch settings in server.py so whoami uses the mock URL
        monkeypatch.setattr("ows_gde_mcp.server.settings", test_settings)

        httpx_mock.add_response(
            url="https://testbed.example.com/portal/web/rest/v1/user/my-info",
            method="GET",
            json={
                "userId": "U00001",
                "userAccount": "awx1320635",
                "userName": "Azhar Wahid",
                "tenantId": 1057,
                "timeZone": "+08:00",
            },
        )
        httpx_mock.add_response(
            url="https://testbed.example.com/portal/web/rest/sso/check",
            method="GET",
            json={"data": "ok"},
        )

        result = await whoami(tenant="testbed")

        assert result["tenant"] == "testbed"
        assert result["userId"] == "U00001"
        assert result["userAccount"] == "awx1320635"
        assert result["userName"] == "Azhar Wahid"
        assert result["tenantId"] == 1057
        assert result["timeZone"] == "+08:00"
        assert result["_session_alive"] is True

    async def test_whoami_returns_error_dict_on_ows_api_error(
        self, httpx_mock, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """When the my-info endpoint returns a structured OWS error, we get a dict with 'error' key."""
        test_settings = Settings(
            OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
            OWS_TESTBED_SESSION_COOKIE="k=v",
            OWS_TESTBED_CSRF_TOKEN="csrf-test",
        )
        monkeypatch.setattr("ows_gde_mcp.server.settings", test_settings)

        # OWS returns structured errors as {"error": {...}}
        httpx_mock.add_response(
            url="https://testbed.example.com/portal/web/rest/v1/user/my-info",
            method="GET",
            status_code=401,
            json={
                "error": {
                    "code": "ADC.COMM.SDK.03240001",
                    "message": "Session expired",
                }
            },
        )

        result = await whoami(tenant="testbed")

        assert "error" in result
        assert result["error"]["code"] == "ADC.COMM.SDK.03240001"
        assert "hint" in result
        assert "SESSION_COOKIE" in result["hint"]

    async def test_whoami_prod_uses_prod_runtime_url(
        self, httpx_mock, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Prod traffic goes to the prod runtime URL, not testbed."""
        test_settings = Settings(
            OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
            OWS_TESTBED_SESSION_COOKIE="k=v",
            OWS_TESTBED_CSRF_TOKEN="csrf-test",
            OWS_PROD_RUNTIME_URL="https://prod.example.com",
            OWS_PROD_SESSION_COOKIE="k=v",
            OWS_PROD_CSRF_TOKEN="csrf-prod",
            OWS_PROD_WRITE_ENABLED=True,
        )
        monkeypatch.setattr("ows_gde_mcp.server.settings", test_settings)

        httpx_mock.add_response(
            url="https://prod.example.com/portal/web/rest/v1/user/my-info",
            method="GET",
            json={
                "userId": "U00099",
                "userAccount": "admin",
                "userName": "Prod Admin",
                "tenantId": 1057,
                "timeZone": "+08:00",
            },
        )
        httpx_mock.add_response(
            url="https://prod.example.com/portal/web/rest/sso/check",
            method="GET",
            json={"data": "ok"},
        )

        result = await whoami(tenant="prod")

        assert result["tenant"] == "prod"
        assert result["userAccount"] == "admin"
