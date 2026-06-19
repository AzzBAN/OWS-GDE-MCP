"""MCP tools for the OWS Studio help corpus — local-cache only.

The help docs are static documentation pages bundled with OWS. They never
change between tool calls in a session, so we fetch them once with
`scripts/fetch_help_docs.py` into `docs/help/<lang>/` and serve from disk.

This file deliberately makes NO live network calls. If the cache is missing
or stale, the tools return a structured `error.no_cache` and tell the caller
how to populate it.

## Layout of the local cache

    docs/help/en_US/
        nav_tree.json    — full hierarchical nav (kept for breadcrumbs)
        nav_index.json   — flat list: {id, parent_id, name, local, depth, path}
        toctopics/...html, adc_dev_overview_002.html, ...   — topic HTML files

Topic IDs are stable integers assigned by the OWS docs build (1..N). Topic
file names (`local`) are stable too — they're shipped with the corpus and
referenced by `nav_index.json`. Tools accept either an integer `id` or the
human-friendly `local` filename.

## Why local-cache

Documentation is static and 3.6k topics is too much to hammer the help
endpoint with on every agent question. Local search is also fast enough
(< 100 ms for 3.6k topics) that we don't need an external index.
"""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

# Cache root — relative to repo root. The fetcher script writes here.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_CACHE_ROOT = _REPO_ROOT / "docs" / "help"

# Default language. The corpus also exists in zh_CN; not fetched today.
_DEFAULT_LANG = "en_US"


def _cache_dir(lang: str = _DEFAULT_LANG) -> Path:
    return _CACHE_ROOT / lang


def _no_cache_error(lang: str) -> dict[str, Any]:
    return {
        "error": {
            "code": "no_cache",
            "message": (
                f"Help cache for {lang!r} is empty at {_cache_dir(lang)}. "
                "Run `uv run python scripts/fetch_help_docs.py` to populate it."
            ),
        }
    }


def _load_index(lang: str) -> list[dict] | None:
    path = _cache_dir(lang) / "nav_index.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


# ---------------- HTML extraction ----------------


