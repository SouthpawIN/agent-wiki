---
title: Unleashed Backup
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, model, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Unleashed Backup

## What

Keep Unleashed Q3_K_XL as the safe long-context backup when MTPLX overcommits memory or Hermes reloads fail.

## Why

Chris explicitly said "Keep the Unleashed Q3_K_XL as backup (slower but handles 131K via llama.cpp offload)" and Unleashed+DFlash2 provides:
- Stable 131K context (~5 tok/s)
- Vision projector (MTPLX does not replace this)
- DFlash2 integration via dedicated dflash2-llama.cpp fork
- Smaller footprint than MTPLX (12.31 GB vs 19.3 GB)

## Memory Comparison

| Model | Weights | KV @131K | Total | Status |
|-------|---------|----------|-------|--------|
| **Unleashed Q3_K_XL + DFlash2** | 12.31 GB + 1.06 GB | ~8 GB (q8) | ~21 GB | Fits |
| MTPLX Qwen 3.8 Optimized | 19.3 GB | ~8 GB | ~28 GB | Overcommit |

## Status Updates (2026-09-07)

The following events occurred during the session:

1. **MTPLX instability**: Multiple `-9` exits and `OVERCOMMITTED` warnings at 131K
2. **Deletion claimed**: Hermes summary stated Maple (53GB) and Unleashed (23GB) deleted, freeing 76GB
3. **Re-download**: Later turns re-downloaded Unleashed Q3_K_XL and DFlash2 files
4. **Final state**: Unleashed+DFlash2 active on `:11606` at 131K with q8 KV cache

**Key insight**: The disk state is contested - files were deleted then re-downloaded.

## When

- Set 2026-09-07 00:25 after MTPLX `-9` exits
- Re-confirmed 2026-09-07 02:33 after DFlash2 integration failed with invalid flags
- Active 2026-09-07 03:03 with q8 KV quantization

## Conclusion

Unleashed Q3_K_XL remains the **only viable 131K solution** on this 32 GB hardware. It:
- Fits within memory limits (21 GB total with DFlash2)
- Provides stable ~5 tok/s throughput
- Has vision capability via mmproj projector

## Related

- [[unleashed-27b|Unleashed 27B]]
- [[dflash2-draft|DFlash2 Draft]]
- [[main-model-selection|Main Model Selection]]
- [[mtplx-context-overcommit|MPLX Context Overcommit]]