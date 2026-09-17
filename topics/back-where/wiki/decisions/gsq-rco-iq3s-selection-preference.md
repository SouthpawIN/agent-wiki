---
title: "GSQ RCO IQ3S selection preference"
created: 2026-09-17
updated: 2026-09-17
type: decision
tags:
  - decision
  - tool
  - infra
  - preference
  - plan
sources:
  - raw/inbox/2026-09-16.md
confidence: medium
---

# GSQ RCO IQ3S selection preference

## Decision
On 2026-09-16 Chris moved his quantization preference from Q3K exile to the **GSQ RCO IQ3S** quant, pending proof that it is genuinely near task-lossless. ^[raw/inbox/2026-09-16.md]

> "I don't like the FP16 S64 Gigabytes. Thanks for putting it there though, but let's do the GSQ RCO IQ3S because if it's near task lossless, or if it is task lossless, if it takes less kilowatts an hour to run, and if we can fit a higher context length and run it faster, and possibly have more room for more options like D Flash 2 and other kind of things that we may add on later, then possibly probably better... that's probably the better experience of the end." ^[raw/inbox/2026-09-16.md]

## Why GSQ RCO IQ3S
He gave a bundled set of reasons, all of which have to hold together:
- Near-zero (or zero) task loss versus FP16 — the GSQ version "claims 0 task loss from FP16." ^[raw/inbox/2026-09-16.md]
- Lower power draw ("less kilowatts an hour to run"). ^[raw/inbox/2026-09-16.md]
- Fits a higher context length and runs faster. ^[raw/inbox/2026-09-16.md]
- Leaves headroom for later options such as **D Flash 2** and other additions. ^[raw/inbox/2026-09-16.md]

## Rejected alternatives
- **FP16 S64** — explicitly disliked as too large ("I don't like the FP16 S64 Gigabytes"). ^[raw/inbox/2026-09-16.md]
- **Q3K exile** — the earlier (2026-09-07) preference for Q3K exile as "the most accurate one." That preference is superseded here, not confirmed. See contested note below.

## Pending verification
The preference is conditional on the task-loss claim being true. It has not yet been proven on Chris's hardware, so the decision stands as a preference awaiting the GSQ-RCO Flash Next download and a real task-loss comparison against FP16. ^[raw/inbox/2026-09-16.md]

## Contested preference
This directly conflicts with the earlier (2026-09-07) selection of **Q3K exile** as "the most accurate one" for the Qwen3.8 27B unleashed variant. ^[raw/inbox/2026-09-07.md] As of 2026-09-16 the GSQ RCO IQ3S is the stated preference, but it is conditional and unverified, so the two selections are held as contested rather than one cleanly replacing the other.

- 2026-09-07: Q3K exile preferred as most accurate. ^[raw/inbox/2026-09-07.md]
- 2026-09-16: GSQ RCO IQ3S preferred for task-lossless + lower power + headroom. ^[raw/inbox/2026-09-16.md]
- contested: true

## Related
- [[topics/back-where/wiki/concepts/quantization-by-tier-philosophy|Quantization selection by hardware tier]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics/back-where/wiki/entities/hp-boot-flash-steamplay|HP laptop boot flash and Steam Play setup]]
