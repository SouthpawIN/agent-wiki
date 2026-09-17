---
title: "Quantization selection by hardware tier"
created: 2026-09-17
updated: 2026-09-17
type: concept
tags:
  - preference
  - idea
  - tool
  - infra
sources:
  - raw/inbox/2026-09-16.md
confidence: high
---

# Quantization selection by hardware tier

## The philosophy
On 2026-09-16 Chris laid out a tier-based rule for choosing quantization: there is no single best quant, only the optimal quant *for each hardware tier*. The job is to "figure the optimal quant and model for each hardware tier" rather than optimize one configuration in the abstract. ^[raw/inbox/2026-09-16.md]

## Q2 is too broken
His floor is clear: a Q2 quant is not worth it, because it is "too broken to be as accurate as a smaller model's full precision." In other words, a smaller model at full precision beats a bigger model at Q2. Accuracy-per-watt, not raw parameter count, is the yardstick. ^[raw/inbox/2026-09-16.md]

## The 27B is the middle swatch
Chris placed the 27B family as the broad middle band of the quant spectrum, running "from Q3 to FP16." The useful quant for a 27B therefore sits somewhere in that Q3→FP16 range, chosen by how much accuracy is lost per unit of power and memory saved. ^[raw/inbox/2026-09-16.md]

## The GSQ preference (task-lossless wins)
The deciding factor he named is power efficiency when accuracy is preserved: the GSQ version of the model "claims 0 task loss from FP16, and if that is at least close to the case, it would be preferred bc it does effectively the same job at a lower power requirement." ^[raw/inbox/2026-09-16.md] So a quant that matches FP16 output while drawing less power is the preferred choice — the task-lossless-at-lower-power point is the target. ^[raw/inbox/2026-09-16.md]

## Related
- [[wiki-topics/back-where/wiki/decisions/gsq-rco-iq3s-selection-preference|GSQ RCO IQ3S selection preference]]
- [[wiki-topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[wiki-topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[wiki-topics/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]]
- [[wiki-topics/back-where/wiki/decisions/131k-audition-rejection|131K audition rejection and speed target]]
