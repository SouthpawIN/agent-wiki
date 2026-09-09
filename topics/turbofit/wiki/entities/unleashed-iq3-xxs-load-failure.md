---
title: Unleashed IQ3 XXS Load Failure
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [pain, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Unleashed IQ3 XXS Load Failure

`Qwen3.8-27B-Unleashed-UD-IQ3_XXS.gguf` failed to load in the `dflash2-llama.cpp` fork Metal server after a DFlash warning about missing `ctx_other` and then a tensor bounds failure ^[raw/inbox/2026-09-07.md].

## Evidence

- Warning: `dflash requires ctx_other to be set`
- Error: `tensor 'blk.2.attn_qkv.weight' data is not within the file bounds, model is corrupted or incomplete`
- Same load path repeated for `blk.2.ffn_down.weight`
- Server exited due to model loading error

## Note

This failure is specific to this quant artifact and this fork load path. It does not invalidate `Q3_K_XL`, which has served as the stable long-context backup in earlier evidence.

## Related

- [[topics/turbofit/wiki/entities/unleashed-27b|Unleashed 27B]]
- [[topics/turbofit/wiki/decisions/unleashed-backup|Unleashed Backup]]
- [[topics/turbofit/wiki/concepts/dflash2-compat-boundary|DFlash2 Compatibility Boundary]]
