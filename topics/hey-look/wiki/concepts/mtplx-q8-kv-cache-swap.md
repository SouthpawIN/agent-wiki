---
title: q8 KV cache + swap
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [mtplx, mac, context, memory, qwen, hardware]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# q8 KV cache + swap

A configuration path observed on 2026-09-07 that changed the operating envelope for 131K context on the 32GB Mac.^[raw/inbox/2026-09-07.md]

## Observed behavior

- With `--paged-kv-quantization q8 --allow-swap`, 131K context became stable for small/medium prompts without OOM.^[raw/inbox/2026-09-07.md]
- KV cache memory dropped from ~8GB at 131K to ~4GB, allowing 19.3GB weights + ~4GB KV to stay closer to the 24GB engine budget.^[raw/inbox/2026-09-07.md]
- Measured results on the q8 path: 6.9 tok/s on a 35-token prompt/800-token generation, and 0.6 tok/s on a 5K prompt/100-token generation.^[raw/inbox/2026-09-07.md]

## Why it matters

This is the first observed non-OOM path for 131K on this hardware, but speed is materially lower than 65K. It reframes the operating-mode decision: 131K is possible, but not at the same throughput as 65K.^[raw/inbox/2026-09-07.md]

## Related

- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]