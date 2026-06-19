# Knowledge-Helper → OWS-GDE-MCP Integration — PR Execution Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the proven capabilities from the `knowledge-helper` project (TypeScript) into `ows-gde-mcp` (Python) so the MCP can authenticate to OWS Studio for non-GET calls, ship a populated help corpus, and harden its service-invocation surface.

**Architecture:** Five independent, sequentially-mergeable PRs. PR1 is foundational (it unblocks every studio POST and therefore the cpq probe-verify loop); PR2–PR5 each deliver standalone value and can be reviewed/merged on their own. No PR rewrites the other MCP; we cherry-pick assets and re-implement them idiomatically in Python.

**Tech Stack:** Python 3.11+, `httpx`, `pydantic-settings`, `mcp[cli]` (FastMCP), `playwright` (optional extra), `pytest` + `pytest-asyncio` + `pytest-httpx`, `ruff`.

---

## Background: What is `knowledge-helper`?

> Read this first — the rest of the plan refers to it constantly.

`knowledge-helper` is a small internal tool (TypeScript / Bun) that was built for a different purpose than `ows-gde-mcp` but happens to target **the exact same OWS tenant** (`1057-sg[-studio].teleows.com`). Its original job: **scrape the OWS Studio help documentation into a searchable Obsidian knowledge vault** so the platform docs are usable offline and by AI tooling.

To do that job it had to solve a chain of OWS-platform problems end-to-end:

- **Log in to OWS like a real user.** It drives a headless Chromium through the CAS login form, persists the session, and — critically — reads the SPA's **CSRF token** out of the browser (`localStorage.csrfTokens`). This is the piece `ows-gde-mcp` has *not* solved.
- **Crawl the help corpus.** It discovered the authoritative navigation source (`/adc-studio-project-mgt/web/rest/help/doc/en_US/data/nav_json.js`), walked the full tree, and converted **3,592 help pages** to Markdown.
- **Query OWS data safely.** It ships a tiny read-only MCP with an OWS client, a **name-based "read-only" guard** (blocks anything that looks like a write), and a small **catalog** of verified read services for our domain (SFO / CMDB).

In short, `knowledge-helper` is a **proven, working reference implementation** of several OWS-integration problems that `ows-gde-mcp` (our Python MCP) still has open or unimplemented.

**Intent of this PR series:** *do not* merge the two tools or rewrite either one. Instead, **cherry-pick the five capabilities `knowledge-helper` already proved out and re-implement them idiomatically in the Python MCP.** The biggest win — PR1 — is the CSRF mechanism: without it the Python MCP cannot make any non-GET call to OWS Studio (running a service, querying a model, reading a service script all fail), which blocks the team's main use case of iterating on Studio service scripts. The remaining PRs bring across the scraped help corpus, the safety guard, a missing API path, and login resilience.

`knowledge-helper` itself stays where it is; this plan only borrows from it.

---

## How this relates to the shipped `ows-skills` plugin

The MCP repo already ships an `ows-skills` plugin (`.claude/plugins/ows-skills/`) with seven skills, advertised in the README: `ows-query`, `ows-page-analysis`, `ows-debug-service`, `ows-flow-debug`, `ows-new-service`, `ows-new-page`, and `ows-mcp-tools`. **These are guidance layers, not new capability** — decision trees and checklists that route a question to the *existing* MCP tools (`query_model_data`, `get_page_detail`, `invoke_service`, …). This plan is a **prerequisite for those skills to work**, not a duplicate of them:

1. **PR1 makes the skills functional.** Every skill that answers a "show data / analyze a page / debug / test a service" question routes through a **POST** tool (`query_model_data`, `get_page_detail`, `invoke_service`). Those fail today with `csrf_token is required`. The shipped skills are partly aspirational until PR1 lands.
2. **PR4 fills a gap the skills already reveal.** `ows-mcp-tools` lists no help-doc tool in its decision tree — consistent with the help corpus being empty. After PR4 populates it, `ows-mcp-tools` should be updated to route doc questions to `search_help` / `get_help_topic`.
3. **No write capability is added or implied.** `ows-new-service` / `ows-new-page` are *design + "test via `invoke_service` on testbed"* checklists; neither creates nor saves an element — building/deploying still happens in Studio or via package export. This plan keeps that boundary (it improves read + run + auth only).

In short: the skills are the UX; this plan fixes the plumbing they depend on.

---

## Executive Summary (for internal review)

`knowledge-helper` and `ows-gde-mcp` target the **same OWS tenant** (`1057-sg[-studio].teleows.com`). The TypeScript project already solved several problems the Python MCP has open. This plan moves five of those across:

| PR | Title | Problem it fixes | Value | Size | Depends on |
|----|-------|------------------|-------|------|------------|
| **PR1** | CSRF acquisition + dynamic header | Python MCP's HTTP login mints **no CSRF token**, so every non-GET Studio call (run service, query model, read service script) fails. | **Unblocker** — without it the MCP is GET-only against Studio. | S–M | — |
| **PR2** | Read-only service-name guard + catalog | The `call_ows_api`/`invoke_service` escape hatches are ungated on testbed; a prompt-injected agent could invoke a write service. | Safety hardening (closes a MEDIUM audit finding). | S | — |
| **PR3** | Legacy service-invoke path + tenant headers | Python MCP can't call **legacy** (`/legacy/services/<name>`) services that cpq depends on (e.g. `cmdb_site_getList`). | Endpoint coverage. | S | PR1 |
| **PR4** | Help corpus integration | The MCP's `list/get/search_help` tools serve an **empty** corpus; the fetcher is unimplemented. | Populates a shipped-but-dead feature with 3,592 docs. | M | — |
| **PR5** | CAS relogin robustness | Relogin breaks on the password-expiry interstitial and mid-flow CAS redirects. | Reliability. | S | PR1 |

