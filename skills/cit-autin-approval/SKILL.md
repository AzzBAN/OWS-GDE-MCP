---
name: cit-autin-approval
description: Validate CIT account-upgrade tickets sitting in the AUTIN approval queue. Reports APPROVE / REJECT / NEEDS_REVIEW per ticket based on attachment rules derived from the requester's USER_EXTRA profile, then awaits user confirmation to execute approval.
---

# CIT AUTIN Approval Validation Skill

Validates CIT account-upgrade tickets, reports verdicts, and awaits user confirmation to execute approvals via the OWS L1/L2 approval service.

## Prerequisites

- **tesseract** system binary: `brew install tesseract` (macOS) / `apt install tesseract-ocr` (Linux)
- **Python packages**: `pip install pytesseract Pillow`
- **OCR script**: `scripts/ocr_attachment.py` (thin wrapper around tesseract; defaults to PSM 6, falls back to PSM 3)
- **OWS MCP server**: configured and connected (for ticket queries + service invocation)
- Stop and inform the user if any prerequisite is missing.

## Tool Mapping & Constraints

### Tool Mapping Table
| Abstract Operation | MCP (opencode / Claude Code) | Direct HTTP | No MCP (Cursor / Copilot) |
|---|---|---|---|
| Query ticket data | `query_model_data` | POST /adc-app-ops/.../tql/execute | Ask user to run TQL |
| Invoke OWS service | `invoke_service` | POST /adc-app-ops/.../service/test | Ask user to run |
| List attachments | `list_file_attachments` | GET /adc-file/.../file/list | Ask user |
| Download attachment | `download_file_attachment` | GET /adc-file/.../file/download | Ask user |
| Run OCR | `bash: python3 scripts/ocr_attachment.py <path>` | Same | Same |
| Dispatch subagent | `Agent` tool (if available) | N/A — sequential | N/A — sequential |

### Constraints — READ BEFORE EXECUTING
- **Use ONLY** `scripts/ocr_attachment.py` for OCR. Do NOT write, edit, or generate any new script/Python files.
- **Do NOT** use the Write tool to create helper scripts. All text matching, date comparison, and validation is done inline by the agent.
- **Bash** is ONLY for: `mkdir -p tmp_attachments/<id>`, `rm -rf tmp_attachments`, and running the OCR script.
- **Read** is ONLY for reading OCR text files.
- **Never use Playwright/browser.**

## Scope
A ticket is in scope only if: `cit_type = 'account'`, `current_operator = 'group:AUTIN'`, `order_status = 'running'`, and `current_phase_name IN ('Approval L1', 'Approval L2')`.

## Attachment Rules — Resolved Live Per Run
Pull the live USER_EXTRA registry at the start of each run:
```python
invoke_service(tenant="prod", project_name="centralized_inquiry_tracker", module_name="centralized_inquiry_tracker", service_name="centralize_user_extra_info_get_list", payload={"start": 0, "limit": 100}, confirm=True)
```
Page through with `start` increments if `total > limit`. Filter to `active == true`.
Waterfall match the ticket's `user_group` + `cit_domain` + `cit_sub_domain` against active rows:
1. **Triple match**: `user_group_id == ticket.user_group AND user_domain_id == ticket.cit_domain AND sub_user_domain_id == ticket.cit_sub_domain`
2. **Group + domain**: `user_group_id == ticket.user_group AND user_domain_id == ticket.cit_domain AND sub_user_domain_id IS NULL`
3. **Group root**: `user_group_id == ticket.user_group AND user_domain_id IS NULL`
4. **No match**: Verdict → `NEEDS_REVIEW — user_extra unresolvable`. (If registry call fails, stop and mark all as `NEEDS_REVIEW — registry unreachable`).

Determine attachment requirements from the matched row's flags:
- `csc_cert = true` → `certificate_attachment` (Netcare CSC) + `spv_approval` required
- `csc_cert = false` AND `ioh_counterpart = true` → `spv_approval` + `ioh_approval` required
- `csc_cert = false` AND `ioh_counterpart = false` → `spv_approval` only

## Validation Rules
Verify the OCR-extracted text of attachments against these rules (OCR all files for multi-file attachments; APPROVE if ANY matches):

