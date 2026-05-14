"""Parser for OWS / GDE app package files (`.gpk`).

A `.gpk` is a zip archive with this canonical layout:

    manifest.json             — app-level metadata (name, version, dependencies, …)
    category.json             — business-type categorization
    patch.json                — { source_version, target_version }
    resources/
        birth_permit.json     — issuing tenant / dev environment metadata
        logo.svg              — app icon
    modules/
        <project_name>/
            <module_name>/
                module.json   — declared `supported_item_types`, dependencies, …
                studio.json   — Studio menu config
                <TYPE>/       — one dir per artifact type
                    <name>.json
                    …
                    (some types embed extra subdirs, e.g. SERVICE has
                     RunScript/, ScriptLib/, Translator/, Validator/;
                     PAGE has script/ for JS/CSS; WORKFLOW is a subdir per
                     workflow with multiple json files; I18N has per-locale
                     directories.)

Artifact type names (from `module.supported_item_types`) we've seen in real
samples: PERMISSION, INBOUND_REST, INBOUND_API, EVENT_LISTENER, TRIGGER,
DATA_PACKAGE, MOBILE_PAGE, PAGE, MODEL, MODEL_DATA_ACCESS, EVENT, MATELINE,
ERROR_CODE, CARD, DATA_IMPORT, OUTBOUND_REST, MODEL_ARCHIVE, DOCUMENT,
SERVICE, DATA_EXPORT, MENU, JOB, WORKFLOW, I18N.

The Studio also declares Data Factory / AI Studio / Agent / MCP / RPA types
which simply do not appear in the sample apps shipped with this repo.
"""

from __future__ import annotations

import io
import json
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Type names that are stored as a single .json file at <TYPE>/<name>.json.
_FILE_BASED_TYPES = {
    "MODEL",
    "MODEL_DATA_ACCESS",
    "MODEL_ARCHIVE",
    "PAGE",
    "MOBILE_PAGE",
    "SERVICE",
    "TRIGGER",
    "EVENT",
    "EVENT_LISTENER",
    "JOB",
    "MENU",
    "CARD",
    "DOCUMENT",
    "DATA_EXPORT",
    "DATA_IMPORT",
    "INBOUND_REST",
    "OUTBOUND_REST",
    "INBOUND_API",
    "ERROR_CODE",
    "DATA_PACKAGE",
    "MATELINE",
}

# Type names whose unit is a *directory* (e.g., WORKFLOW).
_DIR_BASED_TYPES = {"WORKFLOW"}

# Type names with a fixed set of files (not one-per-artifact).
_BUNDLE_TYPES = {"PERMISSION", "I18N"}


@dataclass
class Artifact:
    """A single artifact inside a module (e.g., one Model, one Page)."""

    type: str
    """Artifact type name (e.g., "MODEL", "PAGE", "SERVICE", "WORKFLOW")."""

    name: str
    """Artifact name (filename without extension or directory name)."""

    project: str
    module: str

    files: list[str] = field(default_factory=list)
    """All zip-relative file paths comprising this artifact."""

    raw: dict[str, Any] | None = None
    """Parsed JSON of the primary artifact file (None if multi-file or non-JSON)."""

    @property
    def uri(self) -> str:
        """Canonical OWS asset URI: `/<project>/<module>/<name>`."""
        return f"/{self.project}/{self.module}/{self.name}"


@dataclass
class Module:
    project: str
    name: str
    config: dict[str, Any] = field(default_factory=dict)
    """Parsed project-level `module.json` (shared across modules in the same project)."""
    studio: dict[str, Any] | None = None
    """Parsed project-level `studio.json` if present."""
    brief: dict[str, Any] | None = None
    """Parsed module-level `brief.json` if present."""
    artifacts: dict[str, list[Artifact]] = field(default_factory=dict)
    """Indexed by artifact type — e.g., `artifacts["MODEL"]`."""

    def all_artifacts(self) -> list[Artifact]:
        out: list[Artifact] = []
        for v in self.artifacts.values():
            out.extend(v)
        return out


