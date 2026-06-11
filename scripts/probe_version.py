"""Probe OWS for version / build info.

Tries the standard places:
- /portal/web/rest/v1/uiconfig/info  (the SPA fetches this on bootstrap)
- /actuator/info under various surfaces
- HTML page meta tags
- known asset paths with version stamps in their query strings
"""

from __future__ import annotations

import asyncio
import os
import re
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = (
    os.getenv("OWS_TESTBED_STUDIO_URL", "")
    or os.getenv("OWS_TESTBED_RUNTIME_URL", "")
).rstrip("/")
COOKIE = os.getenv("OWS_TESTBED_SESSION_COOKIE", "")

PROBES = [
    "/portal/web/rest/v1/uiconfig/info",
    "/portal/web/rest/v1/version",
    "/portal/web/rest/v1/info",
    "/portal/web/rest/v1/about",
    "/portal/web/rest/v1/system/info",
    "/portal/web/rest/v1/sys-config/version",
    "/portal/web/rest/v1/sys-config/get-cookie-config",
    "/portal/web/rest/v1/manifest",
    "/portal/web/manifest.json",
    "/portal-web/manifest.json",
    "/portal-web/version.json",
    "/portal-web/build.json",
    "/adc-web/manifest.json",
    "/adc-web/version.json",
    "/adc-web/ui/manifest.json",
    "/adc-web/ui/version.json",
    "/adc-studio-project-mgt/web/rest/v1/version",
    "/adc-studio-service/web/rest/v1/version",
]


async def main() -> int:
    if not BASE_URL:
        print("ERROR: set OWS_TESTBED_STUDIO_URL or OWS_TESTBED_RUNTIME_URL", file=sys.stderr)
        return 2

    async with httpx.AsyncClient(timeout=15.0, follow_redirects=False) as client:
        headers: dict[str, str] = {"Accept": "application/json,text/html,*/*"}
        if COOKIE:
            headers["Cookie"] = COOKIE

        print(f"Probing {BASE_URL}\n")
        print(f"{'STATUS':6s}  PATH                                                       SUMMARY")
        print("-" * 100)
        for path in PROBES:
            try:
                r = await client.get(BASE_URL + path, headers=headers)
            except httpx.HTTPError as e:
                print(f"  ERR   {path}  ({type(e).__name__}: {e})")
                continue
            ct = r.headers.get("content-type", "")
            note = ""
            if r.status_code == 200:
                if "json" in ct:
                    try:
                        j = r.json()
                        note = str(j)[:200]
                    except Exception:
                        note = r.text[:200]
                else:
                    # Look for version-y strings in HTML.
                    text = r.text[:5000]
                    matches = re.findall(
                        r'(?:version|build)["\s:=]+([0-9]+\.[0-9]+\.[0-9.]+(?:-[A-Za-z0-9]+)?)',
                        text,
                        flags=re.I,
                    )
                    if matches:
                        note = f"version-ish: {matches[:5]}"
                    else:
                        note = ct
            elif r.status_code in (301, 302, 303, 307, 308):
                note = f"-> {r.headers.get('location', '')[:60]}"
            else:
                note = ct
            print(f"  {r.status_code:5d}  {path:55s}  {note}")

        # Pull homepage HTML and grep for build / version stamps.
        print("\n--- Probing homepage HTML for version markers ---")
        try:
            r = await client.get(BASE_URL + "/", headers=headers, follow_redirects=True)
            text = r.text
            for pattern in [
                r'(?:appVersion|buildVersion|version)["\s:=]+["\']?([0-9][^"\'<>\s]{0,50})',
                r'(?:OWS|GDE|ADC)[\s:_-]+v?([0-9]+\.[0-9]+\.[0-9.]+)',
                r'manifest_version["\s:=]+["\']?([^"\'<>\s,]+)',
            ]:
                hits = re.findall(pattern, text, flags=re.I)
                if hits:
                    uniq = sorted(set(hits))[:8]
                    print(f"  pattern {pattern[:40]}...: {uniq}")
        except httpx.HTTPError as e:
            print(f"  homepage probe failed: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
