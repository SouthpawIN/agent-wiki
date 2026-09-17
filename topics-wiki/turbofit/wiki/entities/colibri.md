---
title: Colibri
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, pain, candidate]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Colibri

## What this is

Colibri is a custom-architecture model with `base_model: deepgrove/maple-preview`. It requires custom Maple MLX training/inference code and is incompatible with the standard `mlx_lm` server ^[raw/inbox/2026-09-07.md].

## Status

- **Incompatible with standard MLX server**: The `mlx_lm` server from the deepgrove-ai fork failed to start because it could not find `config.json` at `/Users/sovthpaw/Models/storage/colibri/config.json` ^[raw/inbox/2026-09-07.md]. The model uses a custom Maple format that generic MLX servers cannot load.
- **Removed**: Chris's subagents removed Colibri from the candidate set because its custom format is incompatible with standard MLX server execution paths.

## Why it failed

Colibri's `base_model: deepgrove/maple-preview` means it requires the Maple-specific MLX codepath, not the generic mlx_lm server. The custom code that trains and runs Maple models is not present in standard mlx_lm distributions ^[raw/inbox/2026-09-07.md].

## Chris's directive

Chris explicitly redirected focus from Bonsai and Colibri to Ornith: "Don't worry about bonsai" and "I said the model that we're using is too dumb, okay? So we need to focus entirely on getting Ornith up" ^[raw/inbox/2026-09-07.md].

## Related

- [[topics-wiki/turbofit/wiki/entities/maple.md|Maple]]
- [[topics-wiki/turbofit/wiki/entities/ornith-1-5-35b-a3b-mlx-4-bit|Ornith 1.5 35B-A3B MLX 4-bit]]
- [[topics-wiki/turbofit/wiki/decisions/local-main-provider|TurboFit Local Main Provider Decision]]
