---
name: cit-autin-approval
description: Validate CIT account-upgrade tickets sitting in the AUTIN approval queue. Reports APPROVE / REJECT / NEEDS_REVIEW per ticket based on attachment rules derived from the requester's USER_EXTRA profile (CSC cert, IOH counterpart, or spv-only), then awaits user confirmation before executing the approval via the OWS L1/L2 service with human-like descriptions. Use when asked to "review CIT", "check AUTIN queue", "validate approval", or "approve CIT" for one or more tickets.
---

# CIT AUTIN Approval Validation Skill

Validates CIT account-upgrade tickets in the AUTIN approval queue, reports APPROVE/REJECT/NEEDS_REVIEW per ticket, then **awaits user confirmation** before executing the approval via the OWS approval service.

## Image extraction — OCR, not vision

Attachments are screenshots of machine-rendered text (Outlook, Netcare, Huawei certificates, WhatsApp). We use **tesseract OCR** to extract text — faster, deterministic, and works on any model variant.

**OCR script:** `scripts/ocr_attachment.py` — a thin wrapper around tesseract. Takes an image path, outputs plain text to stdout.

```bash
python3 scripts/ocr_attachment.py tmp_attachments/<ticket_id>/spv_approval__<file>
```

PSM 6 (uniform block of text) is the default — correct for email screenshots, portal pages, and certificate forms. Use `--psm 4` for single-column layouts or `--psm 3` for fully automatic mode if the default produces garbage text.

## Parallel subagent fan-out (default for queues of 3+ tickets)

This is the **single biggest perf lever**. Each ticket needs up to 3 downloads + up to 3 OCR runs at ~300ms each. Sequential = 30-60s. Parallel = bounded by the slowest chunk.

**Default execution path when validating 3+ tickets:**

1. Main agent does steps 0-3 (registry pull, queue build, requirement derivation, null triage). These are cheap and benefit from a single shared registry fetch.
2. Main agent splits the **remaining tickets** (those that need attachment validation) into chunks of 3-4 and dispatches **one subagent per chunk in a single message** (multiple `Agent` tool blocks in one assistant turn — they run concurrently).
3. Each subagent receives: the ticket rows (with tokens), pre-computed required-attachments per ticket, the validation rules from this skill, and instructions to return only the verdict table.
4. Main agent collects subagent results and assembles the final report.

