---
title: "Restoration and billing"
created: 2026-09-06
updated: 2026-09-06
type: query
tags:
  - question
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
confidence: medium
---

# Restoration and billing

## Open questions
1. Where did the $2,000 credit payment go in Portal billing, and why is TTS still unavailable?
2. Which model is treated as the current backup model, and what triggers automatic fallback?
3. What exact change caused the UI to push from centered to flush right after showing diffs?
4. What batch-size or prefill-capacity change is needed so the chosen model can load at Q3 with 262k contacts and D flash 2 without falling back due to prefill timeout?

## Why these matter
Chris wants the UI and model behavior restored to the pre-diff state; billing verification is tied to restoring TTS. These questions are unresolved and should be answered before declaring the regression closed. Question 4 surfaced from the same session after the initial UI repair failed: Chris does not want silent model swaps when prefill is the actual bottleneck.

## Related
- [[topics/back-where/wiki/entities/ui-layout-regression|UI layout regression after diff view change]]
- [[topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics/back-where/wiki/concepts/tts-credit-outage|TTS failure during credit outage]]
