---
title: What blocks local music generation right now?
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, music, infra, timeline]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---
# What blocks local music generation right now?

## Answer (as of 2026-09-07)
Three layers:
1. Memory: [[wiki-topics/music/wiki/concepts/local-music-memory-budget|MTPLX uses ~20 GB]], so only a ~2 GB music model can run concurrently. ^[raw/inbox/2026-09-07.md]
2. Runner: `mlx_audio` does not support ACE-Step's model type, and `soundfile` is missing, so generation fails even though the model is downloaded. ^[raw/inbox/2026-09-07.md]
3. Packaging/discoverability: Chris expects MLX/quant builds to exist for the desired models; if they do, they are not currently wired into the workflow. ^[raw/inbox/2026-09-07.md]

MiniMax Music 3 is downloaded but unverified; its runtime blocker set may overlap with ACE-Step's, but that is not yet known. A later Hermes note introduced Step-Audio-2-mini as another candidate despite its larger stated size because it may have a favorable active-parameters profile. ^[raw/inbox/2026-09-07.md]

## Runner coverage
- ACE-Step 1.5 4B: `mlx_audio` rejected the model type. ^[raw/inbox/2026-09-07.md]
- MiniMax Music 3: runner support unknown; not tested. ^[raw/inbox/2026-09-07.md]
- Step-Audio-2-mini: MLX 4-bit candidate; no runner test recorded. ^[raw/inbox/2026-09-07.md]
- Ternary-Bonsai-27B-mlx-2bit: downloaded, runner compatibility unknown. ^[raw/inbox/2026-09-07.md]
- Bonsai-27B-mlx-1bit, Calibri 27B, Ornith-MLX: no runner test recorded. ^[raw/inbox/2026-09-07.md]

## Timeline
- 2026-09-07 ~02:32 — download + test strategy started; Hermes began comparison work. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 ~02:40 — Hermes identified memory split and runner issues as the active blockers. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 03:04 — Hermes reported ACE-Step load failure and empty `Beats/`. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 05:46 — Chris noted an MLX/quant build "might" or "should" exist for the desired path. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 05:47 — Hermes noted Step-Audio-2-mini has ~35B total but only ~3B active params per forward pass, potentially 10+ tok/s. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 11:25 — Chris said to apply the same validation to Calibri and bonsai, and if MLX fails, try another optimized runner such as TurboFit. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 12:32 — Hermes confirmed ternary Bonsai download and proposed the 1-bit Bonsai follow-up. ^[raw/inbox/2026-09-07.md]
- 2026-09-07 14:01 — Hermes noted adding the Ornith-MLX provider entry as pending catalog work. ^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]
- [[wiki-topics/music/wiki/entities/minimax-music-3|MiniMax Music 3 (mxfp8)]]
- [[wiki-topics/music/wiki/decisions/2026-09-07-music-model-priority|2026-09-07 local music model priority]]
- [[wiki-topics/music/wiki/comparisons/local-music-models|Local music models]]
- [[wiki-topics/music/wiki/queries/local-music-runner-support|Which music candidates actually run under which runner on this Mac?]]
