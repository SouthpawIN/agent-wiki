---
title: "What triggers SIGKILL in mlx_lm server during long prompt processing: cache limits, memory pressure, or timeout?"
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question]
sources: [raw/inbox/2026-09-07.md]
proposed: 2026-09-07 10:23
confidence: low
---

# What triggers SIGKILL in mlx_lm server during long prompt processing: cache limits, memory pressure, or timeout?

Chris hit a hard kill after 40k tokens on the ornith `mlx_lm` server; knowing the cause informs whether to tune cache, add swap, or switch servers.

_Approve to run the research; the answer lands here._

Related: [[topics-wiki/self-file/wiki/entities/ornith-server|ornith server]], [[topics-wiki/self-file/wiki/entities/mltplx-server|MTPLX server]], [[topics-wiki/self-file/wiki/concepts/local-model-serving|local model serving]], [[topics-wiki/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], [[topics-wiki/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]], and [[topics-wiki/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
