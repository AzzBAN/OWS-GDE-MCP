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
import re
from dataclasses import dataclass

import httpx
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


class HttpLoginError(RuntimeError):
    """HTTP CAS login could not establish a session. Caller should fall back."""


def rsa_oaep_encrypt(plaintext: str, public_key_pem: str) -> str:
    """Encrypt `plaintext` with RSA-OAEP/SHA-256, return base64 ciphertext.

    Mirrors the browser's WebCrypto `encrypt({name:'RSA-OAEP'}, key, ...)`
    where the key was imported with hash 'SHA-256'. `public_key_pem` may
    contain literal `\\n` sequences and JS/JSON-escaped `\\/` forward slashes
    (as embedded in the login page JS); both are unescaped before parsing.
    """
    pem = public_key_pem.replace("\\/", "/").replace("\\n", "\n").strip()
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


_EXECUTION_RE = re.compile(r'name="execution"\s+value="([^"]+)"')
_PUBKEY_RE = re.compile(r'rsaPubBase64Str\s*=\s*"([^"]+)"')
_PUBVER_RE = re.compile(r'rsaPubVersion\s*=\s*"([^"]+)"')


@dataclass
class LoginPage:
    """The three hidden values scraped from GET /dspcas/login."""

    execution: str
    rsa_pub_pem: str       # PEM, real newlines + '/' (literal \n and \/ normalised)
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
        rsa_pub_pem=pub_m.group(1).replace("\\/", "/").replace("\\n", "\n"),
        rsa_pub_version=ver_m.group(1) if ver_m else "",
    )


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


_UICONFIG_PATH = "/portal/web/rest/v1/uiconfig/info"


async def _fetch_csrf(client: httpx.AsyncClient) -> str | None:
    """Fetch the CSRF token via the SPA's uiconfig endpoint.

    GET /portal/web/rest/v1/uiconfig/info returns JSON with a `csrf_token`
    field — the same 48-digit token the SPA stores in `localStorage.csrfTokens`
    (the SPA's `getADCCsrfUrl()` builds this path from the constant
    `"/web/rest/v1/uiconfig/info"` + portal prefix). Verified on both testbed
    and prod. Best-effort: returns None on any failure so the caller falls back
    to the `OWS_<TENANT>_CSRF_TOKEN` env var or the Playwright path.
    """
    try:
        resp = await client.get(
            _UICONFIG_PATH,
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        resp.raise_for_status()
        token = resp.json().get("csrf_token")
        return token if isinstance(token, str) and token else None
    except Exception:
        return None
