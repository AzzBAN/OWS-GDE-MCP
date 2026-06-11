"""Log Analysis service — runtime log search and trace correlation.

OWS exposes a `/loganalysis/service/` endpoint family that aggregates
runtime logs across every app deployed on the tenant. Filters include time
range, service identity (`app_name` / `module_name` / `element_name`),
log level, trace id, etc. Each log entry carries a `trace_id` that links
it to the rest of the call chain.

This module is *separate* from `tools/live.py` because Log Analysis uses a
different auth scheme:

- CSRF header is `X-CSRF-TOKEN` (vs `x-gde-csrf-token`).
- Token source is a JS variable embedded in
  `/loganalysis/service/index.html` (vs `localStorage.csrfTokens`).
- The standard GDE anti-tamper headers (`x-adc-page-token`, etc) are
  rejected — must be omitted.
- The `referer` must be `/loganalysis/service/index.html`.

The tools reuse the per-tenant session cookie (and the per-tenant relogin
lock) from `ows_gde_mcp.client`. Concurrency control:

- One CSRF fetch per tenant. Concurrent first-callers serialise on
  `_csrf_locks[tenant]` so we don't fire 66 parallel `index.html` GETs
  the first time `audit_artifact_usage` runs.
- One CAS relogin per tenant. Shared with `OwsClient` via
  `client.refresh_tenant_session` so an expired session triggered mid-
  audit doesn't launch 66 headless Chromium instances.
- Concurrent log probes share a single `httpx.AsyncClient` via
  `_get_client` (connection pooling).

## Retention caveat

The tenant retains logs for ~3 days. A service with zero log hits in a
3-day window may still be in active use via a longer-interval schedule,
so absence of hits is **not** proof of disuse. Tools cap windows at 3
days and surface an explicit warning so callers don't silently get empty
results from a 30-day query.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import time
from pathlib import Path
from typing import Any

import httpx

from ows_gde_mcp.client import _auth_for_tenant, refresh_tenant_session
from ows_gde_mcp.config import Surface, Tenant
from ows_gde_mcp.config import settings as _settings

_LOG_INDEX_PATH = "/loganalysis/service/index.html"
_LOG_SEARCH_PATH = "/loganalysis/service/logsearch/v3/logs/search"
_CSRF_RE = re.compile(r'token\s*:\s*"([A-F0-9]{32,})"')

# Tenant -> CSRF token. Cached per process; refreshed on demand on 403.
_csrf_cache: dict[Tenant, str] = {}

# On-disk cache for the CSRF token, shared across server restarts.
# Path is overridable via OWS_CACHE_DIR for tests / containers.
_DEFAULT_CACHE_DIR = Path(
    os.environ.get("OWS_CACHE_DIR")
    or (Path.home() / ".cache" / "ows-gde-mcp")
)
_CSRF_DISK_PATH = _DEFAULT_CACHE_DIR / "csrf.json"
# Conservative TTL — log-analysis CSRFs rotate at session boundaries, but
# the 403-retry path catches stale tokens automatically. An hour is a
# good middle ground that saves the warm-up cost on most restarts.
_CSRF_TTL_SECONDS = 60 * 60

# Per-tenant lock that serialises CSRF fetches. Without this, the first
# `audit_artifact_usage` run on a fresh process starts 66 concurrent
# probes, each finding an empty cache and racing to GET index.html.
_csrf_locks: dict[Tenant, asyncio.Lock] = {}

# Per-tenant pooled httpx.AsyncClient. Reused across log probes for
# connection pooling — without this each probe opens its own TCP/TLS
# session. Created lazily on first use; closed when the process exits.
_http_clients: dict[Tenant, httpx.AsyncClient] = {}

# Hard cap on the lookback window. The tenant's log retention is ~3 days;
# a longer window silently yields gaps so we refuse and warn the caller.
_MAX_WINDOW_MS = 3 * 24 * 60 * 60 * 1000

_RETENTION_WARNING = (
    "Tenant log retention is ~3 days. Absence of hits is NOT proof of disuse — "
    "a service called weekly via a scheduled job will appear quiet here."
)


def _csrf_lock(tenant: Tenant) -> asyncio.Lock:
    lock = _csrf_locks.get(tenant)
    if lock is None:
        lock = asyncio.Lock()
        _csrf_locks[tenant] = lock
    return lock


def _read_disk_csrf(tenant: Tenant) -> str | None:
    """Return a non-stale CSRF token from disk for `tenant`, or None.

    Disk format: `{tenant_value: {token, fetched_at_epoch_seconds}}`.
    Tokens older than `_CSRF_TTL_SECONDS` are treated as expired and
    refetched. Any read error degrades silently to None — the cache is
    a perf hint, never load-bearing.
    """
    if not _CSRF_DISK_PATH.exists():
        return None
    try:
        data = json.loads(_CSRF_DISK_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    entry = data.get(tenant.value) if isinstance(data, dict) else None
    if not isinstance(entry, dict):
        return None
    token = entry.get("token")
    fetched = entry.get("fetched_at")
    if not isinstance(token, str) or not isinstance(fetched, (int, float)):
        return None
    if time.time() - fetched > _CSRF_TTL_SECONDS:
        return None
    return token


def _write_disk_csrf(tenant: Tenant, token: str) -> None:
    """Persist the token to disk; failures are silent."""
    try:
        _CSRF_DISK_PATH.parent.mkdir(parents=True, exist_ok=True)
        data: dict[str, Any] = {}
        if _CSRF_DISK_PATH.exists():
            try:
                data = json.loads(_CSRF_DISK_PATH.read_text(encoding="utf-8")) or {}
            except (OSError, ValueError):
                data = {}
        data[tenant.value] = {"token": token, "fetched_at": time.time()}
        _CSRF_DISK_PATH.write_text(json.dumps(data), encoding="utf-8")
        # Best-effort tighten perms — token is auth-bearing.
        try:
            os.chmod(_CSRF_DISK_PATH, 0o600)
        except OSError:
            pass
    except OSError:
        pass


def _invalidate_disk_csrf(tenant: Tenant) -> None:
    """Drop the disk entry for `tenant` (e.g. on 403)."""
    if not _CSRF_DISK_PATH.exists():
        return
    try:
        data = json.loads(_CSRF_DISK_PATH.read_text(encoding="utf-8")) or {}
    except (OSError, ValueError):
        return
    if isinstance(data, dict) and tenant.value in data:
        data.pop(tenant.value, None)
        try:
            _CSRF_DISK_PATH.write_text(json.dumps(data), encoding="utf-8")
        except OSError:
            pass


def _get_client(tenant: Tenant) -> httpx.AsyncClient:
    """Return the per-tenant pooled `httpx.AsyncClient`, creating once.

    Routes through the **runtime** surface — Log Analysis is a runtime
    app (it lives at `/loganalysis/service/...` on the runtime host).
    Prod tenants typically don't expose Studio at all, so RUNTIME is the
    only viable surface either way.
    """
    client = _http_clients.get(tenant)
    if client is None or client.is_closed:
        base_url = _settings.base_url(tenant, Surface.RUNTIME)
        client = httpx.AsyncClient(
            base_url=base_url,
            timeout=30.0,
            limits=httpx.Limits(max_connections=10, max_keepalive_connections=10),
        )
        _http_clients[tenant] = client
    return client


async def _fetch_csrf_uncached(tenant: Tenant) -> str:
    """Fetch the Log Analysis CSRF from `/loganalysis/service/index.html`.

    The token is embedded in inline JavaScript:
      `var csrftoken = {header:"X-CSRF-TOKEN", param:"_csrf", token:"<HEX>"};`

    On expired-session 302→CAS, runs one auto-relogin via
    `client.refresh_tenant_session` (shared lock) and retries.
    """
    auth = _auth_for_tenant(tenant, _settings)
    client = _get_client(tenant)
    resp = await client.get(
        _LOG_INDEX_PATH,
        headers={"Cookie": auth.cookie, "User-Agent": auth.user_agent},
        follow_redirects=False,
    )
    # CAS expired-session bounce: 302 → /dspcas/login. Refresh shared and retry.
    if resp.status_code in (301, 302, 303, 307, 308):
        location = resp.headers.get("location") or resp.headers.get("Location") or ""
        if "/dspcas" in location.lower():
            await refresh_tenant_session(tenant, _settings)
            auth = _auth_for_tenant(tenant, _settings)  # refreshed in place
            resp = await client.get(
                _LOG_INDEX_PATH,
                headers={"Cookie": auth.cookie, "User-Agent": auth.user_agent},
                follow_redirects=False,
            )
    resp.raise_for_status()
    match = _CSRF_RE.search(resp.text)
    if not match:
        raise RuntimeError(
            "Could not extract X-CSRF-TOKEN from /loganalysis/service/index.html. "
            "The page layout may have changed."
        )
    return match.group(1)


async def _csrf_for(tenant: Tenant) -> str:
    """Return cached CSRF, fetching once even under concurrent first-callers.

    Three-layer cache:
    1. In-memory (`_csrf_cache`) — process-local, dict access.
    2. On-disk (`~/.cache/ows-gde-mcp/csrf.json`) — survives restarts.
    3. Network — fetch from `/loganalysis/service/index.html`.

    The disk cache shaves the ~1 s startup probe off restart time. Tokens
    older than `_CSRF_TTL_SECONDS` are treated as expired; the 403 retry
    path in `_post` invalidates the disk entry too so a poisoned token
    can't survive a restart.

    The lock matters because `audit_artifact_usage` fans out N probes via
    `asyncio.gather`. Without the lock, all N find an empty cache and each
    issues its own index.html GET (and, on a 302, its own Playwright
    relogin). With the lock, exactly one fetches; the rest read the cache.
    """
    cached = _csrf_cache.get(tenant)
    if cached is not None:
        return cached
    async with _csrf_lock(tenant):
        cached = _csrf_cache.get(tenant)  # double-checked under lock
        if cached is not None:
            return cached
        from_disk = _read_disk_csrf(tenant)
        if from_disk is not None:
            _csrf_cache[tenant] = from_disk
            return from_disk
        token = await _fetch_csrf_uncached(tenant)
        _csrf_cache[tenant] = token
        _write_disk_csrf(tenant, token)
        return token


async def _post(tenant: str, path: str, body: dict[str, Any]) -> dict[str, Any]:
    """POST against the Log Analysis service with the right header set.

    Auto-retries once on 403 by refreshing the CSRF cache (the page
    rotates the token at session boundaries).
    """
    t = Tenant(tenant)
    auth = _auth_for_tenant(t, _settings)
    base_url = _settings.base_url(t, Surface.RUNTIME)
    client = _get_client(t)

    async def _do(csrf: str) -> httpx.Response:
        return await client.post(
            path,
            json=body,
            headers={
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Cookie": auth.cookie,
                "User-Agent": auth.user_agent,
                "Referer": base_url + _LOG_INDEX_PATH,
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF-TOKEN": csrf,
            },
            follow_redirects=False,
        )

    csrf = await _csrf_for(t)
    resp = await _do(csrf)
    if resp.status_code == 403:
        # CSRF likely rotated — invalidate cache (memory + disk) and refetch.
        _csrf_cache.pop(t, None)
        _invalidate_disk_csrf(t)
        new_csrf = await _csrf_for(t)
        resp = await _do(new_csrf)
    resp.raise_for_status()
    return resp.json()


def _validate_window(start_ms: int, end_ms: int) -> tuple[int, int, list[str]]:
    """Clamp the search window to the tenant's retention. Returns (start, end, warnings)."""
    warnings: list[str] = []
    if end_ms <= start_ms:
        raise ValueError(f"end_ms ({end_ms}) must be greater than start_ms ({start_ms})")
    span = end_ms - start_ms
    if span > _MAX_WINDOW_MS:
        new_start = end_ms - _MAX_WINDOW_MS
        warnings.append(
            f"Search window ({span / 1000 / 3600:.1f} h) exceeds tenant retention "
            f"of 3 days. Clamped to start_ms={new_start}."
        )
        start_ms = new_start
    return start_ms, end_ms, warnings