**Recommended merge order:** PR1 → PR5 (both touch auth; PR5 builds on PR1) → PR2 → PR3 → PR4. PR2 and PR4 are independent and can run in parallel.

**Out of scope (tracked separately):** the HIGH-severity path-traversal in `download_file_attachment` (`tools/files.py`) surfaced in the earlier security audit is **not** a knowledge-helper integration and is excluded here. It should ship as its own fix PR; see Appendix A for the one-line cross-reference.

---

## File Structure

Files created or modified across the plan:

```
src/ows_gde_mcp/
  auth.py                 MODIFY  AuthContext gains `csrf_header` (dynamic header name)
  auth_login.py           MODIFY  add browser CSRF capture + expiry/redirect robustness (PR1, PR5)
  client.py               MODIFY  CSRF bootstrap calls browser capture when login yields none (PR1)
  service_guard.py        CREATE  read-only service-name guard ported from ows/guard.ts (PR2)
  service_catalog.py      CREATE  curated read-service catalog ported from ows/catalog.ts (PR2)
  tools/live.py           MODIFY  wire guard into call_ows_api; legacy path + headers in invoke_service (PR2, PR3)
  tools/help.py           MODIFY  serve Markdown topic bodies (PR4)
scripts/
  import_help_corpus.py   CREATE  adapter: knowledge-helper vault -> nav_index.json + topics.jsonl (PR4)
tests/
  test_auth_csrf.py       CREATE  PR1
  test_service_guard.py   CREATE  PR2
  test_invoke_legacy.py   CREATE  PR3
  test_help_corpus.py     CREATE  PR4
  test_auto_relogin.py    MODIFY  PR5 (extend existing)
docs/superpowers/plans/
  2026-06-11-knowledge-helper-integration.md   (this file)
```

---

## PR1: CSRF acquisition + dynamic header name

**Goal:** Make non-GET calls against the Studio surface work by capturing the SPA CSRF token (and its header name) even when the pure-HTTP CAS login succeeds.

**Rationale / source:** `knowledge-helper/src/shared/session.ts:pollCsrf()` proves the token is **not** available from any REST endpoint — it lives in the browser at `localStorage.csrfTokens[0]`, with the header name in the sibling field `headerKey` (default `x-gde-csrf-token`). The Python MCP's `auth_login_http._fetch_csrf` returns `None` ("OPEN QUESTION"), and the Playwright fallback only runs when HTTP login *fails*. Since HTTP login succeeds against `1057-sg-studio`, the CSRF stays empty and `AuthContext.headers_for` raises on every POST/PUT/DELETE.

**Design:** Decouple CSRF acquisition from the login transport. After any successful login that yielded no CSRF, run a lightweight headless-browser capture that reads `localStorage.csrfTokens[0]`. Store both the token and its header name on `AuthContext`. The existing `OWS_<TENANT>_CSRF_TOKEN` env override remains the no-Playwright path.

**Files:**
- Modify: `src/ows_gde_mcp/auth.py` (add `csrf_header` field; use it in `headers_for`)
- Modify: `src/ows_gde_mcp/auth_login.py` (add `fetch_csrf_via_browser`)
- Modify: `src/ows_gde_mcp/client.py:refresh_host_session` (call capture when csrf missing)
- Test: `tests/test_auth_csrf.py`

- [ ] **Step 1: Write the failing test for the dynamic header name**

`tests/test_auth_csrf.py`:

```python
from ows_gde_mcp.auth import AuthContext


def test_headers_use_custom_csrf_header_name():
    auth = AuthContext(cookie="k=v", csrf_token="TOK123", csrf_header="X-CSRF-TOKEN")
    headers = auth.headers_for("POST", "/adc-studio-service/web/rest/v1/app/service/test/p/m/s")
    assert headers["X-CSRF-TOKEN"] == "TOK123"
    assert "x-gde-csrf-token" not in headers


def test_headers_default_csrf_header_name():
    auth = AuthContext(cookie="k=v", csrf_token="TOK123")
    headers = auth.headers_for("POST", "/x")
    assert headers["x-gde-csrf-token"] == "TOK123"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_auth_csrf.py -v`
Expected: FAIL — `AuthContext.__init__() got an unexpected keyword argument 'csrf_header'`

- [ ] **Step 3: Add the `csrf_header` field and use it**

In `src/ows_gde_mcp/auth.py`, add the field to the dataclass (after `csrf_token`):

```python
    csrf_header: str = "x-gde-csrf-token"
    """Header name for the CSRF token. Usually `x-gde-csrf-token`, but the
    SPA reports it per-tenant as `localStorage.csrfTokens[0].headerKey`."""
```

In `headers_for`, replace the hardcoded header assignment:

```python
        if method.upper() != "GET":
            if not self.csrf_token:
                raise RuntimeError(
                    "csrf_token is required for non-GET requests. "
                    "Set OWS_<TENANT>_CSRF_TOKEN or capture window.csrfToken "
                    "from a logged-in browser session."
                )
            headers[self.csrf_header] = self.csrf_token
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_auth_csrf.py -v`
Expected: PASS (both tests)

- [ ] **Step 5: Commit**

