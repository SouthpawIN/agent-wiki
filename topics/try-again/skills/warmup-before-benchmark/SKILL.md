---
name: warmup-before-benchmark
description: Use when benchmarking local inference on Apple Silicon. Run a warmup prompt before measuring tok/s.
version: 0.1.0
distilled: 2026-09-07 08:40
topic: try-again
---
# warmup-before-benchmark
## Warmup-Before-Benchmark Skill

### When to use
- Any tok/s test on Apple Silicon local inference.
- Applies to Qwen 3.8 27B, Tiel Coder, Dirk 27B, ACE-Step, or any future model in the sweep.

### Steps
1. Load the exact target model and quant intended for measurement.
2. Run a warmup prompt first; do not record tok/s from this pass.
3. Run the benchmark prompt after warmup completes.
4. Record tok/s from the post-warmup pass only.
5. Report per-test: model ID, quant, engine, warmup used, tok/s.

### Pitfalls
- Do not use cold-start tok/s; Metal compilation and memory compaction skew early numbers.
- For Dirk 27B, test with MTP enabled and disabled as separate cases.
- Use the latest available artifact for Tiel Coder.

## Evidence
> "Remember to let each model do a warmup prompt and then test their speed while it's warm"
> "Report tok/s for each test."