**Subagent brief template** (paste the rule sections inline so the subagent doesn't need to re-load the skill):

```
You are validating <N> CIT AUTIN tickets. For each ticket:
- ticket_id: ...
- required attachments: [spv_approval, certificate_attachment, ioh_approval]
- tokens: { spv_approval: "...", certificate_attachment: "...", ioh_approval: "..." }
- expected identities: spv_name, spv_id, ioh_name, ioh_id, ioh_email,
  csc_cert_id, csc_cert_end_date, email_new, account_ows, name_new, no_hp_input, create_time
- profile keycode + match level (for the report)
- **Staleness**: order_category + threshold in months (extend=3, upgrade=product_duration from matched USER_EXTRA product_map)

For each ticket, in parallel where possible:
1. list_file_attachments + download_file_attachment for each required token
2. Run OCR on each saved file: python3 scripts/ocr_attachment.py <file>
3. Apply validation rules (paste section 6 A/B/C below — text-based checks)
4. Return only: { ticket_id, verdict, reason, profile, required, evidence_summary }

Tools: Use ONLY mcp__ows-gde__*, Bash (for mkdir + OCR), and Read (only to read OCR text output if needed). Never use Playwright/browser.

VALIDATION DISCIPLINE — read carefully, this is where prior runs failed:

- OCR output IS the evidence. Search the extracted text for expected fields (names, cert IDs, dates, approval keywords). Don't second-guess it.
- File size is not a legibility signal. Do not cite "image too small (X KB)". Cite what OCR actually failed to extract.
- Multi-file attachments: OCR ALL files. If ANY file's extracted text matches the requirements, the verdict is APPROVE for that attachment. Only REJECT if none match.
- Staleness compares the date written INSIDE the evidence (email Sent: header, WhatsApp timestamp, signed form date) against create_time. Never use file capture/upload/download metadata. The threshold depends on `order_category`:
  - **extend_account**: REJECT if approval > 3 months before create_time.
  - **upgrade_account**: look up `product_duration` (months) from the matched USER_EXTRA row's `product_map` for the ticket's `product` — REJECT if approval > `product_duration` months before create_time.
  Approvals on or after create_time always pass (neither rule REJECTs post-date approvals).
- Partial text matches that are unambiguous (e.g. "Oscarivan Gan..." for "Oscarivan Ganadi") are matches. Don't hedge.
- NEEDS_REVIEW is a last resort. When you do use it, the reason must follow this format:
    "OCR'd <filename>. Found: <fields verified>. Missing: <specific field>. Reason: <specific issue>."
  Vague reasons ("legibility insufficient", "ambiguous", "unclear") are rejected. If the OCR output is empty or clearly wrong content (e.g. OCR on a photo of a cat), that's the specific issue.

Do NOT re-query the registry. Do NOT echo attachment file lists or full OCR transcripts.
Save under tmp_attachments/<ticket_id>/ as usual.
```

**Skip subagent fan-out only when:**
- `Agent` tool unavailable (you are already a subagent — proceed directly).
- Queue is 1-2 tickets — overhead not worth it.
- Every remaining ticket already has a hard reject from null triage — nothing to validate.

## Scope (which tickets this skill handles)

A ticket is in scope **only if** all of:
- `cit_type = 'account'`
- `current_operator = 'group:AUTIN'`
- `order_status = 'running'`
- `current_phase_name IN ('Approval L1', 'Approval L2')`

If a ticket falls outside this scope, say so and stop. Do not validate.

## Inputs

The user may pass:
- A specific `ticket_id` (e.g. `CIT-20260525-00000149`) — validate only that ticket.
- A list of ticket IDs — validate each.
- Nothing / "all open" / "AUTIN queue" — scan all open AUTIN-owned tickets in scope.

---

## Attachment Rules — Resolved Live, Per Run

**This is the most important section.** Required attachments differ per requester type. **Never hardcode the rule.** The USER_EXTRA registry (which determines whether a CSC cert is required, whether IOH counterpart approval is required) is owned by ops and changes over time — new profiles get added, flags flip, domains/sub-domains move between groups. The skill must always pull the **current** registry at the start of each run.

### Step A — Pull the live registry (always, every run)

```
invoke_service(tenant="prod",
               project_name="centralized_inquiry_tracker",
               module_name="centralized_inquiry_tracker",
               service_name="centralize_user_extra_info_get_list",
               payload={"start": 0, "limit": 100},
               confirm=True)
```

If `result.total > result.results.length`, page through with `start` increments until you have every row. Cache the result **only for the duration of this single conversation/run** — never persist it, never assume a previous run's snapshot is still correct.

Each row has the shape:
```
{
  "keycode": "USER_EXTRA-0001",
  "user_group_id": "GROUP_01",
  "user_group_name": "Huawei MS",
  "user_domain_id": "DOMAIN_05" | null,
  "user_domain_name": "FSO" | "",
  "sub_user_domain_id": "SUB-DOMAIN_27" | null,
  "sub_user_domain_name": "FSO" | "",
  "csc_cert": true | false,
  "ioh_counterpart": true | false,
  "account_type": "wxid" | "email" | "3rd" | "ioh",
  "active": true | false
  // ...other fields ignored
}
```

Filter to `active == true` only. Inactive rows are tombstones — do not match against them.

### Step B — Waterfall match (per ticket)

For each ticket, match its `user_group` + `cit_domain` + `cit_sub_domain` against the live rows in this order. The first hit wins:

1. **Triple match** — `user_group_id == ticket.user_group AND user_domain_id == ticket.cit_domain AND sub_user_domain_id == ticket.cit_sub_domain`.
2. **Group + domain** (sub-domain wildcard) — `user_group_id == ticket.user_group AND user_domain_id == ticket.cit_domain AND sub_user_domain_id IS NULL`.
3. **Group root** (domain wildcard) — `user_group_id == ticket.user_group AND user_domain_id IS NULL`.
4. **No match** → `NEEDS_REVIEW — user_extra unresolvable`. Do not guess.

A row that specifies only `user_group_id` (no domain, no sub-domain) is the **default for that whole group**. A more specific row with the same `user_group_id` and a populated `user_domain_id` (and optionally `sub_user_domain_id`) **overrides** the root rule for tickets matching that domain.

When citing a profile in the report, always include the keycode AND which level matched (e.g. `USER_EXTRA-0009 (group+domain)`, `USER_EXTRA-0001 (group root)`). This makes the rule path auditable.

### Step C — Read `csc_cert` and `ioh_counterpart` from the matched row

These two boolean flags on the matched row determine attachment requirements:

- `csc_cert = true` → `certificate_attachment` (Netcare CSC) is **required** + `spv_approval`
- `csc_cert = false` AND `ioh_counterpart = true` → `spv_approval` + `ioh_approval` (IOH counterpart) **required**
- `csc_cert = false` AND `ioh_counterpart = false` → `spv_approval` only

`spv_approval` is required for **every** profile.

The ticket model exposes `ioh_name`, `ioh_id`, `ioh_email` for verifying the IOH counterpart's identity inside the `ioh_approval` attachment — never use `spv_*` fields for that check.

### What NOT to do

- ❌ Do not maintain a hardcoded keycode → flags table in this skill, in CLAUDE.md, or in memory. The registry is the source of truth.
- ❌ Do not memo-ize the registry across runs. Tokens, flags, and profile lists drift; pull fresh every time.
- ❌ Do not skip the `active` filter — inactive rows can still be returned by the endpoint.
- ❌ Do not assume a missing keycode means "no rule" — re-page the registry first; if still absent, surface as `NEEDS_REVIEW — user_extra unresolvable`.

### Fallback if the endpoint is unavailable

If `invoke_service` for `centralize_user_extra_info_get_list` fails (auth, network, tenant outage), do **not** validate any ticket whose attachment requirements can't be resolved. Mark every affected ticket `NEEDS_REVIEW — registry unreachable` and stop. Do not guess from prior runs.

---

## Steps

### Clean slate — clear previous attachments

**Before starting any validation**, wipe the attachment cache so previous-run files don't leak into the current session:

```bash
rm -rf tmp_attachments
```

This ensures every file you download belongs to the current run. Run this even when validating a single ticket.

### 0. Pull the live USER_EXTRA registry (always first)

Before touching any ticket, run **Step A** of the Attachment Rules section. You need the registry resolved before you can decide which attachments each ticket actually requires. If the registry call fails, stop — do not validate.

### 1. Build the queue (skip if user gave specific IDs)

```
select t.ticket_id, t.order_id, t.cit_username, t.ows_account, t.csc_cert_id,
       t.csc_cert_end_date, t.spv_name, t.spv_id, t.spv_email,
       t.ioh_name, t.ioh_id, t.ioh_email,
       t.certificate_attachment, t.spv_approval, t.ioh_approval,
       t.create_time, t.current_phase_name, t.cit_type, t.current_operator,
       t.order_status, t.user_group, t.cit_domain, t.cit_sub_domain,
       t.email_new, t.account_ows, t.name_new, t.no_hp_input, t.nik,
       t.order_category, t.product
from "/centralized_inquiry_tracker/centralized_inquiry_tracker/centralize_inquiry_ticket" as t
where t.cit_type = 'account'
  and t.current_operator = 'group:AUTIN'
  and t.order_status = 'running'
order by t.create_time desc
```

Filter client-side for `current_phase_name` = `Approval L1` or `Approval L2`.

### 2. Determine required attachments per ticket

Run **Step B** (waterfall match) and **Step C** (read flags) of the Attachment Rules section against the registry pulled in Step 0. Outputs per ticket:

- Matched keycode + level (triple / group+domain / group root) — record this for the report
- `csc_cert` flag → `certificate_attachment` required?
- `ioh_counterpart` flag → `ioh_approval` required?
- `spv_approval` is always required.

#### Determine staleness threshold per ticket

For each ticket, compute the staleness threshold based on `order_category`:

- **`extend_account`**: threshold = 3 months.
- **`upgrade_account`**: look up `product_duration` from the matched USER_EXTRA row's `product_map`. Find the entry where `product_id` matches the ticket's `product` field. The entry's `product_duration` (in months) is the threshold. If no matching entry found → mark `NEEDS_REVIEW — product not found in USER_EXTRA product_map`.

Record the threshold for the report.

If the waterfall returns no match → mark `NEEDS_REVIEW — user_extra unresolvable` and skip to next ticket.

### 3. Triage null attachments immediately

Before downloading anything:

- If `certificate_attachment` is **null** AND it is required → `REJECT — no cert attached`
- If `ioh_approval` is **null** AND it is required → `REJECT — no IOH counterpart approval attached`
- If `spv_approval` is **null** → `REJECT — no spv approval attached`

Skip all downloads for any ticket that already has a hard reject from null fields.

### 4. Dispatch validation work (parallel subagents preferred)

Use the **Parallel subagent fan-out** section above. Default path for 3+ tickets is one subagent per 3-4 tickets, dispatched concurrently. The main agent assembles results.

**Token freshness:** tokens from the bulk query in step 1 are valid ~30 min. Do **not** preemptively re-query — only re-query if a download returns `File token timed out!`. Preemptive re-queries add 11+ TQL round-trips for no benefit on a queue that completes in minutes.

**If proceeding inline (1-2 tickets, or already a subagent):** validate each ticket end-to-end before moving on. Output partial results between tickets only when the user is watching a long queue and needs streaming feedback.

**Re-query single ticket on token expiry:**
```
select t.certificate_attachment, t.spv_approval, t.ioh_approval
from "/centralized_inquiry_tracker/centralized_inquiry_tracker/centralize_inquiry_ticket" as t
where t.ticket_id = '<ID>' limit 1
```

### 5. Download required attachments

Only download attachments that are required for the ticket's USER_EXTRA profile.

```python
# Always download spv_approval
list_file_attachments(tenant="prod", token=row["spv_approval"])
download_file_attachment(tenant="prod", token=..., file_name=...,
                        save_dir=f"tmp_attachments/{ticket_id}",
                        save_as=f"spv_approval__{file_name}")

# If csc_cert required:
list_file_attachments(tenant="prod", token=row["certificate_attachment"])
download_file_attachment(tenant="prod", token=..., file_name=...,
                        save_dir=f"tmp_attachments/{ticket_id}",
                        save_as=f"certificate_attachment__{file_name}")

# If ioh_counterpart required:
list_file_attachments(tenant="prod", token=row["ioh_approval"])
download_file_attachment(tenant="prod", token=..., file_name=...,
                        save_dir=f"tmp_attachments/{ticket_id}",
                        save_as=f"ioh_approval__{file_name}")
```

**Token expiry:** If `list_file_attachments` returns `File token timed out!`, re-query the row and retry once. If still expired → `NEEDS_REVIEW — token expired after retry`.

**Server errors:** HTTP 500 from `download_file_attachment` → retry once. If it fails again → `NEEDS_REVIEW — attachment download failed`.

### 6. OCR and validate attachments

**Step 6a — Run OCR on every downloaded file:**

```bash
python3 scripts/ocr_attachment.py "tmp_attachments/<ticket_id>/<saved_file>"
```

Run all OCR calls in parallel (one Bash tool call per file in a single turn). Each call returns plain text in ~300ms. If OCR returns empty or exits non-zero, retry once with `--psm 3` (auto mode). If still empty → `NEEDS_REVIEW — attachment unreadable` with the specific reason.

**Step 6b — Validate the extracted text against the rules below.**

#### A. CSC Certificate validation (`certificate_attachment`) — only if `csc_cert = true`

The image is typically a Netcare portal screenshot or a Huawei Cyber Security Certificate.

Search the OCR-extracted text for these checks:

| Check | How to verify in extracted text |
|---|---|
| Cert ID | Text contains `csc_cert_id` exactly (e.g. search for `NSE-0202286` or `NSE-0-0202286` — both forms appear). Use case-insensitive substring match: `csc_cert_id` with hyphens normalized. |
| Validity | Text contains `valid` (case-insensitive) near the cert ID. For the formal certificate, check that the end date string (e.g. `May 07,2027`) parses to a date `>= today`. |
| End date sanity | If an end date is visible, compare loosely against `csc_cert_end_date`. Warn on mismatch; don't reject on this alone. |

#### B. Supervisor approval validation (`spv_approval`) — always required

Typically an Outlook email screenshot or signed form. Search the OCR-extracted text:

| Check | How to verify in extracted text |
|---|---|
| Approver identity | Text contains `spv_name` (or a substring that unambiguously matches it) OR `spv_id` (email). Look near `From:` lines in email headers. |
| Approval text | Text contains at least one of: `approved`, `approve`, `ok approved`, `setuju`, `disetujui` (case-insensitive). |
| Requested account mentioned | Text contains one of: `email_new`, `account_ows`, `name_new`, or `no_hp_input`. |
| Date freshness | Extract the date from the email `Sent:` header or signature block. Threshold depends on `order_category`: **extend_account** → 3 months; **upgrade_account** → `product_duration` from the matched USER_EXTRA row's `product_map` for the ticket's `product`. REJECT if approval > threshold before `create_time`. Approvals on or after create_time pass. If no date is found, check for a month name + day near the top of an email screenshot. |

#### C. IOH counterpart approval validation (`ioh_approval`) — only if `ioh_counterpart = true`

Typically an email, WhatsApp screenshot, or signed document from the IOH counterpart (customer side). Search the OCR-extracted text:

| Check | How to verify in extracted text |
|---|---|
| Approver identity | Text contains `ioh_name` OR `ioh_id` OR `ioh_email` (the customer-side counterpart fields, NOT `spv_*`). |
| Approval text | Text contains `approved`, `approve`, `setuju`, or equivalent (case-insensitive). |
| Requested account mentioned | Text contains one of: `email_new`, `account_ows`, `name_new`, or `no_hp_input`. |

Note: For USER_EXTRA-0007 (Customer/IOH requesters) the requester themselves is IOH-side; in that case the spv and ioh fields often point to the same person and `spv_approval`/`ioh_approval` may be the same evidence.

If the OCR output is empty, garbled beyond recognition, or clearly the wrong content → `NEEDS_REVIEW`, not `REJECT`.

### 6.5 Validation discipline (read this before deciding NEEDS_REVIEW)

NEEDS_REVIEW is a **last resort**, not an easy-out. OCR is fast and deterministic — it either extracts the text or it doesn't. Apply these rules:

**1. OCR output IS the evidence.** Run `python3 scripts/ocr_attachment.py <file>`, read the result. If the text contains what you need, decide APPROVE/REJECT. Never say "needs vision confirmation" or "needs OCR" — you just ran OCR. The text is in front of you.

**2. File size ≠ legibility.** Many valid Netcare/Outlook/WhatsApp screenshots are <100KB and OCR perfectly. Do not cite "image too small (X KB)" as a reason. Cite what OCR actually failed to extract.

**3. Multi-file attachments = OCR each.** If a token returns two or more files (dual cert, two screenshots), OCR all of them. Verdict logic:
   - Cert: if **any** file's OCR text contains `csc_cert_id` and `valid` → APPROVE. None match → REJECT with cert ID mismatch.
   - Spv/IOH: if **any** file's OCR text passes all required checks → APPROVE. None pass → REJECT with the failed rule.
   Never punt to NEEDS_REVIEW because "there were multiple files".

**4. Staleness uses the date *inside* the evidence, not file metadata.** The threshold depends on `order_category`:
   - **extend_account**: REJECT if approval > 3 months before `create_time`.
   - **upgrade_account**: look up `product_duration` from the matched USER_EXTRA row's `product_map` (find the entry with `product_id` matching the ticket's `product` field). REJECT if approval > `product_duration` months before `create_time`.
   Approvals on or after create_time always pass. The file's capture/upload/download time is otherwise irrelevant. Do not REJECT or NEEDS_REVIEW based on "screenshot captured Nd after create_time".

