---
title: MPTX Context Overcommit
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [pain, hardware, memory]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MPTX Context Overcommit

On the 32 GB Mac, `mtplx serve` with `--context-window 131072` loads the model in 6-9s and installs the native MTP draft head, but the printed memory plan marks `OVERCOMMITTED` and warns that the requested context exceeds the machine fit.

## Memory Plan Evidence

From the memory plan output:
```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED), session bank up to 1.7G (yields to 1.0G under long-context load)
Memory plan: requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB; expect cache shedding and, past the fit, swap
```

## Why It Fails

```
Total needed:
- Model weights: 19.3 GB (MTPLX 27B Optimized Speed)
- KV cache @ 131K q8: 8.0 GB
- macOS + Hermes: ~8 GB
- Total: ~35.3 GB > 32 GB available
```

## Observed Failures

1. **OOM during load**: `RuntimeError: [METAL] Command buffer execution failed: Insufficient Memory`
2. **Insufficient Storage**: During 5K+ prompt generation at 131K context
3. **End-to-end slowdown**: 0.39 tok/s observed for 2005-token history

## Stable Alternative

65K context works stably:
- Memory after model: 24.0 GB budget
- KV cache @ 65K q8: ~4 GB
- Fits within 32 GB Mac memory

## Related

- [[mplx|MPLX]]
- [[mtplx-qwen-38-27b-optimized-speed|MPLX Qwen 3.8 27B Optimized Speed]]
- [[mtplx-memory-guard|MPLX Memory Guard]]