```bash
git add src/ows_gde_mcp/auth.py tests/test_auth_csrf.py
git commit -m "feat(auth): make CSRF header name configurable on AuthContext"
```

- [ ] **Step 6: Add the browser CSRF capture function**

In `src/ows_gde_mcp/auth_login.py`, add (mirrors `session.ts:pollCsrf` and the existing `wait_for_function` block in `login`):

```python
async def fetch_csrf_via_browser(base_url: str) -> tuple[str, str]:
    """Open the portal headless and read `localStorage.csrfTokens[0]`.

    Returns `(csrf_token, csrf_header)`. The token is set by the SPA's
    bootstrap JS, so it is only reachable from a real browser context —
    there is no REST endpoint that mints it. Reuses any cookies the caller
    has already established by visiting the portal first.

    Raises:
        RuntimeError: if playwright isn't installed or the token never
            appears (likely the session isn't actually logged in).
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError as e:
        raise RuntimeError(
            "playwright is required to capture the CSRF token. Install with: "
            "uv pip install -e '.[login]' && playwright install chromium"
        ) from e

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            context = await browser.new_context(ignore_https_errors=True)
            page = await context.new_page()
            await page.goto(base_url.rstrip("/") + "/portal-web/", timeout=45_000)
            handle = await page.wait_for_function(
                """() => {
                    const raw = window.localStorage &&
                        localStorage.getItem('csrfTokens');
                    if (!raw) return window.csrfToken
                        ? {csrfToken: window.csrfToken, headerKey: 'x-gde-csrf-token'}
                        : null;
                    try {
                        const arr = JSON.parse(raw);
                        const e = arr && arr[0];
                        return (e && e.csrfToken)
                            ? {csrfToken: e.csrfToken, headerKey: e.headerKey || 'x-gde-csrf-token'}
                            : null;
                    } catch (err) { return null; }
                }""",
                timeout=30_000,
            )
            data = await handle.json_value()
        finally:
            await browser.close()
    token = (data or {}).get("csrfToken")
    header = (data or {}).get("headerKey") or "x-gde-csrf-token"
    if not token:
        raise RuntimeError("CSRF token not found in localStorage.csrfTokens.")
    return token, header
```

- [ ] **Step 7: Wire the capture into `refresh_host_session`**

In `src/ows_gde_mcp/client.py`, import the helper at the top:

```python
from ows_gde_mcp.auth_login import fetch_csrf_via_browser as _fetch_csrf_browser
```

In `refresh_host_session`, after the `auth.cookie`/`auth.csrf_token` assignment block, add a best-effort capture when CSRF is still missing:

```python
        # CSRF often comes only from the browser SPA (localStorage.csrfTokens).
        # If login gave us a cookie but no CSRF, capture it so non-GET calls
        # work. Best-effort: skip silently if playwright isn't installed —
        # GET-only workflows still function.
        if not auth.csrf_token:
            try:
                token, header = await _fetch_csrf_browser(base_url)
                auth.csrf_token = token
                auth.csrf_header = header
            except RuntimeError:
                pass
        _last_relogin_at[host] = time.monotonic()
```

- [ ] **Step 8: Add a test for the env-override path (no browser needed)**

Append to `tests/test_auth_csrf.py`:

```python
import pytest
from ows_gde_mcp.config import Settings, Surface, Tenant
from ows_gde_mcp.client import _auth_for_host


def test_env_csrf_token_populates_auth(monkeypatch):
    for var in ("OWS_TESTBED_STUDIO_URL", "OWS_TESTBED_SESSION_COOKIE",
                "OWS_TESTBED_CSRF_TOKEN"):
        monkeypatch.delenv(var, raising=False)
    s = Settings(
        _env_file=None,
        OWS_TESTBED_STUDIO_URL="https://testbed-studio.example.com",
        OWS_TESTBED_SESSION_COOKIE="k=v",
        OWS_TESTBED_CSRF_TOKEN="ENVTOK",
    )
    import ows_gde_mcp.client as c
    c._auth_cache.clear()
    auth = _auth_for_host(s.base_url(Tenant.TESTBED, Surface.STUDIO), Tenant.TESTBED, s)
    headers = auth.headers_for("POST", "/x")
    assert headers["x-gde-csrf-token"] == "ENVTOK"
```

- [ ] **Step 9: Run the full auth test file**

Run: `uv run pytest tests/test_auth_csrf.py -v`
Expected: PASS (all)

- [ ] **Step 10: Lint**

Run: `uv run ruff check src/ows_gde_mcp/auth.py src/ows_gde_mcp/auth_login.py src/ows_gde_mcp/client.py`
Expected: no errors

- [ ] **Step 11: Commit**

```bash
git add src/ows_gde_mcp/auth_login.py src/ows_gde_mcp/client.py tests/test_auth_csrf.py
git commit -m "feat(auth): capture SPA CSRF token via headless browser when login yields none"
```

**Acceptance criteria:**
- A non-GET call against the Studio surface no longer raises `csrf_token is required` once a session is established (with `playwright` installed *or* `OWS_<TENANT>_CSRF_TOKEN` set).
- The header name honors `localStorage.csrfTokens[0].headerKey`.
- GET-only workflows still work with no `playwright` and no env token (capture failure is swallowed).

**Manual verification (requires live creds):** with the testbed env configured, call `invoke_service(tenant="testbed", project="IOH_Service_Forecast_Order", module="IOH_Service_Forecast_Order", service="tql_probe", payload={"step": 1})` and confirm a 200 with `debug_output` containing the probe's `console.log` lines.

