"""Headless CAS login for auto-relogin.

When the captured session cookie expires, OWS redirects API calls (302) to
`/dspcas/login`. The client detects that, calls `login(...)` here to
re-authenticate, swaps the new cookie/CSRF into the in-memory `AuthContext`,
and retries the original request once.

Playwright is imported lazily so users who never trigger relogin don't need
the dep installed. Install with: `uv pip install -e '.[login]' && playwright
install chromium`.

Credentials come from env (`OWS_<TENANT>_USERNAME` / `_PASSWORD`) via
`Settings`. They're never logged or returned in errors.
"""

from __future__ import annotations

import contextlib

from ows_gde_mcp.config import Settings, Tenant


async def login(
    tenant: Tenant, settings: Settings, base_url: str | None = None
) -> tuple[str, str]:
    """Run a headless CAS login and return (cookie_header, csrf_token).

    The CAS server is shared across surfaces of the same tenant, so one
    login covers both Studio and Runtime. We pick whichever surface is
    configured (runtime first — it's the one that's reliably present on
    every tenant the user can reach).

    Args:
        tenant: which tenant to log in to.
        settings: app settings (credentials, URLs).
        base_url: optional host to drive the login against (e.g.
            ``https://ows.example.com``). When omitted, the first
            configured surface's host is used (existing behaviour).

    Raises:
        RuntimeError: if creds aren't configured, no surface is configured,
            playwright isn't installed, or the login flow fails (CAS error,
            missing CSRF token, etc.). Error messages never include the
            password.
    """
    tenant_upper = tenant.value.upper()
    username = (
        settings.OWS_TESTBED_USERNAME if tenant == Tenant.TESTBED else settings.OWS_PROD_USERNAME
    )
    password = (
        settings.OWS_TESTBED_PASSWORD if tenant == Tenant.TESTBED else settings.OWS_PROD_PASSWORD
    )
    if not username or not password:
        raise RuntimeError(
            f"OWS_{tenant_upper}_USERNAME and OWS_{tenant_upper}_PASSWORD must be set in .env "
            "to enable auto-relogin."
        )

    if base_url is None:
        surfaces = settings.configured_surfaces(tenant)
        if not surfaces:
            raise RuntimeError(
                f"Cannot run CAS login for tenant '{tenant.value}': no studio or "
                f"runtime URL is configured. Set OWS_{tenant_upper}_RUNTIME_URL or "
                f"OWS_{tenant_upper}_STUDIO_URL in .env."
            )
        base_url = settings.base_url(tenant, surfaces[0])

    try:
        from playwright.async_api import async_playwright
    except ImportError as e:
        raise RuntimeError(
            "playwright is required for auto-relogin. Install with: "
            "uv pip install -e '.[login]' && playwright install chromium"
        ) from e

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(base_url + "/")

            # CAS form: two textboxes (User Account, Password) + Log In button.
            await page.get_by_role("textbox", name="Enter the user account.").fill(username)
            await page.get_by_role("textbox", name="Enter the password.").fill(password)
            await page.get_by_role("button", name="Log In").click()

            # CAS may interrupt the redirect with a "password about to expire"
            # interstitial ("Change Later" / "Change"). The credentials are
            # already accepted at this point; we just need to defer the change
            # so the redirect chain continues. Best-effort — absent on accounts
            # whose password isn't near expiry.
            with contextlib.suppress(Exception):
                await page.get_by_role("button", name="Change Later").click(timeout=5_000)

            # Wait until the redirect chain settles on the portal homepage,
            # then wait for the SPA's bootstrap network calls to drain — some
            # session-establishment cookies are only set by post-homepage XHRs.
            await page.wait_for_url("**/portal-web/portal/homepage.html", timeout=30_000)
            # Some tenants keep long-poll connections open and networkidle
            # never fires. The sso/check self-test below catches that.
            with contextlib.suppress(Exception):
                await page.wait_for_load_state("networkidle", timeout=15_000)

            # Self-test: confirm the session is actually alive from inside the
            # browser before exporting cookies. Catches the common failure
            # where login form submission "succeeded" but OWS didn't issue a
            # working session (wrong password silently accepted, MFA prompt,
            # tenant-switch interstitial, etc.).
            sso_alive = await page.evaluate(
                """async () => {
                    try {
                        const r = await fetch('/portal/web/rest/sso/check', {
                            credentials: 'include',
                            headers: {'X-Requested-With': 'XMLHttpRequest'},
                        });
                        if (!r.ok) return {ok: false, status: r.status};
                        const body = await r.json().catch(() => null);
                        return {ok: body === true, status: r.status, body: body};
                    } catch (e) {
                        return {ok: false, error: String(e)};
                    }
                }"""
            )
            if not sso_alive.get("ok"):
                raise RuntimeError(
                    f"CAS login for {tenant.value} navigated to the homepage but "
                    f"/portal/web/rest/sso/check did not return true: {sso_alive}. "
                    "Likely causes: wrong credentials, MFA prompt, tenant-switch "
                    "interstitial, or account locked."
                )

            # Visit `/loganalysis/service/index.html` so its sticky cookie
            # (`loganalysis_sticky=...`) gets minted on this CAS session.
            # Without this, audit_artifact_usage's runtime probes 302 to
            # CAS even though the portal session works.
            with contextlib.suppress(Exception):
                await page.goto(
                    base_url + "/loganalysis/service/index.html",
                    wait_until="domcontentloaded",
                    timeout=15_000,
                )

            # Export every cookie in the context — passing a URL would filter
            # by path/domain match, dropping cookies the SPA actually relies on
            # (e.g. ones scoped to /portal-web or /adc-*). Server-side, OWS
            # picks the ones it needs from the Cookie header.
            cookies = await context.cookies()
            cookie_header = "; ".join(f"{c['name']}={c['value']}" for c in cookies)

            # `window.csrfToken` and `localStorage.csrfTokens` are populated
            # by the SPA's bootstrap JS which runs *after* wait_for_url
            # returns. Poll for up to 15s - typically lands within 1-2s.
            csrf_handle = await page.wait_for_function(
                """() => {
                    if (window.csrfToken) return window.csrfToken;
                    const raw = window.localStorage && localStorage.getItem('csrfTokens');
                    if (!raw) return null;
                    try {
                        const arr = JSON.parse(raw);
                        return (arr && arr[0] && arr[0].csrfToken) || null;
                    } catch (e) {
                        return null;
                    }
                }""",
                timeout=15_000,
            )
            csrf = await csrf_handle.json_value()
        finally:
            await browser.close()

    if not cookie_header:
        raise RuntimeError(f"CAS login for {tenant.value} returned no cookies.")
    if not csrf:
        raise RuntimeError(
            f"CAS login for {tenant.value} succeeded but no CSRF token was found "
            "(checked window.csrfToken and localStorage.csrfTokens)."
        )
    return cookie_header, csrf


