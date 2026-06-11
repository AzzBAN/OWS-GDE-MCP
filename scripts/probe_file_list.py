"""One-off probe: list files for a `mateinfo-file-token`.

Hits the file API directly via httpx so we see raw bytes / content-type.

Usage:
    uv run python scripts/probe_file_list.py <token>
"""

from __future__ import annotations

import asyncio
import sys

import httpx

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings


async def main(token: str) -> None:
    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, settings) as client:
        await client._refresh_session()
        for path in [
            "/adc-file/web/rest/v1/file/list",
            "/adc-file/web/rest/v1/file/getFileList",
            "/adc-file/web/rest/v1/file/query",
            "/adc-file/web/rest/v1/file/info",
        ]:
            print(f"\n=== GET {path} ===", flush=True)
            headers = client._auth.headers_for("GET", path, extra={"mateinfo-file-token": token})
            try:
                resp = await client._client.request("GET", path, headers=headers)
                print(f"  status: {resp.status_code}", flush=True)
                print(f"  content-type: {resp.headers.get('content-type')}", flush=True)
                print(f"  bytes: {len(resp.content)}", flush=True)
                ct = resp.headers.get("content-type", "")
                if "json" in ct or "text" in ct:
                    print(f"  body: {resp.text[:2000]}", flush=True)
                else:
                    print(f"  binary head (hex): {resp.content[:32].hex()}", flush=True)
            except httpx.HTTPError as e:
                print(f"  ERROR: {e}", flush=True)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
