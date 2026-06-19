---
name: ows-new-page
description: Checklist and patterns for building a new OWS page element. Use when asked to create or design a page.
---

# OWS New Page Skill

## Before You Start

1. **Check existing pages** — use `list_pages(tenant, project, module)` to find similar pages
2. **Analyze a reference page** — use `get_page_detail(tenant, page_id, parsed=True)` to understand component patterns
3. **Identify services needed** — what data does the page display? What actions does it trigger?

## Common Page Layouts

### Query / List page
```
toolbar (search inputs + filters + buttons)
  └── textInput, dropdownOptionGroup, dateInput, advancedSearch
datagrid (results table)
  └── column, linkColumn, personColumn
```
- Toolbar filters feed into a list service call
- Datagrid `id` is referenced in page scripts to load/refresh data

### Detail / Form page
```
formPanel (field inputs)
  └── textInput, select, dateInput, personSelect, switchButton
toolbar (action buttons)
  └── button, serviceButton
```
- `serviceButton` directly invokes a service on click
- `button` triggers a JS handler in page scripts

## Page Script Structure

| Script | Purpose |
|--------|---------|
| `init` | Runs on load — call services, set defaults, hide/show sections |
| `utils` | Shared helpers — formatters, validators, common service callers |
| `events` | User interaction handlers — search, reset, row click |

### init pattern
```javascript
// Load dropdown options
var categoryRes = $service.invoke("centralize_order_category_get_list", {});
$component.get("order_category").setOptions(categoryRes.data);

// Load initial grid data
utils.loadGrid({});
```

### utils pattern
```javascript
// Reusable grid loader
function loadGrid(params) {
    var res = $service.invoke("ticket_get_list_datagrid", params);
    $component.get("cit_listGrid").setData(res.data, res.total);
}
```

## Checklist

- [ ] Page name follows convention: `<module>_<purpose>` (e.g. `cit_query`, `cm_detail`)
- [ ] `open_level` set correctly
- [ ] init script loads all required dropdown/select options
- [ ] Datagrid wired to a list service with pagination
- [ ] Reset button clears all filter inputs
- [ ] Error handling in service calls (check response before using data)

## Notes

- Component `id` in props is the JS handle — keep them meaningful: `order_id`, `cit_listGrid`
- Behavior goes in page scripts, not SPL props — SPL is declarative structure only
- Use `propsBind` sparingly — most dynamic behavior is easier to manage in scripts
