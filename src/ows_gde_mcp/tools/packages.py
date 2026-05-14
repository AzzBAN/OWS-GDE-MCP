"""MCP tools that operate on local OWS app package files (`.gpk`).

These tools don't touch any remote OWS host — they parse the offline export
of an app and let an agent introspect Models, Pages, Services, Workflows,
Triggers, etc. without auth.

Default search location is `docs/discovery/<tenant>/sample-apps/` relative to
the project root. Tools accept an explicit `path` to override.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ows_gde_mcp.package import AppPackage, open_package

# Project root (3 levels up from this file: src/ows_gde_mcp/tools/packages.py)
_PROJECT_ROOT = Path(__file__).resolve().parents[3]


def _default_search_dirs() -> list[Path]:
    return [
        _PROJECT_ROOT / "docs" / "discovery" / "testbed" / "sample-apps",
        _PROJECT_ROOT / "docs" / "discovery" / "prod" / "sample-apps",
    ]


def _resolve_package_path(name_or_path: str) -> Path:
    """Accept either an absolute/relative path or a bare app name and find it."""
    p = Path(name_or_path)
    if p.is_file():
        return p
    # Try relative to project root.
    rel = _PROJECT_ROOT / name_or_path
    if rel.is_file():
        return rel
    # Search for a file whose stem starts with the given name.
    for d in _default_search_dirs():
        if not d.is_dir():
            continue
        # exact stem match first
        for f in sorted(d.glob("*.gpk")):
            if f.stem == name_or_path or f.name == name_or_path:
                return f
        # then prefix match (allow "tt_improvement" to match "tt_improvement_0.0.80.gpk")
        for f in sorted(d.glob("*.gpk")):
            stem = f.stem
            if stem.startswith(name_or_path + "_") or stem.startswith(name_or_path):
                return f
    raise FileNotFoundError(
        f"Couldn't find package '{name_or_path}'. "
        f"Try an absolute path or place the .gpk under docs/discovery/<tenant>/sample-apps/."
    )


# ---------------- listing & summaries ----------------


def list_app_packages() -> list[dict[str, Any]]:
    """List every `.gpk` file discovered under `docs/discovery/*/sample-apps/`.

    Each entry has `path`, `name`, `version`, `tenant_dir`, and basic counts
    (modules, total artifact count). Doesn't fully parse — fast.
    """
    out: list[dict[str, Any]] = []
    for d in _default_search_dirs():
        if not d.is_dir():
            continue
        tenant = d.parent.name
        for f in sorted(d.glob("*.gpk")):
            try:
                pkg = open_package(f)
                arts = pkg.all_artifacts()
                out.append(
                    {
                        "path": str(f),
                        "filename": f.name,
                        "name": pkg.name,
                        "version": pkg.version,
                        "type": pkg.app_type,
                        "tenant_dir": tenant,
                        "module_count": len(pkg.modules),
                        "artifact_count": len(arts),
                        "artifact_types": sorted({a.type for a in arts}),
                    }
                )
            except Exception as e:
                out.append({"path": str(f), "error": str(e)})
    return out


def get_app_package_info(name_or_path: str) -> dict[str, Any]:
    """Return a structured summary of one package: manifest highlights,
    modules, per-type artifact counts, and creator/dev-environment info.

    Args:
        name_or_path: bare app name (e.g., "tt_improvement") or path to a .gpk.
    """
    pkg = open_package(_resolve_package_path(name_or_path))
    return pkg.summary()


# ---------------- artifacts inside a package ----------------


def list_app_artifacts(
    name_or_path: str,
    *,
    type: str | None = None,
    module: str | None = None,
    name_contains: str | None = None,
    limit: int = 200,
) -> list[dict[str, Any]]:
    """List artifacts inside one app package.

    Args:
        name_or_path: bare app name or .gpk path.
        type: filter by artifact type (e.g., "MODEL", "PAGE", "SERVICE").
              Case-insensitive.
        module: filter to artifacts in a specific module name.
        name_contains: case-insensitive substring filter on artifact name.
        limit: cap the number of results (default 200).
    """
    pkg = open_package(_resolve_package_path(name_or_path))
    type_u = type.upper() if type else None
    out: list[dict[str, Any]] = []
    for a in pkg.all_artifacts():
        if type_u and a.type != type_u:
            continue
        if module and a.module != module:
            continue
        if name_contains and name_contains.lower() not in a.name.lower():
            continue
        out.append(
            {
                "type": a.type,
                "name": a.name,
                "project": a.project,
                "module": a.module,
                "uri": a.uri,
                "file_count": len(a.files),
            }
        )
        if len(out) >= limit:
            break
    return out


def get_app_artifact(
    name_or_path: str,
    type: str,
    name: str,
    *,
    module: str | None = None,
    include_files: bool = True,
) -> dict[str, Any]:
    """Fetch one artifact's parsed JSON + accompanying file list.

    Args:
        name_or_path: bare app name or .gpk path.
        type: artifact type (case-insensitive: "MODEL", "PAGE", ...).
        name: artifact name (e.g., "tts_data" for a Model, "tts_query" for a Page).
        module: optional disambiguation if the same artifact name exists in
                multiple modules.
        include_files: include the list of zip-relative file paths comprising
                this artifact.
    """
    pkg = open_package(_resolve_package_path(name_or_path))
    type_u = type.upper()
    matches = [
        a
        for a in pkg.all_artifacts()
        if a.type == type_u and a.name == name and (module is None or a.module == module)
    ]
    if not matches:
        raise ValueError(f"No {type_u} artifact named '{name}' found in package '{pkg.name}'.")
    if len(matches) > 1 and module is None:
        raise ValueError(
            f"{len(matches)} {type_u} artifacts named '{name}' across modules: "
            f"{[a.module for a in matches]}. Pass `module=` to disambiguate."
        )
    a = matches[0]
    out: dict[str, Any] = {
        "type": a.type,
        "name": a.name,
        "project": a.project,
        "module": a.module,
        "uri": a.uri,
        "raw": a.raw,
    }
    if include_files:
        out["files"] = a.files
    return out


def search_app_artifacts(
    query: str,
    *,
    type: str | None = None,
    limit: int = 50,
) -> list[dict[str, Any]]:
    """Search artifact names across **all** locally available packages.

    Useful when you don't know which app contains an artifact.
    """
    type_u = type.upper() if type else None
    q = query.lower()
    out: list[dict[str, Any]] = []
    for d in _default_search_dirs():
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.gpk")):
            try:
                pkg = open_package(f)
            except Exception:
                continue
            for a in pkg.all_artifacts():
                if type_u and a.type != type_u:
                    continue
                if q not in a.name.lower():
                    continue
                out.append(
                    {
                        "package": pkg.name,
                        "package_path": str(f),
                        "type": a.type,
                        "name": a.name,
                        "module": a.module,
                        "uri": a.uri,
                    }
                )
                if len(out) >= limit:
                    return out
    return out


# Re-exports for ergonomic import elsewhere.
__all__ = [
    "AppPackage",
    "get_app_artifact",
    "get_app_package_info",
    "list_app_artifacts",
    "list_app_packages",
    "search_app_artifacts",
]
