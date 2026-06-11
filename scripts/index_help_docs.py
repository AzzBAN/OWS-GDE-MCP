"""Build a flat search index from the local OWS help cache.

The help fetcher writes 1387+ HTML topic files to `docs/help/<lang>/`.
`search_help` originally read all of them from disk on every call and
re-parsed each HTML, which scales poorly. This script extracts the
title + plain text once and writes one JSON object per line to
`topics.jsonl`. `search_help` then reads that single file and skips
HTML parsing entirely — search drops from a few hundred ms to ~10 ms.

Run after the fetcher:

    uv run python scripts/index_help_docs.py

Idempotent: re-running rebuilds the index from the current HTML cache.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ows_gde_mcp.tools.help import _extract_topic_body

ROOT = Path(__file__).resolve().parent.parent
HELP_ROOT = ROOT / "docs" / "help"


def index_lang(lang_dir: Path) -> int:
    """Build `topics.jsonl` from `nav_index.json` + on-disk topic HTML."""
    nav_path = lang_dir / "nav_index.json"
    if not nav_path.exists():
        print(f"  skip: {nav_path} missing")
        return 0

    nav = json.loads(nav_path.read_text(encoding="utf-8"))
    out_path = lang_dir / "topics.jsonl"
    written = 0
    missing = 0
    seen_locals: set[str] = set()

    with out_path.open("w", encoding="utf-8") as f:
        for row in nav:
            local = row.get("local")
            if not local or local in seen_locals:
                continue
            seen_locals.add(local)
            file_path = lang_dir / local
            if not file_path.exists():
                missing += 1
                continue
            html = file_path.read_text(encoding="utf-8")
            title, text, parent = _extract_topic_body(html)
            entry = {
                "id": row.get("id"),
                "name": row.get("name"),
                "local": local,
                "title": title,
                "text": text,
                "parent": parent,
            }
            f.write(json.dumps(entry, ensure_ascii=False))
            f.write("\n")
            written += 1

    size_kb = out_path.stat().st_size // 1024
    print(f"  wrote {written} topics to {out_path.name} ({size_kb} KB), {missing} missing files")
    return written


def main() -> int:
    if not HELP_ROOT.exists():
        print(f"No help cache at {HELP_ROOT} — run scripts/fetch_help_docs.py first.")
        return 1
    total = 0
    for lang_dir in sorted(HELP_ROOT.iterdir()):
        if not lang_dir.is_dir():
            continue
        print(f"Indexing {lang_dir.name}...")
        total += index_lang(lang_dir)
    print(f"\nIndexed {total} topics across all languages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
