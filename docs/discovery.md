# Discovery — Testbed walk (Phase 0)

Findings from headed-browser exploration of `https://<your-tenant>-studio.example.com/`
via Playwright MCP. **Authentication scheme is fully reverse-engineered.**

Raw captures live in `docs/discovery/testbed/raw/` (gitignored except sanitized
examples). Sample app exports live in `docs/discovery/testbed/sample-apps/`.

---

## Tenants & surfaces

OWS has two independent axes:

- **Tenant** — `prod` or `testbed`. Separate environments with their own
  accounts and CAS servers.
- **Surface** — `studio` (design-time authoring; APIs under `/adc-studio-*/`)
  or `runtime` (deployed apps; portal + `/adc-model/` + `/adc-service/`).

A tenant can have either, both, or neither surface available to a given user.
Typical workflow: author in testbed studio → preview on testbed runtime →
deploy to prod runtime. Production studio is normally unavailable to
developers.

| Tenant   | Studio (design-time)                  | Runtime (deployed apps)              |
|----------|---------------------------------------|--------------------------------------|
| Testbed  | `https://<tenant>-studio.example.com` | `https://<tenant>-studio.example.com` (same host on this testbed) |
| Prod     | _typically unavailable to developers_ | `https://<tenant>.example.com`        |

On the testbed Studio host the same origin serves both surfaces (design
portal exposed via `?isStudio=true`, runtime mission console via the default
homepage). Auth is shared across surfaces of the same tenant — one CAS
session covers both.

---

## Authentication

OWS uses a layered scheme:

1. **CAS-based SSO.** Hitting any portal URL when unauthenticated redirects to
   `/dspcas/login?service=<encoded portal URL>`. After login CAS redirects back
   with `?ticket=ST-...-cas` which the portal exchanges for a session.
2. **Session cookies (HttpOnly).** After login the browser holds session
   cookies — these are HttpOnly and *not* visible from JS. Visible
   non-HttpOnly cookies seen so far:
   - `tenant_id`, `x-gde-tenant-id` = `<tenantId>`
   - `username` = `<your-account>`
   - `x-gde-locale`, `_LOCALE_`, `locale`
   - `x-gde-timezone` (JSON)
   - `lastestOperationTime` (epoch ms)
3. **Per-request anti-tamper headers** (gate every authenticated API call):
   - `x-adc-page-timestamp: <epoch ms>` — `Date.now()`
   - `x-adc-page-token: <signed 32-bit int>` — `javaStringHashCode(path + str(ts))`
     where **path is the request URL stripped of query string**
   - `x-gde-src-page: /portal-web/portal/homepage.html` — the page making the call
   - `x-gde-target-app: <appName>` — empty when calling from same app
   - `X-Requested-With: XMLHttpRequest`
4. **CSRF on non-GET requests:**
   - Header name: `x-gde-csrf-token`
   - Header value: 48-digit numeric string, returned at login and stored in
     `localStorage.csrfTokens` (also exposed as `window.csrfToken`)
   - Form field alternative: `_csrf` (multipart/form posts)
   - CAS keepalive endpoint: `GET /dspcas/service/checkAlive?request-source=portalWeb&updateTGT=`

Without (1) or (3) the controller responds:

```json
{"context":null,"error":{"source":"ADC.COMM.SDK","code":"03240001",
 "args":["<path>"], "message":"Failed to verify the open level of the controller interface:<path>.",
 "solution":"Please check the access URL.","caused_by":null}}
```

### Algorithm — Page token

Verified against two live samples:

| URL                                                              | TS            | Expected     | jhash(path+ts) | Match |
|------------------------------------------------------------------|---------------|--------------|----------------|-------|
| `/portal/web/rest/v1/user/my-info`                               | 1778751584033 | -1955536328  | -1955536328    | ✅    |
| `/portal/web/rest/v1/menu/manage/app/getGranted?granted=true`    | 1778751584193 | 440037745    | 440037745      | ✅    |

