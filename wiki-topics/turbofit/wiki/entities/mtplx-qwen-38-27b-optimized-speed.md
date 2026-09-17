---
title: MTPLX Qwen 3.8 27B Optimized Speed
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool, decision, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# MTPLX Qwen 3.8 27B Optimized Speed

`Youssofal/Qwen3.8-27B-MTPLX-Optimized-Speed` is the candidate Hermes TurboFit provider discovered on 2026-09-07. It is served via `~/turbofit/.venv/bin/mtplx serve` and exposes an OpenAI-compatible endpoint on this box ^[raw/inbox/2026-09-07.md].

## Runtime facts

- Weights: 19.3 GB.
- Engine budget: 24.0 GB.
- Stable observed context: 65,536 tokens.
- 131,072-token context prints `OVERCOMMITTED`, warns `requested context 131072 exceeds the machine fit 8192`, and then exits under generation pressure ^[raw/inbox/2026-09-07.md].
- Memory guard clears KV cache when projected bytes exceed threshold ^[raw/inbox/2026-09-07.md].
- `--memory-budget` is not a valid CLI flag; the supported path is env/runtime config ^[raw/inbox/2026-09-07.md].

## Performance

| Context | Throughput | Notes |
|---------|-----------|-------|
| 500 tokens | 8–12 tok/s | Stable short context |
| 65K | ~7 tok/s | Stable daily-driver target |
| 131K | 6–7 tok/s short | Hermes summary claim |
| 5K+ prompts at 131K | 507 Insufficient Storage | Observed failure |
| End-to-end @ 131K 2005-token history | 0.39 tok/s | `end_to_end_tok_s` observed |

## Artifacts

- Hermes summary claimed config locked to `custom:turbofit-mtplx` as main provider, but that state is contested because later command evidence reverted to Unleashed+DFlash2 after repeated instability ^[raw/inbox/2026-09-07.md].

## Related

- [[wiki-topics/turbofit/wiki/entities/mplx.md|MPLX]]
- [[wiki-topics/turbofit/wiki/decisions/mtplx-main-provider.md|MPLX Main Provider]]
- [[wiki-topics/turbofit/wiki/decisions/context-window-decision.md|Context Window Decision]]
- [[wiki-topics/turbofit/wiki/entities/mtplx-memory-guard.md|MPLX Memory Guard]]
- [[wiki-topics/turbofit/wiki/entities/mtplx-service-arg-validation.md|MPLX Service Arg Validation]]
- [[wiki-topics/turbofit/wiki/concepts/mtplx-32gb-memory-and-evidence-reliability.md|MPLX 32GB Memory and Evidence Reliability]]
