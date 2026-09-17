---
title: "GSQ RCO IQ3S picked and Bonsai MLX snapshot pending"
created: 2026-09-17
updated: 2026-09-17
type: entity
tags:
  - tool
  - infra
  - plan
  - pain
sources:
  - raw/inbox/2026-09-16.md
confidence: high
---

# GSQ RCO IQ3S picked and Bonsai MLX snapshot pending

## The GSQ RCO IQ3S pick
On 2026-09-16 Chris selected the **GSQ RCO IQ3S** as the working quant, displacing the earlier Q3K exile preference. His reasoning bundled accuracy, power, context length, speed, and future headroom: ^[raw/inbox/2026-09-16.md]

> "I don't like the FP16 S64 Gigabytes. Thanks for putting it there though, but let's do the GSQ RCO IQ3S because if it's near task lossless, or if it is task lossless, if it takes less kilowatts an hour to run, and if we can fit a higher context length and run it faster, and possibly have more room for more options like D Flash 2 and other kind of things that we may add on later, then possibly probably better... that's probably the better experience of the end." ^[raw/inbox/2026-09-16.md]

## The download gap
Hermes's first download on 2026-09-16 only fetched the **vision projector** — the model weights themselves were not included. Hermes then started the actual model download at 20:17. ^[raw/inbox/2026-09-16.md] This is the same class of incomplete-download problem seen earlier (2026-09-07) and must be verified complete before the GSQ config can be tested. ^[raw/inbox/2026-09-16.md]

## Five focused subagents
While the GSQ-RCO Flash Next download ran, Hermes reported **five focused subagents** still researching their respective models. The plan on Hermes's side: verify the download completes, then proceed. ^[raw/inbox/2026-09-16.md] The subagents' findings are not yet in the raw item, so their results are pending. ^[raw/inbox/2026-09-16.md]

## Bonsai MLX snapshot still pending
The compacted Historical Task Snapshot on 2026-09-16 shows an in-flight request to organize the end of a section "with how we're doing it, such as **Bonsai MLX**." ^[raw/inbox/2026-09-16.md] That work was not completed in the raw item — it is a dangling follow-up that should be checked for on-disk state before being resumed. ^[raw/inbox/2026-09-16.md] This mirrors the recurring interrupted-turn pattern (see [[topics-wiki/back-where/wiki/entities/interrupted-calibri-bonsai-request|Interrupted Calibri and Bonsai request]]).

## Why it matters
The concrete quant is now named (GSQ RCO IQ3S) but the supporting download is incomplete and the Bonsai MLX organization task is still open. Per the recovery pattern, on-disk state should be verified before redoing either. ^[raw/inbox/2026-09-16.md]

## Related
- [[topics-wiki/back-where/wiki/decisions/gsq-rco-iq3s-selection-preference|GSQ RCO IQ3S selection preference]]
- [[topics-wiki/back-where/wiki/concepts/quantization-by-tier-philosophy|Quantization selection by hardware tier]]
- [[topics-wiki/back-where/wiki/entities/interrupted-calibri-bonsai-request|Interrupted Calibri and Bonsai request]]
- [[topics-wiki/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics-wiki/back-where/wiki/queries/download-completion-verification|20.8GB download completion and loadability verification]]