**5. Bias toward APPROVE/REJECT.** If the checks are all decisively pass or fail from the OCR text, return APPROVE or REJECT. Don't add hedging like "but sender truncated" if the visible portion clearly matches `spv_name` (e.g. "Oscarivan Gan..." matches "Oscarivan Ganadi"). Partial-text matches that are unambiguous are matches.

**6. Short-circuit on spv failure.** `spv_approval` is required for every profile. Run OCR on spv first — if it fails, the ticket is REJECT regardless of cert/ioh. Skip OCR on the remaining attachments to save time.

**7. NEEDS_REVIEW must show your work.** Any reason category is acceptable as long as it's backed by specific evidence from the OCR output. The reason must follow this format:

> "OCR'd <filename>. Found: <list of fields you DID extract, e.g. sender 'Rizal Fauji', date 'May 22'>. Missing: <specific field you couldn't verify, e.g. approval keyword — none of approved/approve/setuju found in OCR text>. Reason: <what you think happened, e.g. the approval was given verbally on a call and the email only says 'as discussed', or tesseract misread the text due to unusual font>."

**Invalid NEEDS_REVIEW** — these are vague and will be rejected. They indicate you didn't actually run OCR and read the output:

- `NEEDS_REVIEW — OCR unclear` → unclear HOW? What did the OCR output actually say?
- `NEEDS_REVIEW — attachment ambiguous` → what specifically was ambiguous?
- `NEEDS_REVIEW — legibility insufficient` → which field couldn't you read? Show the OCR output.
- `NEEDS_REVIEW — needs OCR confirmation` → you just ran OCR. The output IS the confirmation.

