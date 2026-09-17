---
title: Local music models
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [music, decision, tool, infra, comparison]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# Local music models

Comparison of local generative-music candidates Chris considered on his 32 GB Mac on 2026-09-07. Memory numbers come from Hermes's model-size check; actual runtime RAM may differ. ^[raw/inbox/2026-09-07.md]

## Candidates

| Model | Quant / note | Reported size | Fits alongside MTPLX (~20 GB used) | Verdict |
|---|---|---|---|---|
| ACE-Step 1.5 4B | MLX 4bit | ~2.06 GB | ✅ | First choice; downloaded, then blocked by runner support. See [[topics-wiki/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]. |
| MiniMax Music 3 | mxfp8 | ~13 GB | ❌ | Second choice; requires MTPLX swap. See [[topics-wiki/music/wiki/entities/minimax-music-3|MiniMax Music 3 (mxfp8)]]. |
| Step-Audio-2-mini | ~35B total / ~3B active per forward pass; MLX 4-bit candidate | ~15.5 GB baseline | ❌ | Size-based drop, but became relevant again because of the active-parameters argument and Chris's stated expectation that an MLX/quant path should exist. ^[raw/inbox/2026-09-07.md] |
| Ternary-Bonsai-27B-mlx-2bit | 2-bit ternary | ~7.91 GB | ❌ | Downloaded but not executed as a music candidate; runner compatibility unknown. See [[topics-wiki/music/wiki/entities/ternary-bonsai-27b|Ternary-Bonsai-27B-mlx-2bit]]. |
| Bonsai-27B-mlx-1bit | 1-bit binary proposed | Unknown | Unknown | Proposed follow-up to ternary Bonsai; no confirmed artifact. See [[topics-wiki/music/wiki/entities/bonsai-27b|Bonsai-27B-mlx-1bit]]. |
| Calibri 27B | Unknown | Unknown | Unknown | Named by Chris as required; no artifact or runner result recorded. See [[topics-wiki/music/wiki/entities/calibri-27b|Calibri 27B]]. |

## Local budget reality
Chris's Mac has 32 GB RAM. With [[topics-wiki/music/wiki/concepts/local-music-memory-budget|MTPLX already near 20 GB]], only the smallest music model can run without swapping workloads. That is the root cause behind choosing ACE-Step first and deferring MiniMax to a swap. ^[raw/inbox/2026-09-07.md]

## Runner support reality
Downloaded size alone is not enough. ACE-Step failed because `mlx_audio` rejected its model type, which makes runner support a first-class comparison axis. See [[topics-wiki/music/wiki/queries/local-music-runner-support|Which music candidates actually run under which runner on this Mac?]] for the runner-by-runner verdicts that are still pending.

## Contested / open
- Size numbers are Hermes's best available check; actual model memory footprint under MLX inference could differ.
- ACE-Step failed to run for support reasons unrelated to size, so "fits" does not mean "works yet."
- Step-Audio-2-mini's active-parameters claim changes its effective memory profile if MLX can exploit it, but that is unverified.
- Chris expects MLX/quant builds to exist; if so, the comparison should be rerun against those specific artifacts rather than base reported sizes.
- Hermes added Ornith-MLX provider setup to its catalog work, but its music-task candidacy is unconfirmed. See [[topics-wiki/music/wiki/entities/ornith-mlx|Ornith-MLX / ornith-1-5-35a3b]].
