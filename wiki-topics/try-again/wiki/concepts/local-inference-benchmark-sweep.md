---
title: Local Inference Benchmark Sweep
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [inference, apple-silicon, qwen, benchmark, research, decision]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: medium
---

# Local Inference Benchmark Sweep

As of 2026-09-07, Chris is running a local inference benchmark sweep on Apple Silicon M1 32GB with the goal of making larger models runnable locally at maximum speed. ^[raw/inbox/2026-09-07.md]

Earlier, on 2026-09-06, Chris framed the same need as: "Try a different inference engine — part of turbofit is to try out different inference engines... expand out and make this model work on this computer." ^[raw/inbox/2026-09-06.md]

## Scope and requirements
- Primary request: "Research ALL possible ways to run Qwen 3.8 27B on Apple Silicon M1 32GB at 131K context with maximum speed. Find FreeToken, OMLX, MLX, and any other backends. Report specific model IDs, commands, and expected tok/s for each approach." ^[raw/inbox/2026-09-07.md]
- Required reporting: "Report tok/s for each test." ^[raw/inbox/2026-09-07.md]
- Measurement rule: every model must complete a warmup prompt before measuring tok/s. ^[raw/inbox/2026-09-07.md]

## Dispatch record
- Dispatched at 2026-09-07 03:06:01 as a leaf-role task. ^[raw/inbox/2026-09-07.md]
- Task: research and test all available Apple Silicon inference engines for Qwen 3.8 27B to find the fastest configuration. ^[raw/inbox/2026-09-07.md]
- Duration: 3400.47s. ^[raw/inbox/2026-09-07.md]
- Result: failed. ^[raw/inbox/2026-09-07.md]

## Finalized protocol
- Ordered steps: warmup, short prompt, 5K prompt. ^[raw/inbox/2026-09-07.md]
- Prompt sizes: 500-token short prompt, 100-token 5K prompt. ^[raw/inbox/2026-09-07.md]
- Cleanup: clear the previously loaded model before switching candidates. ^[raw/inbox/2026-09-07.md]
- Quote: "Run warmup, then short prompt (500 tokens), then 5K prompt (100 tokens). Report tok/s for each." ^[raw/inbox/2026-09-07.md]
- Quote: "Make sure to clear the old model off before testing the new one." ^[raw/inbox/2026-09-07.md]

## Candidate evolution
- Initial candidates included Qwen 3.8 27B, Tiel Coder, and Dirk 27B. ^[raw/inbox/2026-09-07.md]
- Active candidates as of 2026-09-07 10:37: Bonsai, Maple Colibri, and Ornith 1.5 35A3B. ^[raw/inbox/2026-09-07.md]
- ACE-Step remains a separate run target, not part of this benchmark comparison. ^[raw/inbox/2026-09-07.md]

## Partial results
- Tiel Coder: 22.1 tok/s short and 3.9 tok/s 5K at an earlier context; 23.1 tok/s short and 4.2 tok/s 5K at 65K. ^[raw/inbox/2026-09-07.md]
- Dirk 27B: 6.0 tok/s short and 0.8 tok/s 5K at 32K after OOMs at higher contexts. ^[raw/inbox/2026-09-07.md]
- No finalized Bonsai, Colibri, or Ornith numbers are recorded yet under the latest protocol. ^[raw/inbox/2026-09-07.md]

## Operational status
- A 2026-09-07 task intended to run the finalized protocol was interrupted after 1944.94s with 50 API calls. ^[raw/inbox/2026-09-07.md]
- System-side config edits were blocked; Hermes working notes suggest using Hermes/write_file-based paths instead. ^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/try-again/wiki/entities/ace-step|ACE-Step]]
- [[wiki-topics/try-again/wiki/entities/qwen-3-8-27b|Qwen 3.8 27B]]
- [[wiki-topics/try-again/wiki/entities/tiel-coder|Tiel Coder]]
- [[wiki-topics/try-again/wiki/entities/dirk-27b|Dirk 27B]]
- [[wiki-topics/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[wiki-topics/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[wiki-topics/try-again/wiki/decisions/benchmark-protocol|Benchmark Protocol]]
- [[wiki-topics/try-again/wiki/comparisons/2026-09-07-candidate-narrowing|2026-09-07 Candidate Narrowing]]
