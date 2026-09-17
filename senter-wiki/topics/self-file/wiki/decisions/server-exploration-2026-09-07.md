---
title: "Server exploration note — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, plan, infra]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Server exploration note — 2026-09-07

On 2026-09-07 Chris said he had good info on the current setup and intended to test both existing servers and explore other options. ^[raw/inbox/2026-09-07.md] He also confirmed that, despite changing ports and restarts, he was on ornith. ^[raw/inbox/2026-09-07.md]

## Evidence

During the same period a local `mlx_lm` instance serving the `ornith` model on `127.0.0.1:11620` was killed with SIGKILL after processing a 40011-token prompt, then repeatedly restarted while Colibri was tested and ruled out for standard `mlx_lm`; Hermes recorded, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md]

## Port landscape

During exploration, multiple port assignments surfaced. Earlier compiled evidence placed ornith on `127.0.0.1:11620`. ^[raw/inbox/2026-09-07.md] Later Hermes mapped MTPLX to `127.0.0.1:11613` and ornith to `127.0.0.1:11622`, then returned to ornith on `11613` after restarts. Chris said at 14:25 he was on ornith. ^[raw/inbox/2026-09-07.md]

Related: [[topics/self-file/wiki/entities/colibri|Colibri]], [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/entities/mltplx-server|MTPLX server]], [[topics/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]], [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
