# Tools — `ows-gde-mcp`

Auto-generated from the FastMCP server. **50 tools total.**

Regenerate with `uv run python scripts/gen_tools_md.py`.

## Diagnostics

### `status()`

Report MCP server status & which (tenant, surface) cells have URLs/secrets configured.

### `whoami(tenant: string)`

Return the logged-in user profile for the given tenant.

## Live OWS (require `OWS_<TENANT>_SESSION_COOKIE`)

### `audit_artifact_usage(tenant: string, project_name: string, module_name: string, artifact_type?: string = 'service', search_project?: string | null, search_module?: string | null, include_runtime?: boolean = True, runtime_tenant?: string | null, runtime_since_ms?: integer | null, runtime_until_ms?: integer | null, include_used?: boolean = False, start?: integer = 0, limit?: integer = 0)`

Audit usage of every artifact of `artifact_type` in (project, module).

### `call_ows_api(tenant: string, method: string, path: string, surface?: string = 'runtime', body?: ?, params?: dict | null, confirm?: boolean = False)`

Generic escape hatch — call any OWS endpoint that we haven't yet

### `count_service_invocations(tenant: string, project_name: string, module_name: string, service_name: string, start_ms?: integer | null, end_ms?: integer | null)`

Quick "is this service used?" answer.

### `diff_service_io(tenant: string, caller_project: string, caller_module: string, caller_service: string, callee_project: string, callee_module: string, callee_service: string)`

Compare a caller's `InvokeService` payload to the callee's input schema.

### `find_artifact_references(tenant: string, target_uri: string, search_project?: string | null, search_module?: string | null, from_package?: string | null, with_excerpts?: boolean = False)`

Find every artifact in scope that references `target_uri`.

### `find_unused_artifacts(tenant: string, project_name: string, module_name: string, artifact_type?: string = 'service', search_project?: string | null, search_module?: string | null, from_package?: string | null)`

List artifacts of `artifact_type` in (project, module) with zero references.

### `get_favorite_menus(tenant: string)`

Return the current user's pinned/favorite menu entries.

### `get_help_topic(topic: integer | string, lang?: string = 'en_US', include_html?: boolean = False)`

Fetch one topic from the local help cache.

### `get_log_trace(tenant: string, trace_id: string, start_ms?: integer | null, end_ms?: integer | null, page_size?: integer = 200, content_preview_chars?: integer = 200)`

Fetch every log entry sharing a `trace_id` — the cross-service trace tree.

### `get_model(tenant: string, model_id: integer, properties_only?: boolean = False)`

Fetch a Data Model's full schema by id (every property + restrictions).

### `get_model_fields(tenant: string, asset_uri: string)`

Return the TQL queryable-field schema for a Model asset.

### `get_page(tenant: string, project_name: string, module_name: string, page_name: string, page_type?: string = 'responsive-web')`

Fetch one Page's metadata row by name.

### `get_page_detail(tenant: string, page_id: string, summary_only?: boolean = False, parsed?: boolean = False)`

Fetch one Page's full definition by id, including the SPL content tree.

### `get_page_scripts(tenant: string, page_id: string, include_content?: boolean = True, include_css?: boolean = True)`

Fetch the JS (and optionally CSS) scripts wired to a page.

### `get_process(tenant: string, project_name: string, module_name: string, process_key: string)`

Get one BPM process definition by (project, module, process_key).

### `get_service(tenant: string, project_name: string, module_name: string, service_name: string, flow_only?: boolean = False)`

Fetch one Service's full definition (including its `flow` steps).

### `get_service_script(tenant: string, project_name: string, module_name: string, script_name: string, script_type?: string)`

Fetch a service script's full JS body and metadata.

### `get_studio_module(tenant: string, module_id: integer)`

Get module detail including which artifact types it supports.

### `get_studio_project(tenant: string, project: string | integer)`

Get one Studio project by id or by name.

### `get_trigger(tenant: string, project_name: string, module_name: string, trigger_name: string)`

Fetch one Trigger by name.

### `invoke_service(tenant: string, project_name: string, module_name: string, service_name: string, payload?: dict | null, confirm?: boolean = False)`

Execute a Service from the Studio service playground with a JSON payload.

### `lint_service_script(tenant: string, project_name: string, module_name: string, script_name: string)`