`jhash` = standard Java `String.hashCode()`:

```python
def java_hashcode(s: str) -> int:
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    if h >= 0x80000000:
        h -= 0x100000000
    return h

def page_token(url_or_path: str, ts_ms: int) -> int:
    path = url_or_path.split("?", 1)[0]  # strip query
    return java_hashcode(path + str(ts_ms))
```

JavaScript reference (from `chunk-vigour.294ef8b0.js`):

```js
// constants
x = "x-gde-src-page"
T = "x-adc-page-token"
O = "x-gde-target-app"
S = "x-adc-page-timestamp"

// jQuery ajaxSetup beforeSend (paraphrased)
$.ajaxSetup({beforeSend: function (xhr, n) {
  const r = E.getTimeStampValue();        // Date.now()
  const i = E.getPageTokenValue(n, r);    // javaHashCode(path + ts)
  xhr.setRequestHeader(E.getCurrentTimestamp(), r);
  xhr.setRequestHeader(E.getTokenKey(), i);
  if (n.type.toUpperCase() !== "GET") {
    xhr.setRequestHeader(T.getCsrfHeaderKey(), T.getCsrfToken());
  }
}})
```

---

## API host map (backend services discovered)

All same-origin under `https://<tenant>-studio.example.com`:

| Mount                                | Purpose |
|--------------------------------------|---------|
| `/dspcas/...`                        | CAS authentication server |
| `/portal/web/rest/v1/...`            | Portal — user, menu, theme, i18n, notifications, banners |
| `/portal/web/rest/sso/check`         | SSO session-alive check (returns `true`/`false`) |
| `/portal-web/portal/...`             | Portal SPA static + entry |
| `/portal-web/static/js/chunk-*.js`   | Bundled JS chunks |
| `/adc-ui/web/rest/v1/...`            | ADC UI — panels, pages, themes, user-data |
| `/adc-agent/web/rest/v1/...`         | ADC Agent — async tasks |
| `/adc-service/web/rest/v1/services/...`        | **Typed service invocation** — `<App>/<module>/<serviceName>` |
| `/adc-service/web/rest/v1/legacy/services/...` | **Legacy service invocation** — `<serviceName>` directly |
| `/adc-model/web/rest/v1/...`         | ADC Model — TQL queries, model property lists, data-exist checks |
| `/adc-studio-project-mgt/web/rest/...` | Project management & online help docs |
| `/adc-static/...`                    | Static assets per tenant/project/module |
| `/adc-copilot/...`                   | AI copilot |

---

## Key endpoints captured

### Identity & session
| Op | Method | Path |
|---|---|---|
| Current user info | GET | `/portal/web/rest/v1/user/my-info` |
| Session alive | GET | `/portal/web/rest/sso/check` |
| CAS keepalive | GET | `/dspcas/service/checkAlive?request-source=portalWeb&updateTGT=` |
| Available tenants | GET | `/portal/web/rest/v1/user/switch-tenant/support-list` |
| User config | GET | `/portal/web/rest/v1/user-config` |

### Apps, menus, permissions
| Op | Method | Path |
|---|---|---|
| Granted apps | GET | `/portal/web/rest/v1/menu/manage/app/getGranted?granted=true` |
| Granted toolbar | GET | `/portal/web/rest/v1/banner/getGrantedToolbar` |
| Favorites | GET | `/portal/web/rest/v1/menu/favorites` |
| RBAC menu tabs | GET | `/portal/web/rest/v1/rbacMenu/menuTabsConfig/findAll` |
| Page-level access | POST | `/adc-ui/web/rest/v1/page-core/page/check-accesss-control` |