def _summarize_log_row(row: dict[str, Any], *, content_preview_chars: int = 200) -> dict[str, Any]:
    """Return only the human-relevant fields from a log entry.

    `log_content` is truncated to `content_preview_chars` (with an
    ellipsis suffix when truncated). Pass `0` to keep the full content
    body — useful when the caller actually needs the message text.
    """
    raw_content = row.get("log_content")
    if (
        content_preview_chars > 0
        and isinstance(raw_content, str)
        and len(raw_content) > content_preview_chars
    ):
        log_content: Any = raw_content[:content_preview_chars] + "..."
    else:
        log_content = raw_content
    return {
        "id": row.get("id"),
        "log_time_ms": row.get("log_time_millis") or row.get("log_time"),
        "trace_id": row.get("trace_id"),
        "operator": (row.get("operator") or "").strip(),
        "app_name": row.get("app_name"),
        "module_name": row.get("module_name"),
        "element_type": row.get("element_type"),
        "element_name": row.get("element_name"),
        "operation_type": row.get("operation_type"),
        "log_level": row.get("log_level"),
        "duration_ms": row.get("cost_time"),
        "log_content": log_content,
        "location_info": row.get("location_info"),
    }


# ============================================================
# Public MCP tools
# ============================================================


async def search_service_logs(
    tenant: str,
    *,
    project_name: str = "",
    module_name: str = "",
    service_name: str = "",
    trace_id: str = "",
    log_level: str = "",
    start_ms: int | None = None,
    end_ms: int | None = None,
    page: int = 1,
    page_size: int = 50,
    case_sensitive: bool = True,
    content_preview_chars: int = 200,
) -> dict[str, Any]:
    """Search runtime logs for a service or trace.

    Backed by `POST /loganalysis/service/logsearch/v3/logs/search`. All
    filters are AND-combined on the server. Default time window is the
    last 3 days (the tenant's log retention).

    Args:
        tenant: "prod" or "testbed".
        project_name: maps to `app_name` in the log schema.
        module_name: maps to `module_name`.
        service_name: maps to `element_name`.
        trace_id: filter to one trace (cross-service correlation).
        log_level: e.g. "ERROR", "WARN", "INFO", "DEBUG".
        start_ms / end_ms: epoch ms; defaults to last 3 days.
        page / page_size: 1-indexed pagination.
        case_sensitive: passed through as `isCaseSensitive`.
        content_preview_chars: truncate `log_content` to this many chars
            with a trailing ellipsis. Default 200 — keeps the head of
            stack traces and most info messages while shaving the bulk
            of the response payload. Pass `0` to keep full content
            (e.g. when grepping for a specific deep substring).

    Returns:
        {
          "total": int,
          "page": int,
          "page_size": int,
          "logs": [{id, log_time_ms, trace_id, operator, app_name,
                    module_name, element_type, element_name,
                    operation_type, log_level, duration_ms, log_content,
                    location_info}, ...],
          "warnings": [...],
        }
    """
    import time

    now_ms = int(time.time() * 1000)
    if end_ms is None:
        end_ms = now_ms
    if start_ms is None:
        start_ms = end_ms - _MAX_WINDOW_MS
    start_ms, end_ms, warnings = _validate_window(start_ms, end_ms)
    warnings.append(_RETENTION_WARNING)

    # Filter shape captured from the live UI on 2026-05-16. The server
    # rejects `filters: [{field, value}]` with 400 — it expects nested
    # `filterList: [{filterType, filters: [{key, value, opType}]}]`.
    # Empty inner-filter list is dropped so a no-filter call still works.
    inner: list[dict[str, str]] = []
    if project_name:
        inner.append({"key": "app_name", "filterType": "and", "value": project_name, "opType": "="})
    if module_name:
        inner.append(
            {"key": "module_name", "filterType": "and", "value": module_name, "opType": "="}
        )
    if service_name:
        inner.append(
            {"key": "element_name", "filterType": "and", "value": service_name, "opType": "="}
        )
    if trace_id:
        inner.append({"key": "trace_id", "filterType": "and", "value": trace_id, "opType": "="})
    if log_level:
        inner.append({"key": "log_level", "filterType": "and", "value": log_level, "opType": "="})

    body: dict[str, Any] = {
        "tableType": 2,
        "pageIndex": page,
        "pageSize": page_size,
        "startTime": start_ms,
        "endTime": end_ms,
        "isCaseSensitive": case_sensitive,
    }
    if inner:
        body["filterList"] = [{"filterType": "and", "filters": inner}]

    raw = await _post(tenant, _LOG_SEARCH_PATH, body)
    result = raw.get("result") or {}
    rows = result.get("result") or []
    return {
        "total": result.get("recordCount", 0),
        "page": result.get("pageIndex", page),
        "page_size": result.get("pageSize", page_size),
        "start_ms": start_ms,
        "end_ms": end_ms,
        "logs": [
            _summarize_log_row(r, content_preview_chars=content_preview_chars)
            for r in rows
            if isinstance(r, dict)
        ],
        "warnings": warnings,
    }


