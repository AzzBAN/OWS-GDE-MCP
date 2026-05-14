# Tools — `ows-gde-mcp`

Auto-generated from the FastMCP server. **20 tools total.**

Regenerate with `uv run python scripts/gen_tools_md.py`.

## Diagnostics

### `status()`

Report MCP server status & which tenants have URLs/secrets configured.

### `whoami(tenant: string)`

Return the logged-in user profile for the given tenant.

## Live OWS (require `OWS_<TENANT>_SESSION_COOKIE`)

### `call_ows_api(tenant: string, method: string, path: string, body?: ?, params?: dict | null, confirm?: boolean = False)`

Generic escape hatch — call any OWS endpoint that we haven't yet

### `get_favorite_menus(tenant: string)`

Return the current user's pinned/favorite menu entries.

### `get_model(tenant: string, model_id: integer)`

Fetch a Data Model's full schema by id (every property + restrictions).

### `get_model_fields(tenant: string, asset_uri: string)`

Return the TQL queryable-field schema for a Model asset.

### `get_service(tenant: string, project_name: string, module_name: string, service_name: string)`

Fetch one Service's full definition (including its `flow` steps).

### `get_studio_module(tenant: string, module_id: integer)`

Get module detail including which artifact types it supports.

### `get_studio_project(tenant: string, project: string | integer)`

Get one Studio project by id or by name.

### `list_live_apps(tenant: string)`

List unique OWS apps the current user has access to.

### `list_live_menus(tenant: string, flatten?: boolean = False, only_with_url?: boolean = False)`

List the menu tree granted to the current user.

### `list_models(tenant: string, project_name: string, module_name: string, model_name?: string, model_type?: string, active?: string, start?: integer = 0, limit?: integer = 50)`

List Data Models declared in a Studio project module.

### `list_project_modules(tenant: string, project_id: integer)`

List modules inside a Studio project.

### `list_services(tenant: string, project_name: string, module_name: string, service_name?: string, start?: integer = 0, limit?: integer = 50)`

List Services declared in a Studio project module.

### `list_studio_projects(tenant: string, start?: integer = 0, limit?: integer = 50)`

List recently-viewed Studio projects with full metadata.

## Offline `.gpk` introspection (no auth)

### `get_app_artifact(name_or_path: string, type: string, name: string, module?: string | null, include_files?: boolean = True)`

Fetch one artifact's parsed JSON + accompanying file list.

### `get_app_package_info(name_or_path: string)`

Return a structured summary of one package: manifest highlights,

### `list_app_artifacts(name_or_path: string, type?: string | null, module?: string | null, name_contains?: string | null, limit?: integer = 200)`

List artifacts inside one app package.

### `list_app_packages()`

List every `.gpk` file discovered under `docs/discovery/*/sample-apps/`.

### `search_app_artifacts(query: string, type?: string | null, limit?: integer = 50)`

Search artifact names across **all** locally available packages.
