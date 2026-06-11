"""Tests for the local-cache help-doc tools.

These tools never call the network — they read from a local HTML+JSON
corpus populated by `scripts/fetch_help_docs.py`. Tests build a tiny
fake cache in `tmp_path`, monkeypatch the `_CACHE_ROOT` constant, and
exercise the public surface end-to-end.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ows_gde_mcp.tools import help as _help


# ---------------- fixtures ----------------


@pytest.fixture
def fake_cache(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Build a small, realistic help-cache structure in `tmp_path`."""
    root = tmp_path / "help"
    en = root / "en_US"
    en.mkdir(parents=True)

    # Two-topic mini corpus, one with a parent-link.
    nav = [
        {"id": 1, "parent_id": 0, "name": "Low-Code Orchestration",
         "local": "root.html", "depth": 0, "path": [1]},
        {"id": 9, "parent_id": 1, "name": "Application Development Overview",
         "local": "adc_dev_overview_001.html", "depth": 1, "path": [1, 9]},
        {"id": 12, "parent_id": 9, "name": "Understanding the Low-Code Development Platform",
         "local": "adc_dev_overview_002.html", "depth": 2, "path": [1, 9, 12]},
        {"id": 99, "parent_id": 1, "name": "Bridge example",
         "local": "rule_bridge.html", "depth": 1, "path": [1, 99]},
    ]
    (en / "nav_index.json").write_text(json.dumps(nav))
    (en / "nav_tree.json").write_text(json.dumps([]))  # not used by these tools

    (en / "root.html").write_text(
        "<html><body><h1 class='topictitle1'>Low-Code Orchestration</h1>"
        "<p>Welcome.</p></body></html>"
    )
    (en / "adc_dev_overview_001.html").write_text(
        "<html><body><h1 class='topictitle1'>Application Development Overview</h1>"
        "<p>Overview body.</p>"
        "<div class='familylinks'><div class='parentlink'>"
        "<strong>Parent topic:</strong> "
        "<a href='root.html'>Low-Code Orchestration</a></div></div>"
        "</body></html>"
    )
    (en / "adc_dev_overview_002.html").write_text(
        "<html><body><h1 class='topictitle1'>"
        "Understanding the Low-Code Development Platform</h1>"
        "<script>console.log('ignored');</script>"
        "<p>GDE provides full-scenario tools for runScript, ScriptLib, and "
        "Translator orchestration.</p>"
        "<div class='parentlink'>Parent topic: <a href='adc_dev_overview_001.html'>"
        "Application Development Overview</a></div></body></html>"
    )
    (en / "rule_bridge.html").write_text(
        "<html><body><h1 class='topictitle1'>Bridge example</h1>"
        "<p>This rule covers RunScript bridging.</p></body></html>"
    )

    monkeypatch.setattr(_help, "_CACHE_ROOT", root)
    return root


# ---------------- list_help_topics ----------------


def test_list_help_topics_no_cache_returns_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(_help, "_CACHE_ROOT", tmp_path / "missing")
    out = _help.list_help_topics()
    assert "error" in out
    assert out["error"]["code"] == "no_cache"
    assert "fetch_help_docs.py" in out["error"]["message"]


def test_list_help_topics_query_filter(fake_cache: Path) -> None:
    out = _help.list_help_topics(query="overview")
    assert out["total"] == 1
    assert out["topics"][0]["id"] == 9


def test_list_help_topics_parent_filter(fake_cache: Path) -> None:
    out = _help.list_help_topics(parent_id=1)
    names = {t["name"] for t in out["topics"]}
    assert names == {"Application Development Overview", "Bridge example"}


def test_list_help_topics_depth_max(fake_cache: Path) -> None:
    out = _help.list_help_topics(depth_max=1)
    ids = {t["id"] for t in out["topics"]}
    # Depth 0 (root=1) and depth 1 (9, 99) — but not depth 2 (12).
    assert ids == {1, 9, 99}


