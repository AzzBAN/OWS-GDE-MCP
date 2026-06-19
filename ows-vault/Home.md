---
tags: [moc]
---
# OWS / ADC Knowledge Vault

A shared, evolving knowledge base for the **OWS Studio / ADC low-code platform**
(`teleows.com`). Two layers:

- **Findings** (`00 Findings/`) — hand-curated, production-confirmed notes.
  Short and high-signal. **Read these first** — they exist to save you a dive
  into the 3.6k-page reference corpus. Git-tracked; everyone contributes.
- **Reference** (`Reference/`) — the full OWS Studio help corpus, imported
  verbatim from the scraped vault (Obsidian-navigable, `[[wikilinks]]` intact).
  Auto-generated and gitignored — regenerate with the importer (see below).

## 00 Findings
<!-- Add a bullet here when you add a note under "00 Findings/". -->
- [[OWS Platform Findings]] — running list of platform gotchas confirmed in practice

## Reference corpus
- Root: `Reference/Low-Code Orchestration/` — User Guide, App Development,
  API Reference, Development Specifications, Release & Verification, FAQs.
- Don't hand-edit anything under `Reference/`; it's overwritten on re-import.

## How to use this vault (for agents)
1. Call `get_help_home` (this file) to orient.
2. Call `search_help("<topic>")` — **findings rank above the reference corpus**,
   so a curated note short-circuits the full-text search.
3. Read a hit with `get_help_topic(<id or local path>)`. Findings are readable
   by path too, e.g. `get_help_topic("00 Findings/OWS Platform Findings.md")`.

## How to contribute a finding (for humans)
1. Add a `.md` file under `00 Findings/` (one topic per file, like the
   `cpq/vault/02 Platform Findings` notes — title as `# Heading`, terse,
   production-confirmed).
2. Add a bullet under **00 Findings** above so it's linked from the MOC.
3. Commit it. No re-import needed — `search_help` reads findings live.

## Regenerating the Reference corpus
```
uv run python scripts/import_help_corpus.py \
    --vault ~/codes/huaweed/knowledge-helper/vault --lang en_US
```
This rewrites `Reference/` + `docs/help/index/en_US/` only; `Home.md` and
`00 Findings/` are never touched.
