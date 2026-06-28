"""Security-focused tests for `OwsClient`.

Covers:
- SSRF guard: reject absolute URLs, protocol-relative paths, and `..`
  traversal segments before any network I/O.
- Prod write-gate enforcement at the client layer (not just in
  `call_ows_api`), with `confirm=True` propagation through the verb wrappers.
- `(tenant, surface)` routing — missing-surface raises a clear error.
"""

from __future__ import annotations

import pytest

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Settings, Surface, Tenant

# ---------------- fixtures ----------------


@pytest.fixture
def fake_settings(monkeypatch: pytest.MonkeyPatch) -> Settings:
    """Construct a `Settings` with both tenants fully configured.

    Both surfaces are configured for both tenants (testbed gets distinct
    studio + runtime hosts; prod gets only runtime to mirror reality)
    so each test can pick the cell it needs. `monkeypatch.delenv` clears
    any host env that would otherwise leak in via pydantic-settings'
    env-precedence — explicit kwargs still win, but defaults for
    unspecified fields should not pull from a developer's shell.
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
    return Settings(
        _env_file=None,
        OWS_TESTBED_STUDIO_URL="https://testbed-studio.example.com",
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="csrf-testbed",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=False,
    )


@pytest.fixture
def prod_writable(monkeypatch: pytest.MonkeyPatch) -> Settings:
    """Same as `fake_settings` but with the env-gate flipped on."""
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
    return Settings(
        OWS_TESTBED_STUDIO_URL="https://testbed-studio.example.com",
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="csrf-testbed",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
        OWS_PROD_WRITE_ENABLED=True,
    )


# ---------------- SSRF guard ----------------


@pytest.mark.parametrize(
    "bad_path",
    [
        "https://attacker.example.com/x",
        "http://attacker.example.com/x",
        "//evil.example.com/x",
        "/foo/../bar",
        "/foo/%2e%2e/bar",
        "/foo/%2E%2E/bar",
        "/a/b/../../etc/passwd",
        "",
    ],
)
async def test_request_rejects_unsafe_paths(fake_settings: Settings, bad_path: str) -> None:
    """Path validator must fire before any network I/O.

    `pytest-httpx` is configured (via its default behaviour) to fail the test
    if an unmatched request is made. We register no mock, so a ValueError
    raised before `httpx.AsyncClient.request` is the only way the test can
    pass.
    """
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        with pytest.raises(ValueError):
            await client.request("GET", bad_path)


async def test_request_accepts_safe_relative_path(fake_settings: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        json={"ok": True},
    )
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        out = await client.get("/portal/x")
    assert out == {"ok": True}


async def test_request_accepts_path_with_query_string(fake_settings: Settings, httpx_mock) -> None:
    """Query strings, percent-encoded chars, and nested paths should all pass."""
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/web/rest/v1/x?a=1&b=hello%20world",
        method="GET",
        json={"ok": True},
    )
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        out = await client.get("/portal/web/rest/v1/x?a=1&b=hello%20world")
    assert out == {"ok": True}


# ---------------- prod write-gate ----------------


async def test_prod_non_get_blocked_when_write_disabled(
    fake_settings: Settings,
) -> None:
    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, fake_settings) as client:
        with pytest.raises(PermissionError, match="OWS_PROD_WRITE_ENABLED"):
            await client.post("/portal/x", json={})


async def test_prod_non_get_blocked_without_confirm(
    prod_writable: Settings,
) -> None:
    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, prod_writable) as client:
        with pytest.raises(ValueError, match="confirm=True"):
            await client.post("/portal/x", json={})


async def test_prod_non_get_succeeds_with_confirm(prod_writable: Settings, httpx_mock) -> None:
    httpx_mock.add_response(
        url="https://prod.example.com/portal/x",
        method="POST",
        json={"ok": True},
    )
    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, prod_writable) as client:
        out = await client.post("/portal/x", json={}, confirm=True)
    assert out == {"ok": True}


async def test_testbed_non_get_succeeds_without_confirm(
    fake_settings: Settings, httpx_mock
) -> None:
    """Write-gate must only fire for prod; testbed mutations are unrestricted."""
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="POST",
        json={"ok": True},
    )
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as client:
        out = await client.post("/portal/x", json={})
    assert out == {"ok": True}


async def test_prod_get_succeeds_without_confirm(fake_settings: Settings, httpx_mock) -> None:
    """GET on prod must not be gated, even with the env flag off."""
    httpx_mock.add_response(
        url="https://prod.example.com/portal/x",
        method="GET",
        json={"ok": True},
    )
    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, fake_settings) as client:
        out = await client.get("/portal/x")
    assert out == {"ok": True}


# ---------------- (tenant, surface) routing ----------------


def test_missing_surface_raises_clear_error(fake_settings: Settings) -> None:
    """Prod has no studio URL configured in the fixture — calling the
    studio surface must fail fast with a message naming the env var."""
    with pytest.raises(RuntimeError, match="OWS_PROD_STUDIO_URL"):
        OwsClient.for_surface(Tenant.PROD, Surface.STUDIO, fake_settings)


async def test_studio_and_runtime_route_to_distinct_hosts(
    fake_settings: Settings, httpx_mock
) -> None:
    """A studio call goes to the studio host; a runtime call goes to the
    runtime host. Same tenant, different base URLs."""
    httpx_mock.add_response(
        url="https://testbed-studio.example.com/adc-studio-model/x",
        method="GET",
        json={"surface": "studio"},
    )
    httpx_mock.add_response(
        url="https://testbed.example.com/portal/x",
        method="GET",
        json={"surface": "runtime"},
    )
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.STUDIO, fake_settings) as c1:
        s_out = await c1.get("/adc-studio-model/x")
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, fake_settings) as c2:
        r_out = await c2.get("/portal/x")
    assert s_out == {"surface": "studio"}
    assert r_out == {"surface": "runtime"}


def test_auth_shared_across_surfaces_on_same_host(monkeypatch: pytest.MonkeyPatch) -> None:
    """Auth is keyed by host, not tenant. Real testbed serves studio + runtime
    from one host, so two surfaces that resolve to the same host must reuse the
    same AuthContext (one CAS session covers both). Surfaces on distinct hosts
    (prod's separate studio + runtime) must NOT share — each host logs in
    independently."""
    for var in (
        "OWS_TESTBED_STUDIO_URL",
        "OWS_TESTBED_RUNTIME_URL",
        "OWS_TESTBED_SESSION_COOKIE",
        "OWS_TESTBED_CSRF_TOKEN",
        "OWS_PROD_STUDIO_URL",
        "OWS_PROD_RUNTIME_URL",
        "OWS_PROD_SESSION_COOKIE",
        "OWS_PROD_CSRF_TOKEN",
    ):
        monkeypatch.delenv(var, raising=False)
    settings = Settings(
        _env_file=None,
        # Testbed: studio + runtime on the SAME host (mirrors reality).
        OWS_TESTBED_STUDIO_URL="https://testbed.example.com",
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="csrf-testbed",
        # Prod: studio + runtime on DISTINCT hosts.
        OWS_PROD_STUDIO_URL="https://prod-studio.example.com",
        OWS_PROD_RUNTIME_URL="https://prod.example.com",
        OWS_PROD_SESSION_COOKIE="k=v",
        OWS_PROD_CSRF_TOKEN="csrf-prod",
    )
    # Same host → shared AuthContext.
    c1 = OwsClient.for_surface(Tenant.TESTBED, Surface.STUDIO, settings)
    c2 = OwsClient.for_surface(Tenant.TESTBED, Surface.RUNTIME, settings)
    assert c1._auth is c2._auth
    # Distinct hosts → independent AuthContexts.
    p1 = OwsClient.for_surface(Tenant.PROD, Surface.STUDIO, settings)
    p2 = OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, settings)
    assert p1._auth is not p2._auth
