---
title: "Colibri ruling — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, infra, plan]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: false
---

# Colibri ruling — 2026-09-07

On 2026-09-07, after downloading and attempting to use Colibri, Hermes decided it was not compatible with standard `mlx_lm` and switched back to ornith. Hermes wrote, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md] It then said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md]

## Evidence

- Colibri download started while ornith was live.
- Ornith was killed to free port `11613`.
- After returning to ornith, Hermes concluded Colibri needed custom Maple MLX code.
- Bonsai MLX was named as the next path.

## Outcome

Colibri remains untaken as the local backend unless custom Maple MLX code is supplied. Ornith MLX is treated as the provisional winner from the same session, while Bonsai MLX becomes the explored alternative.

Related: [[wiki-topics/self-file/wiki/entities/colibri|Colibri]], [[wiki-topics/self-file/wiki/entities/ornith-server|ornith server]], [[wiki-topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], [[wiki-topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], and [[wiki-topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