### Pages & themes
| Op | Method | Path |
|---|---|---|
| Get page config | GET | `/adc-ui/web/rest/v1/page-core/page/<App>/<module>/<pageName>?isSearchCustomPage=true&locale=en_US` |
| Page-core config | GET | `/adc-ui/web/rest/v1/page-core/page/get-config` |
| Theme detail | GET | `/portal/web/rest/v1/theme/default/detail` |
| ADC theme | GET | `/adc-ui/web/rest/v1/theme?name=light&loadExtend=true` |
| TQL → JS | POST | `/adc-ui/web/rest/v1/page-core/page/tql2js` |

### Models (data layer)
| Op | Method | Path |
|---|---|---|
| Init TQL on asset | POST | `/adc-model/web/rest/v1/app/tql/init?asset_uri=<uri>` |
| Query model properties (filtered) | POST | `/adc-model/web/rest/v1/models/query-model-property-list-with-filter` |
| Query model properties (simple) | POST | `/adc-model/web/rest/v1/models/simple/query-model-property-list` |
| Model data-exist check | POST | `/adc-model/web/rest/v1/model-instances/<projectName>/<moduleName>/<modelName>/data-exist-check` |

### Service invocation (the big one)
| Op | Method | Path |
|---|---|---|
| Typed service | POST | `/adc-service/web/rest/v1/services/<App>/<module>/<serviceName>` |
| Typed service (extra slashes) | POST | `/adc-service/web/rest/v1/services///<App>/<module>/<serviceName>` |
| Legacy service | POST | `/adc-service/web/rest/v1/legacy/services/<serviceName>` |

### Studio (design-state) — surfaced when `?isStudio=true`

The studio surface lives under `/adc-studio-project-mgt/web/rest/v1/` for
project/module management and `/adc-studio-<TYPE>/web/rest/v1/` for each
artifact type's editor service.

#### Project / module management (`/adc-studio-project-mgt/web/rest/v1/`)
| Op | Method | Path |
|---|---|---|
| Recent projects | GET | `/recent-projects?start=&limit=` |
| Shared projects | POST | `/shared-projects` body `{start,limit}` |
| Favorite project templates | GET | `/favorite-project-template?start=&limit=` |
| Studio menus list | GET | `/common/studio-menus-list` |
| Project by id | GET | `/projects/{project_id}` |
| Project by name | GET | `/projects/name/{name}` |
| Modules in project | GET | `/project/{project_id}/modules` |
| Module detail | GET | `/modules/{module_id}` (contains `items[]` = supported artifact types) |
| Element-type catalog | GET | `/modules/element-type` |
| Recent elements | GET | `/project/element/recent/{project_name}` |
| Last visited module | GET | `/modules/last-visit/{project_id}/` |
| Problem scan | POST | `/problem_scan/get/{project_id}` |
| Online help index | GET | `/help/doc/en_US/index.html` |
| Online help nav tree | GET | `/help/doc/en_US/data/nav_json.js` |
| AQM task | POST | `/aqm/task/execute` |
| Disabled studio editor menus | GET | `/projects/studio-editor-menus/disabled/{project_id}` |

Studio menus endpoint (different from runtime menus):
`GET /portal/web/rest/v1/menu/manage/app/getGranted/studio?granted=true`

#### Model layer (`/adc-studio-model/web/rest/v1/`)
| Op | Method | Path |
|---|---|---|
| List models in a module (no props) | POST | `/models/query-model-no-prop` body `{project_name, module_name, model_name?, model_type?, active?, start, limit}` |
| Get model with props by id | POST | `/models/query-by-id?model_id={id}` |
| Asset-dependency check | GET | `/meta-reference/asset-dependency/exist` |

Model property shape (verified on `tts_data` proxymodel — 92 properties):

```json
{
  "property_id": 355217, "property_name": "order_id",
  "display_name": "Order ID", "property_type": "text",
  "primary_key": true, "required": true, "description": "Order ID",
  "model_id": 15900,
  "restrictions": [{"item": "Max Length", "value": "100"}],
  "customized": false, "self_customized": false, "sort": 0
}
```

Model types seen: `datamodel`, `proxymodel`, `elasticmodel`. `proxymodel`
includes `ext_properties.proxy_type_name` (e.g. `"BPM"`).

