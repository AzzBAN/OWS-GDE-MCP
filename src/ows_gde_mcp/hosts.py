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