The fix for any of the above is the same: re-run OCR (try `--psm 3` if `--psm 6` produced garbage), then write the structured "Found / Missing / Reason" format. If you genuinely cannot produce that format, you haven't looked at the OCR output yet.

**Valid NEEDS_REVIEW examples** (these all pass because they cite specific evidence):

- `OCR'd spv_approval__email.png. Found: sender 'Rizal Fauji', date 'May 22', body mentions 'extend account'. Missing: approval keyword — none of approved/approve/setuju found in OCR text. Reason: the email body says "as per our discussion, please proceed" but never explicitly approves.`
- `OCR'd certificate_attachment__netcare.png. Found: cert table with NSC and PPCC entries visible. Missing: NSE cert ID — csc_cert_id 'NSE-0202286' not found anywhere in OCR text. Reason: the screenshot only shows the NSC/PPCC tabs, not the NSE certification tab.`
- `OCR'd spv_approval__screenshot.jpg. Found: OCR returned 28 chars of noise ('EI 5 3 E q Qe:'). Missing: all fields — no names, dates, or text extracted. Reason: the image appears to be a photo of a printed form taken at an angle; tesseract couldn't resolve any text at --psm 6 or --psm 3.`

### 7. Produce the report

Per ticket, output one of three verdicts:

- **APPROVE** — all required checks passed.
- **REJECT** — at least one hard rule failed. List every failed rule.
- **NEEDS_REVIEW** — OCR output empty/garbled, or token expired after retry.

