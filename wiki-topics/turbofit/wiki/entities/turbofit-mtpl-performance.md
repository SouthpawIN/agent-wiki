---
title: TurboFit MTPLX Performance
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [entity, performance, mtplx, mtp, evidence, pain]
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-07-from-senter.md
confidence: high
contested: true
---

# TurboFit MTPLX Performance

Evidence-observed performance characteristics of `Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` on this 32 GB M1 Mac, including short-context throughput, long-context overcommit, and live memory-guard behavior ^[raw/inbox/2026-09-07.md].

## Throughput

|| Context | Throughput | Notes ||
|---------|-----------|-------|
| 500 tokens | 8–12 tok/s | Stable short context |
| 65K | ~7 tok/s | Stable daily-driver target |
| 131K short prompt | 6–7 tok/s | Hermes summary claim |
| 5K+ prompts at 131K | `507 Insufficient Storage` | Observed failure |
| 131K with 2005-token history | 0.39 tok/s end-to-end | `end_to_end_tok_s` observed |

## Memory-plan evidence

```
Memory plan: 32G Mac: engine budget 24.0G, weights 19.3G, context 131072 (machine-bound) (OVERCOMMITTED)
requested context 131072 exceeds the machine fit 8192: KV at the full window needs 8.0 GiB; expect cache shedding and, past the fit, swap
```

^[raw/inbox/2026-09-07.md]

## Live memory-guard event

On 2026-09-07 00:51, MTPLX emitted a `prefill_admission_shed` for a 5016-token prompt:

```json
{
  "action": "prefill_admission_shed",
  "prompt_tokens": 5016,
  "reusable_prefix_tokens": 0,
  "miss_tokens": 5016,
  "active_bytes": 20702539884,
  "cache_bytes": 2008116674,
  "projected_bytes": 26260610606,
  "threshold_bytes": 24996709662,
  "limit_bytes": 25769803776,
  "cache_cleared": true,
  "projected_bytes_after_cache_clear": 24252493932
}
```

This corroborates the 32 GB / 131K overcommit behavior: live admission is shedding cache to stay under the threshold ^[raw/inbox/2026-09-07-from-senter.md].

## Postcommit reliability

Hermes foreground work under MTPLX produced `cross_session_foreground_preempted` and `foreground_preempted_postcommit` events, followed by `retokenized_history_mismatch` postcommit artifacts. Those artifacts cannot be treated as finished TurboFit evidence without a real Hermes window capture ^[raw/inbox/2026-09-07.md].

## Contested state

Hermes summaries claimed MTPLX was the locked main provider at 131K, but later command evidence reverted to Unleashed+DFlash2 after repeated instability, then to Ornith MLX ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[wiki-topics/turbofit/wiki/concepts/mtplx-context-overcommit.md|MPLX Context Overcommit]]
- [[wiki-topics/turbofit/wiki/entities/turbofit-memory-crash.md|TurboFit Memory Crash]]
- [[wiki-topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[wiki-topics/turbofit/wiki/entities/mtplx-qwen-38-27b-optimized-speed.md|MPLX Qwen 3.8 27B Optimized Speed]]
