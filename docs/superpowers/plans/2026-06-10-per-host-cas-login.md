# Per-Host CAS Login Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make prod **studio** API calls work by authenticating CAS per-host (HTTP-primary login, Playwright fallback) and letting POST-based studio *reads* clear the prod write-gate via a `confirm` param.

**Architecture:** Auth state moves from per-tenant to per-**host** (the `netloc` of the resolved base URL). Each host authenticates independently through a three-step chain: pure-HTTP CAS login → Playwright fallback → actionable manual-cookie error. Testbed (studio == runtime host) keeps one login; prod (two hosts) gets two.

**Tech Stack:** Python 3.11+, httpx, cryptography (RSA-OAEP/SHA-256), Playwright (optional fallback), pytest + pytest-httpx.

**Spec:** `docs/superpowers/specs/2026-06-10-per-host-cas-login-design.md`

---

## File Structure

| File | Responsibility |
|------|----------------|
| `src/ows_gde_mcp/hosts.py` | **NEW** — `host_of(base_url) -> str` helper (urlsplit netloc). Shared by client + login modules. |
| `src/ows_gde_mcp/auth_login_http.py` | **NEW** — pure-HTTP CAS login for one base URL: scrape, RSA-OAEP encrypt, POST, self-test. Returns `(cookie_header, csrf_token \| None)`. |
| `src/ows_gde_mcp/auth_login.py` | **MODIFY** — Playwright login parametrized by base URL instead of `surfaces[0]`. |
| `src/ows_gde_mcp/client.py` | **MODIFY** — auth cache / locks / debounce keyed by host; `refresh_host_session`; login chain. |
| `src/ows_gde_mcp/tools/*.py` | **MODIFY** — add `confirm` param to `get_model_schema`, `get_model`. |
| `pyproject.toml` | **MODIFY** — pin `cryptography` as a direct dep. |
| `.env.example`, `README.md` | **MODIFY** — reframe auth (creds primary, Playwright optional). |
| `tests/test_hosts.py`, `tests/test_auth_login_http.py`, `tests/test_per_host_cache.py` | **NEW** — unit tests. |

---

## Task 1: `host_of` helper + pin cryptography

**Files:**
- Create: `src/ows_gde_mcp/hosts.py`
- Create: `tests/test_hosts.py`
- Modify: `pyproject.toml` (dependencies list)

- [ ] **Step 1: Write the failing test**

```python
# tests/test_hosts.py
import pytest
from ows_gde_mcp.hosts import host_of


@pytest.mark.parametrize("url,expected", [
    ("https://1057-sg.teleows.com", "1057-sg.teleows.com"),
    ("https://1057-sg-studio.teleows.com/", "1057-sg-studio.teleows.com"),
    ("https://1057-sg.teleows.com:443/path?q=1", "1057-sg.teleows.com:443"),
    ("https://A.Example.COM/x", "a.example.com"),
])
def test_host_of(url, expected):
    assert host_of(url) == expected


def test_host_of_rejects_relative():
    with pytest.raises(ValueError):
        host_of("/portal/web/rest")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/azhar/Documents/Huawei/OWS_MCP && .venv/bin/pytest tests/test_hosts.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'ows_gde_mcp.hosts'`

- [ ] **Step 3: Write minimal implementation**

```python
# src/ows_gde_mcp/hosts.py
"""Resolve a base URL to its host (netloc), normalized for use as an auth-cache key.

Auth state in this MCP is keyed by host, not tenant: a CAS session cookie is
bound to the host that issued it. Testbed's studio and runtime share one host
(so one login covers both); prod's are distinct hosts (so each needs its own
login). `host_of` produces the canonical key both the client and the login
modules agree on.
"""

from __future__ import annotations

from urllib.parse import urlsplit


def host_of(base_url: str) -> str:
    """Return the lowercased netloc (host[:port]) of an absolute URL.

    Raises:
        ValueError: if `base_url` has no network location (e.g. a relative path).
    """
    netloc = urlsplit(base_url).netloc
    if not netloc:
        raise ValueError(f"base_url has no host: {base_url!r}")
    return netloc.lower()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/pytest tests/test_hosts.py -v`
Expected: PASS (5 cases)

- [ ] **Step 5: Pin cryptography as a direct dependency**

