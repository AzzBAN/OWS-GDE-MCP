# Per-Host CAS Login (HTTP-primary, Playwright-fallback)

**Date:** 2026-06-10
**Status:** Approved (pending spec review)
**Goal:** Make prod **studio** API calls (`list_services`, `list_pages`,
`list_models`, etc.) work, not just testbed — by fixing how CAS login
authenticates each host.

---

## 1. Problem

The OWS MCP authenticates against OWS via an Apereo CAS session cookie. Auth
state is cached **per tenant**:

```python
_auth_cache: dict[Tenant, AuthContext]      # client.py
refresh_tenant_session(tenant, settings)    # logs into ONE host
```

A tenant has two *surfaces*:

- **studio** — design-time authoring (services, pages, models)
- **runtime** — deployed apps (processes, logs, user info)

Each surface resolves to a base URL / **host**:

| Tenant  | studio host                  | runtime host           | Same host? |
|---------|------------------------------|------------------------|------------|
| testbed | `1057-sg-studio.teleows.com` | `1057-sg-studio.teleows.com` | **Yes** |
| prod    | `1057-sg-studio.teleows.com` | `1057-sg.teleows.com`  | **No**  |

A CAS session cookie is **bound to the host that issued it**. The current
login logs into exactly one host per tenant (runtime — `surfaces[0]`), and
stores a single cookie per tenant. Consequences:

- **testbed** — both surfaces are the same host, so one login covers
  everything. Works today. ✅
- **prod** — runtime host authenticates fine (`whoami`, `list_processes`
  succeed), but every **studio**-host call 302-redirects to
  `/dspcas/login`. Auto-relogin re-runs against the runtime host *again*,
  the studio call still fails, and the user sees:
  > *Auto-relogin for tenant 'prod' completed but the next request was still
  > redirected to CAS …* ❌

### Verified evidence (live, 2026-06-10)

| Call               | Surface | Method | Prod result            |
|--------------------|---------|--------|------------------------|
| `whoami`           | runtime | GET    | ✅ `_session_alive: true` |
| `list_processes`   | runtime | GET    | ✅ 337 processes        |
| `list_models`      | runtime | POST(ro) | ✅ 9 models           |
| `query_model_data` | runtime | POST(ro) | ✅ returned INC ticket row |
| `list_studio_projects` | studio | GET  | ❌ 302 → CAS          |
| `get_model_schema` | studio  | POST   | ❌ blocked at write-gate (no `confirm` param) |
| `call_ows_api` → studio `query-all`, `confirm=true` | studio | POST | ❌ 302 → CAS |

Credentials are correct and identical for both tenants (`.env` lines 17–20);
the same creds authenticate testbed studio successfully. The failure is
purely the per-tenant (single-host) auth model, not bad credentials.

### Two stacked walls for studio POST-read tools

Tools that read Studio data via **POST** (`get_model_schema`, `get_model`)
hit **two** independent blocks on prod, in series:

1. **Write-gate false-positive.** The client blocks every non-GET to prod
   unless `confirm=True`. These tools are reads, but issue POST — and they
   **expose no `confirm` parameter**, so they can never pass the gate. This
   is a *separate bug* from the host issue, fixed by **adding a `confirm`
   parameter** to these tools (threaded through to `client.request`), so the
   caller can explicitly pass `confirm=true` — the same pattern
   `invoke_service` / `call_ows_api` already use. Chosen over silent
   `read_only=True` so prod studio access stays an explicit, auditable act.
2. **Studio-host auth.** Even past the gate (verified via `call_ows_api`
   with `confirm=true`), the prod studio host has no CAS session → 302.
   This is the core per-host fix.

**The per-host login fix alone does NOT make `get_model_schema` work on
prod** — it would still be stuck at wall #1. Both fixes are required.

By contrast, `list_models` / `query_model_data` / `get_model_fields` use the
**runtime** host and are already marked read-only, so neither wall applies —
they work today.

---

## 2. Core fix — key auth by HOST, not by TENANT

Change the auth cache and relogin to be keyed by the resolved **host**:

```python
_auth_cache: dict[str, AuthContext]          # host → cookie/csrf
refresh_host_session(host, tenant, settings) # logs into THAT host
```

Why host (not `(tenant, surface)`):

- testbed studio + runtime → same host → **one** cached login (dedup, no
  behaviour change).
- prod studio + runtime → **two** hosts → **two** independent logins, each
  with its own cookie.

`OwsClient.for_surface(tenant, surface, settings)` already resolves a
surface to a base URL. It will derive the host from that URL and
look up / build that host's `AuthContext`. The existing 302→CAS retry loop
is preserved — it just calls `refresh_host_session(host, …)` for the host
the failing request targeted, instead of a tenant-wide refresh.

**Net effect:** a prod studio call authenticates `1057-sg-studio.teleows.com`
on demand, captures that host's cookie, and succeeds. Testbed is unchanged.

### Concurrency / dedup

The per-tenant relogin lock + 5s debounce (`_relogin_locks`,
`_last_relogin_at`) move to being keyed per **host** as well, so concurrent
callers hitting the same host serialise through one login, and the two prod
hosts can authenticate independently without blocking each other.

---

## 3. Login chain — HTTP → Playwright → manual cookie

`refresh_host_session(host, tenant, settings)` runs a three-step chain
against **one host**. First step to produce a working session wins.

### Step 1 — Pure-HTTP login (primary)  →  new `auth_login_http.py`

1. `GET https://<host>/dspcas/login`
   - scrape hidden `execution` token, `rsaPubBase64Str` (PEM public key),
     `rsaPubVersion`
   - retain the `JSESSIONIDsg` cookie from the response
2. RSA-OAEP / SHA-256 encrypt the password with the scraped public key
   (Python `cryptography` — reproduces the browser's WebCrypto
   `RSA-OAEP` + `SHA-256` exactly).
3. `POST /dspcas/login` with form fields:
   `username`, encrypted `password`, `execution`, `_eventId=submit`
   - follow the service-ticket redirect chain, accumulating Set-Cookie
     into the host's cookie jar
4. Fetch the CSRF token (SPA bootstrap REST endpoint — exact path TBD at
   implementation; see Open Questions).
5. **Self-test:** issue a cheap authenticated GET (e.g.
   `/portal/web/rest/sso/check`) with the new cookie. If it does not come
   back authenticated, Step 1 is considered **failed** → fall through.

Any exception in 1–4, or a failed self-test in 5, triggers Step 2.

### Step 2 — Playwright fallback  →  existing `auth_login.py`, parametrized

The current Playwright flow, changed to log into **the given host** rather
than always `surfaces[0]`. This clears cases HTTP can't: JS-gated
interstitials ("Change Later" password-expiry), `MATEINFO_SESSION_ID`
minting, etc.

- Playwright **installed** → run headless login, capture cookies + CSRF,
  done.
- Playwright **not installed** → raise the Step-3 actionable error
  (do not hang, do not fail cryptically).

### Step 3 — Actionable error (both failed, or Playwright absent)

A single clear message naming the host, the install command, and the
manual-cookie env var, e.g.:

> Auto-login failed for `1057-sg-studio.teleows.com` (HTTP login rejected;
> Playwright not installed). Install it with
> `uv pip install -e '.[login]' && playwright install chromium`, or paste a
> captured cookie into `OWS_PROD_SESSION_COOKIE` in `.env`.

When Playwright *was* tried and also failed, the message instead explains
the likely cause (captcha / MFA / locked account — none of which any
headless flow can clear) and points to the manual-cookie override.

### Decision flow

```
HTTP login → self-test passes?  ──yes──► done
   │ no / threw
   ▼
Playwright installed? ──no──► actionable error (install hint + manual cookie)
   │ yes
   ▼
Playwright login → passes? ──yes──► done
   │ no
   ▼
actionable error (captcha/MFA explanation + manual cookie)
```

---

## 4. New-user experience & docs

