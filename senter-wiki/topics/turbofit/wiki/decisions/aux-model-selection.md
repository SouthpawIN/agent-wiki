---
title: Aux Model Selection
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, model, pain, preference]
sources: [raw/inbox/2026-09-06.md]
confidence: high
---

# Aux Model Selection

## What

Auxiliary and compression routing is Maple MLX on `127.0.0.1:11612`, 131k context, served with `deepgrove-ai/mlx-lm-deepgrove` ^[raw/inbox/2026-09-06.md].

## Why

Chris explicitly asked for Maple as the auxiliary model because it targets Apple Silicon with an MLX focus ^[raw/inbox/2026-09-06.md]. Generic `mlx_lm` was rejected after repeated Metal OOMs; the deepgrove fork is the first working Apple-Silicon path.

## When

Set 2026-09-06 after stock llama.cpp and generic MLX paths failed under load.

## Contested

Multiple Hermes turns declared Maple MLX unstable or impossible before the deepgrove fork proved a working serverless-style path via `generate()` and later server-mode with `--flash-head --trust-remote-code`. Hermes also tried Ornith and Nous free-tier aux as fallback options, which Chris did not accept as permanent replacements ^[raw/inbox/2026-09-06.md].

## Evidence

- "I would rather you use Maple which does have an MLX and does seem to have a focus for Apple development. I want that one to be my auxiliary model" ^[raw/inbox/2026-09-06.md].
- "Maple MLX is stable as aux with the deepgrove fork" ^[raw/inbox/2026-09-06.md].

## Related

- [[topics/turbofit/wiki/entities/maple.md|Maple]]
- [[topics/turbofit/wiki/decisions/main-model-selection.md|Main Model Selection]]
- [[topics/turbofit/wiki/comparisons/aux-runtime-options.md|Aux Runtime Options]]
