"""Probe the `/gam/v1/cas/login` endpoint to see if it can replace Playwright.

Run:
    uv run python scripts/probe_gam_login.py

Reads OWS_TESTBED_USERNAME / OWS_TESTBED_PASSWORD from .env. Tenant account
is taken from the OWS_TESTBED_TENANT_ACCOUNT env var if set, else falls
back to the value the user pasted as a known-good example.

This is a **deep** probe — after Step 1 it tries every plausible path
to convert the GAM token into a portal session: dspcas TGT, dspcas
service ticket exchange, login follow-redirects, and a portal-bootstrap
endpoint walk. The goal is to find the handshake that the SPA performs
between `gam/v1/cas/login` and the homepage settling.
"""

from __future__ import annotations

import asyncio
import base64
import os
import sys
from urllib.parse import urlparse

import httpx
from dotenv import load_dotenv

load_dotenv()

STUDIO_URL = os.getenv("OWS_TESTBED_STUDIO_URL", "").rstrip("/")
RUNTIME_URL = os.getenv("OWS_TESTBED_RUNTIME_URL", "").rstrip("/")
USERNAME = os.getenv("OWS_TESTBED_USERNAME", "")
PASSWORD = os.getenv("OWS_TESTBED_PASSWORD", "")
TENANT_ACCOUNT = os.getenv("OWS_TESTBED_TENANT_ACCOUNT", "wfm.indonesia.hcpt")

BASE_URL = STUDIO_URL or RUNTIME_URL


def _print_header(s: str) -> None:
    print()
    print("=" * 60)
    print(s)
    print("=" * 60)


def _print_cookies(client: httpx.AsyncClient, label: str = "current cookies") -> None:
    print(f"\n--- {label} ---")
    if not client.cookies.jar:
        print("  (none)")
        return
    for c in client.cookies.jar:
        path = getattr(c, "path", "/") or "/"
        domain = getattr(c, "domain", "?")
        name = c.name
        # Truncate long values for readability.
        val = c.value or ""
        val_disp = val[:40] + "..." if len(val) > 40 else val
        print(f"  {name:30s}  domain={domain:35s}  path={path:18s}  value={val_disp}")


