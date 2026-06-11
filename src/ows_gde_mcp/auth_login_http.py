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
