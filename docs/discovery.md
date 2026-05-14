# Discovery

Captured shape of the OWS / GDE API surface, derived from headed-browser
walks via Playwright MCP. Filled in incrementally during Phase 0.

> All sample payloads here must be **sanitized** (no real tokens, customer
> data, IPs, employee IDs). Raw dumps live in `docs/discovery/<tenant>/` and
> are gitignored.

## Tenants & hosts

| Tenant   | Studio (design state)               | Runtime                       | Notes |
|----------|-------------------------------------|-------------------------------|-------|
| Testbed  | `https://1057-sg-studio.teleows.com`| _TBD_                         |       |
| Prod     | _TBD_                               | `https://1057-sg.teleows.com` |       |

## Authentication

_Filled during walk._

- Login URL:
- Method:
- Request payload shape:
- Token / session location (cookie / header / both):
- CSRF / anti-forgery header:
- Token lifetime / refresh mechanism:
- Logout URL:

## API base paths

_Filled during walk._

| Module | Host | Base path |
|---|---|---|
| Process orchestration | studio | |
| UI / Form | studio | |
| Data orchestration | studio | |
| Service orchestration / API Fabric | studio | |
| Asset Store / GDE Store | studio | |
| Data models | studio | |
| Work orders | runtime | |
| Alarms | runtime | |
| SLA/OLA | runtime | |

## Per-module endpoint inventory

### Process orchestration

| Operation | Method | Path | Notes |
|---|---|---|---|
| List definitions | | | |
| Get definition | | | |
| Start instance | | | |
| List instances | | | |
| Get instance | | | |
| List my tasks | | | |
| Complete task | | | |

### Asset Store / GDE Store
_TBD_

### Data orchestration
_TBD_

### Data models
_TBD_

### UI / Forms
_TBD_

### Service orchestration / API Fabric
_TBD_

### Work orders (Runtime)
_TBD_

### Alarms (Runtime)
_TBD_

### SLA/OLA (Runtime)
_TBD_

## Quirks / gotchas

_Things to remember while writing tools._
