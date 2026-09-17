---
title: mlx_audio model support limits
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, music, pain, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---
# mlx_audio model support limits

`mlx_audio` is the runner Hermes tried for local music generation on 2026-09-07. It rejected ACE-Step's model type outright, so a downloaded model can still be unusable if the runner does not support it. Missing `soundfile` then blocked saving output. ^[raw/inbox/2026-09-07.md]

This is not an ACE-Step-only case: any music model landing in `~/Models/storage/music/` still needs a runner path. The same limitation applies to MiniMax Music 3 and Step-Audio-2-mini until their runner compatibility is verified. ^[raw/inbox/2026-09-07.md]

Chris noted after the failure that an MLX/quant build "should be" available, indicating he sees runner support as an availability problem rather than a hard dead end. ^[raw/inbox/2026-09-07.md]

## Why it matters
Size is not the only gate. Even when a model fits in memory, the loader/runtime may not accept its format. That makes "fits = works" a false assumption in this stack. If an MLX/quant build exists but is not discoverable from this runner, the blocker is discoverability/packaging, not hardware. This concept is therefore one of the three root-cause layers recorded in [[topics-wiki/music/wiki/queries/local-music-generation-blockers|What blocks local music generation right now?]].

## Runner support landscape
| Candidate | Runner/test status | Support |
|---|---|---|
| ACE-Step 1.5 4B | Rejected by `mlx_audio` | ❌ |
| MiniMax Music 3 | Untested after download | Unknown |
| Step-Audio-2-mini | Untested; MLX 4-bit candidate proposed | Unknown |

## Evidence
- "ACE-Step couldn't load (model type not supported in mlx_audio), and then soundfile was missing." ^[raw/inbox/2026-09-07.md]
- "Beats folder is empty — the script failed before generating anything." ^[raw/inbox/2026-09-07.md]
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]
- "If it doesn't work with MLX, then you try something besides MLX... turbofit is supposed to support multiple... most optimized way to run these models on this machine." ^[raw/inbox/2026-09-07.md]

## Open questions
- Does `mlx_audio` ever plan to support ACE-Step's model type, or is the answer a different runner entirely?
- Is the correct path a different runner such as TurboFit or an MMLX-style wrapper instead of patching `mlx_audio`?
- For each downloaded model, is the support problem the same, or unique?