def test_list_help_topics_limit(fake_cache: Path) -> None:
    out = _help.list_help_topics(limit=2)
    assert len(out["topics"]) == 2


# ---------------- get_help_topic ----------------


def test_get_help_topic_by_id_extracts_text_and_breadcrumbs(
    fake_cache: Path,
) -> None:
    out = _help.get_help_topic(12)
    assert out["title"] == "Understanding the Low-Code Development Platform"
    assert "GDE provides" in out["text"]
    # Scripts must be stripped.
    assert "console.log" not in out["text"]
    # Breadcrumbs walk root → ... → leaf.
    crumbs = [b["name"] for b in out["breadcrumbs"]]
    assert crumbs == [
        "Low-Code Orchestration",
        "Application Development Overview",
        "Understanding the Low-Code Development Platform",
    ]
    assert out["parent"] == {
        "name": "Application Development Overview",
        "local": "adc_dev_overview_001.html",
    }
    # Default does not include raw HTML.
    assert "html" not in out


def test_get_help_topic_by_local_filename(fake_cache: Path) -> None:
    out = _help.get_help_topic("adc_dev_overview_002.html")
    assert out["id"] == 12


def test_get_help_topic_with_html(fake_cache: Path) -> None:
    out = _help.get_help_topic(12, include_html=True)
    assert "<h1" in out["html"]


def test_get_help_topic_not_found(fake_cache: Path) -> None:
    out = _help.get_help_topic(9999)
    assert out["error"]["code"] == "not_found"


def test_get_help_topic_missing_file(
    fake_cache: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Nav has the entry but the HTML wasn't downloaded."""
    nav = json.loads((fake_cache / "en_US" / "nav_index.json").read_text())
    nav.append(
        {"id": 7777, "parent_id": 1, "name": "Ghost", "local": "ghost.html",
         "depth": 1, "path": [1, 7777]}
    )
    (fake_cache / "en_US" / "nav_index.json").write_text(json.dumps(nav))
    out = _help.get_help_topic(7777)
    assert out["error"]["code"] == "missing_file"


# ---------------- search_help ----------------


def test_search_help_finds_text_in_body(fake_cache: Path) -> None:
    out = _help.search_help("RunScript")
    assert out["total"] == 2
    ids = {h["id"] for h in out["hits"]}
    assert ids == {12, 99}
    # Snippet should contain the matched word.
    for hit in out["hits"]:
        assert "RunScript" in hit["snippet"] or "runScript" in hit["snippet"]


def test_search_help_too_short(fake_cache: Path) -> None:
    out = _help.search_help("a")
    assert out["error"]["code"] == "query_too_short"


def test_search_help_no_match(fake_cache: Path) -> None:
    out = _help.search_help("xyzzy_no_such_term")
    assert out["total"] == 0
    assert out["hits"] == []


def test_search_help_uses_jsonl_when_present(fake_cache: Path) -> None:
    """When `topics.jsonl` exists, search uses the fast path and skips HTML parse."""
    en = fake_cache / "en_US"
    entries = [
        {
            "id": 12,
            "name": "Understanding the Low-Code Development Platform",
            "local": "adc_dev_overview_002.html",
            "title": "Understanding the Low-Code Development Platform",
            "text": "Pre-extracted body about RunScript orchestration.",
            "parent": None,
        },
    ]
    (en / "topics.jsonl").write_text(
        "\n".join(json.dumps(e) for e in entries), encoding="utf-8"
    )
    out = _help.search_help("RunScript")
    assert out["index"] == "jsonl"
    assert out["total"] == 1
    assert out["hits"][0]["id"] == 12


def test_search_help_html_fallback_signals_hint(fake_cache: Path) -> None:
    """Without `topics.jsonl`, search falls back to HTML scan + emits a hint."""
    out = _help.search_help("RunScript")
    assert out["index"] == "html-fallback"
    assert "fetch_help_docs" in out["hint"] or "index_help_docs" in out["hint"]
