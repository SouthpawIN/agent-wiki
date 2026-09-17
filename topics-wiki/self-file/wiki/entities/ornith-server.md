---
title: "ornith server — mlx_lm local instance"
created: 2026-09-07
updated: 2026-09-15
type: entity
tags: [tool, infra, plan]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-13.md, raw/inbox/2026-09-15.md]
confidence: medium
contested: true
---

# ornith server — mlx_lm local instance

Local `mlx_lm` server instance serving the `ornith` model from `/tmp/mlx-lm-deepgrove`, bound to `127.0.0.1` with a contested port. Chris said at 2026-09-07 14:25, "you aew running on ornith now." ^[raw/inbox/2026-09-07.md]

## SIGKILL incident — 2026-09-07 06:04

Process `proc_6601b0a4a07e` exited with code `-9` while processing a 40011-token prompt. The prompt cache state at kill time: 8 sequences / 1.56 GB; assistant cache same; user/system were 0. The last progress marker was `40011/40011`; the HTTP request `POST /v1/chat/completions` had already returned 200 before the process exited. ^[raw/inbox/2026-09-07.md]

## Restart and token desync — 2026-09-08

On 2026-09-08 Hermes restarted the ornith server with `--new-token` and patched code. A stale PID 63522 outlived the restart and kept serving the old token `E5vz4M5lt...` from its `/token` endpoint, even after the token file on disk was rewritten. ^[raw/inbox/2026-09-08.md] Hermes observed a further PID discrepancy (63983 vs 64044), then started a fresh server with PID 64361 and a new token. ^[raw/inbox/2026-09-08.md] The desync remains contested: true pending confirmation that PID 64361 owns the port and serves the new token consistently.

## Port evidence

Chris's records contain conflicting port assignments for the ornith server. Earlier compiled evidence placed ornith on `127.0.0.1:11620`. ^[raw/inbox/2026-09-07.md] Later Hermes observations mapped MTPLX to `127.0.0.1:11613` and ornith to `127.0.0.1:11622`, then repeatedly returned to `11613` after restarts. Chris explicitly framed local port assignments as unstable until verified live, so both mappings remain contested: true. ^[raw/inbox/2026-09-07.md]

## Session notes — 2026-09-07 10:15–13:37

Hermes observed the following sequence in one evaluation run: MTPLX on 11613; ornith reported on 11622; ornith marked loading and then live on 11613 after warmup; Colibri download started and ornith was killed to free the port; ports were reported free and ornith was restarted; later verification found the process running while curl reported down. ^[raw/inbox/2026-09-07.md]

Hermes also recorded, "Colibri requires custom Maple MLX code (not standard mlx_lm)." ^[raw/inbox/2026-09-07.md]

## Remote-host recovery — 2026-09-15

On 2026-09-15 the ornith/remote inference path surfaced a new incident cluster. At 10:12 Hermes found a "Flash Next server (PID 1069592) eating 16 GB on GPU 1," killed it and a new OOM server, and restarted. ^[raw/inbox/2026-09-15.md] At 11:09 it recorded that an earlier background process had "exited code 7 (connection refused)" from a prior check while "Omarchy's server was restarting," and that it was "since been fixed: nginx is up on 8080, model server healthy on 8100, Tailscale reachable from Mac." ^[raw/inbox/2026-09-15.md] At 13:15 Hermes noted "Mac's prompt cache is full from accumulated test history" and restarted fresh; at 13:21–13:22 it confirmed all background processes complete and that an earlier test failure was "the earlier test before ctx was corrected to 65536. All later tests passed." ^[raw/inbox/2026-09-15.md] This marks a shift from local-loopback serving (ornith on 11613) to a remote setup involving nginx on 8080, a model server on 8100, Tailscale reachability, GPU memory contention, and a context-length correction to 65536.

Related: [[topics-wiki/self-file/wiki/entities/mltplx-server|MTPLX server]], [[topics-wiki/self-file/wiki/entities/hermes|Hermes]], [[topics-wiki/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]], [[topics-wiki/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]], [[topics-wiki/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]], and [[topics-wiki/self-file/wiki/queries/mlx-lm-large-prompt-kill-causes|mlx_lm SIGKILL causes]].
