# Plan: Rewrite CIT AUTIN Approval Skill for Multi-Agent Portability

## Goal

Rewrite `skills/cit-autin-approval/SKILL.md` from 574 lines → ~250 lines, making it portable across CLI coding agents (Claude Code, opencode, Antigravity, Cursor, Copilot, Windsurf, Cline, Aider) while preserving all validation logic.

## Target File

```
/Users/azhar/Documents/Huawei/OWS_MCP/skills/cit-autin-approval/SKILL.md
```

## Current Problems

1. **574 lines** — 10x larger than median skill (46-86 lines). Other skills: ows-query=46, ows-debug-service=56, ows-flow-debug=229.
2. **Hardcoded agent capabilities** — references `Agent` tool, `mcp__ows-gde__*` prefix, "tool blocks in a single turn", `Bash` tool, `Read` tool by name. No fallback for agents lacking these.
3. **Script dependency without docs** — `scripts/ocr_attachment.py` requires `pytesseract` + `Pillow` + system `tesseract` binary. No install instructions. Relative path breaks if CWD differs.
4. **No anti-file-creation guard** — agents with a `Write` tool can create new Python helper scripts. Current skill doesn't explicitly forbid this. Has happened in practice.
5. **Massive duplication** — staleness rules explained 5x, NEEDS_REVIEW format 3x, OCR parallelism 4x, subagent template 35 lines inline.
6. **Domain logic mixed with execution mechanics** — validation rules (stable domain knowledge) interleaved with download/OCR/parallelize instructions (agent-specific mechanics).

## Solution Structure (~250 lines)

```
SKILL.md
├── Frontmatter (compact description)                          ~6 lines
├── Overview + Prerequisites (tesseract, python, MCP)         ~15 lines
├── Tool Mapping + Constraints (NEW)                           ~25 lines
│   ├── Abstract→concrete mapping table (6 operations × 3 agent types)
│   └── Tool Constraints block (anti-file-creation rules)
├── Scope (in-scope ticket filter)                             ~8 lines
├── Attachment Rules — USER_EXTRA waterfall (single source)   ~40 lines
│   ├── Step A: pull live registry
│   ├── Step B: waterfall match (triple → group+domain → group root)
│   └── Step C: read csc_cert + ioh_counterpart flags
├── Validation Rules (single source of truth)                 ~50 lines
│   ├── Staleness decision table (1 table, not 5)
│   ├── Cert checks table (1)
│   ├── Spv checks table (1)
│   ├── IOH checks table (1)
│   └── NEEDS_REVIEW format (1 definition, referenced by name)
├── Execution Flow (agent-agnostic, sequential)               ~50 lines
│   ├── Steps 0-4: Setup and Triage
│   ├── Step 5: Download required attachments (incorporating fresh token retry logic)
│   ├── Step 6-7: OCR, validate, and report
│   ├── Step 8: Await user confirmation (HARD GATE)
│   ├── Step 9: Execute approval (L1/L2 service)
│   └── Step 10: Cleanup
├── Report format templates                                    ~20 lines
├── Reject taxonomy (compact list)                            ~12 lines
├── Field reference (compact table)                           ~18 lines
└── Appendix A: Subagent fan-out (optional optimization)      ~25 lines
```

## Key Deduplications

| Rule | Current | After |
|---|---|---|
| Staleness threshold logic | 5 occurrences (subagent brief, step 2, step 6B, section 6.5 rule 4, reject taxonomy) | 1 decision table in Validation Rules, referenced everywhere else |
| NEEDS_REVIEW format | 3 full explanations (subagent brief, section 6.5 rule 7, examples) | 1 definition in Validation Rules, referenced by name |
| OCR parallelism instructions | 4 mentions (subagent brief, step 6a, notes x2) | 1 line in Execution Flow, 1 line in Appendix A |
| Subagent brief template | 35 lines inline | Appendix A reference |
| "Notes" section | 15 bullet points at end | Merged into relevant steps |
| "What NOT to do" lists | 2 separate lists | Merged into Tool Constraints |

## New Additions

### 1. Prerequisites Section

```markdown
## Prerequisites

- **tesseract** system binary: `brew install tesseract` (macOS) / `apt install tesseract-ocr` (Linux)
- **Python packages**: `pip install pytesseract Pillow`
- **OCR script**: `scripts/ocr_attachment.py` (ships with this skill)
- **OWS MCP server**: configured and connected (for ticket queries + service invocation)
- If any prerequisite is missing, inform the user and stop.
```

### 2. Tool Mapping Table