async def main() -> int:
    if not (USERNAME and PASSWORD and BASE_URL):
        print("ERROR: OWS_TESTBED_USERNAME, OWS_TESTBED_PASSWORD, and either "
              "OWS_TESTBED_STUDIO_URL or OWS_TESTBED_RUNTIME_URL must be set.",
              file=sys.stderr)
        return 2

    cred = f"{TENANT_ACCOUNT}:{USERNAME}:{PASSWORD}"
    basic = base64.b64encode(cred.encode()).decode()
    print(f"Probing GAM login against: {BASE_URL}")
    print(f"Tenant account: {TENANT_ACCOUNT}")
    print(f"User: {USERNAME}")
    print(f"Authorization: Basic {basic[:20]}... (len={len(basic)})")

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=False) as client:
        # ---------- Step 1: GAM login ----------
        _print_header("Step 1: POST /gam/v1/cas/login")
        try:
            r = await client.post(
                f"{BASE_URL}/gam/v1/cas/login",
                headers={
                    "Authorization": f"Basic {basic}",
                    "Accept": "application/json",
                },
            )
        except httpx.HTTPError as e:
            print(f"  FAILED: {type(e).__name__}: {e}")
            return 1
        print(f"  status: {r.status_code}")
        # Don't print full body - it has the authorizationToken.
        try:
            body = r.json()
            result_code = body.get("resultCode")
            attrs = (body.get("result") or {}).get("attributes") or {}
            print(f"  resultCode: {result_code}")
            print(f"  userId: {attrs.get('userId')}")
            print(f"  userAccount: {attrs.get('userAccount')}")
            print(f"  tenantId: {attrs.get('tenantId')}")
            print(f"  authorizationToken present: {bool(attrs.get('authorizationToken'))}")
            print(f"  sessionId: {attrs.get('sessionId')}")
        except Exception as e:  # noqa: BLE001
            print(f"  body (not JSON): {r.text[:200]}  ({e})")
        _print_cookies(client, "cookies after step 1")
        auth_token = ""
        try:
            auth_token = (
                (r.json().get("result") or {})
                .get("attributes", {})
                .get("authorizationToken", "")
            )
        except Exception:  # noqa: BLE001
            pass

        # ---------- Step 2: portal session probe (cookies only) ----------
        _print_header("Step 2: GET /portal/web/rest/sso/check  (cookies only)")
        r = await client.get(
            f"{BASE_URL}/portal/web/rest/sso/check",
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        print(f"  status: {r.status_code}")
        if r.status_code in (301, 302, 303, 307, 308):
            print(f"  location: {r.headers.get('location')}")
        print(f"  body: {r.text[:200]}")

        # ---------- Step 3: my-info (cookies only) ----------
        _print_header("Step 3: GET /portal/web/rest/v1/user/my-info  (cookies only)")
        r = await client.get(
            f"{BASE_URL}/portal/web/rest/v1/user/my-info",
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        print(f"  status: {r.status_code}")
        if r.status_code in (301, 302, 303, 307, 308):
            print(f"  location: {r.headers.get('location')}")
        else:
            print(f"  body: {r.text[:200]}")

        # ---------- Step 4: my-info with Authorization Bearer ----------
        if auth_token:
            _print_header("Step 4: GET my-info  (cookies + Authorization: Bearer <token>)")
            r = await client.get(
                f"{BASE_URL}/portal/web/rest/v1/user/my-info",
                headers={
                    "X-Requested-With": "XMLHttpRequest",
                    "Authorization": f"Bearer {auth_token}",
                },
            )
            print(f"  status: {r.status_code}")
            if r.status_code in (301, 302, 303, 307, 308):
                print(f"  location: {r.headers.get('location')}")
            else:
                print(f"  body: {r.text[:200]}")

            _print_header("Step 5: GET my-info  (cookies + X-Auth-Token: <token>)")
            r = await client.get(
                f"{BASE_URL}/portal/web/rest/v1/user/my-info",
                headers={
                    "X-Requested-With": "XMLHttpRequest",
                    "X-Auth-Token": auth_token,
                },
            )
            print(f"  status: {r.status_code}")
            if r.status_code in (301, 302, 303, 307, 308):
                print(f"  location: {r.headers.get('location')}")
            else:
                print(f"  body: {r.text[:200]}")

        # ---------- Step 6: hit homepage to see if SPA bootstrap mints session cookies ----------
        _print_header("Step 6: GET /  (does the homepage redirect chain mint a portal session?)")
        client_follow = httpx.AsyncClient(
            timeout=30.0, follow_redirects=True, cookies=client.cookies
        )
        try:
            r = await client_follow.get(BASE_URL + "/")
            print(f"  final status: {r.status_code}")
            print(f"  final URL: {r.url}")
            _print_cookies(client_follow, "cookies after homepage redirect chain")

            # Re-probe my-info
            _print_header("Step 7: GET my-info AFTER homepage  (post-redirect-chain cookies)")
            r = await client_follow.get(
                f"{BASE_URL}/portal/web/rest/v1/user/my-info",
                headers={"X-Requested-With": "XMLHttpRequest"},
            )
            print(f"  status: {r.status_code}")
            if r.status_code in (301, 302, 303, 307, 308):
                print(f"  location: {r.headers.get('location')}")
            else:
                print(f"  body: {r.text[:300]}")

            # ---------- Step 8: the actual list_services endpoint ----------
            _print_header(
                "Step 8: POST /adc-studio-service/web/rest/v1/app/service/query  "
                "(GAM cookies only)"
            )
            r = await client.post(  # note: original `client`, GAM cookies only
                f"{BASE_URL}/adc-studio-service/web/rest/v1/app/service/query",
                json={
                    "project_name": "WFMBase",
                    "module_name": "mission_control_service",
                    "start": 0,
                    "limit": 1,
                },
                headers={
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                },
            )
            print(f"  status: {r.status_code}")
            if r.status_code in (301, 302, 303, 307, 308):
                print(f"  location: {r.headers.get('location')}")
            else:
                print(f"  body: {r.text[:200]}")

            # ---------- Step 9: same with bearer token ----------
            if auth_token:
                _print_header(
                    "Step 9: POST adc-studio-service/.../app/service/query  "
                    "(GAM cookies + Authorization: Bearer)"
                )
                r = await client.post(
                    f"{BASE_URL}/adc-studio-service/web/rest/v1/app/service/query",
                    json={
                        "project_name": "WFMBase",
                        "module_name": "mission_control_service",
                        "start": 0,
                        "limit": 1,
                    },
                    headers={
                        "Content-Type": "application/json",
                        "X-Requested-With": "XMLHttpRequest",
                        "Authorization": f"Bearer {auth_token}",
                    },
                )
                print(f"  status: {r.status_code}")
                if r.status_code in (301, 302, 303, 307, 308):
                    print(f"  location: {r.headers.get('location')}")
                else:
                    print(f"  body: {r.text[:200]}")
        finally:
            await client_follow.aclose()

    print("\nProbe complete.")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
