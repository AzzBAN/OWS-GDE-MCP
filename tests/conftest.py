"""Shared pytest fixtures for the OWS MCP test suite.

Currently provides the autouse auth-cache reset that was copy-pasted (in
slightly different forms) across several test files. The `fake_settings` and
`prod_writable` fixtures stay per-file because their tenant/URL/cred shapes
genuinely differ between test modules — forcing one shape would break tests.
"""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _clear_auth_cache() -> None:
    """Reset per-process auth state before each test so each starts clean.

    Strict superset of every local copy: clears the auth cache, the relogin
    locks, and the last-relogin timestamp dict so a prior test's 5-second
    relogin debounce window can't suppress a fresh test's relogin.
    """
    from ows_gde_mcp import client as client_mod

    client_mod._auth_cache.clear()
    client_mod._relogin_locks.clear()
    client_mod._last_relogin_at.clear()
