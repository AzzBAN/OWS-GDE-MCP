"""Regenerate `docs/tools.md` from the live FastMCP server.

Run after adding/changing any MCP tool:

    uv run python scripts/gen_tools_md.py

The output is a single Markdown file grouped by category, with full
signatures and the first line of each docstring.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUT_FILE = PROJECT_ROOT / "docs" / "tools.md"


def _format_type(schema: dict | None) -> str:
    """Render a JSON-Schema type spec as `int`, `str | None`, etc."""
    if not isinstance(schema, dict):
        return "?"
    if "anyOf" in schema:
        parts = [_format_type(s) for s in schema["anyOf"]]
        return " | ".join(p for p in parts if p) or "?"
    t = schema.get("type")
    if isinstance(t, list):
        return " | ".join(t)
    if t == "array":
        items = schema.get("items") or {}
        return f"list[{_format_type(items)}]"
    if t == "object":
        return "dict"
    return t or "?"


def _format_signature(tool) -> str:
    schema = tool.inputSchema or {}
    props = schema.get("properties") or {}
    required = set(schema.get("required") or [])
    parts = []
    for name, p in props.items():
        ty = _format_type(p)
        if name in required:
            parts.append(f"{name}: {ty}")
        else:
            default = p.get("default") if isinstance(p, dict) else None
            if default in (None, ""):
                parts.append(f"{name}?: {ty}")
            else:
                parts.append(f"{name}?: {ty} = {default!r}")
    return f"{tool.name}({', '.join(parts)})"


def _category(name: str) -> str:
    if name in ("status", "whoami"):
        return "Diagnostics"
    if "app_package" in name or "app_artifact" in name:
        return "Offline `.gpk` introspection (no auth)"
    return "Live OWS (require `OWS_<TENANT>_SESSION_COOKIE`)"


CATEGORY_ORDER = [
    "Diagnostics",
    "Live OWS (require `OWS_<TENANT>_SESSION_COOKIE`)",
    "Offline `.gpk` introspection (no auth)",
]


async def main() -> None:
    from ows_gde_mcp.server import mcp  # late import so .env is loaded

    tools = await mcp.list_tools()
    grouped: dict[str, list] = {c: [] for c in CATEGORY_ORDER}
    for t in tools:
        grouped[_category(t.name)].append(t)
    for c in grouped:
        grouped[c].sort(key=lambda x: x.name)

    out: list[str] = []
    out.append("# Tools — `ows-gde-mcp`")
    out.append("")
    out.append(f"Auto-generated from the FastMCP server. **{len(tools)} tools total.**")
    out.append("")
    out.append("Regenerate with `uv run python scripts/gen_tools_md.py`.")
    out.append("")

    for cat in CATEGORY_ORDER:
        items = grouped[cat]
        if not items:
            continue
        out.append(f"## {cat}")
        out.append("")
        for t in items:
            sig = _format_signature(t)
            desc = (t.description or "").strip().split("\n")[0]
            out.append(f"### `{sig}`")
            out.append("")
            if desc:
                out.append(desc)
                out.append("")

    OUT_FILE.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT_FILE} ({len(tools)} tools)")


if __name__ == "__main__":
    asyncio.run(main())
