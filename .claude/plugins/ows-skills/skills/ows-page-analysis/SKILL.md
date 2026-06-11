---
name: ows-page-analysis
description: Analyze an OWS Studio page — understand its components, service wiring, and JS behavior. Use when asked to explain, audit, or modify a page element.
---

# OWS Page Analysis Skill

## Delegate to a subagent when possible

If the `Agent` tool is available, dispatch the page reads to a subagent (general-purpose). The subagent absorbs the big SPL + scripts payload and returns just the structured answer; your main context stays small.

Brief it like: "Run `get_page_detail(parsed=True)` on page X, then `get_page_scripts`, then return: (1) component count, (2) service refs, (3) what `init` does, (4) anything unusual. Don't return raw payloads."

If `Agent` is unavailable (you are already a subagent), continue with the steps below using only the lean variants.

## Steps

1. **Find the page** — if you only have a name, use `list_pages(tenant, project_name, module_name, name=<name>)` to get the `id`.

2. **Get parsed structure** — use `get_page_detail(tenant, page_id, parsed=True)`.
   - Returns `parsed_spl.components[]` — flat list of all UI elements with type, id, path
   - Returns `parsed_spl.service_refs[]` — all service URIs wired to the page
   - Returns `parsed_spl.event_handlers[]` — component-level event bindings
   - Returns `parsed_spl.prop_bindings[]` — dynamic prop bindings
   - Much smaller than raw SPL (~13x), use this first

3. **Get page scripts** — use `get_page_scripts(tenant, page_id)` to read the JS layer.
   - `init` — runs on page load, typically calls services and sets initial state
   - `utils` — shared helper functions
   - `events` — user interaction handlers
   - This is where most behavior lives — SPL components are mostly declarative

4. **Trace service calls** — for each service ref found, use `get_service(tenant, project, module, service_name)` to understand what it does.

5. **Cross-reference** — use `find_artifact_references(tenant, target_uri)` to find what else calls the same services.

## Reading the parsed_spl

- `components[].path` shows the nesting: `/page/toolbar/datagrid/column`
- `components[].type` is the element type: `datagrid`, `textInput`, `button`, `select`, etc.
- `components[].id` is the JS-accessible component ID used in page scripts
- Empty `event_handlers` and `prop_bindings` means behavior is entirely in page scripts (common pattern)

## Notes

- Never fetch raw `content` (no flags) unless you specifically need to walk the full tree — it's 50KB+
- Use `summary_only=True` for a quick component count + service ref list
- Use `parsed=True` for understanding structure and wiring
- Use raw only when you need to inspect a specific deeply-nested node
