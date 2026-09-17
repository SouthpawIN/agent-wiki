---
title: ACE-Step
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, music, inference, apple-silicon]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# ACE-Step

Chris has ACE-Step downloaded locally (2.2 GB) and wants to "try to get it running." ^[raw/inbox/2026-09-07.md]

Quote: "ACE-Step is downloaded (2.2GB). Let me try to get it running." ^[raw/inbox/2026-09-07.md]

## Status
- Downloaded and available on this machine as of 2026-09-07 02:47. ^[raw/inbox/2026-09-07.md]
- Goal is operational, not just inspected: "try to get it running." ^[raw/inbox/2026-09-07.md]
- As of 2026-09-07, no successful run is recorded in the raw item; the adjacent Apple Silicon inference task dispatched later failed. ^[raw/inbox/2026-09-07.md]
- Treated as part of the local inference effort alongside the Apple Silicon M1 32GB benchmark sweep. ^[raw/inbox/2026-09-07.md]
- No engine, quant, or tok/s is recorded yet for ACE-Step. ^[raw/inbox/2026-09-07.md]
- ACE-Step is not part of the narrowed Bonsai vs Maple Colibri vs Ornith 1.5 35A3B comparison set as of 2026-09-07 10:37. ^[raw/inbox/2026-09-07.md]
- If tested, ACE-Step should follow the finalized benchmark protocol: warmup → 500-token short prompt → 100-token 5K prompt, then report tok/s for each. ^[raw/inbox/2026-09-07.md]

## Links
- [[topics-wiki/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[topics-wiki/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics-wiki/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
- [[topics-wiki/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
