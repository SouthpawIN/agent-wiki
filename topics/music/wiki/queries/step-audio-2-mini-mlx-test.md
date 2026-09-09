---
title: Step-Audio-2-mini MLX 4-bit test
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, music, infra]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# Step-Audio-2-mini MLX 4-bit test

Step-Audio-2-mini is a candidate with an unusual active-parameters profile that may make it cheaper to run than its 35B total parameter count suggests. Before changing the priority order, we need a concrete test under MLX on Chris's machine.

## Questions
- Is there an MLX 4-bit artifact for Step-Audio-2-mini?
- After download, does it load under `mlx_audio` or another runner without the same model-type rejection seen for ACE-Step?
- What is the actual resident memory under one generation, compared with ACE-Step 1.5 4B and MiniMax Music 3?
- Does the active-parameters story hold at runtime, or only in paper numbers?

## Evidence
- "Only 3B params active per forward pass. That means even though the model is 35B total, it should run like a 3B model — potentially 10+ tok/s. Let me get the MLX 4-bit version and test it." ^[raw/inbox/2026-09-07.md]
- "If it doesn't work with MLX, then you try something besides MLX... turbofit is supposed to support multiple." ^[raw/inbox/2026-09-07.md]

## Related
- [[topics/music/wiki/entities/step-audio-2-mini|Step-Audio-2-mini (active-params candidate)]]
- [[topics/music/wiki/comparisons/local-music-models|Local music models]]
- [[topics/music/wiki/queries/local-music-runner-support|Which music candidates actually run under which runner on this Mac?]]