### Report format

For a single ticket:

```
## CIT-20260525-00000149 — APPROVE

Phase: Approval L1 | Created: 2026-05-25 13:54
Requester: Arief Miftahur Rohman (84250570)
Requested account: name_new=... | account_ows=... | email_new=...
Supervisor: Oscarivan Ganadi (Oscarivan.Ganadi@huawei.com)
Profile: <keycode resolved live> (<match level>) — requires <attachments derived from live flags>

✓ Cert NSE-0202286 valid through 2026-12-16 (OCR confirmed in Netcare screenshot)
✓ Spv approval from Oscarivan Ganadi dated 2026-05-22 (3 days before ticket)
✓ Requested account ("name_new" / "account_ows") present in OCR text
✓ Approval text: "Ok approved, please continue the process."
```

For a queue scan, lead with a summary table. Always include the matched profile keycode AND the match level returned by the live waterfall — never invent a keycode, only cite what the registry returned this run:

```
## AUTIN Queue — 11 tickets in scope

| Ticket ID | Phase | Profile (live) | Required | Verdict | Reason |
|---|---|---|---|---|---|
| CIT-...073 | L1 | <keycode> (group root) | cert+spv | APPROVE | all checks pass |
| CIT-...070 | L1 | <keycode> (group root) | spv+ioh | REJECT | ioh_approval missing |
| CIT-...068 | L1 | <keycode> (group+domain) | spv+ioh | NEEDS_REVIEW | spv OCR text missing sender name |

Then per-ticket details below.
```

