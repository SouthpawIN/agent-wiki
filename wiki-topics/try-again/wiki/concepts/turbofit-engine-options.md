---
title: Turbofit Engine Options
created: 2026-09-06
updated: 2026-09-07
type: concept
tags: [preference, idea, plan, tool, inference]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: medium
---

# Turbofit Engine Options

- Chris said part of Turbofit is trying different inference engines, and he wants them expanded to make the current model work on this computer as the auxiliary model. ^[raw/inbox/2026-09-06.md]
- Quote, 2026-09-06: "Try a different inference engine — part of turbofit is to try out different inference engines... expand out and make this model work on this computer. You absolutely can I gave you no limitations. I said put it as the auxiliary model." ^[raw/inbox/2026-09-06.md]

This implies more is possible than the currently offered configuration; no specific engine was named in the raw input. ^[raw/inbox/2026-09-06.md]

## Evolution, 2026-09-07
- The goal sharpened into a full Apple Silicon M1 32GB sweep for local inference, with named targets: Qwen 3.8 27B, Tiel Coder, and Dirk 27B. ^[raw/inbox/2026-09-07.md]
- Active target set later narrowed to Bonsai, Maple Colibri, and Ornith 1.5 35A3B. ^[raw/inbox/2026-09-07.md]
- The sweep requires warmup before tok/s measurement. ^[raw/inbox/2026-09-07.md]
- Tiel Coder target quant is Q4 K XL; Dirk 27B target quant is Q3 with MTP tested both enabled and disabled. ^[raw/inbox/2026-09-07.md]
- Chris wants per-engine reporting: specific model IDs, commands, and tok/s. ^[raw/inbox/2026-09-07.md]
- Operational blocker: system config edits were blocked; Hermes notes indicate using Hermes command/write_file paths instead. ^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/try-again/wiki/concepts/restore-retry|Restore / Retry]]
- [[wiki-topics/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[wiki-topics/try-again/wiki/entities/qwen-3-8-27b|Qwen 3.8 27B]]
- [[wiki-topics/try-again/wiki/entities/tiel-coder|Tiel Coder]]
- [[wiki-topics/try-again/wiki/entities/dirk-27b|Dirk 27B]]
- [[wiki-topics/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
- [[wiki-topics/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
- [[wiki-topics/try-again/wiki/comparisons/2026-09-07-candidate-narrowing|2026-09-07 Candidate Narrowing]]
