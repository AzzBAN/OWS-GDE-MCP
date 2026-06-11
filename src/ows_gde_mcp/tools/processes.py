"""BPM process-catalog tools.

The OWS BPM admin endpoint that lists every process in a tenant doesn't
expose a clean list-shape (`/adc-studio-bpm/web/rest/process-definition/instances`
returns 500 without a fully-qualified by-id path). The OrderQuery app
ships a service `oq_process_definition_getList` that wraps the same
metadata behind a stable contract, so we route through that.

Tools:
    list_processes — fetch the catalog (live or cached). 365 rows on the
        observed testbed; ships in a single page with a lenient `limit`.
    get_process — by (project, module, process_key); falls back to the
        Studio by-id endpoint to get fields the catalog service drops
        (creator, create_time, etc.).
    resolve_process_by_prefix — given a ticket prefix (INC, BOT, CIT,
        TTS, ...), return its (project, module, process_key, data_model_name).
        Reads the local cache; offers to refresh if missing.
    refresh_process_cache — re-fetch and persist the catalog to
        ~/.cache/ows-gde-mcp/processes-<tenant>.json.

Cache location follows the same OWS_CACHE_DIR convention as the CSRF
disk cache; mode 0o600 since process metadata is moderately sensitive
(reveals the full app surface of the tenant).
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

from ows_gde_mcp.tools.live import _runtime_post, _studio_get

_DEFAULT_CACHE_DIR = Path(
    os.environ.get("OWS_CACHE_DIR") or (Path.home() / ".cache" / "ows-gde-mcp")
)
_CACHE_TTL_SECONDS = 24 * 60 * 60

# The OrderQuery service is registered on the runtime surface — same
# mount real page scripts hit via `MessageProcessor.process({serviceId: ...})`.
# Studio's `/adc-studio-service/.../service/test/...` endpoint requires
# OWS_PROD_STUDIO_URL which not every tenant has configured. Note the
# `/web/` segment — `/adc-service/rest/...` (without /web) is rejected
# by the runtime gateway.
_LIST_SERVICE_PATH = (
    "/adc-service/web/rest/v1/services/"
    "OrderQuery/OrderQuery/oq_process_definition_getList"
)
_BY_ID_PATH = "/adc-studio-bpm/web/rest/process-definition/instances/{project}/{module}/{key}"


def _cache_path(tenant: str) -> Path:
    return _DEFAULT_CACHE_DIR / f"processes-{tenant}.json"


def _read_disk_cache(tenant: str) -> dict[str, Any] | None:
    path = _cache_path(tenant)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or "fetched_at" not in data:
        return None
    if time.time() - data["fetched_at"] > _CACHE_TTL_SECONDS:
        return None
    return data


def _write_disk_cache(tenant: str, processes: list[dict[str, Any]]) -> None:
    path = _cache_path(tenant)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"fetched_at": time.time(), "tenant": tenant, "processes": processes}
        path.write_text(json.dumps(payload))
        os.chmod(path, 0o600)
    except OSError:
        pass


async def _fetch_live_catalog(tenant: str) -> list[dict[str, Any]]:
    # The OrderQuery service-test endpoint returns the process catalog.
    # Bypass `invoke_service` (which gates POSTs as potential writes)
    # because we know this exact service is a read-only getter — same
    # rationale as the `read_only=True` exemption used by query_model_data.
    out = await _runtime_post(
        tenant,
        _LIST_SERVICE_PATH,
        json={"start": 0, "limit": 5000},
        confirm=True,
        read_only=True,
    )
    if not isinstance(out, dict):
        raise RuntimeError(
            f"oq_process_definition_getList returned unexpected type: {type(out).__name__}"
        )
    # Two known shapes:
    # - Studio service-test mount wraps result under `result.debug_output.results`.
    # - Runtime service mount returns `{start, limit, results: [...]}` directly.
    rows = out.get("results")
    if not isinstance(rows, list):
        rows = (
            out.get("result", {}).get("debug_output", {}).get("results")
        )
    if not isinstance(rows, list):
        raise RuntimeError(
            "oq_process_definition_getList returned unexpected shape: "
            f"keys={list(out.keys())}"
        )
    return rows


async def list_processes(
    tenant: str,
    *,
    abbreviation: str = "",
    project_name: str = "",
    module_name: str = "",
    active_only: bool = True,
    refresh: bool = False,
    limit: int = 0,
) -> dict[str, Any]:
    """List BPM processes registered in the tenant.

    Reads from the local cache if fresh (24 h TTL); otherwise fetches
    via the `OrderQuery/OrderQuery/oq_process_definition_getList`
    service. Pass `refresh=True` to force a re-fetch.

    Each process row shape:
        - `abbreviation` — ticket prefix (INC, BOT, CIT, TTS, ...)
        - `app_name` / `module_name` / `name` — locate the process
          (`name` is the `process_key` used by `get_process`)
        - `data_model_name` — the model that holds tickets of this
          process (e.g. `tt_troubleticket` for INC)
        - `display_name`, `workflow_type`, `publish_api`, `auto_process`,
          `active`, `legacy`, `version`, `process_uri`, `sync_data`

    Args:
        tenant: "prod" or "testbed".
        abbreviation: filter by ticket prefix (case-insensitive,
            substring). Empty = all.
        project_name / module_name: filter by location. Empty = all.
        active_only: when True (default), drop rows where `active=false`.
        refresh: bypass the cache and re-fetch live.
        limit: cap the returned rows. 0 = no cap.

    Returns:
        `{"total", "matched", "fetched_at", "from_cache", "processes": [...]}`
    """
    cache = None if refresh else _read_disk_cache(tenant)
    if cache:
        rows = cache["processes"]
        fetched_at = cache["fetched_at"]
        from_cache = True
    else:
        rows = await _fetch_live_catalog(tenant)
        _write_disk_cache(tenant, rows)
        fetched_at = time.time()
        from_cache = False

    matched = rows
    if active_only:
        matched = [r for r in matched if r.get("active")]
    if abbreviation:
        a = abbreviation.lower()
        matched = [r for r in matched if a in (r.get("abbreviation") or "").lower()]
    if project_name:
        matched = [r for r in matched if r.get("app_name") == project_name]
    if module_name:
        matched = [r for r in matched if r.get("module_name") == module_name]
    if limit > 0:
        matched = matched[:limit]

    return {
        "total": len(rows),
        "matched": len(matched),
        "fetched_at": fetched_at,
        "from_cache": from_cache,
        "processes": matched,
    }


async def get_process(
    tenant: str,
    project_name: str,
    module_name: str,
    process_key: str,
) -> dict[str, Any]:
    """Get one BPM process definition by (project, module, process_key).

    Calls the Studio by-id endpoint
    `GET /adc-studio-bpm/web/rest/process-definition/instances/<p>/<m>/<key>`,
    which returns richer metadata than the catalog service (creator,
    create_time, update_time, manifest_version, open_level, come_from,
    page_customizable, ...).

    `process_key` is the `name` field from `list_processes` rows.
    """
    path = _BY_ID_PATH.format(project=project_name, module=module_name, key=process_key)
    return await _studio_get(tenant, path)


async def resolve_process_by_prefix(
    tenant: str,
    prefix: str,
    *,
    refresh: bool = False,
) -> dict[str, Any]:
    """Map a ticket prefix (INC / BOT / CIT / TTS / ...) to its process.

    Resolves the strongest match: exact `abbreviation` equality, with
    `active=true` rows preferred over inactive ones. Reads the local
    cache (24 h TTL) by default.

    Returns the same row shape as `list_processes` plus a `tickets_uri`
    field — the canonical asset URI for the data model that holds
    tickets of this process (the form `query_model_data` accepts).

    On no match: `{"error": {"code": "no_match", "prefix"}}`.
    """
    out = await list_processes(tenant, abbreviation=prefix, active_only=False, refresh=refresh)
    rows = [r for r in out["processes"] if (r.get("abbreviation") or "").upper() == prefix.upper()]
    if not rows:
        return {"error": {"code": "no_match", "prefix": prefix, "hint": "Run with refresh=True if the prefix was added recently."}}
    rows.sort(key=lambda r: (not r.get("active"), bool(r.get("legacy"))))
    pick = rows[0]
    model = pick.get("data_model_name") or ""
    tickets_uri = (
        f"/{pick['app_name']}/{pick['module_name']}/{model}" if model else None
    )
    return {
        **pick,
        "tickets_uri": tickets_uri,
        "alternates": rows[1:] if len(rows) > 1 else [],
    }


async def refresh_process_cache(tenant: str) -> dict[str, Any]:
    """Force a re-fetch of the BPM process catalog and persist to disk.

    Bypasses TTL. Returns `{"total", "fetched_at", "cache_path"}`.
    """
    rows = await _fetch_live_catalog(tenant)
    _write_disk_cache(tenant, rows)
    return {
        "total": len(rows),
        "fetched_at": time.time(),
        "cache_path": str(_cache_path(tenant)),
    }


__all__ = [
    "get_process",
    "list_processes",
    "refresh_process_cache",
    "resolve_process_by_prefix",
]
