---
title: Local music memory budget
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, music, pain, timeline]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# Local music memory budget

On Chris's 32 GB Mac, the already-running [[topics/music/wiki/entities/mtplx|MTPLX]] workload leaves very little headroom for local music generation. Hermes estimated MTPLX at ~20 GB, which makes any music model larger than a few gigabytes impossible to run concurrently. ^[raw/inbox/2026-09-07.md]

This constraint is the root cause of the swap strategy: MiniMax Music 3 is desired, but cannot be loaded while MTPLX is active. The budget also forced dropping Step-Audio-2-mini (~15.5 GB reported size) from immediate consideration. ^[raw/inbox/2026-09-07.md]

Chris later signaled that the expected path is not raw-size filtering, but an MLX/quant build that should exist for the desired models. If such a build changes runtime footprint, the budget calculation may change. ^[raw/inbox/2026-09-07.md]

On 2026-09-16 Chris formalized this budget into an explicit fit-calculation system (model size + KV cache ≤ tier size, checked against every tier) instead of a rough headroom estimate. See [[topics/music/wiki/concepts/music-model-fit-calculation|Music model fit-calculation system]]. ^[raw/inbox/2026-09-16.md]

## What would change the budget
- A smaller quant of the desired music model.
- An MLX/quant build that materially reduces runtime memory vs the reported base size.
- A way to run MTPLX with less memory, or suspend it cleanly before switching to music.
- More RAM, which is not a short-term option.

## Evidence
- "MTPLX is eating ~20GB of your 32GB. Music models need 13-15GB. We can't run both at once without OOM." ^[raw/inbox/2026-09-07.md]
- "Music models need 13-15GB. We can't run both at once without OOM." ^[raw/inbox/2026-09-07.md]
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]
- Step-Audio-2-mini active-params note: "Only 3B params active per forward pass... potentially 10+ tok/s." ^[raw/inbox/2026-09-07.md]