Static analysis of a RunScript body for known anti-patterns.

### `list_help_topics(query?: string, parent_id?: integer | null, depth_max?: integer | null, lang?: string = 'en_US', limit?: integer = 50)`

List topics from the local OWS help corpus.

### `list_live_apps(tenant: string)`

List unique OWS apps the current user has access to.

### `list_live_menus(tenant: string, flatten?: boolean = False, only_with_url?: boolean = False)`

List the menu tree granted to the current user.

### `list_models(tenant: string, project_name?: string, module_name?: string, model_name?: string, model_type?: string, open_level?: string, start?: integer = 0, limit?: integer = 10, brief_query?: boolean = True)`

List Data Models across one or many projects/modules.

### `list_page_scripts(tenant: string, project_name: string, module_name: string, name?: string, page?: integer = 0, page_size?: integer = 50, sort?: string = 'updateTime', direction?: string = 'DESC', include_body?: boolean = False)`

List the page-namespace scripts (the catalog behind Studio's Page → Script Manage tab).

### `list_pages(tenant: string, project_name: string, module_name: string, name?: string, display_name?: string, tag_id?: string, page_type?: string = 'responsive-web', active?: string = 'true', sort?: string = 'updateTime', direction?: string = 'DESC', page?: integer = 0, page_size?: integer = 50, include_raw?: boolean = False)`

List Pages declared in a Studio project module.

### `list_processes(tenant: string, abbreviation?: string, project_name?: string, module_name?: string, active_only?: boolean = True, refresh?: boolean = False, limit?: integer = 0)`

List BPM processes registered in the tenant.

### `list_project_modules(tenant: string, project_id: integer, verbose?: boolean = False)`

List modules inside a Studio project.

### `list_scripts(tenant: string, project_name?: string, module_name?: string, name?: string, script_type?: string, start?: integer = 0, limit?: integer = 50, include_raw?: boolean = False)`

List MCP Scripts (the `Script` tab under Studio's MCP element group).

### `list_service_scripts(tenant: string, project_name: string, module_name: string, script_type?: string, script_name?: string, start?: integer = 0, limit?: integer = 100)`

List the bundled scripts (RunScript, ScriptLib, Translator, Validator) in a module.

### `list_services(tenant: string, project_name: string, module_name: string, service_name?: string, start?: integer = 0, limit?: integer = 50, include_flow?: boolean = False)`

List Services declared in a Studio project module.

### `list_studio_element_types(tenant: string, display_only?: boolean = True)`

Catalogue every Studio artifact "element type" (~80 types).

### `list_studio_projects(tenant: string, start?: integer = 0, limit?: integer = 50, verbose?: boolean = False)`

List recently-viewed Studio projects with full metadata.

### `list_triggers(tenant: string, project_name: string, module_name: string, trigger_name?: string, active?: boolean | null = True, start?: integer = 0, limit?: integer = 50, verbose?: boolean = False)`

List Triggers declared in a Studio project module.

### `query_model_data(tenant: string, tql: string, need_null_value?: boolean = True, validate?: boolean = True)`

Execute a read-only TQL query against a Model and return matching rows.

### `refresh_process_cache(tenant: string)`

Force a re-fetch of the BPM process catalog and persist to disk.

### `refresh_session(tenant: string)`

Force a CAS re-login for the given tenant. Returns the userId on success.

### `resolve_process_by_prefix(tenant: string, prefix: string, refresh?: boolean = False)`

Map a ticket prefix (INC / BOT / CIT / TTS / ...) to its process.

### `search_help(query: string, lang?: string = 'en_US', limit?: integer = 20, snippet_chars?: integer = 240)`

Full-text search across the local help corpus.

### `search_service_logs(tenant: string, project_name?: string, module_name?: string, service_name?: string, trace_id?: string, log_level?: string, start_ms?: integer | null, end_ms?: integer | null, page?: integer = 1, page_size?: integer = 50, case_sensitive?: boolean = True, content_preview_chars?: integer = 200)`

Search runtime logs for a service or trace.

### `walk_service_chain(tenant: string, project_name: string, module_name: string, service_name: string, max_depth?: integer = 5, include_scripts?: boolean = False)`

Recursively follow `InvokeService` steps and return a call tree.

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
