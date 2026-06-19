---
name: ows-capture-finding
description: Capture a reusable OWS/ADC platform finding into the knowledge vault. Use when you confirm a non-obvious, reusable fact about the OWS platform (an API path, a TQL quirk, an auth detail, a service contract) that future sessions should know — so it's recorded once and read first via get_help_home / search_help instead of re-derived.
---

# Capture an OWS Finding

When you (or the user) confirm a **reusable, non-obvious** fact about the
OWS/ADC platform, record it as a finding so it's read first next time instead of
re-derived from the 3.6k-page reference corpus.

## When to capture
- A confirmed API path / endpoint shape, or a request/response contract.
- A TQL quirk, a model/field gotcha, an auth/CSRF/login detail.
- A platform constraint discovered by debugging (it cost real time → save it).

Do **not** capture: project-specific trivia, secrets/credentials, one-off
values, or anything an existing finding already covers.

## Flow
1. **Check first.** Call `search_help("<key terms>")` and `get_help_home` to see
   if a finding already covers this. If so, update that finding rather than
   creating a near-duplicate (re-issue `add_help_finding` with `overwrite=True`).
2. **Write it terse.** Call `add_help_finding(title, body, tags=[...])`:
   - `title`: short, specific (becomes the filename and the `#` heading).
   - `body`: markdown — lead with the confirmed fact, then a minimal example.
     Note production-confirmed facts as such.
   - `tags`: e.g. `["auth"]`, `["tql"]`, `["services"]`.
3. **Confirm.** The tool returns the `local` path; the finding is immediately
   searchable and ranks **above** the reference corpus in `search_help`.

## Notes
- Findings live in the writable vault (`OWS_VAULT_DIR`, default `./ows-vault`)
  under `00 Findings/`. They are meant to be committed and shared by the team.
- The reference corpus under `Reference/` is auto-generated and read-only —
  never write findings there.