**Risk:** Headless-browser capture is hard to unit-test; it's covered by the env-override test + a documented manual check. The capture adds a one-time ~3–5 s cost per host on cold start.

---

## PR2: Read-only service-name guard + service catalog

**Goal:** Add a name-based safety guard so an agent cannot invoke an obvious write service through the generic escape hatch without explicit confirmation, even on the ungated testbed tenant.

**Rationale / source:** Ports `knowledge-helper/src/ows/guard.ts` (`assertReadService`) and `src/ows/catalog.ts` (`SERVICE_CATALOG`). This is defense-in-depth for the MEDIUM audit finding that the Python MCP's prod write-gate is bypassable via per-endpoint `read_only=True` and that `call_ows_api` is ungated on testbed.

**Files:**
- Create: `src/ows_gde_mcp/service_guard.py`
- Create: `src/ows_gde_mcp/service_catalog.py`
- Modify: `src/ows_gde_mcp/tools/live.py` (`call_ows_api`)
- Test: `tests/test_service_guard.py`

- [ ] **Step 1: Write the failing test**

`tests/test_service_guard.py`:

```python
import pytest
from ows_gde_mcp.service_guard import assert_read_service, is_write_service


def test_read_suffix_allowed():
    assert_read_service("cmdb_site_getList")
    assert_read_service("sfo_ticket_query")


def test_write_keyword_blocked():
    with pytest.raises(ValueError, match="write-operation"):
        assert_read_service("sfo_new_forecast_create")


def test_unknown_unsuffixed_blocked():
    with pytest.raises(ValueError, match="read-suffix"):
        assert_read_service("mystery_service")


def test_catalog_service_allowed():
    # A catalog entry with no read suffix is still allowed.
    from ows_gde_mcp.service_catalog import SERVICE_CATALOG  # noqa: F401
    assert_read_service("sfc_service_forecast_order_process_getList")


def test_invalid_chars_blocked():
    with pytest.raises(ValueError, match="invalid characters"):
        assert_read_service("../evil")


def test_is_write_service_helper():
    assert is_write_service("foo_delete") is True
    assert is_write_service("foo_getList") is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_service_guard.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'ows_gde_mcp.service_guard'`

- [ ] **Step 3: Create the catalog**

`src/ows_gde_mcp/service_catalog.py`:

```python
"""Curated catalog of verified read-only OWS services.

Ported from knowledge-helper/src/ows/catalog.ts. Services listed here are
allowed by `service_guard.assert_read_service` even if their name lacks a
read suffix. Extend this list only with services confirmed to be reads.
"""

from __future__ import annotations

SERVICE_CATALOG: list[dict[str, str]] = [
    {
        "service": "cmdb_site_getList",
        "type": "legacy",
        "notes": "CMDB site master — pid, name, projectid, area_id, ...",
    },
    {
        "service": "cmdb_fm_office_getList",
        "type": "legacy",
        "notes": "FM office lookup — id, fm_office_name, keycode, ...",
    },
    {
        "service": "sfc_service_forecast_order_process_getList",
        "project": "IOH_Service_Forecast_Order",
        "module": "IOH_Service_Forecast_Order",
        "type": "project",
        "notes": "SFO ticket/workflow process records.",
    },
]

CATALOG_SERVICE_NAMES: frozenset[str] = frozenset(e["service"] for e in SERVICE_CATALOG)
```

- [ ] **Step 4: Create the guard**

`src/ows_gde_mcp/service_guard.py`:

```python
"""Name-based read-only guard for OWS service invocation.

Ported from knowledge-helper/src/ows/guard.ts. Three checks, in order:
1. Reject names with path/quote characters (injection guard).
2. Reject names matching the write-operation blocklist.
3. Require a read suffix OR catalog membership.
"""

from __future__ import annotations

import re

from ows_gde_mcp.service_catalog import CATALOG_SERVICE_NAMES

_WRITE_KW = re.compile(
    r"\b(create|update|delete|save|submit|insert|remove|dispatch|confirm|"
    r"approve|reject|cancel|modify|set|exec|sync|import|trigger)\b",
    re.IGNORECASE,
)
_READ_SUFFIX = re.compile(
    r"_(get|getlist|query|find|search|count|list|detail|info|load|export)$",
    re.IGNORECASE,
)


def is_write_service(name: str) -> bool:
    """True if the service name matches the write-operation blocklist."""
    return bool(_WRITE_KW.search(name))


def assert_read_service(name: str) -> None:
    """Raise ValueError unless `name` is a recognised read-only service."""
    if re.search(r"[./\\\"]", name):
        raise ValueError(f"Read-only guard: invalid characters in service name {name!r}")
    if _WRITE_KW.search(name):
        raise ValueError(
            f"Read-only guard: service name {name!r} matches the write-operation blocklist. "
            "Pass confirm=True to invoke a write service deliberately."
        )
    if name not in CATALOG_SERVICE_NAMES and not _READ_SUFFIX.search(name):
        raise ValueError(
            f"Read-only guard: service {name!r} has no read suffix (*_getList, *_query, ...) "
            "and isn't in SERVICE_CATALOG. Add it there if it's a verified read service."
        )
```

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run pytest tests/test_service_guard.py -v`
Expected: PASS (all)

- [ ] **Step 6: Wire the guard into `call_ows_api`**

In `src/ows_gde_mcp/tools/live.py`, the `call_ows_api` function gains an opt-out flag and applies the guard to non-GET service calls. Add the import near the top:

```python
from ows_gde_mcp.service_guard import is_write_service
```

Add an `allow_write: bool = False` parameter to `call_ows_api` (after `confirm`) and insert this check immediately before the `async with OwsClient...` block:

```python
    # Name-based safety net for the generic escape hatch: block obvious
    # write services on any tenant unless the caller opts in. Complements
    # the prod write-gate (which only covers the prod tenant).
    if method_u != "GET" and not allow_write:
        last_segment = path.rstrip("/").rsplit("/", 1)[-1].split("?", 1)[0]
        if is_write_service(last_segment):
            return {
                "error": {
                    "code": "write_guard",
                    "message": (
                        f"Path segment {last_segment!r} looks like a write operation. "
                        "Re-issue with allow_write=True if this is intentional."
                    ),
                }
            }
