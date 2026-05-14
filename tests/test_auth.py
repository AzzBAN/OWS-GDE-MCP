"""Tests for the reverse-engineered OWS auth algorithm.

The samples below are real `(url, timestamp, expected x-adc-page-token)`
tuples captured from a logged-in browser session via Playwright MCP. See
`docs/discovery.md` → "Algorithm — Page token" for capture provenance.
"""

from __future__ import annotations

import pytest

from ows_gde_mcp.auth import AuthContext, java_hashcode, page_token

# (url_or_path, timestamp_ms, expected_token)
LIVE_SAMPLES = [
    ("/portal/web/rest/v1/user/my-info", 1778751584033, -1955536328),
    (
        "/portal/web/rest/v1/menu/manage/app/getGranted?granted=true",
        1778751584193,
        440037745,
    ),
    # Plus a POST sample where the path has no query string
    (
        "/adc-service/web/rest/v1/legacy/services/pd_process_definition_getList",
        1778751645967,
        737556385,
    ),
]


@pytest.mark.parametrize("url,ts,expected", LIVE_SAMPLES)
def test_page_token_matches_live_capture(url: str, ts: int, expected: int) -> None:
    assert page_token(url, ts) == expected


def test_java_hashcode_known_values() -> None:
    # Reference values produced by Java `String.hashCode()`.
    assert java_hashcode("") == 0
    assert java_hashcode("a") == 97
    assert java_hashcode("abc") == 96354
    # Negative case — single char that overflows the signed bit only with
    # accumulation. Empty edge case already covered.
    assert java_hashcode("Hello, World!") == 1498789909


def test_page_token_strips_query_string() -> None:
    base = "/api/x"
    ts = 1000
    assert page_token(base, ts) == page_token(base + "?foo=bar&baz=1", ts)


def test_page_token_strips_fragment() -> None:
    base = "/api/x"
    ts = 1000
    assert page_token(base, ts) == page_token(base + "#section", ts)


def test_page_token_accepts_full_url() -> None:
    ts = 1000
    assert page_token("/api/x", ts) == page_token("https://host.example.com/api/x?q=1", ts)


def test_headers_for_get_excludes_csrf() -> None:
    auth = AuthContext(cookie="k=v", csrf_token="abc")
    h = auth.headers_for("GET", "/portal/web/rest/v1/user/my-info", ts_ms=1778751584033)
    assert h["x-adc-page-timestamp"] == "1778751584033"
    assert h["x-adc-page-token"] == "-1955536328"
    assert h["x-gde-src-page"] == "/portal-web/portal/homepage.html"
    assert h["x-gde-target-app"] == ""
    assert h["X-Requested-With"] == "XMLHttpRequest"
    assert h["Cookie"] == "k=v"
    assert "x-gde-csrf-token" not in h


def test_headers_for_post_includes_csrf() -> None:
    auth = AuthContext(cookie="k=v", csrf_token="csrf123")
    h = auth.headers_for(
        "POST",
        "/adc-service/web/rest/v1/legacy/services/foo",
        ts_ms=1778751645967,
    )
    assert h["x-gde-csrf-token"] == "csrf123"


def test_headers_for_post_without_csrf_raises() -> None:
    auth = AuthContext(cookie="k=v", csrf_token=None)
    with pytest.raises(RuntimeError, match="csrf_token is required"):
        auth.headers_for("POST", "/api/x")


def test_headers_for_overrides() -> None:
    auth = AuthContext(cookie="k=v", csrf_token="c")
    h = auth.headers_for(
        "GET",
        "/api/x",
        ts_ms=1,
        src_page="/custom/page.html",
        target_app="someApp",
        extra={"X-Custom": "yes"},
    )
    assert h["x-gde-src-page"] == "/custom/page.html"
    assert h["x-gde-target-app"] == "someApp"
    assert h["X-Custom"] == "yes"
