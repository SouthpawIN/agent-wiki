---
title: Which music candidates actually run under which runner on this Mac?
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, music, infra]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# Which music candidates actually run under which runner on this Mac?

The current blocker is not memory alone. ACE-Step was small enough to download, but `mlx_audio` rejected its model type. We need a runner-by-runner verdict for every downloaded or tracked candidate.

## Candidates
- ACE-Step 1.5 4B
- MiniMax Music 3
- Step-Audio-2-mini
- Ternary-Bonsai-27B-mlx-2bit
- Bonsai-27B-mlx-1bit
- Calibri 27B
- Ornith-MLX / ornith-1-5-35a3b

## Evidence
- "ACE-Step couldn't load (model type not supported in mlx_audio), and then soundfile was missing." ^[raw/inbox/2026-09-07.md]
- "If it doesn't work with MLX, then you try something besides MLX... turbofit is supposed to support multiple." ^[raw/inbox/2026-09-07.md]
- Hermes planned to add Ornith-MLX provider entry. ^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/music/wiki/queries/mlx-audio-model-support|Does mlx_audio support ACE-Step's model format, and what is the smallest quant of MiniMax Music 3 available under MLX?]]
- [[topics-wiki/music/wiki/queries/step-audio-2-mini-mlx-test|Step-Audio-2-mini MLX 4-bit test]]
- [[topics-wiki/music/wiki/queries/local-music-generation-blockers|What blocks local music generation right now?]]