### 1. Attachment Checks
| Attachment | Required Checks |
|---|---|
| **Certificate** | Case-insensitive match on `csc_cert_id` (normalize hyphens). End date parsed from text must be `>= today`. |
| **SPV Approval** | Contains `spv_name` or `spv_id`. Approval keyword present (`approved`, `approve`, `ok approved`, `setuju`, `disetujui`). Mention of `email_new`, `account_ows`, `name_new`, or `no_hp_input`. Date in email Sent/signature block is not stale (see below). |
| **IOH Approval** | Contains `ioh_name`, `ioh_id`, or `ioh_email`. Approval keyword present (`approved`, `approve`, `setuju`). Mention of `email_new`, `account_ows`, `name_new`, or `no_hp_input`. |

### 2. Staleness Rule
- **extend_account**: REJECT if approval date is > 3 months before `create_time`.
- **upgrade_account**: Look up `product_duration` (months) in the matched USER_EXTRA row's `product_map` for the ticket's `product`. REJECT if approval date is > `product_duration` months before `create_time`.
- *Note:* Approvals on/after `create_time` always pass. Never use file upload/download/capture metadata.

### 3. NEEDS_REVIEW Format
If OCR output is empty/garbled or matches are ambiguous, mark as `NEEDS_REVIEW` using this format:
`OCR'd <filename>. Found: <fields verified>. Missing: <specific field>. Reason: <specific issue>.`
- **Valid Example**: `OCR'd spv_approval__email.png. Found: sender 'Rizal Fauji', date 'May 22'. Missing: approval keyword. Reason: the email says "please proceed" but never explicitly approves.`
- **Valid Example**: `OCR'd certificate_attachment__netcare.png. Found: cert table. Missing: csc_cert_id 'NSE-0202286'. Reason: screenshot only shows the NSC tab, not the NSE tab.`
- **Valid Example**: `OCR'd spv_approval__screenshot.jpg. Found: 28 chars of noise ('EI 5 3 E q'). Missing: all fields. Reason: image captured at angle, tesseract couldn't resolve text.`

## Execution Flow
1. **Clear cache**: Run `rm -rf tmp_attachments` (run also at start/end of any execution).
2. **Pull registry**: Run Step A (Attachment Rules). Stop if it fails.
3. **Build queue**: Run TQL query if specific IDs are not provided:
   ```sql
   select t.ticket_id, t.order_id, t.cit_username, t.ows_account, t.csc_cert_id, t.csc_cert_end_date, t.spv_name, t.spv_id, t.spv_email, t.ioh_name, t.ioh_id, t.ioh_email, t.certificate_attachment, t.spv_approval, t.ioh_approval, t.create_time, t.current_phase_name, t.cit_type, t.current_operator, t.order_status, t.user_group, t.cit_domain, t.cit_sub_domain, t.email_new, t.account_ows, t.name_new, t.no_hp_input, t.nik, t.order_category, t.product from "/centralized_inquiry_tracker/centralized_inquiry_tracker/centralize_inquiry_ticket" as t where t.cit_type = 'account' and t.current_operator = 'group:AUTIN' and t.order_status = 'running' order by t.create_time desc
   ```
   Filter client-side for `current_phase_name IN ('Approval L1', 'Approval L2')`.
4. **Triage nulls**: Reject if required fields (`certificate_attachment`, `ioh_approval`, `spv_approval`) are null.
5. **Dispatch/Download**: For 3+ tickets, prefer subagents (Appendix A). For inline, download required tokens. If `File token timed out!`, re-query ticket once to fetch fresh token; retry once. On HTTP 500, retry once. **No-Reject Rule**: If token/download fails, mark `NEEDS_REVIEW — token expired after retry` or `NEEDS_REVIEW — attachment download failed` (never REJECT).
6. **OCR & Validate**: Run `python3 scripts/ocr_attachment.py "tmp_attachments/<ticket_id>/<file>"`. OCR all files in parallel. If empty/error, retry once with `--psm 3`. Short-circuit on SPV failure (skip cert/ioh OCR). Validate against rules.
7. **Report**: Format summary table and per-ticket details (specifying matched profile keycode + match level).
8. **User Gate (HARD GATE)**: Present proposed action table (Accept/Reject/Manual review) and wait for explicit confirmation (e.g., "approve all", "go ahead"). Do not call approval service yet.
9. **Execute**: Map `APPROVE` → `Accept`, `REJECT` → `Reject`. Map `Approval L1` → `centralize_approval_l1` (`operation_mode_l1`/`l1_description`), `Approval L2` → `centralize_approval_l2` (`operation_mode_l2`/`l2_description`). Invoke service in parallel with human-like descriptions containing specific evidence.
10. **Cleanup**: Run `rm -rf tmp_attachments`.

