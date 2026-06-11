import pytest

import ows_gde_mcp.client as clientmod
from ows_gde_mcp.client import refresh_host_session
from ows_gde_mcp.config import Settings, Tenant


@pytest.fixture
def settings(monkeypatch):
    for var in ("OWS_PROD_STUDIO_URL","OWS_PROD_RUNTIME_URL","OWS_PROD_USERNAME",
                "OWS_PROD_PASSWORD","OWS_TESTBED_STUDIO_URL","OWS_TESTBED_RUNTIME_URL",
                "OWS_PROD_SESSION_COOKIE","OWS_PROD_CSRF_TOKEN"):
        monkeypatch.delenv(var, raising=False)
    return Settings(
        _env_file=None,
        OWS_PROD_STUDIO_URL="https://studio.example.com",
        OWS_PROD_RUNTIME_URL="https://runtime.example.com",
        OWS_PROD_USERNAME="u", OWS_PROD_PASSWORD="p",
        OWS_TESTBED_STUDIO_URL="https://same.example.com",
        OWS_TESTBED_RUNTIME_URL="https://same.example.com",
    )


@pytest.fixture(autouse=True)
def _clear():
    clientmod._auth_cache.clear()
    clientmod._relogin_locks.clear()
    clientmod._last_relogin_at.clear()


@pytest.mark.asyncio
async def test_distinct_hosts_login_independently(settings, monkeypatch):
    calls = []
    async def fake_http_login(base_url, username, password):
        calls.append(base_url)
        return (f"COOKIE_FOR={base_url}", "csrf123")
    monkeypatch.setattr(clientmod, "_http_login", fake_http_login)

    await refresh_host_session("https://studio.example.com", Tenant.PROD, settings)
    await refresh_host_session("https://runtime.example.com", Tenant.PROD, settings)

    assert calls == ["https://studio.example.com", "https://runtime.example.com"]
    assert "studio.example.com" in clientmod._auth_cache
    assert "runtime.example.com" in clientmod._auth_cache


@pytest.mark.asyncio
async def test_http_failure_falls_back_to_playwright(settings, monkeypatch):
    from ows_gde_mcp.auth_login_http import HttpLoginError
    pw_calls = []
    async def fail_http(base_url, username, password):
        raise HttpLoginError("captcha")
    async def fake_pw(tenant, s, base_url=None):
        pw_calls.append(base_url)
        return ("PW_COOKIE=1", "pwcsrf")
    monkeypatch.setattr(clientmod, "_http_login", fail_http)
    monkeypatch.setattr(clientmod, "_cas_login", fake_pw)

    await refresh_host_session("https://studio.example.com", Tenant.PROD, settings)
    assert pw_calls == ["https://studio.example.com"]
    assert clientmod._auth_cache["studio.example.com"].cookie == "PW_COOKIE=1"