@dataclass
class AppPackage:
    path: Path
    manifest: dict[str, Any]
    """Parsed `manifest.json`."""
    category: list[dict[str, Any]] | None = None
    patch: dict[str, Any] | None = None
    birth_permit: dict[str, Any] | None = None
    modules: list[Module] = field(default_factory=list)

    # --------- convenience accessors ---------

    @property
    def name(self) -> str:
        return self.manifest.get("name") or self.manifest.get("source_project_name") or ""

    @property
    def version(self) -> str:
        return self.manifest.get("version", "")

    @property
    def app_type(self) -> str:
        return self.manifest.get("type", "")

    def find_module(self, name: str) -> Module | None:
        for m in self.modules:
            if m.name == name:
                return m
        return None

    def all_artifacts(self) -> list[Artifact]:
        out: list[Artifact] = []
        for m in self.modules:
            out.extend(m.all_artifacts())
        return out

    def artifacts_by_type(self) -> dict[str, list[Artifact]]:
        """Aggregate across modules: `{ "MODEL": [...], "PAGE": [...] }`."""
        out: dict[str, list[Artifact]] = {}
        for m in self.modules:
            for type_name, items in m.artifacts.items():
                out.setdefault(type_name, []).extend(items)
        return out

    def summary(self) -> dict[str, Any]:
        """Compact JSON-friendly summary suitable for an MCP response."""
        types: dict[str, int] = {}
        for m in self.modules:
            for t, lst in m.artifacts.items():
                types[t] = types.get(t, 0) + len(lst)
        bp = self.birth_permit or {}
        return {
            "path": str(self.path),
            "name": self.name,
            "version": self.version,
            "type": self.app_type,
            "version_type": self.manifest.get("version_type"),
            "from_gde_version": self.manifest.get("from_gde_version"),
            "scene": (self.manifest.get("scene") or {}).get("name"),
            "modules": [
                {
                    "project": m.project,
                    "name": m.name,
                    "supported_item_types": m.config.get("supported_item_types", []),
                    "artifact_counts": {t: len(v) for t, v in sorted(m.artifacts.items())},
                }
                for m in self.modules
            ],
            "totals": dict(sorted(types.items())),
            "dev_environment": bp.get("dev_environment"),
            "dev_tenant": bp.get("dev_tenant"),
            "creator": bp.get("creator"),
        }


# --------------- core open() ---------------


def open_package(path: str | Path) -> AppPackage:
    """Open a `.gpk` (zip) archive and parse it into an `AppPackage`."""
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Not a file: {p}")

    with zipfile.ZipFile(p) as zf:
        names = zf.namelist()
        manifest = _read_json(zf, "manifest.json", required=True) or {}
        category = _read_json(zf, "category.json")
        patch = _read_json(zf, "patch.json")
        birth_permit = _read_json(zf, "resources/birth_permit.json")

        # Layout in real .gpk files:
        #   modules/<project>/module.json     <- project-level metadata
        #   modules/<project>/studio.json     <- project-level metadata
        #   modules/<project>/<module>/<TYPE>/<artifact>.json
        # A "module" must contain at least one artifact-TYPE subdir.
        module_files: dict[tuple[str, str], list[str]] = {}
        seen_modules: set[tuple[str, str]] = set()
        for n in names:
            if n.endswith("/"):
                continue  # skip explicit directory entries
            parts = n.split("/")
            if len(parts) < 4 or parts[0] != "modules":
                continue
            proj, mod = parts[1], parts[2]
            if not proj or not mod or proj.startswith(".") or mod.startswith("."):
                continue
            if mod.endswith(".json"):
                # this is a project-level metadata file, not a module
                continue
            module_files.setdefault((proj, mod), []).append(n)
            seen_modules.add((proj, mod))

        modules: list[Module] = []
        for (proj, mod), files in module_files.items():
            mod_prefix = f"modules/{proj}/{mod}/"
            project_cfg = _read_json(zf, f"modules/{proj}/module.json") or {}
            project_studio = _read_json(zf, f"modules/{proj}/studio.json")
            module_brief = _read_json(zf, mod_prefix + "brief.json")
            module = Module(
                project=proj,
                name=mod,
                config=project_cfg,
                studio=project_studio,
                brief=module_brief,
            )
            module.artifacts = _index_artifacts(zf, mod_prefix, files, proj, mod)
            modules.append(module)

    return AppPackage(
        path=p,
        manifest=manifest,
        category=category,
        patch=patch,
        birth_permit=birth_permit,
        modules=modules,
    )


# --------------- artifact indexing ---------------


def _index_artifacts(
    zf: zipfile.ZipFile,
    mod_prefix: str,
    all_files: list[str],
    project: str,
    module: str,
) -> dict[str, list[Artifact]]:
    """Walk one module directory and group files into Artifact objects."""

    # Find the immediate type dirs under the module: e.g. modules/X/Y/MODEL/
    type_to_files: dict[str, list[str]] = {}
    for n in all_files:
        suffix = n[len(mod_prefix) :] if n.startswith(mod_prefix) else None
        if not suffix or "/" not in suffix:
            continue
        type_name, *rest = suffix.split("/", 1)
        if not _looks_like_type_dir(type_name):
            continue
        if not rest or not rest[0]:
            continue
        # Skip housekeeping files (e.g. SERVICE/patch.diff.brief.json).
        leaf = rest[0].split("/")[-1]
        if leaf in {"patch.diff.brief.json", "brief.json", "package.json"}:
            continue
        type_to_files.setdefault(type_name, []).append(suffix)

    out: dict[str, list[Artifact]] = {}
    for type_name, suffixes in type_to_files.items():
        artifacts = _group_into_artifacts(zf, mod_prefix, type_name, suffixes, project, module)
        if artifacts:
            out[type_name] = artifacts
    return out


