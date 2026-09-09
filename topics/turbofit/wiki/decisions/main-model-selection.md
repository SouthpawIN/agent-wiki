---
title: Main Model Selection
created: 2026-09-06
updated: 2026-09-07
type: decision
tags: [decision, model, preference, pain]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Main Model Selection

## What

Initial decision: Main inference and vision is Unleashed 27B + DFlash2 draft on `127.0.0.1:11606`, Metal, 131k context ^[raw/inbox/2026-09-06.md].

Updated 2026-09-07 after benchmark sweep: **Ornith MLX 4-bit** is the recommended main provider for daily driver use.

## Why

Chris wants local fast-lane inference with vision capability. Unleashed holds the vision projector, so vision cannot be split from it ^[raw/inbox/2026-09-06.md].

However, benchmark evidence shows:
- **Ornith MLX 4-bit**: 28.5 tok/s short, 5.7 tok/s at 5K, MoE 35B (much faster)
- **Unleashed + DFlash2**: ~5 tok/s stable at 131K, but only when DFlash2 integrates correctly
- **Dirk Q3_K_XL**: 6.0 tok/s at 32K, OOM above

## Contested Evidence

Hermes summary later claimed MTPLX is the locked main provider on `:11613`, while command evidence showed repeated 131K overcommit warnings and `-9` exits ^[raw/inbox/2026-09-07.md].

Multiple provider switches occurred during the session:
1. MTPLX Qwen 3.8 Optimized Speed locked in at 65K (unstable at 131K)
2. Reverted to Unleashed+DFlash2 after MTPLX crashes
3. Final recommendation: Ornith MLX 4-bit as primary

## Final Recommendation

**Lock in Ornith MLX 4-bit** as main provider at 65K context:
- Speed: 28.5 tok/s short-context
- Stability: No OOM at 65K
- Fallback: Unleashed + DFlash2 at 131K for long-context needs

## Related

- [[topics/turbofit/wiki/entities/unleashed-27b.md|Unleashed 27B]]
- [[topics/turbofit/wiki/entities/ornith-35b-mlx.md|Ornith 35B MLX]]
- [[topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[topics/turbofit/wiki/entities/mtplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B]]
- [[topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]