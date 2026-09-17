---
title: 2026-09-07 local music model priority
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, music, timeline, infra]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---
# 2026-09-07 local music model priority

On 2026-09-07, the chosen order of operations for local music models on Chris's 32 GB Mac was:
1. ACE-Step 1.5 4B (MLX 4bit), ~2 GB, for immediate concurrency with MTPLX.
2. MiniMax Music 3, ~13 GB, by swapping MTPLX out when ACE-Step was blocked.

Chris said he wanted "step 1.54-B" usable now, and if MiniMax Music 3 did not work, he wanted both available on the machine. ^[raw/inbox/2026-09-07.md] ACE-Step was downloaded first for that reason. ^[raw/inbox/2026-09-07.md]

Chris later signaled that the priority is not just "download largest possible," but "find the runnable path," noting that an MLX/quant build should exist. ^[raw/inbox/2026-09-07.md] That shifts the priority from size ordering to runner support and packaging discoverability.

The decision is not final because ACE-Step failed to run in `mlx_audio`. MiniMax remains the intended music target; whether it avoids the same runner blocker is still unknown. Its download status is also still unverified: Hermes captured 5,118 MB transferred for `~/Models/storage/music/minimax-music3-mlx.tar`, but full completion is not confirmed. ^[raw/inbox/2026-09-07.md] Step-Audio-2-mini entered consideration as another candidate with an active-parameters argument. ^[raw/inbox/2026-09-07.md]

## Evidence
- "step 1.54-B, the largest one on there, should work just fine on here." ^[raw/inbox/2026-09-07.md]
- "If minimax music 3 does not work, I would actually like you to get both of those and get them running on this machine." ^[raw/inbox/2026-09-07.md]
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]
- "Download ACE-Step 1.5 (2GB) now — it'll fit alongside MTPLX" ^[raw/inbox/2026-09-07.md]
- Step-Audio-2-mini: "Only 3B params active per forward pass... potentially 10+ tok/s. Let me get the MLX 4-bit version and test it." ^[raw/inbox/2026-09-07.md]
