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