def _looks_like_type_dir(name: str) -> bool:
    """Heuristic: artifact type dirs are uppercase with underscores."""
    return bool(name) and name == name.upper() and not name.endswith(".json")


def _group_into_artifacts(
    zf: zipfile.ZipFile,
    mod_prefix: str,
    type_name: str,
    type_suffixes: list[str],
    project: str,
    module: str,
) -> list[Artifact]:
    """Group files inside a single artifact-type directory into Artifacts.

    Strategy:
    - For DIR_BASED types (WORKFLOW): one Artifact per first-level subdir.
    - For BUNDLE types (PERMISSION, I18N): one synthetic Artifact named
      after the type, files = the whole subtree.
    - Otherwise: one Artifact per top-level `.json` file (stem = name).
      Sibling files (e.g., `script/<name>_*.js` for PAGE) are attached.
    """
    type_prefix = f"{type_name}/"
    rel = [s[len(type_prefix) :] for s in type_suffixes if s.startswith(type_prefix)]

    if type_name in _BUNDLE_TYPES:
        files = [mod_prefix + type_prefix + r for r in rel]
        primary = "permissions.json" if type_name == "PERMISSION" else "bundle.json"
        primary_path = mod_prefix + type_prefix + primary
        raw = _safe_read_json(zf, primary_path)
        return [
            Artifact(
                type=type_name,
                name=type_name.lower(),
                project=project,
                module=module,
                files=sorted(files),
                raw=raw,
            )
        ]

    if type_name in _DIR_BASED_TYPES:
        # group by first-level subdir
        groups: dict[str, list[str]] = {}
        for r in rel:
            if "/" not in r:
                continue
            head, _ = r.split("/", 1)
            groups.setdefault(head, []).append(r)
        out: list[Artifact] = []
        for sub, items in sorted(groups.items()):
            files = [mod_prefix + type_prefix + i for i in items]
            # try to read a "<sub>_definition.json"-style primary
            cand = next((f for f in files if f.endswith(f"{sub}_process_definition.json")), None)
            raw = _safe_read_json(zf, cand) if cand else None
            out.append(
                Artifact(
                    type=type_name,
                    name=sub,
                    project=project,
                    module=module,
                    files=sorted(files),
                    raw=raw,
                )
            )
        return out

    # File-based types — top-level .json files become artifacts; siblings
    # (e.g., PAGE/script/<name>_*.js) are attached to their owning artifact.
    by_artifact: dict[str, list[str]] = {}
    primary_files: dict[str, str] = {}
    for r in rel:
        full = mod_prefix + type_prefix + r
        if "/" not in r and r.endswith(".json"):
            stem = r[: -len(".json")]
            primary_files[stem] = full
            by_artifact.setdefault(stem, []).append(full)
        else:
            # subdir file (e.g., script/foo_init.js or RunScript/...). Attach
            # to a stem if its name starts with one we know; otherwise skip
            # — these become module-level supplementary files.
            attached = False
            for stem in list(primary_files):
                if r.split("/", 1)[-1].startswith(stem):
                    by_artifact[stem].append(full)
                    attached = True
                    break
            if not attached:
                # Keep as part of synthetic "_misc" bucket so we don't lose track.
                by_artifact.setdefault(f"_misc:{r.split('/', 1)[0]}", []).append(full)

    out2: list[Artifact] = []
    for name, files in sorted(by_artifact.items()):
        primary = primary_files.get(name)
        raw = _safe_read_json(zf, primary) if primary else None
        out2.append(
            Artifact(
                type=type_name,
                name=name,
                project=project,
                module=module,
                files=sorted(files),
                raw=raw,
            )
        )
    return out2


# --------------- helpers ---------------


def _read_json(zf: zipfile.ZipFile, name: str, *, required: bool = False) -> Any | None:
    if name not in zf.namelist():
        if required:
            raise FileNotFoundError(f"Missing in package: {name}")
        return None
    with zf.open(name) as f:
        try:
            return json.load(io.TextIOWrapper(f, encoding="utf-8"))
        except json.JSONDecodeError as e:
            if required:
                raise
            return {"_parse_error": str(e)}


def _safe_read_json(zf: zipfile.ZipFile, name: str | None) -> Any | None:
    if not name or name not in zf.namelist():
        return None
    return _read_json(zf, name)
