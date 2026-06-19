"""Tests for the local knowledge-vault help tools.

These tools never call the network — they read an Obsidian-standard vault
(`docs/help/vault/`) plus a sidecar search index (`docs/help/index/<lang>/`).
Tests build a tiny fake vault + index in `tmp_path`, monkeypatch the
`_VAULT_ROOT` / `_INDEX_ROOT` constants, and exercise the public surface.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ows_gde_mcp.tools import help as _help


@pytest.fixture
def fake_vault(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Build a small vault (Home + a finding + a 3-deep Reference tree) + index."""
    vault = tmp_path / "vault"
    index = tmp_path / "index"
    (vault / "00 Findings").mkdir(parents=True)
    (vault / "Reference" / "App Development").mkdir(parents=True)

    (vault / "Home.md").write_text(
        "---\ntags: [moc]\n---\n# OWS Knowledge Vault\n\nRead findings first.\n",
        encoding="utf-8",
    )
    (vault / "00 Findings" / "TQL Notes.md").write_text(
        "# TQL Notes\n\nThe asset_uri must be quoted in RunScript orchestration.\n",
        encoding="utf-8",
    )
    (vault / "Reference" / "Overview.md").write_text(
        "# Low-Code Orchestration\n\nWelcome.\n", encoding="utf-8"
    )
    (vault / "Reference" / "App Development" / "Platform.md").write_text(
        "# Understanding the Platform\n\n"
        "GDE provides full-scenario tools for RunScript orchestration.\n",
        encoding="utf-8",
    )

    nav = [
        {"id": 1, "parent_id": 0, "name": "Reference", "local": "Reference",
         "depth": 0, "path": [1], "is_folder": True},
        {"id": 2, "parent_id": 1, "name": "Low-Code Orchestration",
         "local": "Reference/Overview.md", "depth": 1, "path": [1, 2], "is_folder": False},
        {"id": 3, "parent_id": 1, "name": "App Development",
         "local": "Reference/App Development", "depth": 1, "path": [1, 3], "is_folder": True},
        {"id": 4, "parent_id": 3, "name": "Understanding the Platform",
         "local": "Reference/App Development/Platform.md", "depth": 2,
         "path": [1, 3, 4], "is_folder": False},
    ]
    (index / "en_US").mkdir(parents=True)
    (index / "en_US" / "nav_index.json").write_text(json.dumps(nav), encoding="utf-8")
    (index / "en_US" / "topics.jsonl").write_text(
        "\n".join(
            json.dumps(e)
            for e in [
                {"id": 2, "name": "Low-Code Orchestration",
                 "local": "Reference/Overview.md", "title": "Low-Code Orchestration",
                 "text": "Welcome."},
                {"id": 4, "name": "Understanding the Platform",
                 "local": "Reference/App Development/Platform.md",
                 "title": "Understanding the Platform",
                 "text": "GDE provides full-scenario tools for RunScript orchestration."},
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(_help, "_VAULT_ROOT", vault)
    monkeypatch.setattr(_help, "_INDEX_ROOT", index)
    return vault


# ---------------- get_help_home ----------------


def test_get_help_home_returns_moc_and_findings(fake_vault: Path) -> None:
    home = _help.get_help_home()
    assert home["title"] == "OWS Knowledge Vault"
    assert "Read findings first" in home["text"]
    assert {"name": "TQL Notes", "local": "00 Findings/TQL Notes.md"} in home["findings"]


def test_get_help_home_missing_returns_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(_help, "_VAULT_ROOT", tmp_path / "empty")
    out = _help.get_help_home()
    assert out["error"]["code"] == "no_home"


# ---------------- list_help_topics ----------------


def test_list_help_topics_no_cache_returns_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(_help, "_INDEX_ROOT", tmp_path / "missing")
    monkeypatch.setattr(_help, "_VAULT_ROOT", tmp_path / "missing-vault")
    out = _help.list_help_topics()
    assert out["error"]["code"] == "no_cache"
    assert "import_help_corpus.py" in out["error"]["message"]


def test_list_help_topics_query_filter(fake_vault: Path) -> None:
    out = _help.list_help_topics(query="platform")
    assert out["total"] == 1
    assert out["topics"][0]["id"] == 4


def test_list_help_topics_parent_filter(fake_vault: Path) -> None:
    out = _help.list_help_topics(parent_id=1)
    names = {t["name"] for t in out["topics"]}
    assert names == {"Low-Code Orchestration", "App Development"}


def test_list_help_topics_depth_max(fake_vault: Path) -> None:
    out = _help.list_help_topics(depth_max=1)
    ids = {t["id"] for t in out["topics"]}
    assert ids == {1, 2, 3}  # excludes depth-2 (id 4)


def test_list_help_topics_includes_folders(fake_vault: Path) -> None:
    out = _help.list_help_topics()
    assert any(t["is_folder"] for t in out["topics"])


# ---------------- get_help_topic ----------------


def test_get_help_topic_by_id_text_and_breadcrumbs(fake_vault: Path) -> None:
    out = _help.get_help_topic(4)
    assert out["title"] == "Understanding the Platform"
    assert "GDE provides" in out["text"]
    assert out["source"] == "reference"
    crumbs = [b["name"] for b in out["breadcrumbs"]]
    assert crumbs == ["Reference", "App Development", "Understanding the Platform"]
    assert "raw" not in out


def test_get_help_topic_by_local_path(fake_vault: Path) -> None:
    out = _help.get_help_topic("Reference/App Development/Platform.md")
    assert out["title"] == "Understanding the Platform"


def test_get_help_topic_finding_by_path(fake_vault: Path) -> None:
    out = _help.get_help_topic("00 Findings/TQL Notes.md")
    assert out["source"] == "finding"
    assert "asset_uri" in out["text"]


def test_get_help_topic_include_raw(fake_vault: Path) -> None:
    out = _help.get_help_topic(4, include_raw=True)
    assert out["raw"].startswith("# Understanding the Platform")


def test_get_help_topic_not_found(fake_vault: Path) -> None:
    out = _help.get_help_topic(9999)
    assert out["error"]["code"] == "not_found"


def test_get_help_topic_missing_file(
    fake_vault: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    nav_path = fake_vault.parent / "index" / "en_US" / "nav_index.json"
    nav = json.loads(nav_path.read_text())
    nav.append(
        {"id": 7777, "parent_id": 1, "name": "Ghost", "local": "Reference/ghost.md",
         "depth": 1, "path": [1, 7777], "is_folder": False}
    )
    nav_path.write_text(json.dumps(nav))
    out = _help.get_help_topic(7777)
    assert out["error"]["code"] == "missing_file"


def test_get_help_topic_rejects_path_escape(fake_vault: Path) -> None:
    out = _help.get_help_topic("Reference/../../../../etc/passwd.md")
    assert out["error"]["code"] in {"invalid_path", "missing_file"}


# ---------------- search_help ----------------


def test_search_help_ranks_findings_first(fake_vault: Path) -> None:
    out = _help.search_help("orchestration")
    assert out["total"] >= 2
    assert out["findings_count"] >= 1
    assert out["hits"][0]["source"] == "finding"
    assert any(h["source"] == "reference" for h in out["hits"])


def test_search_help_reference_only_when_no_finding_match(fake_vault: Path) -> None:
    out = _help.search_help("GDE provides")
    assert out["findings_count"] == 0
    assert out["total"] == 1
    assert out["hits"][0]["source"] == "reference"
    assert out["hits"][0]["id"] == 4


def test_search_help_too_short(fake_vault: Path) -> None:
    out = _help.search_help("a")
    assert out["error"]["code"] == "query_too_short"


def test_search_help_no_match(fake_vault: Path) -> None:
    out = _help.search_help("xyzzy_no_such_term")
    assert out["total"] == 0
    assert out["hits"] == []
