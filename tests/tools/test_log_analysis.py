"""Unit tests for `log_analysis` summarisation helpers.

Focused on `_summarize_log_row`'s `content_preview_chars` truncation —
the public `search_service_logs` HTTP layer is exercised indirectly via
the audit-flow tests in `tests/tools/test_references.py`.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

from ows_gde_mcp.config import Tenant
from ows_gde_mcp.tools import log_analysis as _logs


def _row(content: str | None = None, **overrides: object) -> dict:
    base = {
        "id": "1",
        "log_time_millis": 1700000000000,
        "trace_id": "trace-abc",
        "operator": "alice ",
        "app_name": "tt_app",
        "module_name": "billing",
        "element_type": "SERVICE",
        "element_name": "compute_total",
        "operation_type": "INVOKE",
        "log_level": "INFO",
        "cost_time": 42,
        "log_content": content,
        "location_info": "service=compute_total | node=s1",
    }
    base.update(overrides)
    return base


def test_summarize_log_row_truncates_long_content() -> None:
    long = "x" * 500
    out = _logs._summarize_log_row(_row(long))
    assert out["log_content"].endswith("...")
    assert len(out["log_content"]) == 203  # 200 + ellipsis


def test_summarize_log_row_preserves_short_content() -> None:
    short = "service started"
    out = _logs._summarize_log_row(_row(short))
    assert out["log_content"] == short


def test_summarize_log_row_zero_keeps_full_content() -> None:
    long = "y" * 500
    out = _logs._summarize_log_row(_row(long), content_preview_chars=0)
    assert out["log_content"] == long


def test_summarize_log_row_custom_preview_chars() -> None:
    long = "z" * 500
    out = _logs._summarize_log_row(_row(long), content_preview_chars=50)
    assert out["log_content"].endswith("...")
    assert len(out["log_content"]) == 53


def test_summarize_log_row_handles_missing_content() -> None:
    out = _logs._summarize_log_row(_row(None))
    assert out["log_content"] is None


def test_summarize_log_row_strips_operator_and_maps_fields() -> None:
    """Trim operator + remap upstream field names (cost_time → duration_ms)."""
    out = _logs._summarize_log_row(_row("hi"))
    assert out["operator"] == "alice"
    assert out["duration_ms"] == 42
    assert out["log_time_ms"] == 1700000000000


# ---------------- CSRF disk-cache helpers ----------------


@pytest.fixture
def disk_csrf_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect the on-disk CSRF cache to `tmp_path` for the test."""
    p = tmp_path / "csrf.json"
    monkeypatch.setattr(_logs, "_CSRF_DISK_PATH", p)
    return p


def test_disk_csrf_round_trip(disk_csrf_path: Path) -> None:
    _logs._write_disk_csrf(Tenant.TESTBED, "ABCDEF123")
    assert _logs._read_disk_csrf(Tenant.TESTBED) == "ABCDEF123"
    # File contents are JSON {tenant: {token, fetched_at}}.
    data = json.loads(disk_csrf_path.read_text(encoding="utf-8"))
    assert data["testbed"]["token"] == "ABCDEF123"
    assert isinstance(data["testbed"]["fetched_at"], (int, float))


def test_disk_csrf_no_file_returns_none(disk_csrf_path: Path) -> None:
    assert _logs._read_disk_csrf(Tenant.TESTBED) is None


def test_disk_csrf_corrupt_json_returns_none(disk_csrf_path: Path) -> None:
    disk_csrf_path.parent.mkdir(parents=True, exist_ok=True)
    disk_csrf_path.write_text("{not-json", encoding="utf-8")
    assert _logs._read_disk_csrf(Tenant.TESTBED) is None


def test_disk_csrf_expired_returns_none(
    disk_csrf_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tokens older than the TTL are treated as missing."""
    disk_csrf_path.parent.mkdir(parents=True, exist_ok=True)
    stale = {"testbed": {"token": "STALE", "fetched_at": time.time() - 9999}}
    disk_csrf_path.write_text(json.dumps(stale), encoding="utf-8")
    monkeypatch.setattr(_logs, "_CSRF_TTL_SECONDS", 60)
    assert _logs._read_disk_csrf(Tenant.TESTBED) is None


def test_disk_csrf_invalidate_drops_only_target_tenant(disk_csrf_path: Path) -> None:
    _logs._write_disk_csrf(Tenant.TESTBED, "T1")
    _logs._write_disk_csrf(Tenant.PROD, "P1")
    _logs._invalidate_disk_csrf(Tenant.TESTBED)
    data = json.loads(disk_csrf_path.read_text(encoding="utf-8"))
    assert "testbed" not in data
    assert data["prod"]["token"] == "P1"
    # And the public reader agrees.
    assert _logs._read_disk_csrf(Tenant.TESTBED) is None
    assert _logs._read_disk_csrf(Tenant.PROD) == "P1"


def test_disk_csrf_write_preserves_other_tenants(disk_csrf_path: Path) -> None:
    _logs._write_disk_csrf(Tenant.TESTBED, "T1")
    _logs._write_disk_csrf(Tenant.PROD, "P1")
    data = json.loads(disk_csrf_path.read_text(encoding="utf-8"))
    assert set(data.keys()) == {"testbed", "prod"}
