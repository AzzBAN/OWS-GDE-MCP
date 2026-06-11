"""Tests for auto-relogin in `OwsClient`.

Covers:
- 302 → /dspcas/login triggers a single relogin + retry.
- Concurrent in-flight requests serialise on one relogin.
- Missing creds surface as a clear error (no second attempt).
- Two consecutive 302s don't loop forever.
- Prod write-gate runs before any network attempt and is not bypassed.

The real Playwright/CAS flow is never exercised — `auth_login.login` is
monkeypatched to return canned credentials.
"""

from __future__ import annotations

import asyncio

import pytest

from ows_gde_mcp import client as client_mod
from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Settings, Surface, Tenant


@pytest.fixture(autouse=True)
def _clear_auth_cache() -> None:
    """Reset per-process auth state between tests so each starts clean.

    Includes the relogin lock + timestamp dict so the 5-second skip
    window from a prior test doesn't suppress a fresh test's relogin.
    """
    client_mod._auth_cache.clear()
    client_mod._relogin_locks.clear()
    client_mod._last_relogin_at.clear()


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
        "OWS_TESTBED_USERNAME",
        "OWS_TESTBED_PASSWORD",
        "OWS_PROD_USERNAME",
        "OWS_PROD_PASSWORD",
    ):
        monkeypatch.delenv(var, raising=False)
    return Settings(
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_SESSION_COOKIE="old-cookie",
        OWS_TESTBED_CSRF_TOKEN="old-csrf",
        OWS_TESTBED_USERNAME="testuser",
        OWS_TESTBED_PASSWORD="testpass",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="old-cookie",
        OWS_PROD_CSRF_TOKEN="old-csrf",
        OWS_PROD_WRITE_ENABLED=False,
    )


def _patch_login(monkeypatch: pytest.MonkeyPatch, fn) -> list[int]:
    calls: list[int] = []

    async def wrapper(tenant, settings):
        calls.append(1)
        return await fn(tenant, settings)

    monkeypatch.setattr(client_mod, "_cas_login", wrapper)
    return calls


async def test_relogin_after_302_succeeds_on_retry(
    fake_settings: Settings, httpx_mock, monkeypatch
) -> None:
    async def fake_login(tenant, settings):
        return "new-cookie", "new-csrf"

    calls = _patch_login(monkeypatch, fake_login)

    # First call: 302 → CAS. Second call (after relogin): 200.
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        status_code=302,
        headers={"location": "https://testbed.example.com/dspcas/login?service=foo"},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        json={"ok": True},
    )

    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        out = await client.get("/portal/x")

    assert out == {"ok": True}
    assert len(calls) == 1
    # AuthContext was mutated in place.
    requests = httpx_mock.get_requests()
    assert requests[0].headers["cookie"] == "old-cookie"
    assert requests[1].headers["cookie"] == "new-cookie"


async def test_concurrent_relogin_runs_login_once(
    fake_settings: Settings, httpx_mock, monkeypatch
) -> None:
    login_started = asyncio.Event()
    login_release = asyncio.Event()

    async def fake_login(tenant, settings):
        login_started.set()
        await login_release.wait()
        return "new-cookie", "new-csrf"

    calls = _patch_login(monkeypatch, fake_login)

    # Five 302s, then five 200s — pytest-httpx matches in registration order
    # for same URL+method.
    for _ in range(5):
        httpx_mock.add_response(
            url="https://testbed.example.com/portal/x",
            method="GET",
            status_code=302,
            headers={"location": "/dspcas/login"},
        )
    for _ in range(5):
        httpx_mock.add_response(
            url="https://testbed.example.com/portal/x",
            method="GET",
            json={"ok": True},
        )

    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        tasks = [asyncio.create_task(client.get("/portal/x")) for _ in range(5)]
        await login_started.wait()
        login_release.set()
        results = await asyncio.gather(*tasks)

    assert results == [{"ok": True}] * 5
    assert len(calls) == 1


async def test_relogin_missing_creds_raises_clear_error(
    fake_settings: Settings, httpx_mock, monkeypatch
) -> None:
    fake_settings.OWS_TESTBED_USERNAME = None
    fake_settings.OWS_TESTBED_PASSWORD = None

    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        status_code=302,
        headers={"location": "/dspcas/login"},
    )

    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        with pytest.raises(RuntimeError, match="USERNAME and OWS_TESTBED_PASSWORD"):
            await client.get("/portal/x")


async def test_two_consecutive_302s_do_not_loop(
    fake_settings: Settings, httpx_mock, monkeypatch
) -> None:
    async def fake_login(tenant, settings):
        return "still-bad-cookie", "still-bad-csrf"

    _patch_login(monkeypatch, fake_login)

    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        status_code=302,
        headers={"location": "/dspcas/login"},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        status_code=302,
        headers={"location": "/dspcas/login"},
    )

    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        with pytest.raises(RuntimeError, match="still redirected to CAS"):
            await client.get("/portal/x")


async def test_prod_write_gate_runs_before_any_network_attempt(
    fake_settings: Settings, monkeypatch
) -> None:
    """Relogin must not bypass the prod write-gate.

    `httpx_mock` is intentionally absent — if the gate fails to fire, the
    request goes out, pytest-httpx fails with no matching response, and the
    test catches it as the wrong exception.
    """

    async def fake_login(tenant, settings):  # pragma: no cover — must not run
        raise AssertionError("login must not be invoked when the write-gate blocks")

    _patch_login(monkeypatch, fake_login)

    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, fake_settings) as client:
        with pytest.raises(PermissionError, match="OWS_PROD_WRITE_ENABLED"):
            await client.post("/portal/x", json={})
