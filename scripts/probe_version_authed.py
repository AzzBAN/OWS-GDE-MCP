"""Probe OWS for its version using our authenticated client.

Goes through OwsClient (auto-relogin via Playwright if needed) so the
probe lands on the real APIs instead of the dspcas redirect wall.
"""

from __future__ import annotations

import asyncio
import json
import sys

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings


async def main() -> int:
    async with OwsClient.for_surface(Tenant.TESTBED, Surface.STUDIO, settings) as c:
        for path in [
            "/portal/web/rest/v1/uiconfig/info",
            "/portal/web/rest/v1/sys-config/get-cookie-config",
            "/portal/web/rest/v1/refreshsession/url",
            "/portal/web/rest/v1/banner/getGrantedToolbar",
            "/portal/web/rest/v1/notice/notices/newest?topN=1",
            "/portal/web/rest/v1/user/my-info",
        ]:
            try:
                r = await c.get(path)
                preview = json.dumps(r, default=str)[:400] if not isinstance(r, str) else r[:400]
                print(f"OK    {path}\n        {preview}\n")
            except Exception as e:  # noqa: BLE001
                print(f"FAIL  {path}: {type(e).__name__}: {e}\n")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
