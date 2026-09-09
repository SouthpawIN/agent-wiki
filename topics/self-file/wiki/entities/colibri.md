---
title: "Colibri"
created: 2026-09-07
updated: 2026-09-08
type: entity
tags: [tool, infra, idea]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md]
confidence: medium
contested: false
---

# Colibri

A local inference target evaluated on 2026-09-07 and ruled out for standard `mlx_lm` because it requires custom Maple MLX code. Hermes recorded, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md]

## Download and port behavior

During evaluation, Colibri started downloading while ornith was running. Hermes killed ornith to free port `11613`, then later said, "Kill the Ornith server so it can use port when done." ^[raw/inbox/2026-09-07.md] After download, Hermes returned to ornith and said, "Ornith is back live. Remove Colibri and lock in Ornith." ^[raw/inbox/2026-09-07.md]

## Post-evaluation stance

Later in the same session, Hermes treated Colibri as incompatible with the current `mlx_lm` path and pivoted to Bonsai MLX. This leaves Colibri in a known-incompatible state unless custom Maple MLX code is provided.

Related: [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
