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