```

Document the new parameter in the `call_ows_api` docstring `Args:` section:

```
        allow_write: set True to bypass the name-based write guard for a
                path whose final segment matches a write keyword.
```

- [ ] **Step 7: Add a test for the call_ows_api guard wiring**

Append to `tests/test_service_guard.py`:

```python
import asyncio
from ows_gde_mcp.tools import live


def test_call_ows_api_blocks_write_path_without_optin(monkeypatch):
    # No network: the guard returns before any client is built.
    out = asyncio.run(
        live.call_ows_api(
            tenant="testbed",
            method="POST",
            path="/adc-service/web/rest/v1/legacy/services/sfo_order_create",
        )
    )
    assert out["error"]["code"] == "write_guard"
```

- [ ] **Step 8: Run tests + lint**

Run: `uv run pytest tests/test_service_guard.py -v && uv run ruff check src/ows_gde_mcp/service_guard.py src/ows_gde_mcp/service_catalog.py src/ows_gde_mcp/tools/live.py`
Expected: PASS, no lint errors

- [ ] **Step 9: Commit**

```bash
git add src/ows_gde_mcp/service_guard.py src/ows_gde_mcp/service_catalog.py src/ows_gde_mcp/tools/live.py tests/test_service_guard.py
git commit -m "feat(safety): add read-only service-name guard to call_ows_api"
```

**Acceptance criteria:**
- `call_ows_api` with a write-named final path segment returns a `write_guard` error unless `allow_write=True`.
- The guard never makes a network call when it blocks.
- `invoke_service` is intentionally left as-is (it is the deliberate write tool, already gated on prod by `confirm`); the guard targets the generic escape hatch.

**Risk:** False positives on legitimately-named reads that contain a blocklist word — mitigated by the catalog allowlist and the `allow_write` opt-out.

---

## PR3: Legacy service-invoke path + tenant headers

**Goal:** Let `invoke_service` call **legacy** services (`/adc-service/web/rest/v1/legacy/services/<service>`, no project/module) that cpq depends on, and optionally attach the tenant/referer headers the SPA sends.

**Rationale / source:** `knowledge-helper/src/ows/client.ts:owsCallService` selects between two URL shapes — project-scoped (`/services/<p>/<m>/<s>`, which the Python MCP already uses) and **legacy** (`/legacy/services/<s>`, which it lacks). `buildHeaders` also sets `x-gde-tenant-id`, `Referer`, and `Origin`.

**Files:**
- Modify: `src/ows_gde_mcp/tools/live.py` (`invoke_service`)
- Test: `tests/test_invoke_legacy.py`

- [ ] **Step 1: Write the failing test (path selection, no network)**

`tests/test_invoke_legacy.py`:

```python
from ows_gde_mcp.tools.live import _service_invoke_path


def test_project_scoped_path():
    p = _service_invoke_path("IOH_Service_Forecast_Order", "IOH_Service_Forecast_Order", "sfo_x_getList")
    assert p == "/adc-service/web/rest/v1/services/IOH_Service_Forecast_Order/IOH_Service_Forecast_Order/sfo_x_getList"


def test_legacy_path_when_no_project_module():
    p = _service_invoke_path("", "", "cmdb_site_getList")
    assert p == "/adc-service/web/rest/v1/legacy/services/cmdb_site_getList"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_invoke_legacy.py -v`
Expected: FAIL — `cannot import name '_service_invoke_path'`

- [ ] **Step 3: Add the path helper**

In `src/ows_gde_mcp/tools/live.py`, near the other service constants:

```python
def _service_invoke_path(project_name: str, module_name: str, service_name: str) -> str:
    """Pick the project-scoped or legacy service-runtime path.

    Legacy services (cmdb_*, shared getters) live at
    `/adc-service/web/rest/v1/legacy/services/<service>` with no
    project/module segment — pass empty project/module to target them.
    """
    if project_name and module_name:
        return f"/adc-service/web/rest/v1/services/{project_name}/{module_name}/{service_name}"
    return f"/adc-service/web/rest/v1/legacy/services/{service_name}"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_invoke_legacy.py -v`
Expected: PASS

- [ ] **Step 5: Use the helper in `invoke_service` (prod runtime branch)**

In `invoke_service`, replace the hardcoded prod `service_uri` construction with the helper so legacy services route correctly:

```python
        if t == Tenant.PROD:
            service_uri = _service_invoke_path(project_name, module_name, service_name)
            return await _runtime_post(
                tenant,
                _SERVICE_TEST_RUNTIME_PATH,
                json={"request_string": service_uri, "raw_body": body},
                confirm=confirm,
            )