### 8. Present report and await user go signal

After producing the full validation report (step 7), **stop and present a verdict summary to the user**. Do NOT call any approval service yet.

Format the summary as a table of proposed actions:

```
## Validation Complete — Awaiting Your Approval to Execute

| Ticket ID | Phase | Verdict | Proposed Action |
|---|---|---|---|
| CIT-...073 | L1 | APPROVE | Accept |
| CIT-...070 | L1 | REJECT | Reject |
| CIT-...068 | L2 | APPROVE | Accept |
| CIT-...066 | L2 | NEEDS_REVIEW | Manual review needed |
```

**Explain clearly:**
- How many tickets will be **Accepted** (APPROVE verdict)
- How many will be **Rejected** (REJECT verdict)
- How many **Need Review** (NEEDS_REVIEW — cannot auto-execute)
- What the proposed actions mean for each

**Then WAIT for the user's go signal.** Present this as a pause, not an auto-continue.

- If the user asks questions or raises concerns → answer them.
- If the user says "there is still something I need you to do" → HOLD. Do not execute. Address their requests.
- Only proceed to step 9 when the user explicitly says "approve all", "go ahead", "do it", "please execute", or equivalent.

### 9. Execute approval

Only proceed when the user **explicitly gives consent** to execute.

For each ticket where the verdict is APPROVE or REJECT:

1. **Map verdict → operation_mode:** `APPROVE` → `"Accept"`, `REJECT` → `"Reject"`
2. **Map phase → service:**
   - `Approval L1` → `service_name="centralize_approval_l1"`, payload keys `operation_mode_l1` / `l1_description`
   - `Approval L2` → `service_name="centralize_approval_l2"`, payload keys `operation_mode_l2` / `l2_description`
3. **Generate a human-like description** — a short, descriptive paragraph explaining the decision (see format below).
4. **Call `invoke_service`:**
   ```python
   invoke_service(
       tenant="prod",
       project_name="centralized_inquiry_tracker",
       module_name="centralized_inquiry_tracker",
       service_name="centralize_approval_l1",  # or _l2
       payload={
           "operation_mode_l1": "Accept",  # or "Reject"
           "order_id": "<order_id>",
           "l1_description": "<human-like description>"
       },
       confirm=True  # required for prod writes
   )
   ```

Call services for independent tickets in parallel (one `invoke_service` tool block per ticket in a single turn).

**NEEDS_REVIEW tickets:** Do NOT execute. Report them to the user as requiring manual review.

**Handle execution results:**
- On success: record `✓ Success`
- On failure: show the error, do not auto-retry — ask the user.

**Report execution results:**

```
## Execution Complete

| Ticket ID | Phase | Verdict | Proposed Action | Result |
|---|---|---|---|---|
| CIT-...073 | L1 | APPROVE | Accept | ✓ Success |
| CIT-...070 | L1 | REJECT | Reject | ✓ Success |
| CIT-...068 | L2 | APPROVE | Accept | ✓ Success |
| CIT-...066 | L2 | NEEDS_REVIEW | Manual review | Skipped |
```

#### Description format

The `l1_description` / `l2_description` must be a **human-like, descriptive, and reasonable paragraph** — not a terse label. It should read like something a human approver would write. Capture:

1. **What was checked** — which attachments were reviewed (spv approval, certificate, ioh approval)
2. **Key evidence findings** — who approved, when, cert validity, any missing items
3. **Decision rationale** — why APPROVE or REJECT

The description must reference **specific evidence** found during OCR (names, dates, cert IDs, explicit outcomes) — no generic text.

> **APPROVE example (L1):** "Supervisor approval from Oscarivan Ganadi (Oscarivan.Ganadi@huawei.com) confirmed via email dated 2026-05-22 with explicit approval text 'Ok approved, please continue the process.' Certificate NSE-0202286 verified valid through December 2026. All required attachments present and validated — no issues found. Account upgrade request approved."
>
> **REJECT example (missing attachment):** "Required IOH counterpart approval document is missing from this request. The ticket was submitted without the necessary customer-side approval from the IOH counterpart. While the supervisor approval from Rizal Fauji was present and valid, the account upgrade cannot proceed without the IOH sign-off. Request rejected."
>
> **REJECT example (stale approval):** "Supervisor approval from Oscarivan Ganadi dated 2026-01-15 is more than 3 months before the ticket creation date of 2026-05-22. Per policy, approvals older than 3 months are not accepted for extend_account requests. A fresh, current approval is required. Request rejected."

### 10. Clean up attachments

After execution is complete (or if the user declines to execute), remove all downloaded files:

```bash
rm -rf tmp_attachments
```

Attachments are sensitive (containing supervisor names, cert IDs, IOH counterpart details) and should not persist on disk between sessions.

---

## Reject taxonomy

