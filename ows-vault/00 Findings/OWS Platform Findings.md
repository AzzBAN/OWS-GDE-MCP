---
tags: [platform, findings, ows, adc, auth]
---
# OWS Platform Findings

Production-confirmed gotchas for the OWS Studio / ADC platform (`teleows.com`).
Terse by design — each item is something that cost real debugging time. Add to
it; keep entries short and confirmed.

## Auth: CSRF token only exists in the browser SPA

Non-GET calls to OWS require a CSRF header. The token is **not** returned by any
REST endpoint — the SPA bootstrap JS writes it to
`localStorage.csrfTokens[0].csrfToken`, with the header name in the sibling
`headerKey` (default `x-gde-csrf-token`). To make POST/PUT/DELETE work you must
either capture it from a logged-in browser (`localStorage`) or paste it into
config. A pure-HTTP login does **not** mint it.

## Auth: the CAS login is a Vue SPA with a tenant field + captcha

`/dspcas/login` on `1057-sg[-studio]` renders its form client-side (Element-UI
`el-button`), has a `#tenant` field, and a conditional captcha / SMS gate.
**Pure-HTTP CAS login cannot clear this tenant** — the POST 401s. Use a pasted
session cookie + CSRF, or a headless browser (Playwright) login. The password is
RSA-encrypted client-side via **WebCrypto RSA-OAEP / SHA-256** (not JSEncrypt /
PKCS#1v1.5), confirmed from `webCryptoUtils.min.js` + `cas-login-code2.js`.

## Auth: the scraped RSA public key escapes `/` as `\/`

The login page embeds the RSA public key (`rsaPubBase64Str`) as a JS string with
newlines escaped as `\n` **and** base64 forward-slashes escaped as `\/`. Both
must be unescaped before `load_pem_public_key`, or it fails with
`Unable to load PEM file ... InvalidByte`. (Fixed in `auth_login_http.py`.)

## Services: project-scoped vs legacy invoke paths

- Project-scoped service (direct call): `/adc-service/web/rest/v1/services/<project>/<module>/<service>`
- Legacy / shared service (direct call): `/adc-service/web/rest/v1/legacy/services/<service>` (no project/module) — e.g. `cmdb_site_getList`.
- The prod runtime **app-ops `/service/test` proxy** takes a `request_string` in
  the **no-`web`** form (`/adc-service/rest/v1/services/...` and
  `/adc-service/rest/v1/legacy/services/...`). The two mounts differ — don't mix them.

## TQL: the asset_uri must be quoted

Complete TQL (the `queryByTql` form) needs the model's canonical asset URI,
double-quoted:

```sql
select * from "/<project>/<module>/<model>" as t limit 1
```

Bare names or dotted paths are rejected by the server-side TQL compiler. (For
data-filtering TQL / string params and pagination caps, see the cpq vault's
`TQL Findings`.)
