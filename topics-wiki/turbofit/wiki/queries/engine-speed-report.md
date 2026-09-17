---
title: Engine Speed Report
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, benchmark, report]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Engine Speed Report

This is the live result surface of Chris's research request for Apple Silicon engine speed testing.

## Winner: Ornith MLX 4-bit

**Selected as primary provider** on 2026-09-07 after comprehensive testing.

## Performance Summary

|| Model | Type | Context | Short | 5K | Status |
||-------|------|---------|-------|-----|--------|
|| **Ornith MLX 4-bit** | MoE 35B | **131K** | **28.5 tok/s** | **5.7 tok/s** | ✅ Winner |
|| MTPLX Optimized Speed | 27B | 65K | 8-12 tok/s | - | - |
|| Nail Q4_K_XL | MoE 35B | 32K | 23.4 tok/s | 4.7 tok/s | ⚠️ Not fit at 131K |
|| Tiel-Coder Q4_K_XL | MoE 35B | 65K | 23.1 tok/s | 4.2 tok/s | ⚠️ Not fit at 131K |
|| Dirk Q3_K_XL | Dense 27B | 32K | 6.0 tok/s | 0.8 tok/s | ⚠️ OOM above 32K |

^[raw/inbox/2026-09-07.md]

## Contested promotion

Ornith is configured as default at 131K, but Hermes `custom:turbofit` showed persistent `Connection error` timeouts (code: timeout, 2026-09-07T19:26:47) after the 14:25 config change. A Hermes session restart is required to clear stale connection state before the promotion can be considered verified live.

## Why Ornith Won

1. **Only model at 131K**: Ornith is the only candidate that actually works at 131K context
2. **Best short-context speed**: 28.5 tok/s beats all competitors
3. **MoE efficiency**: 35B total params, 3B active per token = fast and memory-efficient
4. **MLX backend**: Native Metal acceleration on Apple Silicon

## The Hardware Reality

> "10+ tok/s at 131K is not happening on M1 32GB with a 27B model. It's like asking a Honda Civic to go 200mph."

The M1 32GB simply cannot hold:
- 19.3 GB model weights (MTPLX)
- 8 GB KV cache at 131K
- 8 GB macOS + Hermes

**Total: ~35 GB needed > 32 GB available**

## Final Recommendations

| Use Case | Model | Context | Speed |
|----------|-------|---------|-------|
| Daily driver (short/medium) | **Ornith MLX** | 131K | 28.5 tok/s short |
| Long-context heavy | Unleashed+DFlash2 | 131K | ~5 tok/s stable |
| Storage-constrained | Nail | 32K | 23.4 tok/s |

## Active Configuration

```yaml
model:
  default: ornith-1-5-35a3b-mlx
  provider: custom:turbofit
providers:
  turbofit:
    api: http://127.0.0.1:11613/v1
    default_model: ornith-1-5-35a3b-mlx
```

## Related

- [[topics-wiki/turbofit/wiki/queries/apple-silicon-runtime-benchmark.md|APL_Silicon Runtime Benchmark]]
- [[topics-wiki/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics-wiki/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]