---
title: Nail Qwen 3.6 35B UD Q4_K_XL
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Nail Qwen 3.6 35B UD Q4_K_XL

`Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf` (~20.82 GB) and its `mmproj-F16.gguf` (~858 MB) were downloaded to `~/Models/storage/nail/` for testing. This is a MoE architecture model (3B active params per token).

## Benchmark Results (M1 MacBook 32GB)

|| Model | Type | Context | Warmup | Short | 5K | Status |
||-------|------|---------|--------|-------|-----|--------|
|| **Nail Q4_K_XL** | MoE 35B | 32K | ~3s | **23.4 tok/s** | **4.7 tok/s** | Winner |

## Key Findings

- **Best measured at 32K**: 23.4 tok/s short-context, 4.7 tok/s at 5K prompt.
- **Long-context status**: deferred from 131K testing because 20.8 GB weights plus ~8 GB KV at full window exceeds stable 32 GB fit before benchmark ^[raw/inbox/2026-09-07.md].
- **MoE advantage**: only 3B active params per token keeps memory footprint lower than dense 27B rivals, but it is not enough for 131K on this box.

## Why It Won

`Nail` and `Tiel-Coder` are both MoE 35B models with 3B active parameters, making them far more memory-efficient than dense 27B models like Dirk. Combined with the Q4_K_XL quantization, Nail achieved the best balance of speed and stability on this hardware.

## Vision Support

The `mmproj-F16.gguf` file (858 MB) provides vision capability. Test verification:
```
- Nail-Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf: 22,360,465,312 bytes (20.82 GB)
- mmproj-F16.gguf: 899,283,680 bytes (858 MB)
```

## Related

- [[apple-silicon-runtime-benchmark|Speed Test Results]]
- [[candidate-quant-preference|Candidate Quant Preference]]
- [[ornith-35b-mlx|Ornith 35B MLX]]