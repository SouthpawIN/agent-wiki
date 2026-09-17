---
title: "MTPLX server"
created: 2026-09-07
updated: 2026-09-09
type: entity
tags: [tool, infra]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md]
confidence: high
---

# MTPLX server

A local inference server observed on `127.0.0.1:11613`. On 2026-09-07 Hermes noted, "The server on 11613 is MTPLX." ^[raw/inbox/2026-09-07.md]

## Port lock evidence

During 2026-09-07 exploration, port `11613` was repeatedly reassigned: Hermes first reported MTPLX on 11613, then Colibri occupied it during download, then ornith was started on 11613, then verification found the process running while curl said down. ^[raw/inbox/2026-09-07.md] On 2026-09-08 Hermes revisited port assignments while restarting the ornith server with `--new-token`; the stale-process issue affected ornith on 11613, not MTPLX itself. ^[raw/inbox/2026-09-08.md]

Related: [[topics/self-file/wiki/entities/colibri|Colibri]], [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], [[topics/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]], [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
