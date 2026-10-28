---
title: Tiel Coder
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Tiel Coder

Tiel-Coder is a queued local GGUF candidate. The primary MLX download in `~/Models/storage/tiel-coder/` remained incomplete (~15 GB of ~19 GB), and a GGUF test path at `~/Models/storage/tiel-coder-gguf/Tiel-Coder-35B-A3B-UD-Q4_K_XL.gguf` was launched at 131K but not benchmarked before the session ended.

## Status

- MLX download incomplete (15 GB of 19 GB)
- GGUF Q4_K_XL version tested and working at 65K
- Benchmarked: 65K context, 23.1 tok/s short, 4.2 tok/s at 5K
- 131K benchmark deferred due to OOM expectation (22 GB + 8 GB KV)

## Benchmark Results

|| Model | Type | Context | Short | 5K | Status |
||-------|------|---------|-------|-----|--------|
|| **Tiel-Coder Q4_K_XL** | MoE 35B | 65K | **23.1 tok/s** | 4.2 tok/s | Viable |

## MoE Advantage

Tiel-Coder is MoE 35B with 3B active params, making it memory-efficient and fast. Similar to Nail and Ornith.

## Download Status

The tiel-coder background process completed successfully:
```
all downloads complete
```
Files available at:
- `~/Models/storage/tiel-coder/` (MLX, incomplete)
- `~/Models/storage/tiel-coder-gguf/` (GGUF Q4_K_XL, 22.16 GB)

## Related

- [[apple-silicon-runtime-benchmark|Speed Test Results]]
- [[ornith-35b-mlx|Ornith 35B MLX]]
- [[nail-qwen36-35b|Nail Qwen 3.6 35B UD Q4_K_XL]]
- [[context-window-decision|Context Window Decision]]