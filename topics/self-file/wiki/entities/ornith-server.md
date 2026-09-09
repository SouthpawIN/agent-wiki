---
title: "ornith server — mlx_lm local instance"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [tool, infra]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
contested: true
---

# ornith server — mlx_lm local instance

Local `mlx_lm` server instance serving the `ornith` model from `/tmp/mlx-lm-deepgrove`, bound to `127.0.0.1` with a contested port. Chris said at 2026-09-07 14:25, "you aew running on ornith now." ^[raw/inbox/2026-09-07.md]

## SIGKILL incident — 2026-09-07 06:04

Process `proc_6601b0a4a07e` exited with code `-9` while processing a 40011-token prompt. The prompt cache state at kill time: 8 sequences / 1.56 GB; assistant cache same; user/system were 0. The last progress marker was `40011/40011`; the HTTP request `POST /v1/chat/completions` had already returned 200 before the process exited. ^[raw/inbox/2026-09-07.md]

## Port evidence

Chris's records contain conflicting port assignments for the ornith server. Earlier compiled evidence placed ornith on `127.0.0.1:11620`. ^[raw/inbox/2026-09-07.md] Later Hermes observations mapped MTPLX to `127.0.0.1:11613` and ornith to `127.0.0.1:11622`, then repeatedly returned to `11613` after restarts. Chris explicitly framed local port assignments as unstable until verified live, so both mappings remain contested: true. ^[raw/inbox/2026-09-07.md]

## Session notes — 2026-09-07 10:15–13:37

Hermes observed the following sequence in one evaluation run: MTPLX on 11613; ornith reported on 11622; ornith marked loading and then live on 11613 after warmup; Colibri download started and ornith was killed to free the port; ports were reported free and ornith was restarted; later verification found the process running while curl reported down. ^[raw/inbox/2026-09-07.md]

Hermes also recorded, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md]

Related: [[topics/self-file/wiki/entities/mltplx-server|MTPLX server]], [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]], and [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]].
