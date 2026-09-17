---
title: "UI restoration verification check (2026-09-08)"
created: 2026-09-08
updated: 2026-09-08
type: entity
tags:
  - ui
  - preference
  - pain
sources:
  - raw/inbox/2026-09-08.md
raw_context:
  The 2026-09-08.md raw item is a compaction/summary handoff (lines 7-9, 15-16, 26-27) containing a repeated system instruction telling Hermes to \"Respond ONLY to the latest user message that appears AFTER this summary\" plus Hermes working prose. The Hermes lines at 09:14 and 09:41 are working notes, not Chris utterances. The single Chris-relevant signal is the restoration completion claim quoted on line 38.
confidence: high
---

# UI restoration verification check (2026-09-08)

## Restoration claim
A later session turn reported UI restoration complete and moved into verification.

> "The UI restoration is complete. Let me verify the final state by checking a few key elements:" ^[raw/inbox/2026-09-08.md]

## Active rule
This is not a new regression; it is the same pattern Chris enforced earlier: completion claims are accepted only after the actual Hermes surface is checked, not inferred from internal work alone.

> "I need you to actually test it through hermes before saying it's done" ^[raw/inbox/2026-09-06.md]

## Related
- [[wiki-topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[wiki-topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[wiki-topics/back-where/wiki/entities/token-startup-race|Token startup race condition]]
- [[wiki-topics/back-where/wiki/entities/compaction-handoff-repetition|Context compaction handoff repetition (2026-09-09)]]
- [[wiki-topics/back-where/wiki/decisions/completion-criterion-explicit-statement|Explicit completion and block criterion]]
