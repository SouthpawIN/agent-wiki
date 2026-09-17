---
title: "Local servers — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: comparison
tags: [infra, tool, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# Local servers — 2026-09-07

| Server | Port evidence | Status notes | Source |
|---|---|---|---|
| MTPLX | `127.0.0.1:11613` | Named in later Hermes observation; served as a fixed landmark during port churn | ^[raw/inbox/2026-09-07.md] |
| ornith | `127.0.0.1:11620`, then `11622`, then `11613` | Earlier compile said `11620`; later observation said `11622`; later Hermes restarted it on `11613`; Chris confirmed at 14:25 he was on ornith | ^[raw/inbox/2026-09-07.md] |

The ornith port mapping is contested: true. Chris wanted to test existing servers and explore other options, making live port verification a prerequisite for reliable comparison. ^[raw/inbox/2026-09-07.md]

Related: [[topics/self-file/wiki/entities/colibri|Colibri]], [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/entities/mltplx-server|MTPLX server]], [[topics/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]], [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
