"""Fetch the OWS Studio help corpus to a local cache.

Run once when you set up the repo, or whenever you want to refresh:

    uv run python scripts/fetch_help_docs.py

Downloads:
- The nav tree from `/adc-studio-project-mgt/web/rest/help/doc/en_US/data/nav_json.js`
- Every topic HTML referenced by the nav (typically ~3.6k pages)
- Saves them to `docs/help/en_US/` so the runtime MCP tools can read locally.

Authentication uses the existing `OwsClient` (CAS / cookie / auto-relogin),
so set `OWS_TESTBED_USERNAME` / `OWS_TESTBED_PASSWORD` (or session cookie)
in `.env` first. The corpus is identical between testbed and prod tenants
— testbed is preferred to avoid loading prod with thousands of GETs.

After running this once, the MCP help tools (`tools/help.py`) require no
network access — they read from the cache only.
"""

from __future__ import annotations

import asyncio
import json
import re
import sys
from pathlib import Path

from ows_gde_mcp.client import OwsClient
from ows_gde_mcp.config import Surface, Tenant, settings

HELP_BASE = "/adc-studio-project-mgt/web/rest/help/doc/en_US"
NAV_PATH = f"{HELP_BASE}/data/nav_json.js"

# Default destination: <repo>/docs/help/en_US
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs" / "help" / "en_US"

# Concurrency limit — be polite to the help server.
CONCURRENCY = 8

# JSONP-ish nav payload preamble.
_NAV_RE = re.compile(r"naviData\s*=\s*(\[.*?\]);", re.DOTALL)


async def _fetch_nav(client: OwsClient) -> list[dict]:
    print(f"GET  {NAV_PATH}")
    text = await client.get(NAV_PATH)
    if not isinstance(text, str):
        raise RuntimeError("nav_json.js returned non-text payload")
    m = _NAV_RE.search(text)
    if not m:
        raise RuntimeError("nav_json.js shape changed; could not extract naviData=[...]")
    return json.loads(m.group(1))


def _flatten(nodes: list[dict]) -> list[dict]:
    """Flatten the nav tree into one list, preserving id/parent/depth/local."""
    out: list[dict] = []

    def walk(items: list[dict], parents: list[int]) -> None:
        for n in items:
            out.append(
                {
                    "id": n.get("id"),
                    "parent_id": n.get("parentId"),
                    "name": n.get("name"),
                    "local": n.get("local"),
                    "depth": len(parents),
                    "path": parents + [n["id"]] if n.get("id") is not None else parents,
                }
            )
            if n.get("children"):
                walk(n["children"], parents + [n["id"]] if n.get("id") is not None else parents)

    walk(nodes, [])
    return out


async def _fetch_topic(
    client: OwsClient, sem: asyncio.Semaphore, rel_path: str, dest: Path
) -> tuple[str, bool, str]:
    """Fetch one topic HTML (or skip if already cached)."""
    if dest.exists():
        return rel_path, True, "cached"
    async with sem:
        try:
            text = await client.get(f"{HELP_BASE}/{rel_path}")
        except Exception as e:  # noqa: BLE001
            return rel_path, False, f"{type(e).__name__}: {e}"
    if not isinstance(text, str):
        return rel_path, False, "non-text response"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return rel_path, True, "fetched"


async def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    print(f"Cache root: {DEST}")

    async with OwsClient.for_surface(Tenant.TESTBED, Surface.STUDIO, settings) as client:
        nav_tree = await _fetch_nav(client)
        nav_index = _flatten(nav_tree)

        # Persist the full nav once. We keep both the original tree and a
        # flat index — flat is what the MCP tools query, tree preserves
        # parent links for breadcrumbs.
        (DEST / "nav_tree.json").write_text(json.dumps(nav_tree, indent=2))
        (DEST / "nav_index.json").write_text(json.dumps(nav_index, indent=2))
        print(f"Saved nav: {len(nav_index)} topics")

        # Deduplicate `local` values (a few topics share files).
        rels = sorted({n["local"] for n in nav_index if n.get("local")})
        print(f"Unique topic files: {len(rels)}")

        sem = asyncio.Semaphore(CONCURRENCY)
        tasks = [
            _fetch_topic(client, sem, rel, DEST / rel) for rel in rels
        ]
        ok = 0
        cached = 0
        failed: list[tuple[str, str]] = []
        for coro in asyncio.as_completed(tasks):
            rel, success, status = await coro
            if not success:
                failed.append((rel, status))
                continue
            if status == "cached":
                cached += 1
            else:
                ok += 1
            done = ok + cached + len(failed)
            if done % 100 == 0:
                print(f"  ... {done}/{len(rels)} (ok={ok} cached={cached} failed={len(failed)})")

        print(f"\nDone. fetched={ok}  cached={cached}  failed={len(failed)}")
        if failed:
            print("Failures (first 20):")
            for rel, err in failed[:20]:
                print(f"  - {rel}: {err}")
        return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
