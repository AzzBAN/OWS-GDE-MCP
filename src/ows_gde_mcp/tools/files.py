"""MCP tools for OWS file attachments.

Some OWS data models store file uploads (images, PDFs, supervisor approvals)
behind a `mateinfo-file-token` value — typically a long base64 blob ending
in `@@@<hex_signature>`. The actual file bytes live behind a separate
`/adc-file/web/rest/v1/file/*` API on the **runtime** surface, NOT the
`/adc-model/...` paths you might guess from the data model side.

Two endpoints discovered (verified 2026-05-27 against prod
`1057-sg.teleows.com` for ticket `CIT-20260525-00000149`):

| Endpoint | Method | Auth | Purpose |
|---|---|---|---|
| `/adc-file/web/rest/v1/file/list` | GET | header `mateinfo-file-token: <token>` | enumerate files for a token |
| `/adc-file/web/rest/v1/file/download?file_name=<name>&mateinfo_file_token=<token>` | GET | standard CAS cookie | fetch one file's bytes |

Tokens are short-lived. If `list_file_attachments` returns a `File token
timed out!` error, re-fetch the token from its source model row (e.g. via
`query_model_data`) and retry.

Typical workflow:

    >>> # 1. Get fresh token from the model row
    >>> rows = query_model_data(
    ...     tenant="prod",
    ...     tql='select t.certificate_attachment from "..." as t where t.ticket_id = ...'
    ... )
    >>> token = rows["rows"][0]["certificate_attachment"]
    >>> # 2. List files for that token
    >>> files = list_file_attachments(tenant="prod", token=token)
    >>> # 3. Download one
    >>> download_file_attachment(tenant="prod", token=token,
    ...                          file_name=files["file_names"][0]["file_name"])
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings


_LIST_PATH = "/adc-file/web/rest/v1/file/list"
_DOWNLOAD_PATH = "/adc-file/web/rest/v1/file/download"
_DEFAULT_SAVE_DIR = "tmp_attachments"


async def list_file_attachments(
    tenant: str,
    token: str,
) -> dict[str, Any]:
    """List the files attached to a `mateinfo-file-token`.

    Calls `GET /adc-file/web/rest/v1/file/list` with the token in the
    `mateinfo-file-token` request header (NOT a query param — the server
    returns 400 if you pass it as a param).

    Args:
        tenant: "prod" or "testbed". Routes through the runtime surface.
        token: the `mateinfo-file-token` value, typically read from a model
            field like `certificate_attachment` or `spv_approval`. Tokens
            are short-lived; re-fetch from the source row if expired.

    Returns:
        On success:
            ```
            {
                "file_names": [
                    {"file_name": "Netcare.jpg", "file_size": 199180},
                    ...
                ]
            }
            ```
        On error (expired token, bad token, etc):
            `{"error": {"status", "body"}}`
    """
    t = Tenant(tenant)
    async with OwsClient.for_surface(t, Surface.RUNTIME, settings) as client:
        # Fresh session before hitting the file API — avoids 302→CAS races.
        await client._refresh_session()

        headers = client._auth.headers_for(
            "GET",
            _LIST_PATH,
            extra={"mateinfo-file-token": token},
        )
        try:
            resp = await client._client.request("GET", _LIST_PATH, headers=headers)
        except httpx.HTTPError as e:
            return {"error": {"status": 0, "body": f"{type(e).__name__}: {e}"}}

        if resp.status_code != 200:
            return {
                "error": {
                    "status": resp.status_code,
                    "body": resp.text[:500],
                }
            }
        try:
            return resp.json()
        except ValueError:
            return {"error": {"status": resp.status_code, "body": resp.text[:500]}}


async def download_file_attachment(
    tenant: str,
    token: str,
    file_name: str,
    *,
    save_dir: str = _DEFAULT_SAVE_DIR,
    save_as: str | None = None,
) -> dict[str, Any]:
    """Download one file by `file_name` + `mateinfo-file-token` and save to disk.

    Calls `GET /adc-file/web/rest/v1/file/download?file_name=<name>
    &mateinfo_file_token=<token>` on the runtime surface. Both values are
    URL-encoded automatically. The response is binary regardless of the
    file's actual MIME type — the server reports `content-type:
    application/x-www-form-urlencoded` for everything.

    The file is written to `<save_dir>/<save_as or file_name>`. The save
    directory is created if it doesn't exist. Returns metadata about the
    saved file rather than the bytes themselves to keep MCP responses
    compact — use the returned `saved_path` to read the file with the Read
    tool if you need to inspect contents.

    Args:
        tenant: "prod" or "testbed".
        token: the same `mateinfo-file-token` used to list. Must be fresh.
        file_name: exact name from `list_file_attachments` (e.g.
            "Netcare.jpg"). Spaces and unicode are handled.
        save_dir: directory to write into. Created if missing. Defaults to
            `tmp_attachments/` in the current working directory.
        save_as: optional override for the saved filename. Useful when
            disambiguating files from multiple tokens (e.g.
            `"certificate_attachment__Netcare.jpg"`). Defaults to
            `file_name`.

    Returns:
        On success:
            ```
            {
                "file_name": "Netcare.jpg",
                "saved_path": "tmp_attachments/Netcare.jpg",
                "bytes": 199180,
                "content_type": "application/x-www-form-urlencoded"
            }
            ```
        On error:
            `{"error": {"status", "body"}}`
    """
    t = Tenant(tenant)
    out_dir = Path(save_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / (save_as or file_name)

    dl_path = (
        f"{_DOWNLOAD_PATH}?file_name={quote(file_name)}"
        f"&mateinfo_file_token={quote(token)}"
    )

    async with OwsClient.for_surface(t, Surface.RUNTIME, settings) as client:
        await client._refresh_session()
        headers = client._auth.headers_for("GET", dl_path)
        try:
            resp = await client._client.request("GET", dl_path, headers=headers)
        except httpx.HTTPError as e:
            return {"error": {"status": 0, "body": f"{type(e).__name__}: {e}"}}

        if resp.status_code != 200:
            return {
                "error": {
                    "status": resp.status_code,
                    "body": resp.text[:500],
                }
            }

        target.write_bytes(resp.content)
        return {
            "file_name": file_name,
            "saved_path": str(target),
            "bytes": len(resp.content),
            "content_type": resp.headers.get("content-type", ""),
        }


__all__ = ["list_file_attachments", "download_file_attachment"]
