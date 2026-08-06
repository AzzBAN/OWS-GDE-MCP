"""Tests for cross-reference analysis tools.

Covers:
- URI normalization (canonical form, runtime-prefix form, error cases).
- Reference scanning: strong (typed-URI fields) vs weak (substring), with
  self-reference exclusion.
- find_artifact_references end-to-end with mocked list_services.
- find_unused_artifacts with a mix of used and unused services.

The tools route through `ows_gde_mcp.tools.live.list_services` (and
friends), which we monkeypatch directly so these tests don't need
`pytest-httpx`.
"""

from __future__ import annotations

import json
from typing import Any

import pytest

from ows_gde_mcp.tools import references as _refs

# ---------------- URI normalization ----------------


def test_normalize_canonical() -> None:
    assert _refs._normalize_target_uri("/proj/mod/name") == "/proj/mod/name"


def test_normalize_strips_runtime_prefix() -> None:
    full = "/adc-service/rest/v1/services/proj/mod/name"
    assert _refs._normalize_target_uri(full) == "/proj/mod/name"


@pytest.mark.parametrize(
    "bad",
    ["", "name", "proj/mod/name", "/proj/mod", "/proj/mod/name/extra"],
)
def test_normalize_rejects_bad_input(bad: str) -> None:
    with pytest.raises(ValueError):
        _refs._normalize_target_uri(bad)


# ---------------- _scan_body_for_refs ----------------


def test_scan_strong_ref_in_typed_uri_field() -> None:
    body = {
        "steps": {
            "step1": {
                "type": "modelInstanceGetList",
                "model_uri": "/proj/mod/tts_task",
            }
        }
    }
    refs = _refs._scan_body_for_refs(body, "/proj/mod/tts_task")
    assert len(refs) == 1
    assert refs[0]["kind"] == "strong"
    assert refs[0]["field"] == "model_uri"


def test_scan_weak_ref_in_description() -> None:
    body = {"description": "calls /proj/mod/foo for cleanup"}
    refs = _refs._scan_body_for_refs(body, "/proj/mod/foo")
    assert len(refs) == 1
    assert refs[0]["kind"] == "weak"
    assert refs[0]["field"] == "description"


def test_scan_returns_empty_when_no_match() -> None:
    body = {"a": "/other/path/x", "b": [1, 2, 3]}
    assert _refs._scan_body_for_refs(body, "/proj/mod/foo") == []


def test_scan_finds_refs_inside_arrays_and_nested_dicts() -> None:
    body = {
        "steps": [
            {"name": "s1", "service_uri": "/proj/mod/foo"},
            {"name": "s2", "config": {"bind_model_uri": "/proj/mod/foo"}},
        ]
    }
    refs = _refs._scan_body_for_refs(body, "/proj/mod/foo")
    fields = {r["field"] for r in refs}
    assert fields == {"service_uri", "bind_model_uri"}
    assert all(r["kind"] == "strong" for r in refs)


def test_scan_excerpt_truncated_for_long_values() -> None:
    long = "/proj/mod/foo" + ("x" * 500)
    body = {"description": long}
    refs = _refs._scan_body_for_refs(body, "/proj/mod/foo")
    assert len(refs) == 1
    assert refs[0]["excerpt"].endswith("...")
    assert len(refs[0]["excerpt"]) <= 203  # 200 + "..."


# ---------------- self-reference detection ----------------


def test_self_reference_excluded() -> None:
    assert _refs._is_self_reference("foo", "proj", "mod", "/proj/mod/foo")


def test_self_reference_distinct_when_name_differs() -> None:
    assert not _refs._is_self_reference("foo", "proj", "mod", "/proj/mod/bar")


# ---------------- find_artifact_references (mocked) ----------------


