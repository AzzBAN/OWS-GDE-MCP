"""Download files via /adc-file/web/rest/v1/file/download.

Lists files for each token, then downloads each one to ./tmp_attachments/.

Usage:
    uv run python scripts/download_ticket_files.py <ticket_id>
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path
from urllib.parse import quote

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings


FIELDS = ["certificate_attachment", "spv_approval"]


async def main(ticket_id: str) -> None:
    out_dir = Path("tmp_attachments") / ticket_id
    out_dir.mkdir(parents=True, exist_ok=True)

    async with OwsClient.for_surface(Tenant.PROD, Surface.RUNTIME, settings) as client:
        await client._refresh_session()

        # Refetch fresh tokens via TQL
        select_clause = ", ".join(f"t.{f}" for f in FIELDS)
        tql = (
            f'select {select_clause} from '
            f'"/centralized_inquiry_tracker/centralized_inquiry_tracker/centralize_inquiry_ticket" '
            f'as t where t.ticket_id = \'{ticket_id}\' limit 1'
        )
        body = {"tql": tql, "need_null_value": True}
        resp = await client.request(
            "POST",
            "/adc-app-ops/web/rest/v1/model-data-management/queryByTql",
            json=body,
            confirm=True,
            read_only=True,
        )
        print(f"TQL resp type: {type(resp).__name__}")
        if isinstance(resp, list):
            row = resp[0]
        elif isinstance(resp, dict):
            row = resp.get("rows", [resp])[0]
        else:
            print(f"Unexpected resp: {resp!r}"[:500])
            return

        for field in FIELDS:
            token = row.get(field)
            if not token:
                print(f"\n[{field}] EMPTY — no file uploaded")
                continue

            print(f"\n[{field}] listing files...")
            list_headers = client._auth.headers_for(
                "GET",
                "/adc-file/web/rest/v1/file/list",
                extra={"mateinfo-file-token": token},
            )
            list_resp = await client._client.request(
                "GET",
                "/adc-file/web/rest/v1/file/list",
                headers=list_headers,
            )
            print(f"  status={list_resp.status_code} body={list_resp.text[:300]}")
            files = list_resp.json().get("file_names", [])

            for f in files:
                fname = f["file_name"]
                fsize = f["file_size"]
                print(f"  -> downloading {fname} ({fsize} B)")
                dl_path = (
                    f"/adc-file/web/rest/v1/file/download?"
                    f"file_name={quote(fname)}&mateinfo_file_token={quote(token)}"
                )
                dl_headers = client._auth.headers_for("GET", dl_path)
                dl_resp = await client._client.request("GET", dl_path, headers=dl_headers)
                print(f"     status={dl_resp.status_code} ct={dl_resp.headers.get('content-type')} bytes={len(dl_resp.content)}")
                if dl_resp.status_code == 200:
                    target = out_dir / f"{field}__{fname}"
                    target.write_bytes(dl_resp.content)
                    print(f"     saved -> {target}")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
