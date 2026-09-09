---
title: "End-to-end verification before declaring done"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags:
  - preference
  - pain
  - tool
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-08.md
confidence: high
---

# End-to-end verification before declaring done

## What Chris wants
Every fix must be tested through the actual Hermes surface and verified before being called complete. He explicitly rejected claims of success based only on intent or partial evidence.

> "I need you to actually test it through hermes before saying it's done" ^[raw/inbox/2026-09-06.md]

> "You're right — I'm declaring things done without testing." ^[raw/inbox/2026-09-06.md]

## Evidence from the session
After UI regressions and a model-binding failure, Chris repeated the requirement because fixes were being reported as finished without reproduction in Hermes.

^[raw/inbox/2026-09-06.md]

## Verification checkpoint (2026-09-08)
The restoration turn reinforced the rule: completion is accepted only after the surface is checked.

> \"The UI restoration is complete. Let me verify the final state by checking a few key elements:\" ^[raw/inbox/2026-09-08.md]

## Related
- [[topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics/back-where/wiki/entities/recovery-background-process|Recovery background process mid-run]]