@pytest.fixture
def patched_live(monkeypatch: pytest.MonkeyPatch):
    """Replace every live OWS call the references tools use.

    Returns a `Live` namespace exposing two mutable lists the tests prime:
    `services` (full flow rows) and `pages` (rows with stringified
    `content`). list_pages serves the metadata view (no `content`),
    get_page_detail serves the full row, list_services serves both
    summary and full-flow modes per `include_flow`.
    """

    class Live:
        def __init__(self) -> None:
            self.services: list[dict[str, Any]] = []
            self.pages: list[dict[str, Any]] = []
            self.triggers: list[dict[str, Any]] = []

    live = Live()

    async def fake_list_services(
        tenant: str,
        project_name: str,
        module_name: str,
        *,
        start: int = 0,
        limit: int = 50,
        include_flow: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        if include_flow:
            return {"total": len(live.services), "services": live.services}
        summary = [{k: v for k, v in s.items() if k != "flow"} for s in live.services]
        return {"total": len(summary), "services": summary}

    async def fake_list_pages(
        tenant: str,
        project_name: str,
        module_name: str,
        *,
        page: int = 0,
        page_size: int = 50,
        **kwargs: Any,
    ) -> dict[str, Any]:
        # list_pages returns metadata only - no `content`.
        rows = [{k: v for k, v in p.items() if k != "content"} for p in live.pages]
        return {"total": len(rows), "pages": rows, "page": page, "pageSize": page_size}

    async def fake_get_page_detail(tenant: str, page_id: str) -> dict[str, Any]:
        for p in live.pages:
            if str(p.get("id")) == str(page_id):
                return p
        return {"error": f"page {page_id!r} not found"}

    async def fake_list_triggers(
        tenant: str,
        project_name: str,
        module_name: str,
        *,
        trigger_name: str = "",
        active: bool | None = True,
        start: int = 0,
        limit: int = 50,
    ) -> dict[str, Any]:
        return {
            "total": len(live.triggers),
            "page_size": limit,
            "triggers": live.triggers,
        }

    monkeypatch.setattr("ows_gde_mcp.tools.live.list_services", fake_list_services)
    monkeypatch.setattr("ows_gde_mcp.tools.pages.list_pages", fake_list_pages)
    monkeypatch.setattr("ows_gde_mcp.tools.pages.get_page_detail", fake_get_page_detail)
    monkeypatch.setattr("ows_gde_mcp.tools.live.list_triggers", fake_list_triggers)
    return live


async def test_find_references_returns_strong_and_weak(
    patched_live,
) -> None:
    patched_live.services.extend(
        [
            {
                "service_name": "caller",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {
                    "steps": {
                        "s1": {
                            "type": "invoke",
                            "service_uri": "/proj/mod/target",
                        }
                    }
                },
            },
            {
                "service_name": "mentioner",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {
                    "steps": {
                        "s1": {
                            "type": "input",
                            "description": "see /proj/mod/target for details",
                        }
                    }
                },
            },
            {
                "service_name": "unrelated",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {"steps": {"s1": {"type": "input"}}},
            },
        ]
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["target"] == "/proj/mod/target"
    assert out["sources_scanned"]["services"] == 3
    assert out["sources_scanned"]["pages"] == 0
    assert out["ref_count"] == 2
    assert out["strong_ref_count"] == 1
    assert out["weak_ref_count"] == 1
    sources = {r["in"] for r in out["references"]}
    assert sources == {"/proj/mod/caller", "/proj/mod/mentioner"}
    # Default behaviour: excerpts are dropped from the public payload.
    for r in out["references"]:
        assert "excerpt" not in r
    # Coverage warning is always present.
    assert out["warnings"]


async def test_find_references_with_excerpts_keeps_excerpt_field(
    patched_live,
) -> None:
    """`with_excerpts=True` opts back into the excerpt field on each row."""
    patched_live.services.append(
        {
            "service_name": "caller",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {
                "steps": {
                    "s1": {"type": "invoke", "service_uri": "/proj/mod/target"},
                }
            },
        }
    )
    out = await _refs.find_artifact_references(
        "testbed", "/proj/mod/target", with_excerpts=True
    )
    assert out["ref_count"] == 1
    assert "excerpt" in out["references"][0]
    assert out["references"][0]["excerpt"] == "/proj/mod/target"


async def test_find_references_excludes_self(
    patched_live,
) -> None:
    """A service's own service_uri must not be counted as a reference to itself."""
    patched_live.services.append(
        {
            "service_name": "target",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {"service_uri": "/proj/mod/target"},
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["ref_count"] == 0


async def test_find_references_accepts_runtime_uri(
    patched_live,
) -> None:
    patched_live.services.append(
        {
            "service_name": "caller",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {"steps": {"s1": {"service_uri": "/proj/mod/target"}}},
        }
    )
    out = await _refs.find_artifact_references(
        "testbed",
        "/adc-service/rest/v1/services/proj/mod/target",
    )
    assert out["target"] == "/proj/mod/target"
    assert out["ref_count"] == 1


async def test_find_references_accepts_web_runtime_uri(patched_live) -> None:
    """The /adc-service/web/rest/v1/services/... prefix (used by pages) also normalises."""
    patched_live.services.append(
        {
            "service_name": "caller",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {"steps": {"s1": {"service_uri": "/proj/mod/target"}}},
        }
    )
    out = await _refs.find_artifact_references(
        "testbed",
        "/adc-service/web/rest/v1/services/proj/mod/target",
    )
    assert out["target"] == "/proj/mod/target"
    assert out["ref_count"] == 1


# ---------------- page-scanning ----------------


async def test_find_references_scans_page_props(patched_live) -> None:
    """Page component props (serviceName/serviceId/location) match strongly."""
    page_content = {
        "id": "page",
        "name": "page",
        "children": [
            {
                "name": "select",
                "props": {
                    "serviceName": "/adc-service/web/rest/v1/services/proj/mod/target",
                },
            },
            {
                "name": "datagrid",
                "props": {
                    "serviceId": "/adc-service/web/rest/v1/services/proj/mod/target",
                },
            },
            {
                "name": "redirectButton",
                "props": {"location": "/proj/mod/target"},
            },
        ],
    }
    patched_live.pages.append(
        {
            "id": "page-1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": json.dumps(page_content),
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["sources_scanned"]["pages"] == 1
    assert out["ref_count"] == 3
    assert out["strong_ref_count"] == 3
    assert all(r["in_type"] == "page" for r in out["references"])
    fields = {r["field"] for r in out["references"]}
    assert fields == {"serviceName", "serviceId", "location"}


async def test_find_references_scans_inline_page_script(patched_live) -> None:
    """Service URIs embedded in the page's js_content (Script tab) match weakly."""
    page_content = {
        "id": "page",
        "name": "page",
        "js_content": {
            "proj/mod/utils": (
                "function exportTask() {\n"
                "  MessageProcessor.process({\n"
                '    serviceId: "/adc-service/rest/v1/services/proj/mod/target",\n'
                "    data: {}\n"
                "  });\n"
                "}"
            ),
        },
    }
    patched_live.pages.append(
        {
            "id": "page-1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": json.dumps(page_content),
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["ref_count"] == 1
    ref = out["references"][0]
    assert ref["in_type"] == "page"
    # inline JS strings are weak refs (the field key is "proj/mod/utils", not a typed-URI field)
    assert ref["kind"] == "weak"


async def test_find_references_relative_form_in_templates(patched_live) -> None:
    """No-leading-slash form (used in `templates: ["proj/mod/name"]`) matches with word boundary."""
    page_content = {
        "id": "page",
        "name": "page",
        "props": {"templates": ["proj/mod/target"]},
    }
    patched_live.pages.append(
        {
            "id": "page-1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": json.dumps(page_content),
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["ref_count"] == 1


async def test_find_references_relative_form_word_boundary(patched_live) -> None:
    """`proj/mod/target` must NOT match `proj/mod/target_extra`."""
    page_content = {
        "id": "page",
        "name": "page",
        "props": {"templates": ["proj/mod/target_extra"]},
    }
    patched_live.pages.append(
        {
            "id": "page-1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": json.dumps(page_content),
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    assert out["ref_count"] == 0


async def test_find_references_handles_malformed_page_content(patched_live) -> None:
    """Pages with malformed `content` JSON fall back to scanning the raw string."""
    patched_live.pages.append(
        {
            "id": "page-1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": '{"this is not valid json with /proj/mod/target inside',
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/target")
    # Still finds the URI in the raw string.
    assert out["ref_count"] == 1


async def test_find_references_rejects_from_package() -> None:
    with pytest.raises(NotImplementedError):
        await _refs.find_artifact_references(
            "testbed",
            "/proj/mod/target",
            from_package="some.gpk",
        )


# ---------------- find_unused_artifacts (mocked) ----------------


async def test_find_unused_services_separates_used_and_unused(patched_live) -> None:
    """Three target services (A, B, C). A is invoked, B is mentioned, C is unused."""
    patched_live.services.extend(
        [
            {
                "service_name": "A",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {"steps": {}},
            },
            {
                "service_name": "B",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {"steps": {}},
            },
            {
                "service_name": "C",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {"steps": {}},
            },
            {
                "service_name": "caller",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {
                    "steps": {
                        "s1": {"type": "invoke", "service_uri": "/proj/mod/A"},
                        "s2": {"type": "invoke", "service_uri": "/proj/mod/A"},
                        "s3": {"description": "see /proj/mod/B"},
                    }
                },
            },
        ]
    )

    out = await _refs.find_unused_artifacts("testbed", "proj", "mod", "service")

    unused_names = {row["name"] for row in out["definitely_unused"]}
    assert "C" in unused_names
    assert "caller" in unused_names  # nothing references caller
    assert "A" not in unused_names
    assert "B" not in unused_names

    assert out["used_summary"]["A"] == 2
    assert out["used_summary"]["B"] == 1
    assert next(iter(out["used_summary"])) == "A"


async def test_find_unused_counts_page_references_too(patched_live) -> None:
    """A service referenced only from a page must NOT show up as unused."""
    patched_live.services.append(
        {
            "service_name": "target",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {"steps": {}},
        }
    )
    patched_live.pages.append(
        {
            "id": "p1",
            "name": "tts_query",
            "project_name": "proj",
            "module_name": "mod",
            "content": json.dumps(
                {
                    "id": "page",
                    "props": {"serviceId": "/adc-service/web/rest/v1/services/proj/mod/target"},
                }
            ),
        }
    )
    out = await _refs.find_unused_artifacts("testbed", "proj", "mod", "service")
    unused_names = {row["name"] for row in out["definitely_unused"]}
    assert "target" not in unused_names
    assert out["used_summary"].get("target") == 1


async def test_find_unused_rejects_unknown_artifact_type() -> None:
    with pytest.raises(ValueError, match="unsupported artifact_type"):
        await _refs.find_unused_artifacts("testbed", "proj", "mod", "trigger")


async def test_find_unused_rejects_from_package() -> None:
    with pytest.raises(NotImplementedError):
        await _refs.find_unused_artifacts(
            "testbed",
            "proj",
            "mod",
            "service",
            from_package="some.gpk",
        )


# ---------------- RunScript / ScriptLib virtual URIs ----------------


def test_normalize_accepts_virtual_runscript_uri() -> None:
    """4-segment URI with _RunScript bucket is a valid virtual target."""
    assert _refs._normalize_target_uri("/proj/mod/_RunScript/foo") == "/proj/mod/_RunScript/foo"


def test_normalize_accepts_virtual_scriptlib_uri() -> None:
    assert _refs._normalize_target_uri("/proj/mod/_ScriptLib/utils") == "/proj/mod/_ScriptLib/utils"


def test_normalize_rejects_unknown_virtual_bucket() -> None:
    """A 4-segment URI with an unknown bucket is rejected (no silent passthrough)."""
    with pytest.raises(ValueError):
        _refs._normalize_target_uri("/proj/mod/_NotABucket/foo")


async def test_find_references_to_runscript(patched_live) -> None:
    """A runScript step's script_name registers as a strong ref to the
    virtual `/proj/mod/_RunScript/<name>` URI."""
    patched_live.services.extend(
        [
            {
                "service_name": "tts_check_faultlevel",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {
                    "steps": {
                        "runScript_1": {
                            "type": "runScript",
                            "name": "runScript_1",
                            "script_name": "runScript_check_faultlevel",
                            "next": "output_node",
                        }
                    }
                },
            },
            {
                "service_name": "unrelated",
                "project_name": "proj",
                "module_name": "mod",
                "flow": {"steps": {"input_node": {"type": "input"}}},
            },
        ]
    )
    out = await _refs.find_artifact_references(
        "testbed", "/proj/mod/_RunScript/runScript_check_faultlevel"
    )
    assert out["target"] == "/proj/mod/_RunScript/runScript_check_faultlevel"
    assert out["ref_count"] == 1
    ref = out["references"][0]
    assert ref["kind"] == "strong"
    assert ref["field"] == "script_name"
    assert ref["in"] == "/proj/mod/tts_check_faultlevel"
    assert ref["in_type"] == "service"


async def test_runscript_lookup_ignores_other_modules(patched_live) -> None:
    """RunScripts are bundled per-module — services in a different module
    cannot reference them, even if the script_name string happens to match.

    The scanner enforces this with a project/module match check before
    looking at runScript steps. (The fixture's `fake_list_services`
    intentionally ignores the project/module args so we can exercise this
    in-scanner guard directly.)"""
    patched_live.services.append(
        {
            "service_name": "different_module_service",
            "project_name": "proj",
            "module_name": "OTHER",  # different module
            "flow": {
                "steps": {
                    "runScript_1": {
                        "type": "runScript",
                        "script_name": "runScript_check_faultlevel",
                    }
                }
            },
        }
    )
    out = await _refs.find_artifact_references(
        "testbed",
        "/proj/mod/_RunScript/runScript_check_faultlevel",
    )
    # The OTHER-module service was returned by the fake fetcher but the
    # scanner correctly rejects it because runscript bundling is per-module.
    assert out["ref_count"] == 0


async def test_runscript_lookup_ignores_non_runscript_steps(patched_live) -> None:
    """A modelInstanceGetList step with a `script_name` (which it shouldn't
    have, but defensively) must not match the RunScript lookup."""
    patched_live.services.append(
        {
            "service_name": "weird",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {
                "steps": {
                    "step1": {
                        "type": "modelInstanceGetList",
                        "script_name": "runScript_check_faultlevel",  # noise
                    }
                }
            },
        }
    )
    out = await _refs.find_artifact_references(
        "testbed", "/proj/mod/_RunScript/runScript_check_faultlevel"
    )
    assert out["ref_count"] == 0


async def test_scriptlib_lookup_uses_runScriptLib_step_type(patched_live) -> None:
    """ScriptLib targets match runScriptLib steps, not runScript steps."""
    patched_live.services.append(
        {
            "service_name": "uses_lib",
            "project_name": "proj",
            "module_name": "mod",
            "flow": {
                "steps": {
                    "lib_1": {
                        "type": "runScriptLib",
                        "script_name": "shared_helper",
                    }
                }
            },
        }
    )
    out = await _refs.find_artifact_references("testbed", "/proj/mod/_ScriptLib/shared_helper")
    assert out["ref_count"] == 1
    assert out["references"][0]["in"] == "/proj/mod/uses_lib"


# ---------------- triggers as a reference source (PR3b) ----------------


async def test_find_references_scans_triggers(patched_live) -> None:
    """A trigger that fires a service registers a strong ref to that service."""
    patched_live.triggers.append(
        {
            "trigger_name": "review_accept_trigger",
            "project_name": "p",
            "module_name": "m",
            "model_uri": "/p/m/the_model",
            "event_type": "update",
            "before_or_after": "after",
            "active": True,
            "trigger_activities": [
                {
                    "activity_type": "Invoke Service",
                    "service_rest_uri": "/adc-service/rest/v1/services/p/m/target",
                }
            ],
        }
    )
    out = await _refs.find_artifact_references("testbed", "/p/m/target")
    assert out["sources_scanned"]["triggers"] == 1
    # exactly one strong ref via service_rest_uri
    assert out["ref_count"] == 1
    ref = out["references"][0]
    assert ref["kind"] == "strong"
    assert ref["field"] == "service_rest_uri"
    assert ref["in_type"] == "trigger"
    assert ref["in"] == "/p/m/review_accept_trigger"


async def test_find_references_scans_trigger_model_uri(patched_live) -> None:
    """A trigger's model_uri makes that model show as referenced (kind=strong)."""
    patched_live.triggers.append(
        {
            "trigger_name": "review_accept_trigger",
            "project_name": "p",
            "module_name": "m",
            "model_uri": "/p/m/the_model",
            "trigger_activities": [],
        }
    )
    out = await _refs.find_artifact_references("testbed", "/p/m/the_model")
    assert out["ref_count"] == 1
    ref = out["references"][0]
    assert ref["field"] == "model_uri"
    assert ref["in_type"] == "trigger"


async def test_find_unused_uses_triggers_as_source(patched_live) -> None:
    """A service referenced ONLY from a trigger must NOT show up as unused."""
    patched_live.services.append(
        {
            "service_name": "tts_review_process_order",
            "project_name": "p",
            "module_name": "m",
            "flow": {"steps": {}},
        }
    )
    patched_live.triggers.append(
        {
            "trigger_name": "review_accept_trigger",
            "project_name": "p",
            "module_name": "m",
            "model_uri": "/p/m/the_model",
            "trigger_activities": [
                {
                    "activity_type": "Invoke Service",
                    "service_rest_uri": (
                        "/adc-service/rest/v1/services/p/m/tts_review_process_order"
                    ),
                }
            ],
        }
    )
    out = await _refs.find_unused_artifacts("testbed", "p", "m", "service")
    unused_names = {row["name"] for row in out["definitely_unused"]}
    assert "tts_review_process_order" not in unused_names
    assert out["used_summary"].get("tts_review_process_order") == 1
    assert out["sources_scanned"]["triggers"] == 1


@pytest.fixture
def patched_log_counts(monkeypatch: pytest.MonkeyPatch):
    """Replace `count_service_invocations` with a stub keyed by service name.

    Tests prime the dict before calling audit_artifact_usage. Default is
    0 hits so unprimed services drop into `likely_unused_candidates`.
    """
    hits: dict[str, int] = {}

    async def fake_count(
        tenant: str,
        project_name: str,
        module_name: str,
        service_name: str,
        *,
        start_ms: int | None = None,
        end_ms: int | None = None,
    ) -> dict[str, Any]:
        return {
            "service": f"/{project_name}/{module_name}/{service_name}",
            "total_hits": hits.get(service_name, 0),
            "start_ms": 0,
            "end_ms": 0,
            "warnings": [],
        }

    monkeypatch.setattr("ows_gde_mcp.tools.log_analysis.count_service_invocations", fake_count)
    return hits


async def test_audit_buckets_static_only_used_runtime_only_and_candidates(
    patched_live, patched_log_counts
) -> None:
    """Four services exercise every bucket of the audit output:
    A: 1 static ref, 0 log hits        → static_refs
    B: 1 static ref, 5 log hits        → both
    C: 0 static refs, 3 log hits       → runtime_only (likely Trigger)
    D: 0 static refs, 0 log hits       → likely_unused_candidates
    """
    patched_live.services.extend(
        [
            {
                "service_name": "A",
                "project_name": "p",
                "module_name": "m",
                "flow": {"steps": {}},
            },
            {
                "service_name": "B",
                "project_name": "p",
                "module_name": "m",
                "flow": {"steps": {}},
            },
            {
                "service_name": "C",
                "project_name": "p",
                "module_name": "m",
                "flow": {"steps": {}},
            },
            {
                "service_name": "D",
                "project_name": "p",
                "module_name": "m",
                "flow": {"steps": {}},
            },
            {
                "service_name": "caller",
                "project_name": "p",
                "module_name": "m",
                "flow": {
                    "steps": {
                        "s1": {"type": "invoke", "service_uri": "/p/m/A"},
                        "s2": {"type": "invoke", "service_uri": "/p/m/B"},
                    }
                },
            },
        ]
    )
    patched_log_counts.update({"B": 5, "C": 3})

    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service", include_used=True)

    static_only = {row["name"] for row in out["definitely_used"]["static_refs"]}
    both = {row["name"] for row in out["definitely_used"]["both"]}
    runtime_only = {row["name"] for row in out["definitely_used"]["runtime_only"]}
    candidates = {row["name"] for row in out["likely_unused_candidates"]}

    assert "A" in static_only
    assert "B" in both
    assert "C" in runtime_only
    assert "D" in candidates

    a_row = next(r for r in out["definitely_used"]["static_refs"] if r["name"] == "A")
    assert a_row["runtime_hits"] == 0


async def test_audit_lean_default_returns_counts_only(
    patched_live, patched_log_counts
) -> None:
    """Default `include_used=False` returns counts, not the full bucket arrays.

    Pagination metadata is always present.
    """
    patched_live.services.extend(
        [
            {"service_name": n, "project_name": "p", "module_name": "m", "flow": {"steps": {}}}
            for n in ("A", "B", "C", "D")
        ]
        + [
            {
                "service_name": "caller",
                "project_name": "p",
                "module_name": "m",
                "flow": {
                    "steps": {
                        "s1": {"type": "invoke", "service_uri": "/p/m/A"},
                        "s2": {"type": "invoke", "service_uri": "/p/m/B"},
                    }
                },
            }
        ]
    )
    patched_log_counts.update({"B": 5, "C": 3})

    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service")

    used = out["definitely_used"]
    assert set(used.keys()) == {"both_count", "static_refs_count", "runtime_only_count"}
    assert used["both_count"] == 1  # B
    assert used["static_refs_count"] == 1  # A
    assert used["runtime_only_count"] == 1  # C
    # `caller` itself has no incoming refs and no log hits, so it's also a
    # candidate alongside `D`.
    assert {row["name"] for row in out["likely_unused_candidates"]} == {"D", "caller"}
    assert out["pagination"] == {
        "start": 0,
        "limit": 0,
        "total_in_scope": 5,
        "returned": 5,
    }


async def test_audit_pagination_slices_artifacts(patched_live, patched_log_counts) -> None:
    """`start` + `limit` audit only the named slice; total_in_scope reports module size."""
    patched_live.services.extend(
        [
            {"service_name": n, "project_name": "p", "module_name": "m", "flow": {"steps": {}}}
            for n in ("alpha", "beta", "gamma", "delta", "epsilon")
        ]
    )
    out = await _refs.audit_artifact_usage(
        "testbed", "p", "m", "service", limit=2, include_used=True
    )
    assert out["pagination"]["total_in_scope"] == 5
    assert out["pagination"]["returned"] == 2
    page_names = {row["name"] for row in out["likely_unused_candidates"]}
    page_names |= {row["name"] for row in out["definitely_used"]["static_refs"]}
    page_names |= {row["name"] for row in out["definitely_used"]["both"]}
    page_names |= {row["name"] for row in out["definitely_used"]["runtime_only"]}
    assert len(page_names) == 2

    out2 = await _refs.audit_artifact_usage(
        "testbed", "p", "m", "service", start=2, limit=2, include_used=True
    )
    page2_names = {row["name"] for row in out2["likely_unused_candidates"]}
    assert len(page2_names) == 2
    assert page2_names.isdisjoint(page_names)


async def test_audit_candidate_confidence_is_medium_when_workflows_unscanned(
    patched_live, patched_log_counts
) -> None:
    """Triggers ARE scanned (PR3b) but workflows aren't → confidence is 'medium'."""
    patched_live.services.append(
        {
            "service_name": "orphan",
            "project_name": "p",
            "module_name": "m",
            "flow": {"steps": {}},
        }
    )
    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service")
    candidates = out["likely_unused_candidates"]
    assert len(candidates) == 1
    row = candidates[0]
    assert row["name"] == "orphan"
    assert row["confidence"] == "medium"
    caveats_blob = " ".join(row["caveats"])
    assert "Workflow" in caveats_blob
    assert "external" in caveats_blob.lower()
    # Trigger caveat removed in PR3b.
    assert "Trigger artifacts are NOT" not in caveats_blob


async def test_audit_skip_runtime_keeps_runtime_hits_none(
    patched_live, monkeypatch: pytest.MonkeyPatch
) -> None:
    """include_runtime=False must NOT call count_service_invocations.

    Contract: runtime_hits is None per row so callers can tell
    'not measured' from 'measured 0'."""

    async def must_not_run(*args, **kwargs):  # pragma: no cover
        raise AssertionError("count_service_invocations must not be called")

    monkeypatch.setattr("ows_gde_mcp.tools.log_analysis.count_service_invocations", must_not_run)
    patched_live.services.append(
        {
            "service_name": "X",
            "project_name": "p",
            "module_name": "m",
            "flow": {"steps": {}},
        }
    )
    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service", include_runtime=False)
    assert any(row["runtime_hits"] is None for row in out["likely_unused_candidates"])
    assert any("include_runtime=False" in w for w in out["warnings"])


async def test_audit_no_definitely_unused_bucket(patched_live, patched_log_counts) -> None:
    """The audit output must NOT contain a `definitely_unused` key — even
    candidates with zero signals are only `likely_unused_candidates`."""
    patched_live.services.append(
        {
            "service_name": "orphan",
            "project_name": "p",
            "module_name": "m",
            "flow": {"steps": {}},
        }
    )
    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service")
    assert "definitely_unused" not in out


# ---------------- Phase 3: RunScript correlation ----------------


def test_bundled_scripts_for_returns_runscript_and_scriptlib_names() -> None:
    """The helper finds every script name across runScript + runScriptLib steps."""
    flow = {
        "steps": {
            "s1": {"type": "runScript", "script_name": "calc_total"},
            "s2": {"type": "invoke", "service_uri": "/p/m/x"},
            "s3": {"type": "runScriptLib", "script_name": "shared_helper"},
            "s4": {"type": "runScript"},  # no script_name → skipped
        }
    }
    assert sorted(_refs._bundled_scripts_for(flow)) == ["calc_total", "shared_helper"]


def test_bundled_scripts_for_tolerates_bad_input() -> None:
    """Non-dict flow / non-dict steps must not raise."""
    assert _refs._bundled_scripts_for(None) == []
    assert _refs._bundled_scripts_for("not a flow") == []
    assert _refs._bundled_scripts_for({"steps": "wat"}) == []


async def test_audit_correlates_via_bundled_scripts(
    patched_live, patched_log_counts
) -> None:
    """A service with a RunScript whose name appears in logs surfaces as used.

    Before PR3c the audit probed only the parent service name; the
    log-by-script-name signal was lost and the service appeared as a
    candidate. Now hits roll up to the parent.
    """
    patched_live.services.append(
        {
            "service_name": "tts_check_faultlevel",
            "project_name": "p",
            "module_name": "m",
            "flow": {
                "steps": {
                    "s1": {
                        "type": "runScript",
                        "script_name": "runScript_check_faultlevel",
                    }
                }
            },
        }
    )
    # Log Analysis records `element_name=runScript_check_faultlevel`,
    # not the parent service name.
    patched_log_counts["runScript_check_faultlevel"] = 7

    out = await _refs.audit_artifact_usage(
        "testbed", "p", "m", "service", include_used=True
    )
    runtime_only = {row["name"] for row in out["definitely_used"]["runtime_only"]}
    candidates = {row["name"] for row in out["likely_unused_candidates"]}
    assert "tts_check_faultlevel" in runtime_only
    assert "tts_check_faultlevel" not in candidates
    row = next(
        r for r in out["definitely_used"]["runtime_only"]
        if r["name"] == "tts_check_faultlevel"
    )
    assert row["runtime_hits"] == 7


async def test_audit_unused_runscript_does_not_get_credit_from_other_scripts(
    patched_live, patched_log_counts
) -> None:
    """Hits on script names belonging to OTHER services don't roll up here."""
    patched_live.services.extend(
        [
            {
                "service_name": "called_service",
                "project_name": "p",
                "module_name": "m",
                "flow": {
                    "steps": {
                        "s1": {"type": "runScript", "script_name": "really_busy_script"}
                    }
                },
            },
            {
                "service_name": "orphan_service",
                "project_name": "p",
                "module_name": "m",
                "flow": {"steps": {}},
            },
        ]
    )
    patched_log_counts["really_busy_script"] = 99

    out = await _refs.audit_artifact_usage(
        "testbed", "p", "m", "service", include_used=True
    )
    candidates = {row["name"] for row in out["likely_unused_candidates"]}
    runtime_only = {row["name"] for row in out["definitely_used"]["runtime_only"]}
    assert "orphan_service" in candidates
    assert "called_service" in runtime_only


async def test_audit_caveats_no_longer_mention_runscript_correlation(
    patched_live, patched_log_counts
) -> None:
    """The 'Log Analysis filters by element_name only' caveat is gone — fixed in PR3c."""
    patched_live.services.append(
        {
            "service_name": "orphan",
            "project_name": "p",
            "module_name": "m",
            "flow": {"steps": {}},
        }
    )
    out = await _refs.audit_artifact_usage("testbed", "p", "m", "service")
    row = out["likely_unused_candidates"][0]
    caveats_blob = " ".join(row["caveats"])
    assert "RunScript" not in caveats_blob
    assert "element_name" not in caveats_blob
