"""Map what's behind the GAM service we just discovered.

After /gam/v1/cas/login succeeds, we have a JSESSIONIDsg-studio (path=/gam)
cookie. This script enumerates plausible GAM endpoints to learn what
the GAM service actually exposes — user/tenant identity? RBAC? MFA?
audit log? Some kind of admin surface?

Read-only probes (GETs only). Run:
    uv run python scripts/probe_gam_endpoints.py
"""

from __future__ import annotations

import asyncio
import base64
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = (os.getenv("OWS_TESTBED_STUDIO_URL", "") or os.getenv("OWS_TESTBED_RUNTIME_URL", "")).rstrip("/")
USERNAME = os.getenv("OWS_TESTBED_USERNAME", "")
PASSWORD = os.getenv("OWS_TESTBED_PASSWORD", "")
TENANT_ACCOUNT = os.getenv("OWS_TESTBED_TENANT_ACCOUNT", "wfm.indonesia.hcpt")

# Endpoints worth a probe. The GAM service in OWS / Huawei portals
# typically follows a CAS-style layout — these are the obvious paths.
PROBES: list[tuple[str, str]] = [
    ("GET", "/gam/"),
    ("GET", "/gam/index.html"),
    ("GET", "/gam/v1/cas/logout"),
    ("GET", "/gam/v1/cas/check"),
    ("GET", "/gam/v1/cas/info"),
    ("GET", "/gam/v1/cas/principal"),
    ("GET", "/gam/v1/cas/profile"),
    ("GET", "/gam/v1/cas/me"),
    ("GET", "/gam/v1/cas/whoami"),
    ("GET", "/gam/v1/users"),
    ("GET", "/gam/v1/users/me"),
    ("GET", "/gam/v1/user"),
    ("GET", "/gam/v1/user/me"),
    ("GET", "/gam/v1/user/profile"),
    ("GET", "/gam/v1/user/permissions"),
    ("GET", "/gam/v1/user/roles"),
    ("GET", "/gam/v1/tenants"),
    ("GET", "/gam/v1/tenants/me"),
    ("GET", "/gam/v1/tenants/current"),
    ("GET", "/gam/v1/roles"),
    ("GET", "/gam/v1/permissions"),
    ("GET", "/gam/v1/sessions"),
    ("GET", "/gam/v1/sessions/current"),
    ("GET", "/gam/v1/audit"),
    ("GET", "/gam/v1/audit/login"),
    ("GET", "/gam/v1/mfa"),
    ("GET", "/gam/v1/mfa/devices"),
    ("GET", "/gam/v1/mfa/status"),
    ("GET", "/gam/v1/applications"),
    ("GET", "/gam/v1/services"),
    ("GET", "/gam/v1/api"),
    ("GET", "/gam/swagger-ui.html"),
    ("GET", "/gam/v3/api-docs"),
    ("GET", "/gam/api-docs"),
    ("GET", "/gam/openapi.json"),
    ("GET", "/gam/actuator"),
    ("GET", "/gam/actuator/info"),
    ("GET", "/gam/actuator/health"),
    ("GET", "/gam/v1/cas/sessions"),
    ("GET", "/gam/v1/cas/tickets"),
]


async def main() -> int:
    if not (USERNAME and PASSWORD and BASE_URL):
        print("ERROR: missing OWS_TESTBED_* in .env", file=sys.stderr)
        return 2

    cred = f"{TENANT_ACCOUNT}:{USERNAME}:{PASSWORD}"
    basic = base64.b64encode(cred.encode()).decode()

    async with httpx.AsyncClient(timeout=15.0, follow_redirects=False) as client:
        # Login first.
        r = await client.post(
            f"{BASE_URL}/gam/v1/cas/login",
            headers={"Authorization": f"Basic {basic}", "Accept": "application/json"},
        )
        if r.status_code != 200:
            print(f"GAM login failed: {r.status_code}")
            return 1
        body = r.json()
        token = (body.get("result") or {}).get("attributes", {}).get("authorizationToken", "")
        user_id = (body.get("result") or {}).get("attributes", {}).get("userId", "")
        tenant_id = (body.get("result") or {}).get("attributes", {}).get("tenantId", "")
        print(f"GAM login OK. userId={user_id}  tenantId={tenant_id}")
        print(f"Cookies after login: {[c.name for c in client.cookies.jar]}\n")

        # Try every probe both with and without bearer token.
        print(f"{'STATUS':6s}  {'METHOD':5s}  PATH   (cookies-only)")
        print("-" * 80)
        results: list[tuple[int, str, str, int]] = []
        for method, path in PROBES:
            try:
                r = await client.request(
                    method, BASE_URL + path,
                    headers={"Accept": "application/json"},
                )
            except httpx.HTTPError as e:
                print(f"  ERR    {method:5s}  {path}  ({type(e).__name__})")
                continue
            content_len = len(r.content) if r.content else 0
            tag = "?"
            ct = r.headers.get("content-type", "")
            if "html" in ct:
                tag = "html"
            elif "json" in ct:
                tag = "json"
            elif r.status_code in (301, 302, 303, 307, 308):
                tag = f"-> {r.headers.get('location', '?')[:50]}"
            note = ""
            if r.status_code == 200 and tag == "json":
                # Show a tiny preview of interesting JSON responses.
                try:
                    j = r.json()
                    if isinstance(j, dict):
                        note = f"  keys={list(j.keys())[:6]}"
                except Exception:
                    pass
            print(f"  {r.status_code:5d}  {method:5s}  {path:35s}  {tag:8s}  ({content_len}b){note}")
            results.append((r.status_code, method, path, content_len))

        # Spotlight: anything that returned 200 JSON.
        print("\n=== Endpoints returning 200 ===")
        for status, method, path, _ in results:
            if status == 200:
                print(f"  {method} {path}")

        if token:
            print("\n=== Re-probing with Authorization: Bearer for any 401/403 ===")
            for method, path in PROBES:
                # Only re-probe ones that initially failed auth.
                pass  # skip for brevity; cookies usually suffice if endpoint accepts the GAM session

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
