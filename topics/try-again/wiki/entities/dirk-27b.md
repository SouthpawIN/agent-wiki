---
title: Dirk 27B
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, inference, apple-silicon, testing]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Dirk 27B

At 2026-09-07 08:17, Chris added Dirk 27B to the Apple Silicon inference benchmark sweep. ^[raw/inbox/2026-09-07.md]

Quote: "Try Tiel Coder and Dirk 27B as well." ^[raw/inbox/2026-09-07.md]

## Target settings
- Quant: Q3. ^[raw/inbox/2026-09-07.md]
- Model variant: Dirk 3.8 27B with MTP, tested with and without. ^[raw/inbox/2026-09-07.md]
- Quote: "Q4 K XL for Tiel Coder and that Q3 I mentioned for Dirk. Make sure to grab Dirk 3.8 27B with the MTP, test with and without, and grab the latest Tiel Coder." ^[raw/inbox/2026-09-07.md]

## Status
- Added as a benchmark candidate after the initial Qwen 3.8 27B sweep failed. ^[raw/inbox/2026-09-07.md]
- Downloads complete as of 2026-09-07 09:26, but server was still loading the model (13 GB). ^[raw/inbox/2026-09-07.md]
- OOMs at 131K context. ^[raw/inbox/2026-09-07.md]
- Retried at 65K context after OOM, then restarted at 32K. ^[raw/inbox/2026-09-07.md]
- Result at 32K: 6.0 tok/s short, 0.8 tok/s 5K. ^[raw/inbox/2026-09-07.md]
- Dirk command/model ID not yet recorded. ^[raw/inbox/2026-09-07.md]
- Covered by the warmup-before-tok/s measurement rule. ^[raw/inbox/2026-09-07.md]

## Links
- [[topics/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[topics/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