class _TopicTextExtractor(HTMLParser):
    """Pull title + plain text from an OWS help topic HTML page.

    The corpus uses a stable shape: `<h1 class="topictitle1">…</h1>` for the
    title, the body inside `<div id="body...">`, and a "Parent topic" link
    in `<div class="parentlink">`. We strip scripts/styles and keep
    block-level whitespace.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._buf: list[str] = []
        self._stack: list[str] = []
        self._title: str | None = None
        self._in_title = False
        self._suppress = 0  # >0 inside <script>/<style>
        self._block_tags = {
            "p", "li", "h1", "h2", "h3", "h4", "h5", "h6",
            "br", "tr", "td", "th", "div", "ul", "ol",
        }
        self._parent_topic: tuple[str, str] | None = None
        self._in_parentlink = False
        self._link_target: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._stack.append(tag)
        attrs_d = dict(attrs)
        if tag == "script" or tag == "style":
            self._suppress += 1
            return
        if tag == "h1" and "topictitle1" in (attrs_d.get("class") or ""):
            self._in_title = True
        if tag == "div" and "parentlink" in (attrs_d.get("class") or ""):
            self._in_parentlink = True
        if tag == "a" and self._in_parentlink:
            self._link_target = attrs_d.get("href")

    def handle_endtag(self, tag: str) -> None:
        if (tag == "script" or tag == "style") and self._suppress > 0:
            self._suppress -= 1
        if tag == "h1":
            self._in_title = False
        if tag == "div" and self._in_parentlink:
            self._in_parentlink = False
        if tag in self._block_tags:
            self._buf.append("\n")
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()

    def handle_data(self, data: str) -> None:
        if self._suppress:
            return
        if self._in_title:
            self._title = (self._title or "") + data
            return
        if self._in_parentlink and self._link_target and data.strip():
            # capture the link text alongside its target
            self._parent_topic = (data.strip(), self._link_target)
            self._link_target = None
        self._buf.append(data)

    @property
    def title(self) -> str | None:
        return self._title.strip() if self._title else None

    @property
    def text(self) -> str:
        # Collapse multiple blank lines.
        joined = "".join(self._buf)
        return re.sub(r"\n{3,}", "\n\n", joined).strip()

    @property
    def parent_topic(self) -> dict[str, str] | None:
        if not self._parent_topic:
            return None
        name, href = self._parent_topic
        return {"name": name, "local": href}


def _extract_topic_body(html: str) -> tuple[str | None, str, dict | None]:
    p = _TopicTextExtractor()
    p.feed(html)
    return p.title, p.text, p.parent_topic


# ---------------- Public MCP tools ----------------


def list_help_topics(
    *,
    query: str = "",
    parent_id: int | None = None,
    depth_max: int | None = None,
    lang: str = _DEFAULT_LANG,
    limit: int = 50,
) -> dict[str, Any]:
    """List topics from the local OWS help corpus.

    Reads `docs/help/<lang>/nav_index.json` — populated by
    `scripts/fetch_help_docs.py`. No live network calls.

    Args:
        query: substring filter on topic name (case-insensitive). Empty = all.
        parent_id: keep only direct children of this parent. None = all.
        depth_max: keep only topics at this nav depth or shallower.
            Depth 0 is the corpus root, 1 is "Overview/User Guide/...", etc.
        lang: language directory under `docs/help/`. Default `en_US`.
        limit: cap the number of rows returned (default 50).

    Returns:
        `{"total", "lang", "topics": [{id, parent_id, name, local, depth}]}`
        or `{"error": {"code": "no_cache", "message": ...}}` if the cache
        hasn't been fetched yet.
    """
    index = _load_index(lang)
    if index is None:
        return _no_cache_error(lang)

    q = query.lower().strip()
    matches = []
    for row in index:
        if q and q not in (row.get("name") or "").lower():
            continue
        if parent_id is not None and row.get("parent_id") != parent_id:
            continue
        if depth_max is not None and row.get("depth", 0) > depth_max:
            continue
        matches.append(
            {
                "id": row.get("id"),
                "parent_id": row.get("parent_id"),
                "name": row.get("name"),
                "local": row.get("local"),
                "depth": row.get("depth", 0),
            }
        )
    return {
        "total": len(matches),
        "lang": lang,
        "topics": matches[:limit],
    }


def get_help_topic(
    topic: int | str,
    *,
    lang: str = _DEFAULT_LANG,
    include_html: bool = False,
) -> dict[str, Any]:
    """Fetch one topic from the local help cache.

    Args:
        topic: integer `id` (e.g. `12`) OR the topic's `local` filename
            (e.g. `"adc_dev_overview_002.html"`). Integer ids are stable
            across cache refreshes; filenames are too but are easier to
            spot-check by hand.
        lang: language directory. Default `en_US`.
        include_html: if True, also return the raw HTML under `html`.
            Default False — most callers want the plain text body.

    Returns:
        `{"id", "name", "local", "parent": {...}, "title", "text",
          "breadcrumbs": [{id, name}], "html"?}` or `{"error": {...}}`.
    """
    index = _load_index(lang)
    if index is None:
        return _no_cache_error(lang)

    by_id = {r["id"]: r for r in index if r.get("id") is not None}
    by_local = {r["local"]: r for r in index if r.get("local")}

    row: dict | None
    if isinstance(topic, int) or (isinstance(topic, str) and topic.isdigit()):
        row = by_id.get(int(topic))
    else:
        row = by_local.get(topic)

    if row is None:
        return {"error": {"code": "not_found", "message": f"Topic {topic!r} not in nav."}}

    file_path = _cache_dir(lang) / row["local"]
    if not file_path.exists():
        return {
            "error": {
                "code": "missing_file",
                "message": (
                    f"Topic {topic!r} is in the nav but the file at "
                    f"{file_path} is missing. Re-run the fetcher."
                ),
            }
        }
    raw = file_path.read_text(encoding="utf-8")
    if str(row["local"]).endswith(".md"):
        # Markdown corpus (imported from knowledge-helper): the body is
        # already plain text. Title = first ATX heading or the nav name.
        lines = raw.splitlines()
        md_title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), None)
        title, text, parent = md_title, raw, None
    else:
        title, text, parent = _extract_topic_body(raw)

    # Breadcrumb path from root to this topic.
    breadcrumbs: list[dict[str, Any]] = []
    for nid in row.get("path") or []:
        crumb_row = by_id.get(nid)
        if crumb_row:
            breadcrumbs.append({"id": nid, "name": crumb_row.get("name")})

    out: dict[str, Any] = {
        "id": row.get("id"),
        "name": row.get("name") or title,
        "local": row.get("local"),
        "title": title,
        "text": text,
        "parent": parent,
        "breadcrumbs": breadcrumbs,
        "lang": lang,
    }
    if include_html:
        out["html"] = raw
    return out


def search_help(
    query: str,
    *,
    lang: str = _DEFAULT_LANG,
    limit: int = 20,
    snippet_chars: int = 240,
) -> dict[str, Any]:
    """Full-text search across the local help corpus.

    Reads `topics.jsonl` (built by `scripts/index_help_docs.py`) when
    available — that path skips HTML parsing entirely and runs in ~10 ms
    for 3.5k topics. Falls back to scanning the on-disk HTML files if the
    index is missing, with a hint to build it.

    Args:
        query: required search string (>=2 chars).
        lang: language directory.
        limit: cap the hit list.
        snippet_chars: characters of context to include around each match.

    Returns:
        `{"query", "total", "hits": [{id, name, local, title, snippet}],
          "index": "jsonl"|"html-fallback"}`
        or `{"error": {...}}` on cache miss / empty query.
    """
    if not query or len(query.strip()) < 2:
        return {
            "error": {
                "code": "query_too_short",
                "message": "Provide a query of at least 2 characters.",
            }
        }
    index_path = _cache_dir(lang) / "topics.jsonl"
    if index_path.exists():
        return _search_jsonl(query, index_path, lang, limit, snippet_chars)

    # Fallback: index hasn't been built. Use the slower nav+HTML scan.
    nav = _load_index(lang)
    if nav is None:
        return _no_cache_error(lang)
    return _search_html_fallback(query, nav, lang, limit, snippet_chars)


def _make_snippet(haystack: str, idx: int, snippet_chars: int) -> str:
    start = max(0, idx - snippet_chars // 2)
    end = min(len(haystack), idx + snippet_chars // 2)
    snippet = haystack[start:end]
    if start > 0:
        snippet = "..." + snippet
    if end < len(haystack):
        snippet = snippet + "..."
    return re.sub(r"\s+", " ", snippet).strip()


def _search_jsonl(
    query: str, index_path: Path, lang: str, limit: int, snippet_chars: int
) -> dict[str, Any]:
    q = query.lower().strip()
    hits: list[dict[str, Any]] = []
    with index_path.open(encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            haystack = f"{entry.get('title') or ''}\n{entry.get('text') or ''}"
            idx = haystack.lower().find(q)
            if idx < 0:
                continue
            hits.append(
                {
                    "id": entry.get("id"),
                    "name": entry.get("name"),
                    "local": entry.get("local"),
                    "title": entry.get("title"),
                    "snippet": _make_snippet(haystack, idx, snippet_chars),
                }
            )
            if len(hits) >= limit:
                break
    return {
        "query": query,
        "total": len(hits),
        "hits": hits,
        "lang": lang,
        "index": "jsonl",
    }


def _search_html_fallback(
    query: str,
    nav: list[dict],
    lang: str,
    limit: int,
    snippet_chars: int,
) -> dict[str, Any]:
    q = query.lower().strip()
    hits: list[dict[str, Any]] = []
    for row in nav:
        local = row.get("local")
        if not local:
            continue
        path = _cache_dir(lang) / local
        if not path.exists():
            continue
        try:
            html = path.read_text(encoding="utf-8")
        except OSError:
            continue
        title, text, _ = _extract_topic_body(html)
        haystack = f"{title or ''}\n{text}"
        idx = haystack.lower().find(q)
        if idx < 0:
            continue
        hits.append(
            {
                "id": row.get("id"),
                "name": row.get("name"),
                "local": local,
                "title": title,
                "snippet": _make_snippet(haystack, idx, snippet_chars),
            }
        )
        if len(hits) >= limit:
            break
    return {
        "query": query,
        "total": len(hits),
        "hits": hits,
        "lang": lang,
        "index": "html-fallback",
        "hint": (
            "Run `uv run python scripts/index_help_docs.py` after the fetcher "
            "to enable the fast jsonl index."
        ),
    }


__all__ = [
    "get_help_topic",
    "list_help_topics",
    "search_help",
]
