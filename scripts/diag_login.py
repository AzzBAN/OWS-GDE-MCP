"""Diagnostic: run the testbed CAS login HEADED and report where it lands.

Tests the hypothesis that the MCP's headless login hangs because CAS
blocks/stalls headless browsers. Reads creds from .env directly so no
secret is ever printed or passed as an argument.

Run: uv run python scripts/diag_login.py
"""

from __future__ import annotations
import asyncio, os, sys
from dotenv import load_dotenv

load_dotenv()
U = os.getenv("OWS_TESTBED_USERNAME", "")
P = os.getenv("OWS_TESTBED_PASSWORD", "")
BASE = (os.getenv("OWS_TESTBED_STUDIO_URL", "") or os.getenv("OWS_TESTBED_RUNTIME_URL", "")).rstrip("/")


async def attempt(headless: bool) -> dict:
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        try:
            page = await (await browser.new_context()).new_page()
            await page.goto(BASE + "/")
            await page.get_by_role("textbox", name="Enter the user account.").fill(U)
            await page.get_by_role("textbox", name="Enter the password.").fill(P)
            await page.get_by_role("button", name="Log In").click()
            # Dismiss the "password about to expire" interstitial if present.
            try:
                await page.get_by_role("button", name="Change Later").click(timeout=5_000)
            except Exception:
                pass
            try:
                await page.wait_for_url("**/portal-web/portal/homepage.html", timeout=15_000)
                reached = True
            except Exception:
                reached = False
            await page.wait_for_timeout(1500)
            body = await page.evaluate("() => document.body ? document.body.innerText : ''")
            return {"headless": headless, "reached_homepage": reached,
                    "final_url": page.url, "body_preview": body[:500]}
        finally:
            await browser.close()


async def main() -> int:
    if not (U and P and BASE):
        print("ERROR: missing OWS_TESTBED_* in .env", file=sys.stderr); return 2
    mode = sys.argv[1] if len(sys.argv) > 1 else "headed"
    res = await attempt(headless=(mode == "headless"))
    print(f"\n=== {mode.upper()} RESULT ===")
    print(f"reached_homepage: {res['reached_homepage']}")
    print(f"final_url: {res['final_url']}")
    print(f"body_preview:\n{res['body_preview']}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