async def get_log_trace(
    tenant: str,
    trace_id: str,
    *,
    start_ms: int | None = None,
    end_ms: int | None = None,
    page_size: int = 200,
    content_preview_chars: int = 200,
) -> dict[str, Any]:
    """Fetch every log entry sharing a `trace_id` — the cross-service trace tree.

    Implemented as a `search_service_logs` call filtered by trace_id with
    a larger default page size since traces commonly span 50+ entries.
    Returns logs in chronological order so the call sequence reads top to
    bottom.
    """
    if not trace_id:
        raise ValueError("trace_id is required")
    out = await search_service_logs(
        tenant,
        trace_id=trace_id,
        start_ms=start_ms,
        end_ms=end_ms,
        page=1,
        page_size=page_size,
        content_preview_chars=content_preview_chars,
    )
    out["logs"].sort(key=lambda r: r.get("log_time_ms") or 0)
    out["trace_id"] = trace_id
    services_in_trace = sorted(
        {
            f"/{r['app_name']}/{r['module_name']}/{r['element_name']}"
            for r in out["logs"]
            if r.get("element_name")
        }
    )
    out["services_in_trace"] = services_in_trace
    return out


async def count_service_invocations(
    tenant: str,
    project_name: str,
    module_name: str,
    service_name: str,
    *,
    start_ms: int | None = None,
    end_ms: int | None = None,
) -> dict[str, Any]:
    """Quick "is this service used?" answer.

    Returns just the total count for the given service over the window —
    no log bodies. Useful when the agent only needs a yes/no signal for
    `audit_artifact_usage`.
    """
    out = await search_service_logs(
        tenant,
        project_name=project_name,
        module_name=module_name,
        service_name=service_name,
        start_ms=start_ms,
        end_ms=end_ms,
        page=1,
        page_size=1,
        content_preview_chars=0,
    )
    return {
        "service": f"/{project_name}/{module_name}/{service_name}",
        "total_hits": out["total"],
        "start_ms": out["start_ms"],
        "end_ms": out["end_ms"],
        "warnings": out["warnings"],
    }


__all__ = [
    "count_service_invocations",
    "get_log_trace",
    "search_service_logs",
]
