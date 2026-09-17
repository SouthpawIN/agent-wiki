---
title: "anser"
created: 2026-09-06
updated: 2026-09-07
type: entity
tags: [bot, tool, idea]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07-from-senter.md]
confidence: low
contested: false
---

# anser

**anser** = "Hermes Agent tech support moderator for the Nous Research Discord" (BRIEF.md, Chris's line — never rewritten). ^[raw/inbox/2026-09-06.md]

## What is known so far
- Topic wiki initialized 2026-09-05; first raw filing arrived 2026-09-06 (log.md).
- The 2026-09-06 filing is a **hermes-sourced** support line (watcher, sim 0.07), not a direct Chris quote: a local model too slow to compress a 387k context, fixed by routing compression to Nous, mid end-to-end verification. See [[topics-wiki/anser/wiki/concepts/local-model-compression|Local-model context compression → route to Nous]]. ^[raw/inbox/2026-09-06.md]
- No Chris quotes about anser are recorded in the wiki yet; role, scope and anti-scope come from BRIEF.md.

## Open questions
- Was the 09-06 compression case actually handled by/for anser in the Discord, or a borderline misroute (sim 0.07)?
- What "done" looks like for anser as moderator — response SLAs, escalation to the Hermes team, PR ledger handoff?

## Known routing behavior
- Watcher filings for `anser` are dominated by Hermes infrastructure signals; those are treated as support evidence, not direct moderation activity. ^[raw/inbox/2026-09-06.md, raw/inbox/2026-09-07-from-senter.md]

## Links
- [[topics-wiki/anser/wiki/entities/anser-workflow|anser workflow — Discord moderation patterns]]
- [[topics-wiki/anser/wiki/concepts/local-model-compression|Local-model context compression → route to Nous]]
- [[topics-wiki/anser/wiki/concepts/native-map-architecture-update|Native-map architecture update — 2026-09-07]]