#### Mobile / other artifact-type editors (TBD)
- `/adc-studio-mobile/web/rest/v1/page-core/page/...`
- `/adc-studio-service/...`, `/adc-studio-page/...`, `/adc-studio-workflow/...`,
  `/adc-studio-trigger/...`, etc — endpoint shapes not yet captured (each
  artifact type has a distinct backend service; will be discovered by clicking
  each tab in the Resource Designer and capturing network calls).

### Async / agent
| Op | Method | Path |
|---|---|---|
| Async task count | GET | `/adc-agent/web/rest/v1/agent/async-task/count-all` |

### Sample legacy services seen (Mission Console homepage)
- `pd_process_definition_getList` — Process orchestration definitions
- `mtask_monitor_tab_all_tasks_for_page` — Work-order/task list
- `mtask_monitor_tab_exceptional_tasks_for_page`
- `dis_dispatcher_config_current_user`, `dis_timing_auto_sch_properties_switch_getList`, `dis_schedule_dispatcher_getList` — Dispatching
- `mission_lock_status_switch_get`, `mission_new_console_query_getList_filter_creator_share`, `mission_app_exist`
- `slm_sla_remind_config_data_getList` — SLA reminders
- `phase_level_config_get_list`, `cp_check_operator_permissions` — Checklist approvals
- `Local2UTC4Page` — utility

---

## Studio artifact taxonomy (target for the MCP)

From the Studio menu picker (Development State Studio → element keyword chooser),
**~50+ artifact types**, grouped:

- **Common** — Model, Service, Event, Event Listener, Data Export, Data Import,
  Page, I18n, Job, Data Visualization, Document, Menu, Permission, Error Code,
  Business Process, Card, Trigger, Mobile Page, Model Dump, Model Load,
  Function Service, Model Archiving, Model Data Access, Model Flow
- **Data Factory** — Data Model, Data Process, Data Source, Data Integration,
  Debugging Management, Extended Functions
- **AI Studio** — Navigational Modeling, AI Dataset, AI Model, AI Service,
  Model Foundry
- **Agent** — Agent, Flow, Prompt, Tool, LUI Card, Skill, SCOT, Agent Group,
  Intent Management Configuration, Rule-of-graph, Knowledge Management
- **Openness Integration** — Tool design, Inbound API, Outbound API, Connector
- **Interface Package** — Inbound REST, Outbound REST, Inbound SOAP, Outbound SOAP
- **RPA** — RPA Script, RPA Plugin
- **OM Events** — Common Event Configuration, Event Identification Rule
- **MCP** — Command, Script
- **Data Package** — Customized Asset
- **Automatic Diagnosis and Recovery** — Automatic Process Orchestration,
  Automation Configuration

The MCP's job is to make every one of these queryable.

---

## Quirks / gotchas

- **POST `/adc-service/.../legacy/services/*` is the dominant call pattern.**
  Service names are global; many encode "<app>_<module>_<entity>_<verb>" e.g.
  `pd_process_definition_getList`, `mtask_monitor_tab_all_tasks_for_page`.
- **`asset_uri=<uri>`** is the canonical ID for a data-model asset (e.g.
  `asset_uri=mtask_work`). Likely the URI also appears in other artifact types.
- **`x-gde-src-page` matters** — controllers check the calling page is allowed.
  Use the deepest page URL the SPA happened to be on, not the API path.
- The portal SPA uses both `fetch` and jQuery `$.ajax`. The anti-tamper headers
  are attached via `$.ajaxSetup({beforeSend})` for jQuery and an equivalent
  interceptor for fetch.
- One asset name observed: `mtask_work` (used 8× in TQL init on homepage).
- Static-asset CDN paths embed `tenantId/Project/Module`, e.g.
  `/adc-static/static/jslibComp/<tenantId>/WFMBase/mission_control_service/...`.