## Report & Execution Templates
### Single Ticket Report
```
## <ticket_id> — <VERDICT>
Phase: <phase> | Created: <create_time> | Requester: <requester>
Requested account: name_new=... | account_ows=... | email_new=...
Supervisor: <spv_name> (<spv_email>)
Profile: <keycode> (<match_level>) — requires <attachments>
[✓/✗] Cert <csc_cert_id> valid/invalid...
[✓/✗] Spv approval from <spv_name> dated <date> (stale/valid)
[✓/✗] Requested account present in OCR
[✓/✗] Approval text: "<excerpt>"
```
### Queue Summary Table
```
## AUTIN Queue — <N> tickets in scope
| Ticket ID | Phase | Profile (live) | Required | Verdict | Reason |
|---|---|---|---|---|---|
| CIT-... | L1 | USER_EXTRA-0001 (group root) | cert+spv | APPROVE | all checks pass |
```
### Action Confirmation Table
```
## Validation Complete — Awaiting Your Approval to Execute
| Ticket ID | Phase | Verdict | Proposed Action |
|---|---|---|---|
| CIT-... | L1 | APPROVE | Accept |
```
### Description Examples
- **APPROVE (L1)**: "Supervisor approval from Oscarivan Ganadi (Oscarivan.Ganadi@huawei.com) confirmed via email dated 2026-05-22 with explicit approval text 'Ok approved, please continue the process.' Certificate NSE-0202286 verified valid through December 2026. All required attachments present and validated — no issues found. Account upgrade request approved."
- **REJECT (missing)**: "Required IOH counterpart approval document is missing from this request. The ticket was submitted without the necessary customer-side approval from the IOH counterpart. While the supervisor approval from Rizal Fauji was present and valid, the account upgrade cannot proceed without the IOH sign-off. Request rejected."
- **REJECT (stale)**: "Supervisor approval from Oscarivan Ganadi dated 2026-01-15 is more than 3 months before the ticket creation date of 2026-05-22. Per policy, approvals older than 3 months are not accepted for extend_account requests. A fresh, current approval is required. Request rejected."

## Reject Taxonomy
- `REJECT — cert ID mismatch` / `REJECT — cert expired` / `REJECT — no cert attached`
- `REJECT — no spv approval attached` / `REJECT — no IOH counterpart approval attached`
- `REJECT — spv name mismatch` / `REJECT — no approval text in attachment` / `REJECT — requested account not mentioned` / `REJECT — spv approval stale`
- `NEEDS_REVIEW — attachment unreadable` / `NEEDS_REVIEW — token expired after retry` / `NEEDS_REVIEW — attachment download failed` / `NEEDS_REVIEW — user_extra unresolvable` / `NEEDS_REVIEW — registry unreachable`

## Field Reference (CIT Model)
| Field | Description / Usage |
|---|---|
| `ticket_id`, `order_id` | Identifiers; `order_id` used for approvals. |
| `current_phase_name` | "Approval L1" / "Approval L2". |
| `current_operator`, `cit_type`, `order_status` | Scope checks (`group:AUTIN`, `account`, `running`). |
| `create_time` | Reference for staleness. |
| `cit_username`, `ows_account` | Requester info (informational only; do NOT match in approval text). |
| `email_new`, `account_ows`, `name_new`, `no_hp_input`, `nik` | Requested account fields to match in OCR text. |
| `spv_name`, `spv_id`, `spv_email` | Expected supervisor fields. |
| `ioh_name`, `ioh_id`, `ioh_email` | Expected customer-side counterpart fields. |
| `order_category`, `product` | Determines staleness: extend=3 months; upgrade=look up `product_duration` in matched USER_EXTRA `product_map` by `product`. |
| `csc_cert_id`, `csc_cert_end_date` | Cert checks on Netcare screenshot. |
| `certificate_attachment`, `spv_approval`, `ioh_approval` | File tokens. |
| `user_group`, `cit_domain`, `cit_sub_domain` | Waterfall keys. |

## Appendix A: Subagent Fan-Out
- **Trigger**: If `Agent` tool is available and queue has 3+ tickets, split remaining tickets into chunks of 3-4.
- **Dispatch**: Launch subagents in parallel using a single message with multiple `Agent` tool blocks.
- **Subagent Brief**: Pass ticket IDs, tokens, expected identities, required attachments, profile keycode/match level, and staleness threshold. Include a reference to this skill's validation/no-reject rules. Subagents run list, download, OCR, and validation, then return *only* the verdict table: `{ ticket_id, verdict, reason, profile, required, evidence_summary }`.
- **Skip**: Queue < 3 tickets, all null-triaged, or tool unavailable.
