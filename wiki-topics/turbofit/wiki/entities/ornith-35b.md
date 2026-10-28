---
title: Ornith 35B A3B
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, preference, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Ornith 35B A3B

`Ornith-1.5-35B-A3B` is a MoE model downloaded to `~/Models/storage/ornith/` as MLX 4-bit on this 32 GB box. A DFlash2 draft package was also downloaded to `~/Models/storage/ornith-dflash2/` ^[raw/inbox/2026-09-07.md].

## Tested speeds on M1 MacBook 32GB

| Context | Tok/s |
|---------|-------|
| Short (~500 tokens) | 28.5 |
| 5K tokens | 4.3 |
| 20K tokens | 1.5 |
| 40K tokens | 0.7 |
| 60K tokens | 0.4 |
| 131K | ~0.5 |

These numbers were gathered in-session against the downloaded artifacts; they are not stable live-route evidence from Hermes ^[raw/inbox/2026-09-07.md].

## DFlash2 candidate

A DFlash2 draft build exists as `jzinno/Ornith-1.5-35B-A3B-DFlash2` on HuggingFace, but community uptake is small (~840 downloads at time of observation). No MTPLX integration path exists because MTPLX uses native MLX MTP heads rather than llama.cpp draft models ^[raw/inbox/2026-09-07.md].

## Contested Evidence

> "The hard truth: On M1 MacBook 32GB with a 27B model at 131K context, **~5-6 tok/s is the ceiling.** You want 10+ tok/s. That's not happening with this hardware — it's like asking a Honda Civic to go 200mph." ^[raw/inbox/2026-09-07.md].

Hermes proposed Ornith MLX 4-bit as daily-driver main provider for short/medium workloads and Unleashed+DFlash2 as long-context fallback. That pairing is contested because it has not been verified as a stable live Hermes route without reload failures or memory overcommit ^[raw/inbox/2026-09-07.md].

## Conclusion

**Recommendation:** Ornith MLX 4-bit as main provider for daily use (short/medium context, 28.5 tok/s) with 65K context as the stable ceiling. Use Unleashed+DFlash2 for 131K long-context needs. 10+ tok/s at 131K is physically unachievable on this 32GB hardware.

## Note

Ornith is fast at short context but loses throughput sharply as KV cache grows. On this hardware, 131K remains the throughput ceiling regardless of runtime.

## Related

- [[aux-model-selection|Aux Model Selection]]
- [[unleashed-backup|Unleashed Backup]]
- [[apple-silicon-runtime-benchmark|Apple Silicon Runtime Benchmark]]
- [[dflash2-draft|DFlash2 Draft]]
- [[ornith-35b-mlx|Ornith 35B MLX]]
- [[ornith-35b-dflash2|Ornith 35B DFlash2]]
