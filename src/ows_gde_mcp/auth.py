"""OWS / GDE authentication & per-request header crafting.

The OWS portal gates every authenticated API call with three families of
secrets:

1. A session cookie (HttpOnly, set by Apereo CAS after `/dspcas/login`).
2. Per-request anti-tamper headers:
   - `x-adc-page-timestamp` — current epoch ms
   - `x-adc-page-token`     — `javaStringHashCode(path_without_query + ts_str)`
   - `x-gde-src-page`       — the page making the call (e.g. `/portal-web/portal/homepage.html`)
   - `x-gde-target-app`     — usually empty (set when calling cross-app)
   - `X-Requested-With`     — `XMLHttpRequest`
3. A CSRF header on non-GET requests:
   - Header name `x-gde-csrf-token`, value = the 48-digit token returned at
     login and exposed to the SPA as `window.csrfToken`.

This module implements (2) and (3); (1) is supplied via env (see
`config.OWS_TESTBED_SESSION_COOKIE` / `OWS_PROD_SESSION_COOKIE`) or future
interactive-login support.

Reverse-engineered from `/portal-web/static/js/chunk-vigour.294ef8b0.js`
on the testbed Studio host. See `docs/discovery.md` for the proof / samples.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from urllib.parse import urlsplit


def java_hashcode(s: str) -> int:
    """Compute Java `String.hashCode()` — used by OWS for `x-adc-page-token`.

    Returns a signed 32-bit integer (range `[-2**31, 2**31 - 1]`).
    """
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    if h >= 0x80000000:
        h -= 0x100000000
    return h


def _path_only(url_or_path: str) -> str:
    """Strip scheme/host/query/fragment, return just the URL path."""
    if "://" in url_or_path:
        parts = urlsplit(url_or_path)
        return parts.path  # already excludes ?query and #fragment
    # already a path; just drop query/fragment
    return url_or_path.split("?", 1)[0].split("#", 1)[0]


def page_token(url_or_path: str, ts_ms: int) -> int:
    """Compute the `x-adc-page-token` value for a given request URL + ts."""
    return java_hashcode(_path_only(url_or_path) + str(ts_ms))


def now_ms() -> int:
    return int(time.time() * 1000)


@dataclass
class AuthContext:
    """Holds session-level secrets the MCP needs to talk to one tenant.

    Built once per tenant from env vars (`config.Settings`). `cookie` and
    `csrf_token` are mutable so the auto-relogin path can refresh them in
    place after a CAS redirect.
    """

    cookie: str
    """Raw `Cookie:` header value captured from a logged-in browser session,
    or assembled from individual cookie name=value pairs."""

    csrf_token: str | None = None
    """Value of `window.csrfToken` / `localStorage.csrfTokens[].csrfToken`.
    Required for any non-GET request."""

    src_page: str = "/portal-web/portal/homepage.html"
    """Default `x-gde-src-page` value. Override per-call if the controller
    requires a more specific page (rare in practice)."""

    target_app: str = ""
    """`x-gde-target-app` — empty for same-app calls (the common case)."""

    user_agent: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    )

    def headers_for(
        self,
        method: str,
        url_or_path: str,
        *,
        ts_ms: int | None = None,
        src_page: str | None = None,
        target_app: str | None = None,
        extra: dict[str, str] | None = None,
    ) -> dict[str, str]:
        """Build the full header set for one request."""
        if ts_ms is None:
            ts_ms = now_ms()
        token = page_token(url_or_path, ts_ms)
        headers: dict[str, str] = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": self.user_agent,
            "X-Requested-With": "XMLHttpRequest",
            "x-adc-page-timestamp": str(ts_ms),
            "x-adc-page-token": str(token),
            "x-gde-src-page": src_page or self.src_page,
            "x-gde-target-app": target_app if target_app is not None else self.target_app,
            "Cookie": self.cookie,
        }
        if method.upper() != "GET":
            if not self.csrf_token:
                raise RuntimeError(
                    "csrf_token is required for non-GET requests. "
                    "Set OWS_<TENANT>_CSRF_TOKEN or capture window.csrfToken "
                    "from a logged-in browser session."
                )
            headers["x-gde-csrf-token"] = self.csrf_token
        if extra:
            headers.update(extra)
        return headers
