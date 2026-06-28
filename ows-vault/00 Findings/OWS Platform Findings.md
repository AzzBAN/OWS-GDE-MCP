---
tags: [platform, findings, ows, adc, auth]
---
# OWS Platform Findings

Production-confirmed gotchas for the OWS Studio / ADC platform (`teleows.com`).
Terse by design — each item is something that cost real debugging time. Add to
it; keep entries short and confirmed.

## Auth: CSRF token — REST endpoint exists (uiconfig/info)

Non-GET calls to OWS require a CSRF header (`x-gde-csrf-token`). The token **IS**
available from a REST endpoint — contrary to an earlier note:

    GET /portal/web/rest/v1/uiconfig/info

returns JSON `{"csrf_token": "<48-digit>", "user_id": ..., "tenant_id": ...}`.
Verified on both testbed (1057-sg-studio) and prod (1057-sg). The SPA's
`getADCCsrfUrl()` (in `chunk-vigour.*.js`) builds this URL from the constant
`aP="/web/rest/v1/uiconfig/info"` + portal prefix `/portal`; it also caches the
token in `localStorage.csrfTokens[0].csrfToken` with sibling `headerKey`
(default `x-gde-csrf-token`).

So a pure-HTTP login mints its own CSRF (`_fetch_csrf` in `auth_login_http.py`) —
no browser/Playwright needed for the token itself. The header name is fixed
`x-gde-csrf-token`; the response has no `headerKey` field. The env override
`OWS_<TENANT>_CSRF_TOKEN` remains the no-network path; Playwright remains the
fallback only when HTTP login can't clear the CAS tenant/captcha gate.

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
