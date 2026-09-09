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
- [[topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
- [[topics/back-where/wiki/entities/token-startup-race|Token startup race condition]]
