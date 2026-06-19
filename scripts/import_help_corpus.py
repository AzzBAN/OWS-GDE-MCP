"""Import the knowledge-helper Markdown vault into the MCP help corpus.

Reads the scraped docs from a knowledge-helper `vault/` directory and emits
the shapes `ows_gde_mcp.tools.help` consumes:
  docs/help/<lang>/nav_index.json   flat [{id, parent_id, name, local, depth, path}]
  docs/help/<lang>/<local>.md       topic bodies (copied verbatim)
  docs/help/<lang>/topics.jsonl     [{id, name, local, title, text}] for fast search

Usage:
  uv run python scripts/import_help_corpus.py \
      --vault ~/codes/huaweed/knowledge-helper/vault \
      --lang en_US
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]

# Most filesystems cap a single path component at 255 bytes. Keep flattened
# slugs comfortably under that, leaving room for the ".md" suffix and a short
# disambiguating hash when we have to truncate.
_MAX_SLUG_LEN = 200


def _slug_to_local(rel: Path) -> str:
    """Stable filename for a vault topic (path-flattened, .md kept).

    Vault paths can flatten to names that exceed the filesystem's 255-byte
    component limit. When that happens we truncate and append a short hash of
    the full relative path so the name stays stable across runs and unique.
    """
    flat = "__".join(rel.with_suffix("").parts)
    flat = re.sub(r"[^A-Za-z0-9_.\-]", "-", flat)
    if len(flat) > _MAX_SLUG_LEN:
        digest = hashlib.sha1(str(rel).encode("utf-8")).hexdigest()[:12]
        flat = f"{flat[: _MAX_SLUG_LEN - len(digest) - 1]}-{digest}"
    return f"{flat}.md"


def _title_of(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, type=Path)
    ap.add_argument("--lang", default="en_US")
    args = ap.parse_args()

    src_root = args.vault.expanduser()
    if not src_root.is_dir():
        raise SystemExit(f"vault not found: {src_root}")

    out_dir = _REPO_ROOT / "docs" / "help" / args.lang
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(p for p in src_root.rglob("*.md") if ".obsidian" not in p.parts)
    nav: list[dict] = []
    jsonl_lines: list[str] = []

    for i, src in enumerate(md_files, start=1):
        rel = src.relative_to(src_root)
        local = _slug_to_local(rel)
        body = src.read_text(encoding="utf-8")
        title = _title_of(body, rel.stem)
        depth = len(rel.parts) - 1
        shutil.copyfile(src, out_dir / local)
        nav.append(
            {
                "id": i,
                "parent_id": 0,  # flat import; nav tree is not reconstructed
                "name": title,
                "local": local,
                "depth": depth,
                "path": [i],
            }
        )
        jsonl_lines.append(
            json.dumps(
                {
                    "id": i,
                    "name": title,
                    "local": local,
                    "title": title,
                    "text": body,
                }
            )
        )

    (out_dir / "nav_index.json").write_text(json.dumps(nav, indent=2), encoding="utf-8")
    (out_dir / "topics.jsonl").write_text("\n".join(jsonl_lines) + "\n", encoding="utf-8")
    print(f"Imported {len(md_files)} topics into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