```markdown
## Tool Mapping

This skill uses 6 abstract operations. Map them to your available tools:

| Abstract Operation | MCP (opencode/Claude Code) | Direct HTTP | No MCP (Cursor/Copilot) |
|---|---|---|---|
| Query ticket data | `query_model_data` | POST /adc-app-ops/.../tql/execute | Ask user to run TQL |
| Invoke OWS service | `invoke_service` | POST /adc-app-ops/.../service/test | Ask user to run |
| List attachments | `list_file_attachments` | GET /adc-file/.../file/list | Ask user |
| Download attachment | `download_file_attachment` | GET /adc-file/.../file/download | Ask user |
| Run OCR | `bash: python3 scripts/ocr_attachment.py <path>` | Same | Same |
| Dispatch subagent | `Agent` tool (if available) | N/A — sequential | N/A — sequential |
```

### 3. Tool Constraints Block (anti-file-creation guard)

```markdown
### Constraints — READ BEFORE EXECUTING

- **Use ONLY** `scripts/ocr_attachment.py` for OCR. Do NOT create, write,
  or generate any new Python/script files during execution.
- **Do NOT** use the Write tool to create helper scripts, text processors,
  date parsers, or any other code. All text matching, date comparison, and
  validation logic is done inline by the agent reading the OCR output.
- **Bash** is ONLY for: `mkdir -p tmp_attachments/<id>`,
  `rm -rf tmp_attachments`, and `python3 scripts/ocr_attachment.py <file>`.
- **Read** is ONLY for reading OCR text output if needed.
- If you find yourself wanting to write a script to "automate" a check — stop.
  Read the OCR text and do the check yourself. You are the text processor.
- **Never use Playwright/browser.**
```

### 4. Appendix A: Subagent Fan-Out (optional)

Moved from inline section to appendix. Core flow is sequential. The appendix provides:
- Capability detection ("If `Agent` tool is available and queue is 3+ tickets...")
- Chunking strategy (3-4 tickets per subagent)
- Brief template (compressed)
- Skip conditions (1-2 tickets, already a subagent, all hard-rejected)

## What Stays Identical (Logic Preserved)

- USER_EXTRA waterfall matching algorithm (triple → group+domain → group root → no match)
- All attachment validation checks:
  - Cert: ID match, validity, end date sanity
  - Spv: approver identity, approval text, requested account mentioned, date freshness
  - IOH: approver identity, approval text, requested account mentioned
- Staleness thresholds: extend_account=3 months, upgrade_account=product_duration from product_map
- TQL queue query (same SELECT fields, same WHERE clauses)
- invoke_service call shape for L1/L2 approval (same payload keys, same confirm=True)
- Human-like description format + 3 examples (APPROVE, REJECT missing, REJECT stale)
- Reject taxonomy (all 14 categories preserved)
- Field reference (all 24 fields preserved with same semantics)
- User confirmation gate before execution (step 8 — HARD GATE, no auto-execute)
- Clean-slate `rm -rf tmp_attachments` at start and end
- Multi-file attachment handling (OCR all, APPROVE if ANY matches)

## Token Expiry / Download Failure Policy (Updated)

- During Step 5 (Download required attachments), if the agent receives `File token timed out!`, a network/server HTTP error, or an invalid token error:
  1. The agent must immediately run a targeted TQL query to retrieve a fresh token for the ticket.
  2. Retry the download with the new token.
  3. **No-Reject Rule**: Under no circumstances should a token expiration or download failure result in a `REJECT` verdict. The ticket must instead be marked as `NEEDS_REVIEW — token expired after retry` or `NEEDS_REVIEW — attachment download failed`.
- This policy is single-sourced in Step 5 and referenced clearly in the Subagent Brief template (Appendix A) to ensure subagents also adhere to it.

## Execution Steps

1. Read current SKILL.md (already done — 574 lines)
2. Write new SKILL.md (~250 lines) with the structure above
3. Verify: line count ≤ 280, all validation logic preserved, all 14 reject categories present, all 24 fields in reference, tool constraints block present, tool mapping table present, prerequisites section present, appendix A present
4. Run `wc -l` to confirm target
5. Diff-check: grep for key phrases to ensure no logic was dropped:
   - `waterfall` (matching algorithm)
   - `product_duration` (staleness for upgrade)
   - `operation_mode_l1` / `operation_mode_l2` (execution payload)
   - `NEEDS_REVIEW` format definition
   - `Do NOT create` (anti-file-creation guard)
   - `tesseract` (prerequisite)

## Risk Mitigation

- **Risk**: Accidentally dropping a validation rule during compression.
  **Mitigation**: Single-source tables for all rules. After rewrite, grep for each reject category to confirm presence.
- **Risk**: Tool mapping table becomes stale if MCP tools change.
  **Mitigation**: Table is informational, not executable. MCP tool names are stable (wrapped in this repo).
- **Risk**: Anti-file-creation guard too aggressive — blocks legitimate `mkdir`.
  **Mitigation**: Constraint explicitly allows `mkdir` and `rm -rf tmp_attachments` in Bash.

## Out of Scope

- OCR script (`scripts/ocr_attachment.py`) — unchanged
- `~/.agents` copy — synced separately, not edited
- Other skills — not touched
- MCP server code — not touched
