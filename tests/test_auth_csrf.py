from ows_gde_mcp.auth import AuthContext
from ows_gde_mcp.client import _auth_for_host
from ows_gde_mcp.config import Settings, Surface, Tenant


def test_headers_use_custom_csrf_header_name():
    auth = AuthContext(cookie="k=v", csrf_token="TOK123", csrf_header="X-CSRF-TOKEN")
    headers = auth.headers_for("POST", "/adc-studio-service/web/rest/v1/app/service/test/p/m/s")
    assert headers["X-CSRF-TOKEN"] == "TOK123"
    assert "x-gde-csrf-token" not in headers


def test_headers_default_csrf_header_name():
    auth = AuthContext(cookie="k=v", csrf_token="TOK123")
    headers = auth.headers_for("POST", "/x")
    assert headers["x-gde-csrf-token"] == "TOK123"


def test_env_csrf_token_populates_auth(monkeypatch):
    for var in ("OWS_TESTBED_STUDIO_URL", "OWS_TESTBED_SESSION_COOKIE",
                "OWS_TESTBED_CSRF_TOKEN"):
        monkeypatch.delenv(var, raising=False)
    s = Settings(
        _env_file=None,
        OWS_TESTBED_STUDIO_URL="https://testbed-studio.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="ENVTOK",
    )
    import ows_gde_mcp.client as c
    c._auth_cache.clear()
    auth = _auth_for_host(s.base_url(Tenant.TESTBED, Surface.STUDIO), Tenant.TESTBED, s)
    headers = auth.headers_for("POST", "/x")
    assert headers["x-gde-csrf-token"] == "ENVTOK"