- Console errors on first load include a `502 Bad Gateway` for
  `/adc-copilot/static/experiences.js` — the AI copilot is not provisioned on
  this tenant; safe to ignore.

---

## App package (`.gpk`) format — canonical layout

`.gpk` files are **plain zip archives** of an OWS app's Design State assets.
Verified against 7 real exports (see `docs/discovery/testbed/sample-apps/`,
gitignored).

```
manifest.json                 # app-level metadata (name, version, scene, …)
category.json                 # business categorisation
patch.json                    # { source_version, target_version }
resources/
    birth_permit.json         # issuing tenant + dev environment + creator
    logo.svg
modules/
    <project>/                # e.g. "TTS", "c_TroubleTicket"
        module.json           # project-level: name, prefix, supported_item_types[]
        studio.json           # project-level: Studio menu items (artifact types in nav)
        <module>/             # e.g. "general_work"
            brief.json
            package.json
            <TYPE>/           # one dir per artifact type (uppercase)
                <name>.json   # canonical artifact (file-based types)
                ...
```

### Per-type storage convention
| Type group              | Storage shape inside `<TYPE>/`                                                                 |
|-------------------------|------------------------------------------------------------------------------------------------|
| File-based (most types) | one `<name>.json` per artifact (MODEL, PAGE, SERVICE, TRIGGER, MENU, JOB, EVENT, …)            |
| Service / Page extras   | sibling subdirs `RunScript/`, `ScriptLib/`, `Translator/`, `Validator/`, `script/`, `config/`  |
| Directory-based         | `WORKFLOW/<name>/` containing `_bpmn.json`, `_process_definition.json`, `_process_forms.json`, `_process_flow_condition.json`, `_process_assignees.json` |
| Bundle types            | `PERMISSION/{permissions,roles,role_permission_assignments}.json`; `I18N/bundle.json` + per-locale subdirs |
| Housekeeping (skip)     | `*/patch.diff.brief.json`, `<module>/brief.json`, `<module>/package.json`                      |

### Artifact JSON schemas (key fields seen in samples)

- **MODEL** → `model_name, model_type, display_name, active, properties[]`
  with each property `{property_name, display_name, property_type,
  default_value, primary_key, required, restrictions, sort}`.
- **SERVICE** → `service_name, ui_api, open_level, async, legacy, permission,
  flow{start_at, steps{...}}` — flow steps are `input|invoke|transform|...`
  blocks linked by `next`.
- **PAGE** → `name, content{id, name, children[]}` — recursive UI tree of
  components (`name`, `props`, `events`, `children`, `propsBind`).
- **TRIGGER** → `trigger_name, model_uri, event_type, before_or_after,
  condition, source, trigger_activities[]` — activities reference services
  via `service_rest_uri: /adc-service/rest/v1/services/<App>/<module>/<svc>`.
- **MENU** → `name, parent, menuType, url, text, module, openLevel`.
- **PERMISSION** → top-level `permissions[]`, plus separate `roles.json` and
  `role_permission_assignments.json` files.
- **WORKFLOW** → BPMN-style XML embedded in `*_bpmn.json`; activities, forms,
  assignees in sibling files.

### Asset URI convention
The canonical OWS asset URI used in cross-references is:

    /<project>/<module>/<artifact_name>

