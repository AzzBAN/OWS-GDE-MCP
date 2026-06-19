import json
from pathlib import Path

from ows_gde_mcp.tools import help as help_tools


def _seed_corpus(tmp_path: Path) -> Path:
    lang_dir = tmp_path / "en_US"
    lang_dir.mkdir(parents=True)
    (lang_dir / "nav_index.json").write_text(
        json.dumps(
            [
                {
                    "id": 1,
                    "parent_id": 0,
                    "name": "Overview",
                    "local": "overview.md",
                    "depth": 0,
                    "path": [1],
                },
            ]
        ),
        encoding="utf-8",
    )
    (lang_dir / "overview.md").write_text(
        "# Overview\n\nLow-Code Orchestration intro.\n", encoding="utf-8"
    )
    (lang_dir / "topics.jsonl").write_text(
        json.dumps(
            {
                "id": 1,
                "name": "Overview",
                "local": "overview.md",
                "title": "Overview",
                "text": "Low-Code Orchestration intro.",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    return tmp_path


def test_get_help_topic_serves_markdown(tmp_path, monkeypatch):
    root = _seed_corpus(tmp_path)
    monkeypatch.setattr(help_tools, "_CACHE_ROOT", root)
    out = help_tools.get_help_topic(1)
    assert out["title"] == "Overview"
    assert "Low-Code Orchestration" in out["text"]


def test_search_help_uses_jsonl(tmp_path, monkeypatch):
    root = _seed_corpus(tmp_path)
    monkeypatch.setattr(help_tools, "_CACHE_ROOT", root)
    out = help_tools.search_help("orchestration")
    assert out["total"] == 1
    assert out["hits"][0]["local"] == "overview.md"
