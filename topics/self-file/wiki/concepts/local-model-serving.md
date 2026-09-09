---
title: "local model serving"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [infra, tool, plan]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# local model serving

Running LLM inference locally on Chris's machine, rather than via remote API. On 2026-09-07 Chris said, "I have good info on the current setup. Let me test both existing servers and explore other options." ^[raw/inbox/2026-09-07.md] He later said, "you aew running on ornith now." ^[raw/inbox/2026-09-07.md]

On the same day, at least two local inference endpoints were observed: MTPLX on `127.0.0.1:11613` and ornith on either `127.0.0.1:11620` or `127.0.0.1:11622`, with later evidence showing ornith also bound to `11613` after restart. Chris explicitly framed local port assignments as unstable until verified live. ^[raw/inbox/2026-09-07.md]

## Comparison-relevant outcomes

- Colibri was ruled out for standard `mlx_lm`; Hermes recorded, "Colibri requires custom Maple MLX code." ^[raw/inbox/2026-09-07.md]
- The ornith server was killed after a large-prompt run, then restarted as part of testing. ^[raw/inbox/2026-09-07.md]

Related: [[topics/self-file/wiki/entities/colibri|Colibri]], [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], and [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]].
