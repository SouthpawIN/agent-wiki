---
title: Warmup Before Speed Test
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, testing, inference, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Warmup Before Speed Test

On 2026-09-07 at 08:17, Chris directed that every model must complete a warmup prompt before measuring tok/s. ^[raw/inbox/2026-09-07.md]

Quote: "Remember to let each model do a warmup prompt and then test their speed while it's warm" ^[raw/inbox/2026-09-07.md]

## Rationale
Warm runs better represent steady-state throughput on Apple Silicon, where cold-start compilation, memory compaction, and Metal cache effects can skew early measurements. ^[raw/inbox/2026-09-07.md]

## Applied to
- Qwen 3.8 27B engine sweep. ^[raw/inbox/2026-09-07.md]
- Tiel Coder. ^[raw/inbox/2026-09-07.md]
- Dirk 27B. ^[raw/inbox/2026-09-07.md]
- ACE-Step if it is tested. ^[raw/inbox/2026-09-07.md]

## Links
- [[wiki-topics/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[wiki-topics/try-again/wiki/entities/tiel-coder|Tiel Coder]]
- [[wiki-topics/try-again/wiki/entities/dirk-27b|Dirk 27B]]
- [[wiki-topics/try-again/wiki/entities/ace-step|ACE-Step]]
