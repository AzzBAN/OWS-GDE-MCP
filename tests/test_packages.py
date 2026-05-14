"""Tests for the offline `.gpk` parser, exercised against real sample apps.

These tests are skipped automatically when no `.gpk` files are present in
`docs/discovery/testbed/sample-apps/`. Sample apps are gitignored (they hold
proprietary business logic), so CI without them just skips this module.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ows_gde_mcp.package import AppPackage, Artifact, Module, open_package
from ows_gde_mcp.tools.packages import (
    get_app_artifact,
    get_app_package_info,
    list_app_artifacts,
    list_app_packages,
    search_app_artifacts,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLES_DIR = PROJECT_ROOT / "docs" / "discovery" / "testbed" / "sample-apps"


def _samples() -> list[Path]:
    if not SAMPLES_DIR.is_dir():
        return []
    return sorted(SAMPLES_DIR.glob("*.gpk"))


pytestmark = pytest.mark.skipif(
    not _samples(),
    reason="No .gpk sample apps in docs/discovery/testbed/sample-apps/",
)


@pytest.mark.parametrize("path", _samples(), ids=lambda p: p.stem)
def test_open_package_returns_appackage(path: Path) -> None:
    pkg = open_package(path)
    assert isinstance(pkg, AppPackage)
    assert pkg.name, f"package {path.name} has no name in manifest"
    assert pkg.version, f"package {path.name} has no version"


@pytest.mark.parametrize("path", _samples(), ids=lambda p: p.stem)
def test_summary_is_jsonable_and_complete(path: Path) -> None:
    pkg = open_package(path)
    summary = pkg.summary()
    # Required top-level keys
    for key in ("name", "version", "modules", "totals"):
        assert key in summary
    # Each module reports its artifact counts as ints
    for m in summary["modules"]:
        assert isinstance(m["artifact_counts"], dict)
        for k, v in m["artifact_counts"].items():
            assert isinstance(k, str)
            assert isinstance(v, int)
    # The aggregated totals match the per-module sums
    expected: dict[str, int] = {}
    for m in summary["modules"]:
        for t, n in m["artifact_counts"].items():
            expected[t] = expected.get(t, 0) + n
    assert summary["totals"] == dict(sorted(expected.items()))


def test_tt_improvement_has_known_artifacts() -> None:
    """Sanity-check against the canonical sample we used during discovery."""
    matches = list(SAMPLES_DIR.glob("tt_improvement_*.gpk"))
    if not matches:
        pytest.skip("tt_improvement sample not present")
    pkg = open_package(matches[0])

    by_type = pkg.artifacts_by_type()
    # tt_improvement contains MODEL, PAGE, SERVICE, WORKFLOW, TRIGGER, MENU, ...
    for required in ("MODEL", "PAGE", "SERVICE", "WORKFLOW", "TRIGGER", "MENU"):
        assert required in by_type, f"missing {required} in tt_improvement"

    # tts_data is a Model in this app, with an OWS asset URI
    models = {a.name for a in by_type["MODEL"]}
    assert "tts_data" in models
    tts_data = next(a for a in by_type["MODEL"] if a.name == "tts_data")
    assert tts_data.uri.endswith("/tts_data")
    assert isinstance(tts_data.raw, dict)
    assert tts_data.raw.get("model_name") == "tts_data"
    assert isinstance(tts_data.raw.get("properties"), list)

    # tts_process is a Workflow folder with multiple files, no single primary JSON.
    workflows = {a.name for a in by_type["WORKFLOW"]}
    assert "tts_process" in workflows
    wf = next(a for a in by_type["WORKFLOW"] if a.name == "tts_process")
    assert any(f.endswith("_bpmn.json") for f in wf.files)
    assert any(f.endswith("_process_definition.json") for f in wf.files)


def test_list_app_packages_finds_all_samples() -> None:
    listed = list_app_packages()
    sample_names = {p.stem for p in _samples()}
    listed_filenames = {
        item["filename"].rsplit(".gpk", 1)[0] for item in listed if "filename" in item
    }
    assert sample_names <= listed_filenames


def test_list_app_artifacts_filters() -> None:
    pkg_path = next((p for p in _samples() if p.stem.startswith("tt_improvement")), None)
    if not pkg_path:
        pytest.skip("tt_improvement sample not present")

    all_artifacts = list_app_artifacts(str(pkg_path))
    models = list_app_artifacts(str(pkg_path), type="MODEL")
    services = list_app_artifacts(str(pkg_path), type="service")  # case-insensitive
    queries = list_app_artifacts(str(pkg_path), type="PAGE", name_contains="query")

    assert len(all_artifacts) > len(models)
    assert all(a["type"] == "MODEL" for a in models)
    assert all(a["type"] == "SERVICE" for a in services)
    assert all("query" in a["name"].lower() and a["type"] == "PAGE" for a in queries)


def test_get_app_artifact_round_trips() -> None:
    pkg_path = next((p for p in _samples() if p.stem.startswith("tt_improvement")), None)
    if not pkg_path:
        pytest.skip("tt_improvement sample not present")

    art = get_app_artifact(str(pkg_path), type="MODEL", name="tts_data")
    assert art["type"] == "MODEL"
    assert art["name"] == "tts_data"
    assert art["raw"]["model_name"] == "tts_data"
    assert "files" in art


def test_get_app_artifact_resolves_by_name() -> None:
    """Bare app name (e.g., 'tt_improvement') should resolve to the .gpk."""
    if not any(p.stem.startswith("tt_improvement") for p in _samples()):
        pytest.skip("tt_improvement sample not present")
    info = get_app_package_info("tt_improvement")
    assert info["name"] == "tt_improvement"


def test_search_app_artifacts() -> None:
    results = search_app_artifacts("tts_data", type="MODEL", limit=5)
    if any(p.stem.startswith("tt_improvement") for p in _samples()):
        assert any(r["name"] == "tts_data" for r in results)


def test_artifact_module_dataclasses() -> None:
    art = Artifact(type="MODEL", name="x", project="p", module="m")
    assert art.uri == "/p/m/x"
    mod = Module(project="p", name="m", config={})
    assert mod.all_artifacts() == []