With HTTP login primary, **most new users won't need Playwright** — that's
the win. Playwright becomes opt-in, pulled in only when HTTP login can't
clear a host (captcha / MFA / interstitial).

- **`.env.example`** — reframe the auth section: credentials
  (`OWS_*_USERNAME/PASSWORD`) are the *primary* path (HTTP auto-login);
  captured cookie is the manual override; Playwright is the optional
  fallback.
- **`README.md`** — short "Authentication" note: HTTP login works out of the
  box with creds; install Playwright
  (`uv pip install -e '.[login]' && playwright install chromium`) only if
  you hit the fallback error.
- **The Step-3 error message is the just-in-time doc** — names the host, the
  install command, and the manual-cookie env var. A user who never hits it
  never needs to read anything.

---

## 5. Testing & verification

### Unit tests (mocked — no live tenant, no browser)

- **RSA-OAEP encryption** produces a value a mocked CAS accepts; round-trip
  decrypt with a test keypair confirms scheme (`RSA-OAEP` + `SHA-256`).
- **Scraping** `execution` / `rsaPubBase64Str` / `rsaPubVersion` from a
  saved login-page fixture.
- **Decision chain**: HTTP-fails → Playwright invoked; Playwright-absent →
  actionable error raised (assert message names host + install command).
- **Per-host cache**: testbed resolves both surfaces to one host (one
  login); prod resolves to two hosts (two logins). Mock the login fns and
  assert call counts / cache keys.

### Live verification (the real proof, post-implementation)

1. Prod **studio**: `list_services`, `list_pages`, `list_models` return data
   (not the 302→CAS error).
2. Prod **runtime**: `whoami`, `list_processes` still work (no regression).
3. Testbed: re-run a studio + runtime call — unchanged.

---

## 6. File inventory (what changes)

| File | Change |
|------|--------|
| `client.py` | `_auth_cache`, `_relogin_locks`, `_last_relogin_at` keyed by **host**; `for_surface` resolves host → AuthContext; rename/retarget `refresh_tenant_session` → `refresh_host_session`. |
| `auth_login_http.py` | **NEW** — pure-HTTP CAS login for one host (scrape, RSA-OAEP encrypt, POST, follow redirects, CSRF fetch, self-test). |
| `auth_login.py` | Parametrize the Playwright flow to log into a **given host** instead of `surfaces[0]`. |
| `tools/*.py` (model/studio reads) | Add a `confirm` parameter to POST-based studio **read** tools and thread it through to `client.request`: `get_model_schema`, `get_model` (and audit any other studio POST-read that lacks one). Caller passes `confirm=true` to clear the prod write-gate — same pattern as `invoke_service` / `call_ows_api`. Fixes wall #1. |
| `.env.example` | Reframe auth section (creds primary, cookie override, Playwright optional). |
| `README.md` | Short Authentication note. |
| `tests/` | Unit tests per Section 5. |

Helper: a small `host_of(base_url) -> str` (urlsplit netloc) used by both
`client.py` and the login modules.

---

## 7. Open questions (resolve during implementation)

1. **CSRF fetch endpoint over HTTP.** Playwright reads `window.csrfToken`
   from JS; the HTTP path needs the REST call that mints it. If it can't be
   hit headless, the HTTP path may return cookies only and let the
   **Playwright** path supply CSRF. GET-only studio listing works without
   CSRF, so this does **not** block the prod-studio goal — only non-GET
   prod-studio calls would.
2. **`cryptography` availability.** Confirm it's already a dependency; if
   not, add it (pinned) to `pyproject.toml`.
3. **Captcha trigger.** The CAS JS has captcha logic (`validate-captcha`,
   `service/check/normal/<user>`). If this account triggers it, HTTP login
   self-test fails and we fall to Playwright (which also can't solve a
   captcha) → manual-cookie message. Acceptable per design (option C).

---

## 8. Non-goals

- Not rewriting the request/header layer (`auth.py` header crafting stays).
- Not changing the prod write-gate or any tool signatures.
- Not solving captcha/MFA automatically — manual-cookie fallback is the
  honest endpoint.