```

Update the `invoke_service` docstring to note: "Pass empty `project_name`/`module_name` to invoke a legacy service (e.g. `cmdb_site_getList`)."

- [ ] **Step 6: (Optional header parity) add tenant/referer extras**

In `invoke_service`, allow callers to pass through SPA parity headers when an endpoint requires them. Add `extra_headers: dict[str, str] | None = None` to the signature and forward it to `_runtime_post`/`_studio_post` via the existing `extra_headers` kwarg on `client.request`. Document that `x-gde-tenant-id` / `Referer` / `Origin` can be supplied here when a specific endpoint rejects the default header set. (Do **not** hardcode tenant id `1057` — it is tenant-specific and already carried in the session cookie.)

- [ ] **Step 7: Run tests + lint**

Run: `uv run pytest tests/test_invoke_legacy.py -v && uv run ruff check src/ows_gde_mcp/tools/live.py`
Expected: PASS, no lint errors

- [ ] **Step 8: Commit**

```bash
git add src/ows_gde_mcp/tools/live.py tests/test_invoke_legacy.py
git commit -m "feat(live): support legacy service-invoke path in invoke_service"
```

**Acceptance criteria:**
- `invoke_service(..., project_name="", module_name="", service_name="cmdb_site_getList")` targets the `/legacy/services/` path.
- Existing project-scoped invocations are unchanged.

**Risk:** Low. Path selection is pure logic with full test coverage; live behavior is verified manually against a known legacy service.

---

## PR4: Help corpus integration

**Goal:** Populate the MCP's `list_help_topics` / `get_help_topic` / `search_help` tools from the help corpus `knowledge-helper` already scraped (3,592 docs), without re-crawling.

**Rationale / source:** `tools/help.py` reads `docs/help/<lang>/nav_index.json` + topic files (and an optional `topics.jsonl` fast-search index), but the corpus and fetcher don't exist. `knowledge-helper/src/scraper/nav.ts` already discovered the nav source (`/adc-studio-project-mgt/web/rest/help/doc/en_US/data/nav_json.js`) and wrote the full corpus as Markdown into its `vault/`. An adapter converts that into the exact shapes `help.py` consumes.

**Files:**
- Create: `scripts/import_help_corpus.py`
- Modify: `src/ows_gde_mcp/tools/help.py` (serve Markdown bodies)
- Test: `tests/test_help_corpus.py`

- [ ] **Step 1: Confirm the source layout (investigative, not a code change)**

Run: `ls ~/codes/huaweed/knowledge-helper/vault/"Low-Code Orchestration" && head -20 "$(find ~/codes/huaweed/knowledge-helper/vault -name '*.md' | head -1)"`
Record the front-matter keys present (expected via `gray-matter`: `title`, `slug`, source URL, parent). These map to `nav_index.json` fields below.

- [ ] **Step 2: Write the failing test against the target schema**

`tests/test_help_corpus.py`:

```python
import json
from pathlib import Path
from ows_gde_mcp.tools import help as help_tools


def _seed_corpus(tmp_path: Path) -> Path:
    lang_dir = tmp_path / "en_US"
    lang_dir.mkdir(parents=True)
    (lang_dir / "nav_index.json").write_text(json.dumps([
        {"id": 1, "parent_id": 0, "name": "Overview", "local": "overview.md", "depth": 0, "path": [1]},
    ]), encoding="utf-8")
    (lang_dir / "overview.md").write_text("# Overview\n\nLow-Code Orchestration intro.\n", encoding="utf-8")
    (lang_dir / "topics.jsonl").write_text(
        json.dumps({"id": 1, "name": "Overview", "local": "overview.md",
                    "title": "Overview", "text": "Low-Code Orchestration intro."}) + "\n",
        encoding="utf-8",
    )
    return tmp_path


def test_get_help_topic_serves_markdown(tmp_path, monkeypatch):
    root = _seed_corpus(tmp_path)
    monkeypatch.setattr(help_tools, "_CACHE_ROOT", root)
    out = help_tools.get_help_topic(1)
    assert out["title"] == "Overview"
    assert "Low-Code Orchestration" in out["text"]


def test_search_help_uses_jsonl(tmp_path, monkeypatch):
    root = _seed_corpus(tmp_path)
    monkeypatch.setattr(help_tools, "_CACHE_ROOT", root)
    out = help_tools.search_help("orchestration")
    assert out["total"] == 1
    assert out["hits"][0]["local"] == "overview.md"
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/test_help_corpus.py -v`
Expected: FAIL — `test_get_help_topic_serves_markdown` fails because `get_help_topic` parses HTML and returns an empty `text` for a `.md` file.

- [ ] **Step 4: Teach `get_help_topic` to serve Markdown**

In `src/ows_gde_mcp/tools/help.py`, in `get_help_topic`, after `html = file_path.read_text(...)`, branch on extension:

```python
    raw = file_path.read_text(encoding="utf-8")
    if str(row["local"]).endswith(".md"):
        # Markdown corpus (imported from knowledge-helper): the body is
        # already plain text. Title = first ATX heading or the nav name.
        lines = raw.splitlines()
        md_title = next((l[2:].strip() for l in lines if l.startswith("# ")), None)
        title, text, parent = md_title, raw, None
    else:
        title, text, parent = _extract_topic_body(raw)
```

(`search_help` already prefers `topics.jsonl`, so no change is needed there — the adapter just has to emit it.)

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run pytest tests/test_help_corpus.py -v`
Expected: PASS

- [ ] **Step 6: Write the importer adapter**

`scripts/import_help_corpus.py`:

```python
"""Import the knowledge-helper Markdown vault into the MCP help corpus.

Reads the scraped docs from a knowledge-helper `vault/` directory and emits
the shapes `ows_gde_mcp.tools.help` consumes:
  docs/help/<lang>/nav_index.json   flat [{id, parent_id, name, local, depth, path}]
  docs/help/<lang>/<local>.md       topic bodies (copied verbatim)
  docs/help/<lang>/topics.jsonl     [{id, name, local, title, text}] for fast search

Usage:
  uv run python scripts/import_help_corpus.py \
      --vault ~/codes/huaweed/knowledge-helper/vault \
      --lang en_US
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]


def _slug_to_local(rel: Path) -> str:
    """Stable filename for a vault topic (path-flattened, .md kept)."""
    flat = "__".join(rel.with_suffix("").parts)
    flat = re.sub(r"[^A-Za-z0-9_.\-]", "-", flat)
    return f"{flat}.md"


def _title_of(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, type=Path)
    ap.add_argument("--lang", default="en_US")
    args = ap.parse_args()

    src_root = args.vault.expanduser()
    if not src_root.is_dir():
        raise SystemExit(f"vault not found: {src_root}")

    out_dir = _REPO_ROOT / "docs" / "help" / args.lang
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(p for p in src_root.rglob("*.md") if ".obsidian" not in p.parts)
    nav: list[dict] = []
    jsonl_lines: list[str] = []

    for i, src in enumerate(md_files, start=1):
        rel = src.relative_to(src_root)
        local = _slug_to_local(rel)
        body = src.read_text(encoding="utf-8")
        title = _title_of(body, rel.stem)
        depth = len(rel.parts) - 1
        shutil.copyfile(src, out_dir / local)
        nav.append({
            "id": i,
            "parent_id": 0,            # flat import; nav tree is not reconstructed
            "name": title,
            "local": local,
            "depth": depth,
            "path": [i],
        })
        jsonl_lines.append(json.dumps({
            "id": i, "name": title, "local": local,
            "title": title, "text": body,
        }))

    (out_dir / "nav_index.json").write_text(json.dumps(nav, indent=2), encoding="utf-8")
    (out_dir / "topics.jsonl").write_text("\n".join(jsonl_lines) + "\n", encoding="utf-8")
    print(f"Imported {len(md_files)} topics into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 7: Run the importer against the real vault**

Run: `uv run python scripts/import_help_corpus.py --vault ~/codes/huaweed/knowledge-helper/vault --lang en_US`
Expected: `Imported 3592 topics into .../docs/help/en_US` (count may vary)

- [ ] **Step 8: Smoke-test the live tools against the imported corpus**

Run: `uv run python -c "from ows_gde_mcp.tools import help as h; print(h.search_help('forecast')['total']); print(h.list_help_topics(limit=3)['total'])"`
Expected: non-zero counts; no `no_cache` error

- [ ] **Step 9: Confirm `.gitignore` excludes the bulk corpus**

The repo `.gitignore` already ignores `docs/help/**/*.html`, `docs/help/**/*.json`. Extend it so the imported Markdown + jsonl are not committed (the corpus is regenerable):

Add to `.gitignore`:
```
docs/help/**/*.md
docs/help/**/topics.jsonl
docs/help/**/nav_index.json
!docs/help/.gitkeep
```

- [ ] **Step 10: Run tests + lint + commit**

Run: `uv run pytest tests/test_help_corpus.py -v && uv run ruff check scripts/import_help_corpus.py src/ows_gde_mcp/tools/help.py`
Expected: PASS, no lint errors

```bash
git add scripts/import_help_corpus.py src/ows_gde_mcp/tools/help.py tests/test_help_corpus.py .gitignore
git commit -m "feat(help): import knowledge-helper markdown corpus; serve md topic bodies"
```

**Acceptance criteria:**
- After running the importer, `search_help`, `list_help_topics`, and `get_help_topic` return real results.
- Markdown topic bodies render as plain text via `get_help_topic`.
- The bulk corpus is gitignored (regenerable from the vault).

**Risk:** The flat import drops the nav hierarchy (`parent_id`/`path`), so `list_help_topics(parent_id=...)` filtering is degraded. Acceptable for v1 (search + read work fully). A follow-up can reconstruct the tree from `nav_json.js` if breadcrumb navigation is needed. **Note this limitation in the PR description** so it isn't mistaken for full coverage.

---

## PR5: CAS relogin robustness

**Goal:** Make headless relogin survive the two real-world cases `knowledge-helper` handles: the password-expiry interstitial and a mid-flow CAS redirect.

**Rationale / source:** `knowledge-helper/src/shared/session.ts:casLogin` detects `.login-form-error` (bad creds, fail fast) and the `.expire_main` expiry notice (clicks Continue); `src/scraper/fetcher.ts` resolves a mid-flow CAS bounce via the w3 SSO `a[href*="clientredirect"]` link. The Python `auth_login.py` has a "Change Later" handler but not the explicit error-detection or the SSO-redirect recovery.

**Files:**
- Modify: `src/ows_gde_mcp/auth_login.py` (`login`)
- Test: `tests/test_auto_relogin.py` (extend)

- [ ] **Step 1: Add fail-fast credential-error detection**

In `auth_login.py:login`, after the `Log In` click and before `wait_for_url`, add a best-effort error probe (it raises a clear error instead of timing out on bad creds):

```python
            # Fail fast on an explicit CAS credential error rather than
            # waiting out the homepage timeout.
            with contextlib.suppress(Exception):
                err = await page.locator(".login-form-error").first.text_content(timeout=3_000)
                if err and err.strip():
                    raise RuntimeError(
                        f"CAS login for {tenant.value} rejected: {err.strip()!r} "
                        "— check OWS_<TENANT>_USERNAME / _PASSWORD."
                    )