In `pyproject.toml`, add to the `dependencies` list (it's currently only transitive):

```toml
dependencies = [
    "mcp[cli]>=1.2.0,<2",
    "httpx>=0.27,<0.29",
    "pydantic>=2.7,<3",
    "pydantic-settings>=2.4,<3",
    "python-dotenv>=1.0,<2",
    "cryptography>=43,<49",
]
```

- [ ] **Step 6: Commit**

```bash
git add src/ows_gde_mcp/hosts.py tests/test_hosts.py pyproject.toml
git commit -m "feat: add host_of helper and pin cryptography dep"
```

---

## Task 2: RSA-OAEP password encryption

The browser encrypts the password with WebCrypto `RSA-OAEP` + `SHA-256`,
using the PEM public key (`rsaPubBase64Str`) from the login page, then
base64-encodes the ciphertext. This reproduces that exactly. It's a pure
function — testable via encrypt→decrypt round-trip with a generated keypair.

**Files:**
- Create: `src/ows_gde_mcp/auth_login_http.py` (this function only for now)
- Test: `tests/test_auth_login_http.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_auth_login_http.py
import base64

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from ows_gde_mcp.auth_login_http import rsa_oaep_encrypt


def _keypair_pem() -> tuple[str, rsa.RSAPrivateKey]:
    priv = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    pub_pem = priv.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()
    return pub_pem, priv


def test_rsa_oaep_encrypt_roundtrip():
    pub_pem, priv = _keypair_pem()
    ciphertext_b64 = rsa_oaep_encrypt("Ajang03212@!", pub_pem)
    # Server decrypts with RSA-OAEP/SHA-256 — confirm our output round-trips.
    plaintext = priv.decrypt(
        base64.b64decode(ciphertext_b64),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    assert plaintext.decode() == "Ajang03212@!"


def test_rsa_oaep_encrypt_accepts_pem_with_escaped_newlines():
    # The login page embeds the key as a JS string with literal "\n".
    pub_pem, priv = _keypair_pem()
    escaped = pub_pem.replace("\n", "\\n")
    ciphertext_b64 = rsa_oaep_encrypt("secret", escaped)
    plaintext = priv.decrypt(
        base64.b64decode(ciphertext_b64),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    assert plaintext.decode() == "secret"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/azhar/Documents/Huawei/OWS_MCP && .venv/bin/pytest tests/test_auth_login_http.py -v`
Expected: FAIL — `ImportError: cannot import name 'rsa_oaep_encrypt'`

- [ ] **Step 3: Write minimal implementation**

```python
# src/ows_gde_mcp/auth_login_http.py
"""Pure-HTTP CAS login for one OWS host.

Reproduces the browser CAS flow without a headless browser:
  1. GET /dspcas/login    -> scrape `execution` token + RSA public key
  2. RSA-OAEP/SHA-256 encrypt the password with that key (base64 ciphertext)
  3. POST /dspcas/login    -> follow redirects, collect session cookies
  4. self-test the session before returning

Credentials never appear in logs or error messages. Raises HttpLoginError on
any failure so the caller can fall back to Playwright.
"""

from __future__ import annotations

import base64

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


class HttpLoginError(RuntimeError):
    """HTTP CAS login could not establish a session. Caller should fall back."""


def rsa_oaep_encrypt(plaintext: str, public_key_pem: str) -> str:
    """Encrypt `plaintext` with RSA-OAEP/SHA-256, return base64 ciphertext.

    Mirrors the browser's WebCrypto `encrypt({name:'RSA-OAEP'}, key, ...)`
    where the key was imported with hash 'SHA-256'. `public_key_pem` may
    contain literal `\\n` sequences (as embedded in the login page JS); they
    are normalised to real newlines before parsing.
    """
    pem = public_key_pem.replace("\\n", "\n").strip()
    key = serialization.load_pem_public_key(pem.encode())
    ciphertext = key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return base64.b64encode(ciphertext).decode("ascii")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/pytest tests/test_auth_login_http.py -v`
Expected: PASS (2 cases)

- [ ] **Step 5: Commit**

```bash
git add src/ows_gde_mcp/auth_login_http.py tests/test_auth_login_http.py
git commit -m "feat: RSA-OAEP password encryption for HTTP CAS login"
```

---

## Task 3: Scrape the login page (execution token + public key)

The login page embeds three hidden values we need: `execution`,
`rsaPubBase64Str` (a JS string assignment), and `rsaPubVersion`. This is a
pure parse function — no I/O — testable against an inline fixture.

**Files:**
- Modify: `src/ows_gde_mcp/auth_login_http.py` (add `parse_login_page`)
- Test: `tests/test_auth_login_http.py` (add cases)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/test_auth_login_http.py
from ows_gde_mcp.auth_login_http import parse_login_page

_LOGIN_HTML = '''
<form id="submitForm" method="post" onsubmit="return checkSubmit()">
  <input name="execution" value="e91fdd65-7952-47c7_TOKEN" type="hidden" />
  <input name="rsaPubVersion" value="1754756346738" type="hidden" />
</form>
<script>
  var rsaPubBase64Str = "-----BEGIN PUBLIC KEY-----\\nMIIBojANBg==\\n-----END PUBLIC KEY-----";
  var rsaPubVersion = "1754756346738";
</script>
'''


def test_parse_login_page_extracts_fields():
    parsed = parse_login_page(_LOGIN_HTML)
    assert parsed.execution == "e91fdd65-7952-47c7_TOKEN"
    assert parsed.rsa_pub_version == "1754756346738"
    assert parsed.rsa_pub_pem.startswith("-----BEGIN PUBLIC KEY-----")
    assert "MIIBojANBg==" in parsed.rsa_pub_pem


def test_parse_login_page_missing_execution_raises():
    import pytest
    with pytest.raises(Exception):
        parse_login_page("<html>no form here</html>")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/pytest tests/test_auth_login_http.py -k parse_login_page -v`
Expected: FAIL — `ImportError: cannot import name 'parse_login_page'`

- [ ] **Step 3: Write minimal implementation**

```python
# append to src/ows_gde_mcp/auth_login_http.py
import re
from dataclasses import dataclass

_EXECUTION_RE = re.compile(r'name="execution"\s+value="([^"]+)"')
_PUBKEY_RE = re.compile(r'rsaPubBase64Str\s*=\s*"([^"]+)"')
_PUBVER_RE = re.compile(r'rsaPubVersion\s*=\s*"([^"]+)"')


@dataclass
class LoginPage:
    """The three hidden values scraped from GET /dspcas/login."""
    execution: str
    rsa_pub_pem: str       # PEM, real newlines (literal \n already normalised)
    rsa_pub_version: str


def parse_login_page(html: str) -> LoginPage:
    """Extract `execution`, `rsaPubBase64Str`, `rsaPubVersion` from login HTML.

    Raises:
        HttpLoginError: if any required field is absent (page layout changed,
            or we were served something other than the login form).
    """
    exec_m = _EXECUTION_RE.search(html)
    pub_m = _PUBKEY_RE.search(html)
    ver_m = _PUBVER_RE.search(html)
    if not exec_m or not pub_m:
        raise HttpLoginError(
            "Could not parse CAS login page (missing execution token or public "
            "key). The page layout may have changed."
        )
    return LoginPage(
        execution=exec_m.group(1),
        rsa_pub_pem=pub_m.group(1).replace("\\n", "\n"),
        rsa_pub_version=ver_m.group(1) if ver_m else "",
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/pytest tests/test_auth_login_http.py -k parse_login_page -v`
Expected: PASS (2 cases)

- [ ] **Step 5: Commit**

```bash
git add src/ows_gde_mcp/auth_login_http.py tests/test_auth_login_http.py
git commit -m "feat: parse CAS login page for execution token and public key"
```

---

## Task 4: HTTP login orchestrator (`http_login`)

Ties the pieces together for one base URL: GET login page → encrypt →
POST → follow redirects → self-test. Async, uses `httpx.AsyncClient` with
`follow_redirects=True` and a cookie jar. Tested with `pytest-httpx`.

**Files:**
- Modify: `src/ows_gde_mcp/auth_login_http.py` (add `http_login`)
- Test: `tests/test_auth_login_http.py` (add cases)

- [ ] **Step 1: Write the failing test**

```python
# append to tests/test_auth_login_http.py
import httpx
import pytest

from ows_gde_mcp.auth_login_http import http_login, HttpLoginError


@pytest.mark.asyncio
async def test_http_login_success(httpx_mock):
    pub_pem, _ = _keypair_pem()
    esc = pub_pem.replace(chr(10), "\\n")  # PEM as embedded JS string (literal \n)
    login_html = (
        '<input name="execution" value="EXEC1" type="hidden" />'
        f'<script>var rsaPubBase64Str = "{esc}";'
        ' var rsaPubVersion = "9";</script>'
    )
    # GET login page
    httpx_mock.add_response(url="https://h.example.com/dspcas/login", text=login_html)
    # POST credentials -> success redirect chain settles 200
    httpx_mock.add_response(method="POST", url="https://h.example.com/dspcas/login",
                            status_code=200, headers={"set-cookie": "PORTAL_SESSION_ID=abc; Path=/"})
    # self-test sso/check -> true
    httpx_mock.add_response(url="https://h.example.com/portal/web/rest/sso/check", json=True)

    cookie, csrf = await http_login("https://h.example.com", "user", "pass")
    assert "PORTAL_SESSION_ID=abc" in cookie


@pytest.mark.asyncio
async def test_http_login_failed_selftest_raises(httpx_mock):
    pub_pem, _ = _keypair_pem()
    esc = pub_pem.replace(chr(10), "\\n")
    login_html = (
        '<input name="execution" value="E"/>'
        f'<script>var rsaPubBase64Str="{esc}";var rsaPubVersion="9";</script>'
    )
    httpx_mock.add_response(url="https://h.example.com/dspcas/login", text=login_html)
    httpx_mock.add_response(method="POST", url="https://h.example.com/dspcas/login", status_code=200)
    # self-test returns false -> not really logged in
    httpx_mock.add_response(url="https://h.example.com/portal/web/rest/sso/check", json=False)

    with pytest.raises(HttpLoginError):
        await http_login("https://h.example.com", "user", "pass")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/pytest tests/test_auth_login_http.py -k http_login -v`
Expected: FAIL — `ImportError: cannot import name 'http_login'`

- [ ] **Step 3: Write minimal implementation**

```python
# append to src/ows_gde_mcp/auth_login_http.py
import httpx


async def http_login(base_url: str, username: str, password: str) -> tuple[str, str | None]:
    """Run a pure-HTTP CAS login against `base_url`. Return (cookie_header, csrf).

    `csrf` may be None — GET studio reads don't need it, and the caller's
    Playwright path can supply it later if a non-GET requires it.

    Raises:
        HttpLoginError: on any HTTP failure, parse failure, or failed
            self-test. The caller falls back to Playwright. Never includes
            the password in its message.
    """
    base = base_url.rstrip("/")
    async with httpx.AsyncClient(base_url=base, follow_redirects=True, timeout=30.0) as c:
        try:
            page_resp = await c.get("/dspcas/login")
            page_resp.raise_for_status()
            page = parse_login_page(page_resp.text)
            enc_pw = rsa_oaep_encrypt(password, page.rsa_pub_pem)
            await c.post(
                "/dspcas/login",
                data={
                    "username": username,
                    "password": enc_pw,
                    "execution": page.execution,
                    "_eventId": "submit",
                    "rsaPubVersion": page.rsa_pub_version,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
        except HttpLoginError:
            raise
        except Exception as e:
            raise HttpLoginError(f"HTTP CAS login to {host_only(base)} failed: {e}") from e

        # Self-test: confirm the session is real before exporting cookies.
        try:
            check = await c.get(
                "/portal/web/rest/sso/check",
                headers={"X-Requested-With": "XMLHttpRequest"},
            )
            alive = check.status_code == 200 and check.json() is True
        except Exception:
            alive = False
        if not alive:
            raise HttpLoginError(
                f"HTTP CAS login to {host_only(base)} did not establish a live "
                "session (sso/check not true) — likely captcha/MFA. Falling back."
            )

        cookie_header = "; ".join(f"{c_.name}={c_.value}" for c_ in c.cookies.jar)
        csrf = await _fetch_csrf(c)
    if not cookie_header:
        raise HttpLoginError(f"HTTP CAS login to {host_only(base)} returned no cookies.")
    return cookie_header, csrf


def host_only(base_url: str) -> str:
    """Host for log/error messages (no credentials ever included)."""
    from ows_gde_mcp.hosts import host_of
    return host_of(base_url)


async def _fetch_csrf(client: httpx.AsyncClient) -> str | None:
    """Best-effort CSRF fetch. Returns None if unavailable (GET reads don't need it).

    OPEN QUESTION (spec §7.1): confirm the REST endpoint the SPA uses to mint
    `window.csrfToken`. Until verified, return None — non-GET prod-studio
    calls will trigger the Playwright path which captures CSRF reliably.
    """
    return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/pytest tests/test_auth_login_http.py -k http_login -v`
Expected: PASS (2 cases)

- [ ] **Step 5: Commit**

```bash
git add src/ows_gde_mcp/auth_login_http.py tests/test_auth_login_http.py
git commit -m "feat: HTTP CAS login orchestrator with self-test"
```

---

## Task 5: Parametrize Playwright login by base URL

The existing `login(tenant, settings)` in `auth_login.py` always logs into
`surfaces[0]`. Add a `base_url` parameter so the caller picks the host. Keep
backward-compat: when `base_url` is None, fall back to the old
surface-picking behaviour (existing tests in `test_auto_relogin.py` keep
passing).

**Files:**
- Modify: `src/ows_gde_mcp/auth_login.py:23-72`
- Test: `tests/test_auth_login_http.py` (signature smoke test — full flow needs a browser, out of scope for unit tests)

- [ ] **Step 1: Change the signature (surgical edit)**

Replace the `login` signature and the base-URL resolution block. Find:

```python
async def login(tenant: Tenant, settings: Settings) -> tuple[str, str]:
```

Replace with:

```python
async def login(
    tenant: Tenant, settings: Settings, base_url: str | None = None
) -> tuple[str, str]:
```

- [ ] **Step 2: Use the passed base_url when given**

Find this block (around lines 50-57):

```python
    surfaces = settings.configured_surfaces(tenant)
    if not surfaces:
        raise RuntimeError(
            f"Cannot run CAS login for tenant '{tenant.value}': no studio or runtime "
            f"URL is configured. Set OWS_{tenant_upper}_RUNTIME_URL or "
            f"OWS_{tenant_upper}_STUDIO_URL in .env."
        )
    base_url = settings.base_url(tenant, surfaces[0])
```

Replace with:

```python
    if base_url is None:
        surfaces = settings.configured_surfaces(tenant)
        if not surfaces:
            raise RuntimeError(
                f"Cannot run CAS login for tenant '{tenant.value}': no studio or "
                f"runtime URL is configured. Set OWS_{tenant_upper}_RUNTIME_URL or "
                f"OWS_{tenant_upper}_STUDIO_URL in .env."
            )
        base_url = settings.base_url(tenant, surfaces[0])
```

The rest of the function (which already uses the `base_url` local) is unchanged.

- [ ] **Step 3: Run existing Playwright-login tests to confirm no regression**

Run: `.venv/bin/pytest tests/test_auto_relogin.py -v`
Expected: PASS (existing tests monkeypatch `_cas_login`, so the new optional
arg doesn't break them)

- [ ] **Step 4: Commit**

```bash
git add src/ows_gde_mcp/auth_login.py
git commit -m "feat: parametrize Playwright login by base_url"
```

---

## Task 6: Re-key client auth by host + login chain

The core fix. Change `client.py` so the auth cache, relogin lock, and
debounce are keyed by **host** (not tenant), and `refresh_host_session`
runs the HTTP→Playwright→error chain. `OwsClient` learns its own host.

**Files:**
- Modify: `src/ows_gde_mcp/client.py` (cache decls ~48-94, `for_surface` ~195-205, `__init__` ~175-193, `_refresh_session` ~310-319)
- Test: `tests/test_per_host_cache.py` (new)

- [ ] **Step 1: Write the failing test**

```python
# tests/test_per_host_cache.py
import pytest

import ows_gde_mcp.client as clientmod
from ows_gde_mcp.client import OwsClient, refresh_host_session
from ows_gde_mcp.config import Settings, Surface, Tenant


@pytest.fixture
def settings(monkeypatch):
    # prod: two distinct hosts; testbed: one shared host
    monkeypatch.setenv("OWS_PROD_STUDIO_URL", "https://studio.example.com")
    monkeypatch.setenv("OWS_PROD_RUNTIME_URL", "https://runtime.example.com")
    monkeypatch.setenv("OWS_PROD_USERNAME", "u")
    monkeypatch.setenv("OWS_PROD_PASSWORD", "p")
    monkeypatch.setenv("OWS_TESTBED_STUDIO_URL", "https://same.example.com")
    monkeypatch.setenv("OWS_TESTBED_RUNTIME_URL", "https://same.example.com")
    return Settings()


@pytest.mark.asyncio
async def test_distinct_hosts_login_independently(settings, monkeypatch):
    clientmod._auth_cache.clear()
    calls: list[str] = []

    async def fake_http_login(base_url, username, password):
        calls.append(base_url)
        return (f"COOKIE_FOR={base_url}", "csrf123")

    monkeypatch.setattr(clientmod, "_http_login", fake_http_login)

    await refresh_host_session("https://studio.example.com", Tenant.PROD, settings)
    await refresh_host_session("https://runtime.example.com", Tenant.PROD, settings)

    # two distinct hosts -> two logins, two cache entries
    assert calls == ["https://studio.example.com", "https://runtime.example.com"]
    assert "studio.example.com" in clientmod._auth_cache
    assert "runtime.example.com" in clientmod._auth_cache


@pytest.mark.asyncio
async def test_http_failure_falls_back_to_playwright(settings, monkeypatch):
    clientmod._auth_cache.clear()
    pw_calls: list[str] = []

    async def fail_http(base_url, username, password):
        from ows_gde_mcp.auth_login_http import HttpLoginError
        raise HttpLoginError("captcha")

    async def fake_pw(tenant, s, base_url=None):
        pw_calls.append(base_url)
        return ("PW_COOKIE=1", "pwcsrf")

    monkeypatch.setattr(clientmod, "_http_login", fail_http)
    monkeypatch.setattr(clientmod, "_cas_login", fake_pw)

    await refresh_host_session("https://studio.example.com", Tenant.PROD, settings)
    assert pw_calls == ["https://studio.example.com"]
    assert clientmod._auth_cache["studio.example.com"].cookie == "PW_COOKIE=1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/pytest tests/test_per_host_cache.py -v`
Expected: FAIL — `ImportError: cannot import name 'refresh_host_session'`

- [ ] **Step 3: Re-key the module-level caches**

In `client.py`, replace the cache/lock declarations (currently keyed by
`Tenant`) with host-keyed dicts and add the HTTP-login import:

```python
from ows_gde_mcp.auth_login import login as _cas_login
from ows_gde_mcp.auth_login_http import HttpLoginError, http_login as _http_login
from ows_gde_mcp.hosts import host_of

# Per-process AuthContext cache, keyed by HOST (netloc). A CAS cookie is bound
# to its issuing host; testbed's shared host yields one entry, prod's two.
_auth_cache: dict[str, AuthContext] = {}
_relogin_locks: dict[str, asyncio.Lock] = {}
_last_relogin_at: dict[str, float] = {}


def _relogin_lock(host: str) -> asyncio.Lock:
    lock = _relogin_locks.get(host)
    if lock is None:
        lock = asyncio.Lock()
        _relogin_locks[host] = lock
    return lock
```

- [ ] **Step 4: Commit checkpoint**

```bash
git add src/ows_gde_mcp/client.py tests/test_per_host_cache.py
git commit -m "wip: re-key client auth caches by host"
```

- [ ] **Step 5: Add `refresh_host_session` (the login chain)**

Replace the old `refresh_tenant_session` with this host-keyed version:

```python
async def refresh_host_session(base_url: str, tenant: Tenant, settings: Settings) -> None:
    """Authenticate `base_url`'s host via HTTP→Playwright→error, cache the result.

    Serialised + 5s-debounced per host. First step to yield a live session wins.
    """
    host = host_of(base_url)
    async with _relogin_lock(host):
        if time.monotonic() - _last_relogin_at.get(host, 0.0) < 5.0:
            return
        username, password = _creds_for(tenant, settings)
        if not username or not password:
            raise RuntimeError(
                f"No credentials to authenticate host '{host}'. Set "
                f"OWS_{tenant.value.upper()}_USERNAME / _PASSWORD in .env."
            )

        cookie: str
        csrf: str | None
        try:
            cookie, csrf = await _http_login(base_url, username, password)
        except HttpLoginError as http_err:
            # Fall back to Playwright for this exact host.
            try:
                cookie, csrf = await _cas_login(tenant, settings, base_url=base_url)
            except RuntimeError as pw_err:
                raise RuntimeError(
                    f"Auto-login failed for '{host}'. HTTP login: {http_err}. "
                    f"Playwright fallback: {pw_err}. Install Playwright with "
                    "`uv pip install -e '.[login]' && playwright install chromium`, "
                    f"or paste a cookie into OWS_{tenant.value.upper()}_SESSION_COOKIE."
                ) from pw_err

        auth = _auth_cache.get(host)
        if auth is None:
            auth = AuthContext(cookie=cookie, csrf_token=csrf)
            _auth_cache[host] = auth
        else:
            auth.cookie = cookie
            if csrf:
                auth.csrf_token = csrf
        _last_relogin_at[host] = time.monotonic()


def _creds_for(tenant: Tenant, settings: Settings) -> tuple[str | None, str | None]:
    if tenant == Tenant.TESTBED:
        return settings.OWS_TESTBED_USERNAME, settings.OWS_TESTBED_PASSWORD
    return settings.OWS_PROD_USERNAME, settings.OWS_PROD_PASSWORD
```

- [ ] **Step 6: Key `_auth_for_tenant` and `for_surface` by host**

`_auth_for_tenant(tenant, settings)` becomes host-aware. Change its cache
key and add the base_url. Rename to `_auth_for_host` and update callers:

```python
def _auth_for_host(base_url: str, tenant: Tenant, settings: Settings) -> AuthContext:
    host = host_of(base_url)
    cached = _auth_cache.get(host)
    if cached is not None:
        return cached
    # cookie/csrf from env are per-tenant (captured manually); seed the host
    # entry with them, else a placeholder that the first 302 will refresh.
    if tenant == Tenant.TESTBED:
        cookie = settings.OWS_TESTBED_SESSION_COOKIE
        csrf = settings.OWS_TESTBED_CSRF_TOKEN
        username = settings.OWS_TESTBED_USERNAME
    else:
        cookie = settings.OWS_PROD_SESSION_COOKIE
        csrf = settings.OWS_PROD_CSRF_TOKEN
        username = settings.OWS_PROD_USERNAME
    if not cookie:
        if not username:
            raise RuntimeError(
                f"No session cookie configured for host '{host}' and no "
                f"OWS_{tenant.value.upper()}_USERNAME / _PASSWORD for auto-login. "
                f"See README.md."
            )
        cookie = "_placeholder_=1"
    auth = AuthContext(cookie=cookie, csrf_token=csrf)
    _auth_cache[host] = auth
    return auth
```

In `for_surface`, resolve base then auth by host:

```python
    @classmethod
    def for_surface(cls, tenant: Tenant, surface: Surface, settings: Settings) -> OwsClient:
        base = settings.base_url(tenant, surface)
        auth = _auth_for_host(base, tenant, settings)
        return cls(base, auth, tenant, surface, settings)
```

- [ ] **Step 7: Point `_refresh_session` at the client's own base URL**

`OwsClient.__init__` already gets `base_url`. Store it (`self._base_url =
base_url.rstrip("/")`) and change `_refresh_session`:

```python
    async def _refresh_session(self) -> None:
        await refresh_host_session(self._base_url, self._tenant, self._settings)
```

Also update `prewarm_session` to call `refresh_host_session(base, ...)` using
`settings.base_url(tenant, surface)` for each configured surface, so both prod
hosts get prewarmed.

- [ ] **Step 8: Run the per-host tests + full suite**

Run: `.venv/bin/pytest tests/test_per_host_cache.py tests/test_auto_relogin.py -v`
Expected: PASS (new per-host tests + no regression)

- [ ] **Step 9: Commit**

```bash
git add src/ows_gde_mcp/client.py tests/test_per_host_cache.py
git commit -m "feat: per-host CAS auth with HTTP-primary login chain"
```

---

## Task 7: Add `confirm` param to POST-based studio reads (wall #1)

`get_model` and `get_model_schema` (in `live.py`) call `_studio_post`, which
*already accepts* `confirm` and threads it to `client.post`. The tools just
don't expose it — so on prod they can never pass `confirm=True` and die at
the write-gate. Fix: surface the param.

**Files:**
- Modify: `src/ows_gde_mcp/tools/live.py:604-640` (`get_model`)
- Modify: `src/ows_gde_mcp/tools/live.py:643-688` (`get_model_schema`)

- [ ] **Step 1: Add `confirm` to `get_model` and pass it through**

Edit the signature (lines 604-609):

```python
async def get_model(
    tenant: str,
    model_id: int,
    *,
    properties_only: bool = False,
    confirm: bool = False,
) -> dict[str, Any]:
```

And the `_studio_post` call (lines 626-630):

```python
    res = await _studio_post(
        tenant,
        "/adc-studio-model/web/rest/v1/models/query-by-id",
        params={"model_id": model_id},
        confirm=confirm,
    )
```

Add to the docstring Args: `confirm: required True on prod (this is a
read, but issues POST, which the prod write-gate guards).`

- [ ] **Step 2: Add `confirm` to `get_model_schema` and pass it through**

Edit the signature (lines 643-648):

```python
async def get_model_schema(
    tenant: str,
    project_name: str,
    module_name: str,
    model_name: str = "",
    confirm: bool = False,
) -> dict[str, Any]:
```

And the `_studio_post` call (lines 683-688):

```python
        res = await _studio_post(
            tenant,
            "/adc-studio-model/web/rest/v1/models/query-all",
            params={"project_name": project_name, "module_name": module_name},
            json={},
            confirm=confirm,
        )
```

Add the same `confirm:` docstring Args line.

- [ ] **Step 3: Verify the full suite still passes**

Run: `cd /Users/azhar/Documents/Huawei/OWS_MCP && .venv/bin/pytest -q`
Expected: PASS (no regressions)

- [ ] **Step 4: Commit**

```bash
git add src/ows_gde_mcp/tools/live.py
git commit -m "feat: expose confirm param on get_model/get_model_schema for prod"
```

---

## Task 8: Docs — reframe auth (creds primary, Playwright optional)

**Files:**
- Modify: `.env.example` (auth section)
- Modify: `README.md` (Authentication section)

- [ ] **Step 1: Reframe `.env.example` auth comments**

Replace the block above `OWS_TESTBED_SESSION_COOKIE=` so credentials are
described as the **primary** path:

```
# --- Auth (per tenant) ---
# PRIMARY: username + password. The MCP runs a pure-HTTP CAS login on demand
# (no browser needed) and caches the session per host. This is all most users
# need.
OWS_TESTBED_USERNAME=
OWS_TESTBED_PASSWORD=
OWS_PROD_USERNAME=
OWS_PROD_PASSWORD=
#
# FALLBACK: if HTTP login can't clear a host (captcha / MFA / interstitial),
# the MCP falls back to a headless Playwright login. Install only if you hit
# that error:
#     uv pip install -e '.[login]' && playwright install chromium
#
# OVERRIDE: paste a raw Cookie header + window.csrfToken from a logged-in
# browser to skip auto-login entirely (per tenant).
OWS_TESTBED_SESSION_COOKIE=
OWS_PROD_SESSION_COOKIE=
OWS_TESTBED_CSRF_TOKEN=
OWS_PROD_CSRF_TOKEN=
```

- [ ] **Step 2: Add a short README "Authentication" note**

Add under the setup section:

```markdown
## Authentication

Set `OWS_<TENANT>_USERNAME` / `_PASSWORD` in `.env`. The MCP performs a
pure-HTTP CAS login on demand and caches the session **per host** — so prod's
separate studio and runtime hosts each authenticate independently.

If HTTP login can't clear a host (captcha / MFA), install the optional
Playwright fallback:

    uv pip install -e '.[login]' && playwright install chromium

As a last resort you can paste a captured `OWS_<TENANT>_SESSION_COOKIE`
(+ `_CSRF_TOKEN`) from a logged-in browser.

Note: prod studio reads that issue POST (`get_model`, `get_model_schema`)
require `confirm=true`, like other prod write-gated calls.
```

- [ ] **Step 3: Commit**

```bash
git add .env.example README.md
git commit -m "docs: reframe auth — credentials primary, Playwright optional"
```

---

## Task 9: Live verification (the real proof)

No new code — confirm the goal against the live prod tenant via the MCP
tools. Do this after Tasks 1-8 land and the MCP is reconnected (`/mcp`) so it
re-reads the code.

- [ ] **Step 1: Prod studio GET reads now work**

Call `list_services` and `list_pages` against a known-populated prod module
(e.g. `TroubleTicket`/`TroubleTicket`). Expected: JSON with services/pages,
**not** the `…redirected to CAS` error.

- [ ] **Step 2: Prod studio POST reads work with confirm**

Call `get_model_schema(tenant="prod", project_name="TroubleTicket",
module_name="TroubleTicket", model_name="tt_troubleticket", confirm=true)`.
Expected: full property schema, not the write-gate error and not a CAS 302.

- [ ] **Step 3: Prod runtime unchanged (no regression)**

Call `whoami(prod)` and `list_processes(prod)`. Expected: still work.

- [ ] **Step 4: Testbed unchanged (no regression)**

Call `list_studio_projects(testbed)` and `list_services` on a testbed module.
Expected: still work, single login (one host).

- [ ] **Step 5: Final full test run + commit any fixes**

```bash
cd /Users/azhar/Documents/Huawei/OWS_MCP && .venv/bin/pytest -q
```
Expected: all green.
