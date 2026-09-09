---
title: Tiel Coder
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, inference, apple-silicon, testing]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Tiel Coder

At 2026-09-07 08:17, Chris added Tiel Coder to the Apple Silicon inference benchmark sweep. ^[raw/inbox/2026-09-07.md]

Quote: "Try Tiel Coder and Dirk 27B as well." ^[raw/inbox/2026-09-07.md]

## Target settings
- Quant: Q4 K XL. ^[raw/inbox/2026-09-07.md]
- Version: latest available Tiel Coder. ^[raw/inbox/2026-09-07.md]
- Quote: "Q4 K XL for Tiel Coder and that Q3 I mentioned for Dirk. Make sure to grab Dirk 3.8 27B with the MTP, test with and without, and grab the latest Tiel Coder." ^[raw/inbox/2026-09-07.md]

## Status
- Added as a benchmark candidate after the initial Qwen 3.8 27B sweep failed. ^[raw/inbox/2026-09-07.md]
- Tested as of 2026-09-07 09:21–09:22. ^[raw/inbox/2026-09-07.md]
- Quote: "Tiel-Coder: 22.1 tok/s short, 3.9 tok/s 5K." ^[raw/inbox/2026-09-07.md]
- Quote: "Tiel-Coder at 65K: 23.1 tok/s short, 4.2 tok/s 5K." ^[raw/inbox/2026-09-07.md]
- Command/model ID not yet recorded. ^[raw/inbox/2026-09-07.md]
- Covered by the warmup-before-tok/s measurement rule. ^[raw/inbox/2026-09-07.md]

## Links
- [[topics/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[topics/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