async def fetch_csrf_via_browser(base_url: str) -> tuple[str, str]:
    """Open the portal headless and read `localStorage.csrfTokens[0]`.

    Returns `(csrf_token, csrf_header)`. The token is set by the SPA's
    bootstrap JS, so it is only reachable from a real browser context —
    there is no REST endpoint that mints it. Reuses any cookies the caller
    has already established by visiting the portal first.

    Raises:
        RuntimeError: if playwright isn't installed or the token never
            appears (likely the session isn't actually logged in).
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError as e:
        raise RuntimeError(
            "playwright is required to capture the CSRF token. Install with: "
            "uv pip install -e '.[login]' && playwright install chromium"
        ) from e

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context(ignore_https_errors=True)
            page = await context.new_page()
            await page.goto(base_url.rstrip("/") + "/portal-web/", timeout=45_000)
            handle = await page.wait_for_function(
                """() => {
                    const raw = window.localStorage &&
                        localStorage.getItem('csrfTokens');
                    if (!raw) return window.csrfToken
                        ? {csrfToken: window.csrfToken, headerKey: 'x-gde-csrf-token'}
                        : null;
                    try {
                        const arr = JSON.parse(raw);
                        const e = arr && arr[0];
                        return (e && e.csrfToken)
                            ? {csrfToken: e.csrfToken, headerKey: e.headerKey || 'x-gde-csrf-token'}
                            : null;
                    } catch (err) { return null; }
                }""",
                timeout=30_000,
            )
            data = await handle.json_value()
        finally:
            await browser.close()
    token = (data or {}).get("csrfToken")
    header = (data or {}).get("headerKey") or "x-gde-csrf-token"
    if not token:
        raise RuntimeError("CSRF token not found in localStorage.csrfTokens.")
    return token, header
