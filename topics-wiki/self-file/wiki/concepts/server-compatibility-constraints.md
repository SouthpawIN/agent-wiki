---
title: "server compatibility constraints"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, plan, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: false
---

# server compatibility constraints

Constraints that determine whether a local inference target can actually run on Chris's existing `mlx_lm` setup, as opposed to requiring a different server framework or custom code.

## Standard mlx_lm compatibility

Hermes observed during 2026-09-07 testing that some candidates are not plug-compatible with `mlx_lm server`. Specifically, it recorded, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md]

## Implications

- ornith runs on standard `mlx_lm`.
- Colibri is blocked unless custom Maple MLX code is added.
- Bonsai MLX was raised as an alternative path but its compatibility is not yet verified.
- Hermes asked whether to update config and restart ornith, which shows the compatibility question is coupled to endpoint/config management.

## Preference implication

Chris wants to test existing servers and explore other options. That means compatibility is part of the comparison: not just benchmark quality, but whether the server can run without custom code. This should remain explicit in future compiles.

Related: [[topics-wiki/self-file/wiki/entities/colibri|Colibri]], [[topics-wiki/self-file/wiki/entities/ornith-server|ornith server]], and [[topics-wiki/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