- `REJECT — cert ID mismatch` (OCR text does not contain `csc_cert_id`)
- `REJECT — cert expired` (end date < today, or validity status is not `valid`)
- `REJECT — no cert attached` (`certificate_attachment` null, and `csc_cert = true` for this profile)
- `REJECT — no spv approval attached` (`spv_approval` null or empty file list)
- `REJECT — no IOH counterpart approval attached` (`ioh_approval` null, and `ioh_counterpart = true` for this profile)
- `REJECT — spv name mismatch` (OCR text does not contain `spv_name` or `spv_id`)
- `REJECT — no approval text in attachment` (OCR text has no approve / approved / setuju keyword)
- `REJECT — requested account not mentioned` (OCR text has none of `email_new`, `account_ows`, `name_new`, `no_hp_input`)
- `REJECT — spv approval stale` (threshold depends on `order_category`: extend_account → 3 months; upgrade_account → `product_duration` from matched USER_EXTRA `product_map` for ticket's `product`; REJECT if approval > threshold before `create_time`; approvals on or after the ticket date are not stale)
- `NEEDS_REVIEW — attachment unreadable` (must include structured reason per section 6.5 rule 7)
- `NEEDS_REVIEW — token expired after retry`
- `NEEDS_REVIEW — attachment download failed` (HTTP 500 after one retry)
- `NEEDS_REVIEW — user_extra unresolvable` (waterfall returned no match against the live registry)
- `NEEDS_REVIEW — registry unreachable` (live registry endpoint failed; cannot determine required attachments — do not fall back to a stale cache)

---

## Field reference (CIT model)

| Field | Use in skill |
|---|---|
| `ticket_id`, `order_id` | identifier; `order_id` used as the identifier when calling the L1/L2 approval service |
| `current_phase_name` | "Approval L1" / "Approval L2" |
| `current_operator` | must be `group:AUTIN` |
| `cit_type` | must be `account` |
| `order_status` | must be `running` |
| `create_time` | reference for staleness check |
| `cit_username`, `ows_account` | **requester identity** (the person filling the form) — informational only; do NOT match against these in approval evidence |
| `email_new`, `account_ows`, `name_new`, `no_hp_input`, `nik` | **requested account identity** — the actual account being created/upgraded; match these in the approval evidence |
| `spv_name`, `spv_id`, `spv_email` | expected supervisor identity (Huawei-side) |
| `ioh_name`, `ioh_id`, `ioh_email` | expected IOH counterpart identity (customer-side) |
| `order_category` | `extend_account` or `upgrade_account` — determines staleness threshold: extend = 3 months; upgrade = `product_duration` from matched USER_EXTRA `product_map` |
| `product` | Product ID (e.g. `PRODUCT-0001`, `PRODUCT-0008`) — used to look up `product_duration` in the matched USER_EXTRA row's `product_map` when calculating upgrade staleness |
| `csc_cert_id` | expected cert ID on Netcare screenshot |
| `csc_cert_end_date` | expected end date (sanity check only) |
| `certificate_attachment` | mateinfo-file-token → Netcare CSC cert image (only if `csc_cert = true`) |
| `spv_approval` | mateinfo-file-token → supervisor approval evidence (always required) |
| `ioh_approval` | mateinfo-file-token → IOH counterpart approval (only if `ioh_counterpart = true`) |
| `user_group`, `cit_domain`, `cit_sub_domain` | waterfall keys to resolve USER_EXTRA profile (no `user_extra_id` field exists on CIT model) |

---

## Notes

- **OCR is the extraction mechanism.** Attachments are machine-rendered screenshots — tesseract extracts text faster and more deterministically than vision models. Use `scripts/ocr_attachment.py` on every downloaded file.
- **Pull the registry every run.** The USER_EXTRA rules are owned by ops and change over time. Step 0 is non-negotiable; never substitute a hardcoded table.
- **Never assume CSC cert is required.** Always resolve the USER_EXTRA profile first.
- Tokens are short-lived. Re-query right before downloading. One retry is enough.
- Always `tenant="prod"` unless the user says testbed.
- Save downloaded attachments under `tmp_attachments/<ticket_id>/` during validation. **Always clear `tmp_attachments/` at the start of a new session and after the report is delivered** — attachments are sensitive and tokens are session-scoped, so stale files from a prior run can cause confusion or accidental re-use.
- **Execution requires user confirmation.** The skill never executes approval automatically — step 8 mandates a user go signal before step 9 runs.
- **NEEDS_REVIEW tickets are never auto-executed.** They require manual review regardless of user go signal.
- **Queue size:** For 3+ tickets, default to parallel subagent fan-out (see top section). One subagent per 3-4 tickets, all dispatched in a single assistant turn.
- **Parallel downloads:** Within a single ticket, fire `list_file_attachments` + `download_file_attachment` for cert + spv + ioh in parallel (one tool block per call in the same turn). File server handles it.
- **Parallel OCR:** After downloads complete, run OCR on all files in parallel (one Bash call per file in a single turn). Each OCR run is ~300ms independent.
- **Short-circuit on spv:** OCR spv first — if it fails, skip cert/ioh OCR since spv is always required.
- **Token re-query:** Only on `File token timed out!` from a download. Do not preemptively re-query tokens — bulk fetch tokens are valid ~30 min.
- **Server errors vs token errors:** `File token timed out!` → re-query token and retry. HTTP 500 → retry once then `NEEDS_REVIEW — attachment download failed`.
