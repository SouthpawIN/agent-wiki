---
title: MiniMax Music 3 (mxfp8)
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [tool, music, repo, decision, comparison]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---
# MiniMax Music 3 (mxfp8)

A 13 GB music model Chris wants running on his machine. Hermes reported it "won't fit alongside MTPLX" in a 32 GB memory budget, so the current plan is a manual swap: kill MTPLX, run MiniMax, then restart MTPLX. ^[raw/inbox/2026-09-07.md]

## Status (2026-09-07)
- Downloaded into `~/Models/storage/music/minimax-music3-mlx.tar`. ^[raw/inbox/2026-09-07.md]
- Transfer output shows 5,118 MB received, which suggests a partial download of one segment rather than confirmation of the full 13 GB archive. ^[raw/inbox/2026-09-07.md]
- Not yet executed or verified because of the memory constraint, and because the runtime file layout may be incomplete. ^[raw/inbox/2026-09-07.md]
- Chris later expressed an expectation that an MLX/quant build should exist for this path as well. ^[raw/inbox/2026-09-07.md]

## Trade-off
See [[topics-wiki/music/wiki/comparisons/local-music-models|Local music models]] for the size-versus-concurrency comparison that led to the swap plan.

## Provenance
- Hermes curl output for `~/Models/storage/music/minimax-music3-mlx.tar` reached 5,118 MB transferred at 35.2 MB/s and reported 100% through that transferred segment; it is not a confirmed final-model verification. ^[raw/inbox/2026-09-07.md]

## Assumptions Chris stated
- "If minimax music 3 does not work, I would actually like you to get both of those and get them running on this machine." ^[raw/inbox/2026-09-07.md]
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]

## Evidence
- "Download MiniMax Music 3 (13GB) — we'll need to swap it in (kill MTPLX → use MiniMax → restart MTPLX)" ^[raw/inbox/2026-09-07.md]
- "MiniMax Music 3 (mxfp8): 13 GB — won't fit alongside MTPLX ❌" ^[raw/inbox/2026-09-07.md]
- Download command output: `~/Models/storage/music/minimax-music3-mlx.tar`, final progress 5,118 MB / 5,118 MB at ~35.2 MB/s through 100% of the transferred segment. ^[raw/inbox/2026-09-07.md]

## Open questions
- Is the downloaded file a complete model archive or only a single-part segment?
- After swap-in, does MiniMax Music 3 actually run under MLX without the same `mlx_audio` blocker seen with ACE-Step?
- Is there an MLX/quant build that would reduce its memory footprint enough to run alongside MTPLX?
