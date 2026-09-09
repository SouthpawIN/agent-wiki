---
title: Step-Audio-2-mini (active-params candidate)
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [tool, music, repo, decision, comparison]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# Step-Audio-2-mini (active-params candidate)

Step-Audio-2-mini entered local music consideration on 2026-09-07 because its active-parameters profile can change the effective memory and speed story even when its base size is large. Hermes noted it at ~35B total parameters with only ~3B active per forward pass, which can behave more like a small model under MLX. ^[raw/inbox/2026-09-07.md]

## Status (2026-09-07)
- Not downloaded or tested yet.
- An MLX 4-bit build was proposed as the next test target. ^[raw/inbox/2026-09-07.md]
- No runner result or artifact URL is confirmed. ^[raw/inbox/2026-09-07.md]
- Chris said if MLX fails, a fallback runner such as TurboFit should be tried because it is supposed to support multiple optimized local-model paths. ^[raw/inbox/2026-09-07.md]

## Why it matters
If an MLX/quant build exists and MLX can exploit the active-parameters structure, Step-Audio-2-mini could become viable on the 32 GB Mac without the full-size penalty. That would add a third candidate to [[topics/music/wiki/comparisons/local-music-models|Local music models]] and could change the priority order. The active-params argument also makes it relevant beyond raw-size comparisons. ^[raw/inbox/2026-09-07.md]

## Assumptions Chris stated
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]
- "If it doesn't work with MLX, then you try something besides MLX... turbofit is supposed to support multiple... most optimized way to run these models on this machine." ^[raw/inbox/2026-09-07.md]

## Evidence
- "Only 3B params active per forward pass. That means even though the model is 35B total, it should run like a 3B model — potentially 10+ tok/s. Let me get the MLX 4-bit version and test it." ^[raw/inbox/2026-09-07.md]

## Related
- [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]
- [[topics/music/wiki/entities/minimax-music-3|MiniMax Music 3 (mxfp8)]]
- [[topics/music/wiki/decisions/2026-09-07-music-model-priority|2026-09-07 local music model priority]]

## Open questions
- Does an MLX/quant build exist for Step-Audio-2-mini, and is it discoverable?
- Can MLX actually exploit the active-parameters profile to reduce live memory?
- If MLX fails, does TurboFit accept this model type and reduce runtime memory?
