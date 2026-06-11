"""Observe what Playwright does during a CAS login — trace every request.

Run:
    uv run python scripts/trace_playwright_login.py

Logs every URL the browser hits between fetching the homepage and
finishing the SPA bootstrap, plus which cookies get set on which
domain/path. The goal is to find the exact request that converts a
GAM session into a portal `dspcas` session, so we can replicate it
in pure HTTP.
"""

from __future__ import annotations

import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("OWS_TESTBED_USERNAME", "")
PASSWORD = os.getenv("OWS_TESTBED_PASSWORD", "")
BASE_URL = (
    os.getenv("OWS_TESTBED_STUDIO_URL", "")
    or os.getenv("OWS_TESTBED_RUNTIME_URL", "")
).rstrip("/")


async def main() -> int:
    if not (USERNAME and PASSWORD and BASE_URL):
        print("ERROR: missing OWS_TESTBED_* in .env", file=sys.stderr)
        return 2

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: pip install playwright && playwright install chromium")
        return 2

    print(f"Tracing login flow against: {BASE_URL}")
    requests: list[dict] = []
    responses: list[dict] = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context()
            page = await context.new_page()

            def on_request(req):
                # Filter out static assets so the trace is readable.
                url = req.url
                if any(url.endswith(ext) for ext in (".css", ".js", ".png", ".svg", ".woff2", ".woff", ".ico", ".jpg")):
                    return
                requests.append({"method": req.method, "url": url, "post_data": req.post_data})

            def on_response(resp):
                url = resp.url
                if any(url.endswith(ext) for ext in (".css", ".js", ".png", ".svg", ".woff2", ".woff", ".ico", ".jpg")):
                    return
                responses.append(
                    {
                        "status": resp.status,
                        "url": url,
                        "set_cookie": resp.headers.get("set-cookie"),
                    }
                )

            page.on("request", on_request)
            page.on("response", on_response)

            await page.goto(BASE_URL + "/")
            await page.get_by_role("textbox", name="Enter the user account.").fill(USERNAME)
            await page.get_by_role("textbox", name="Enter the password.").fill(PASSWORD)
            await page.get_by_role("button", name="Log In").click()
            await page.wait_for_url("**/portal-web/portal/homepage.html", timeout=30_000)
            try:
                await page.wait_for_load_state("networkidle", timeout=15_000)
            except Exception:
                pass

            cookies = await context.cookies()
        finally:
            await browser.close()

    # --- Print the trace ---
    print(f"\n{len(requests)} non-asset requests:\n")
    for r in requests:
        method, url = r["method"], r["url"]
        post_preview = ""
        if r["post_data"]:
            pd = r["post_data"]
            post_preview = f"  body={pd[:80]}{'...' if len(pd) > 80 else ''}"
        print(f"  {method:5s} {url}{post_preview}")

    print(f"\n{len([r for r in responses if r['set_cookie']])} responses set cookies:\n")
    for r in responses:
        if not r["set_cookie"]:
            continue
        sc = r["set_cookie"]
        # Print only the cookie names (not values) for safety.
        names = [c.split("=", 1)[0].strip() for c in sc.split("\n")]
        print(f"  {r['status']} {r['url']}")
        for n in names:
            print(f"      Set-Cookie: {n}")

    print(f"\nFinal cookie names by domain/path:")
    seen = {}
    for c in cookies:
        key = (c.get("domain"), c.get("path"))
        seen.setdefault(key, []).append(c.get("name"))
    for (domain, path), names in sorted(seen.items()):
        print(f"  domain={domain}  path={path}")
        for n in sorted(names):
            print(f"      {n}")

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