```

- [ ] **Step 2: Add w3 SSO redirect recovery**

After the credential-error probe, add the SSO-link recovery used by the doc fetcher:

```python
            # Some tenants bounce through a w3 SSO interstitial on the way
            # to the portal. Click the clientredirect link to continue.
            with contextlib.suppress(Exception):
                if "/dspcas/login" in page.url.lower():
                    sso = page.locator('a[href*="clientredirect"]').first
                    if await sso.count() > 0:
                        await sso.click(timeout=5_000)
```

- [ ] **Step 3: Add a regression test for the error-message contract**

In `tests/test_auto_relogin.py`, add a test that the rejection raises with the expected message. Because the flow is Playwright-driven, assert at the message-contract level by monkeypatching `login` to a stub that raises the same `RuntimeError`, verifying `refresh_host_session` surfaces it through its wrapper:

```python
import pytest
import ows_gde_mcp.client as client_mod
from ows_gde_mcp.config import Settings, Tenant


async def test_relogin_surfaces_credential_error(monkeypatch):
    s = Settings(
        _env_file=None,
        OWS_TESTBED_RUNTIME_URL="https://testbed.example.com",
        OWS_TESTBED_USERNAME="u", OWS_TESTBED_PASSWORD="p",
    )
    client_mod._auth_cache.clear(); client_mod._last_relogin_at.clear()

    async def boom_http(*a, **k):
        from ows_gde_mcp.auth_login_http import HttpLoginError
        raise HttpLoginError("forced")

    async def boom_cas(*a, **k):
        raise RuntimeError("CAS login for testbed rejected: 'bad password'")

    monkeypatch.setattr(client_mod, "_http_login", boom_http)
    monkeypatch.setattr(client_mod, "_cas_login", boom_cas)
    monkeypatch.setattr(client_mod, "_fetch_csrf_browser", lambda *a, **k: (_ for _ in ()).throw(RuntimeError()))

    with pytest.raises(RuntimeError, match="rejected"):
        await client_mod.refresh_host_session("https://testbed.example.com", Tenant.TESTBED, s)
```

- [ ] **Step 4: Run tests + lint**

Run: `uv run pytest tests/test_auto_relogin.py -v && uv run ruff check src/ows_gde_mcp/auth_login.py`
Expected: PASS, no lint errors

- [ ] **Step 5: Commit**

```bash
git add src/ows_gde_mcp/auth_login.py tests/test_auto_relogin.py
git commit -m "feat(auth): fail fast on CAS credential errors; recover via w3 SSO redirect"
```

**Acceptance criteria:**
- A wrong password produces a clear "rejected" error instead of a 30 s homepage timeout.
- A w3 SSO interstitial no longer strands the login on `/dspcas/login`.

**Risk:** Low; both additions are `contextlib.suppress`-wrapped best-effort probes that don't change the happy path.

---

## Rollout & Sequencing

1. **PR1** must merge first — it is the dependency for any non-GET Studio work and for PR3/PR5 (shared auth files).
2. **PR5** next (same auth files; rebases cleanly on PR1).
3. **PR2** and **PR4** are independent of the auth chain and of each other — run in parallel.
4. **PR3** after PR1 (it relies on a working CSRF for the prod runtime POST).

Each PR is independently shippable and reverts cleanly. Total estimated effort: PR1 ~0.5–1 day (browser capture + manual verification), PR2/PR3/PR5 ~0.5 day each, PR4 ~0.5–1 day (adapter + corpus QA).

**Cross-project note:** PR1 and PR5 only fully verify against the live `1057-sg-studio` tenant, which needs `OWS_TESTBED_*` credentials configured in the MCP `.env`. Those credentials exist in the `knowledge-helper` project (`USERNAME`/`PASSWORD`); copying them into the MCP `.env` is a prerequisite for the manual verification steps (it is **not** committed — `.env` is gitignored).

---

## Appendix A — Related work (out of scope for this plan)

The earlier security audit found a **HIGH-severity path-traversal / arbitrary-file-write** in `tools/files.py:download_file_attachment` (caller-controlled `save_dir`/`save_as`/`file_name`, no confinement). It is unrelated to the knowledge-helper integration and should ship as its own fix PR (confine the write target to a resolved `save_dir`, strip path components from the filename). Flagged here only so reviewers don't assume this plan covers it.

---

## Self-Review

- **Spec coverage:** Each of the five integration items identified in the source analysis maps to a PR — CSRF (PR1), service guard + catalog (PR2), legacy path + headers (PR3), help corpus (PR4), relogin robustness (PR5). Service catalog seed is folded into PR2. No item left unmapped.
- **Placeholder scan:** No "TBD"/"handle edge cases"/"add validation" steps — every code step contains real code; investigative steps (PR4 Step 1) specify the exact command and what to record.
- **Type consistency:** `csrf_header` (PR1) is referenced consistently in `auth.py` and the browser-capture wiring. `assert_read_service` / `is_write_service` (PR2) names match between the module, tests, and the `call_ows_api` wiring. `_service_invoke_path` (PR3) signature matches its test and call site. `_CACHE_ROOT` (PR4) matches the existing attribute in `tools/help.py`.
