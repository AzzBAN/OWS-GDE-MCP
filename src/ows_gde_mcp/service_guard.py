"""Name-based read-only guard for OWS service invocation.

Ported from knowledge-helper/src/ows/guard.ts. Three checks, in order:
1. Reject names with path/quote characters (injection guard).
2. Reject names matching the write-operation blocklist.
3. Require a read suffix OR catalog membership.

Note on the write-keyword regex: the TypeScript source uses `\b...\b`
boundaries, but service names are snake_case and `_` counts as a word
character in both JS and Python regex, so `\bcreate\b` never matches
`sfo_order_create`. We delimit on `_` / string-edges instead so the
blocklist actually fires on snake_case write services.
"""

from __future__ import annotations

import re

from ows_gde_mcp.service_catalog import CATALOG_SERVICE_NAMES

_WRITE_KW = re.compile(
    r"(?:^|_)(create|update|delete|save|submit|insert|remove|dispatch|confirm|"
    r"approve|reject|cancel|modify|set|exec|sync|import|trigger)(?:_|$)",
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
            f"Read-only guard: service {name!r} doesn't match the read-suffix pattern "
            "(*_getList, *_query, ...) and isn't in SERVICE_CATALOG. Add it there if "
            "it's a verified read service."
        )