e.g. `/TTS/general_work/tts_data` (a Model), or
`/SDMToThirdPartySystem/SDMToThirdPartySystem/thirdps_integration_tickets`
(a Model referenced from another app's service flow input).

This URI also appears as `asset_uri=` on the live API
(`POST /adc-model/web/rest/v1/app/tql/init?asset_uri=...`).

---

## Open items for next sub-phases

- [ ] Get a session cookie into `.env` (user-side step, see README/Setup).
- [ ] Walk every Studio module ("Display by Group" picker) and dump network
      requests per artifact type to `docs/discovery/testbed/<module>.json`.
      Especially: AI Studio / Agent / MCP / RPA (not represented in samples).
- [ ] Wrap the online help (`/adc-studio-project-mgt/web/rest/help/doc/...`)
      so the MCP can answer "what is this artifact?" with citations.
- [ ] Determine CAS login flow if we want headless (programmatic) login —
      otherwise rely on cookie paste or interactive Playwright login.

## Endpoints needing live verification

_(none open — list_pages and list_scripts were verified on 2026-05-15 by
walking the page-list and script-management UIs in a logged-in browser
and capturing the network calls. See live-verified entries below.
PR3 added live-verified endpoints for triggers, page-detail, log-search,
and the studio element-type catalogue — all documented below.)_

#### Triggers (`/adc-studio-model/web/rest/v1/triggers/`)
| Op | Method | Path |
|---|---|---|
| List/page-query triggers in module | POST | `/adc-studio-model/web/rest/v1/triggers/page-query-all` body `{project_name, module_name, trigger_name?, active?, start, limit}` |

Response shape (verified):
```json
{
  "content": [{"trigger_id", "trigger_name", "model_uri", "event_type",
                "before_or_after", "active", "condition", "source",
                "trigger_activities": [{"activity_type": "Invoke Service",
                  "service_rest_uri": "/adc-service/rest/v1/services/<p>/<m>/<svc>",
                  "priority", "sync", "write_back", ...}]}],
  "totalElements": int, "totalPages": int, "size": int, "number": int
}
```

`trigger_activities[].service_rest_uri` is the field PR3b's reference
scanner walks to count "service fired by trigger" as a strong static
ref. `model_uri` is the model whose create/update/delete event fires
the trigger.

#### Page detail with content tree (`/adc-studio-ui/web/rest/v1/page-core/page/{id}`)
| Op | Method | Path |
|---|---|---|
| Page detail (full content) | GET | `/adc-studio-ui/web/rest/v1/page-core/page/{page_id}` |

The list endpoint returns metadata only (`content` is null). This
detail endpoint returns the same row plus a `content` field holding the
recursive UI tree as a JSON-encoded string. Scan for service refs in:
- component props (`serviceName`, `serviceId`, `location`)
- `js_content` blocks (the page's Script tab — embedded JS calls
  `MessageProcessor.process({serviceId: "..."})`)
- `propsBind` and event handlers

#### Log Analysis search (`/loganalysis/service/`)

Different auth scheme — see `src/ows_gde_mcp/tools/log_analysis.py`. CSRF
header is `X-CSRF-TOKEN` (not `x-gde-csrf-token`), token is embedded as
inline JS in `/loganalysis/service/index.html`:
```html
<script>(function() {
    var csrftoken = {header:"X-CSRF-TOKEN", param:"_csrf", token:"<HEX>"};
    ...
})()</script>
```
The standard GDE anti-tamper headers (`x-adc-page-token`, etc) are
*rejected* by this service — must be omitted. `referer` must be
`/loganalysis/service/index.html`.

| Op | Method | Path |
|---|---|---|
| Log search | POST | `/loganalysis/service/logsearch/v3/logs/search` body `{tableType: 2, pageIndex, pageSize, startTime, endTime, isCaseSensitive, filters?: [{field, value}]}` |
| Filter conditions | GET | `/loganalysis/service/getFilterCondition?tableType=2` |
| Column fields | GET | `/loganalysis/service/queryColumnField?tableType=2` |

Response shape (verified):
```json
{
  "status": "OK",
  "result": {
    "pageIndex": 1, "pageSize": 20, "recordCount": 280491,
    "result": [{
      "id": "<uuid>", "log_time_millis": ..., "trace_id": "<hex>",
      "operator": "...", "app_name": "...", "module_name": "...",
      "element_type": "JavaScript", "element_name": "<service-or-script>",
      "operation_type": "Log", "log_level": "WARN|ERROR|INFO|DEBUG",
      "cost_time": int, "log_content": "...", "location_info": "service=...| step=...",
      ...
    }, ...]
  }
}
```

Useful filter fields: `app_name`, `module_name`, `element_name`
(service name), `trace_id`, `log_level`. Trace ids correlate
cross-service calls — `get_log_trace(trace_id)` returns every log entry
sharing the trace id, sorted chronologically.

**Retention**: ~3 days on this tenant. Wider windows are silently
rejected — `search_service_logs` clamps and warns.

#### Studio element-type catalogue (`/adc-studio-project-mgt/web/rest/v1/modules/element-type`)
| Op | Method | Path |
|---|---|---|
| All element types | GET | `/adc-studio-project-mgt/web/rest/v1/modules/element-type` |

Returns the master list behind the Studio resource picker — ~80 types
across Common, Data Factory, AI Studio, Agent, Openness Integration,
Interface Package, RPA, OM Events, MCP, Data Package, Automatic
Diagnosis and Recovery. Each row carries `id`, `item_type`, `label`,
`navigate_uri` (double-encoded JSON string with the Studio UI URLs for
this type), `engine_id`, `display`. The wrapper in
`tools/live.py:list_studio_element_types` parses `navigate_uri` and
filters to `display=true` by default.

#### Pages (`/adc-studio-ui/web/rest/v1/page-core/page/`)
| Op | Method | Path |
|---|---|---|
| List pages in a module | GET | `/adc-studio-ui/web/rest/v1/page-core/page/{projectName}/{moduleName}?active=true&sort=updateTime&dir=DESC&page=0&pageSize=10&type=responsive-web&name=&tagId=&displayName=&moduleName=...&projectName=...` |
| List customizable pages | GET | `/adc-studio-ui/web/rest/v1/page-core/page/customizable-page-list?projectName=...&moduleName=...&name=` |
| Page-core page detail (TBD: not yet wrapped) | GET | `/adc-studio-ui/web/rest/v1/page-core/page/...` |

Page list response shape (verified):
```json
{
  "data": [{"id", "name", "display_name", "type", "module_name", "project_name",
            "model_name", "active", "open_level", "manifest_version", "creator",
            "updater", "create_time", "update_time", "tag_id", "customizable",
            "content": null, ...}],
  "total": 35, "totalPage": 7, "page": 0, "pageSize": 5
}
```
The list endpoint never ships the `content` (recursive UI tree) — that needs
a separate detail call.

#### MCP Scripts (`/adc-studio-mcp/web/rest/v1/`)
| Op | Method | Path |
|---|---|---|
| List MCP scripts | GET | `/adc-studio-mcp/web/rest/v1/scriptmgt/scripts?limit=&start=&name=&script_type=&project_name=&module_name=` |
| Script types | GET | `/adc-studio-mcp/web/rest/v1/scriptmgt/scripts/template?...` |
| Script templates | GET | `/adc-studio-mcp/web/rest/v1/scriptmgt/script/templates?limit=100` |
| Name-exists check | GET | `/adc-studio-mcp/web/rest/v1/scriptmgt/scripts/exist/?name=` |

MCP script list response shape (verified):
```json
{
  "resultCode": "0",
  "resultMessage": "Success",
  "result": {
    "results": [{"id", "name", "script_type": "python", "type": "diagnose",
                  "file": "x.py", "project_name", "module_name",
                  "manifest_version", "risk_level": "Low|Medium|High"}],
    "start": 0, "total": 642
  }
}
```

The MCP-Script category is the `Script` element-type id 35 (`SCRIPT_MANAGEMENT`)
and is a *separate* artifact category from RPA Script (id 29), Page Script
(id 45), Mobile Page Script (id 64), Mateline Script (id 56), and the three
CEAE script variants (52/53/55). RPA scripts ship under
`/adc-studio-web/rpa/...` (different backend, not yet wrapped). The inline
`RunScript/`/`ScriptLib/` files that appear in `.gpk` exports under SERVICE/
live *under* a service flow — not as top-level Script artifacts — and are
fetched via the SERVICE endpoint, not list_scripts.
