# Discovery — Testbed walk (Phase 0)

Findings from headed-browser exploration of `https://1057-sg-studio.teleows.com/`
via Playwright MCP. **Authentication scheme is fully reverse-engineered.**

Raw captures live in `docs/discovery/testbed/raw/` (gitignored except sanitized
examples). Sample app exports live in `docs/discovery/testbed/sample-apps/`.

---

## Tenants & hosts

| Tenant   | Studio (design state)               | Runtime                       |
|----------|-------------------------------------|-------------------------------|
| Testbed  | `https://1057-sg-studio.teleows.com`| _unknown — testbed appears to be studio-only_ |
| Prod     | _unknown_                           | `https://1057-sg.teleows.com` |

The testbed Studio host hosts **both** the design portal (`?isStudio=true`) and
the runtime mission console.

---

## Authentication

OWS uses a layered scheme:

1. **CAS-based SSO.** Hitting any portal URL when unauthenticated redirects to
   `/dspcas/login?service=<encoded portal URL>`. After login CAS redirects back
   with `?ticket=ST-...-cas` which the portal exchanges for a session.
2. **Session cookies (HttpOnly).** After login the browser holds session
   cookies — these are HttpOnly and *not* visible from JS. Visible
   non-HttpOnly cookies seen so far:
   - `tenant_id`, `x-gde-tenant-id` = `1057`
   - `username` = `awx1320635`
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

All same-origin under `https://1057-sg-studio.teleows.com`:

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
| Op | Method | Path |
|---|---|---|
| Online help index | GET | `/adc-studio-project-mgt/web/rest/help/doc/en_US/index.html` |
| Online help nav tree | GET | `/adc-studio-project-mgt/web/rest/help/doc/en_US/data/nav_json.js` |
| _More TBD when studio walk + sample app export are processed_ | | |

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
  `/adc-static/static/jslibComp/1057/WFMBase/mission_control_service/...`.
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
- [ ] Confirm whether Production has a separate `*-studio` subdomain or runs
      Studio at the same host.
- [ ] Determine CAS login flow if we want headless (programmatic) login —
      otherwise rely on cookie paste or interactive Playwright login.
