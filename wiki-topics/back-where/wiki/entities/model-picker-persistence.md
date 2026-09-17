---
title: "Model picker persistence until fallback"
created: 2026-09-06
updated: 2026-09-06
type: entity
tags:
  - preference
  - tool
sources:
  - raw/inbox/2026-09-06.md
confidence: high
---

# Model picker persistence until fallback

## Preference
Chris expects a model chosen from the model picker to remain active until it needs to fall back. Selecting a model is treated as a durable binding, not a transient suggestion.

> "If I pick a model from The model picker that it should stay with that model until it needs to fall back." ^[raw/inbox/2026-09-06.md]

## Evidence of degradation
A "backup model" was loaded instead of the intended choice, which he interpreted as the system reverting without cause.

> "No, that's still not the right one. That one's like the backup model. You need to try harder to get it back." ^[raw/inbox/2026-09-06.md]

> "Go through this session. Try hard to get it back. You were being way too casual about the big fuck up you just did." ^[raw/inbox/2026-09-06.md]

## Technical evidence
The session log identified that `stepfun/step-3.7-flash` was being supplied from a fallback list rather than the user's explicit pick. Runtime metadata also showed repeated model switches during the session, which Chris treated as further evidence of unstable binding.

^[raw/inbox/2026-09-06-from-klerik.md]

## Related
- [[wiki-topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[wiki-topics/back-where/wiki/queries/restoration-and-billing|Restoration and billing]]
