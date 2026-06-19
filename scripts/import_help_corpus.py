"""Import the knowledge-helper Markdown vault into the MCP knowledge vault.

Copies the scraped docs from a knowledge-helper `vault/` directory **verbatim**
into an Obsidian-standard Reference tree, and builds a flat sidecar search
index the MCP help tools read:

  docs/help/vault/Reference/<nav tree>/*.md   topic bodies, folders preserved
  docs/help/index/<lang>/nav_index.json       flat [{id, parent_id, name, local,
                                                     depth, path, is_folder}]
  docs/help/index/<lang>/topics.jsonl         [{id, name, local, title, text}]

It NEVER touches the curated, git-tracked parts of the vault
(`docs/help/vault/Home.md`, `docs/help/vault/00 Findings/`). Re-running it
fully regenerates only `Reference/` and the index.

`local` paths in the index are POSIX-relative to the vault root (e.g.
`Reference/Low-Code Orchestration/API Reference/X.md`), so the help tools
resolve them under `docs/help/vault/`.

Usage:
  uv run python scripts/import_help_corpus.py \
      --vault ~/codes/huaweed/knowledge-helper/vault \
      --lang en_US
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

_REFERENCE_DIRNAME = "Reference"


def _resolve_vault(out_arg: str | None) -> Path:
    """Vault dir to write into. Mirrors ows_gde_mcp.tools.help._vault_root.

    Resolution: ``--out`` -> ``OWS_VAULT_DIR`` -> ``<cwd>/ows-vault``, so the
    importer writes exactly where the MCP help tools read.
    """
    target = out_arg or os.environ.get("OWS_VAULT_DIR")
    if target:
        return Path(target).expanduser()
    return Path.cwd() / "ows-vault"


def _title_of(md: str, fallback: str) -> str:
    """Title from the first ATX heading, else front-matter `title:`, else fallback."""
    lines = md.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    # gray-matter front matter: `title: "..."` between leading --- fences.
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip().strip("\"'")
    return fallback


def _copy_reference(src_root: Path, ref_root: Path) -> None:
    """Replace `ref_root` with a verbatim copy of `src_root` (minus .obsidian)."""
    if ref_root.exists():
        shutil.rmtree(ref_root)
    shutil.copytree(
        src_root,
        ref_root,
        ignore=shutil.ignore_patterns(".obsidian", ".git", ".DS_Store"),
    )


def _build_index(vault_root: Path, ref_root: Path) -> tuple[list[dict], list[str]]:
    """Walk the Reference tree, return (nav_index, topics_jsonl_lines).

    Folders and `.md` files both become nav nodes (folders carry `is_folder`)
    so the hierarchy round-trips; only files get a topics.jsonl entry.
    """
    # Deterministic order: the Reference root, then every dir + .md file sorted.
    entries = [ref_root]
    entries += sorted(
        (p for p in ref_root.rglob("*") if p.is_dir() or p.suffix == ".md"),
        key=lambda p: p.as_posix(),
    )

    id_map: dict[Path, int] = {}
    path_map: dict[Path, list[int]] = {}
    nav: list[dict] = []
    jsonl: list[str] = []

    for i, entry in enumerate(entries, start=1):
        id_map[entry] = i
        rel = entry.relative_to(vault_root)  # e.g. Reference/.../X.md
        parent_id = id_map.get(entry.parent, 0)
        path = [*path_map.get(entry.parent, []), i]
        path_map[entry] = path
        depth = len(rel.parts) - 1

        if entry.is_dir():
            name = "Reference" if entry == ref_root else entry.name
            nav.append(
                {
                    "id": i,
                    "parent_id": parent_id,
                    "name": name,
                    "local": rel.as_posix(),
                    "depth": depth,
                    "path": path,
                    "is_folder": True,
                }
            )
            continue

        body = entry.read_text(encoding="utf-8")
        title = _title_of(body, entry.stem)
        local = rel.as_posix()
        nav.append(
            {
                "id": i,
                "parent_id": parent_id,
                "name": title,
                "local": local,
                "depth": depth,
                "path": path,
                "is_folder": False,
            }
        )
        jsonl.append(
            json.dumps(
                {"id": i, "name": title, "local": local, "title": title, "text": body}
            )
        )

    return nav, jsonl


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, type=Path,
                    help="Source knowledge-helper vault to import from.")
    ap.add_argument("--out", default=None, type=str,
                    help="Destination vault dir (default: OWS_VAULT_DIR or ./ows-vault).")
    ap.add_argument("--lang", default="en_US")
    args = ap.parse_args()

    src_root = args.vault.expanduser()
    if not src_root.is_dir():
        raise SystemExit(f"vault not found: {src_root}")

    vault_root = _resolve_vault(args.out)
    ref_root = vault_root / _REFERENCE_DIRNAME
    index_dir = vault_root / ".index" / args.lang
    index_dir.mkdir(parents=True, exist_ok=True)

    _copy_reference(src_root, ref_root)
    nav, jsonl = _build_index(vault_root, ref_root)

    (index_dir / "nav_index.json").write_text(json.dumps(nav, indent=2), encoding="utf-8")
    (index_dir / "topics.jsonl").write_text("\n".join(jsonl) + "\n", encoding="utf-8")

    topic_count = len(jsonl)
    folder_count = len(nav) - topic_count
    print(
        f"Imported {topic_count} topics ({folder_count} folders) into {ref_root}\n"
        f"Index written to {index_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
