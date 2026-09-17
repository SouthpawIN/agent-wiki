---
title: "Remote inference stack — 2026-09-15"
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, tool, plan, pain]
sources: [raw/inbox/2026-09-13.md, raw/inbox/2026-09-15.md]
confidence: medium
contested: true
---

# Remote inference stack — 2026-09-15

A remote inference deployment Chris's setup converged on by 2026-09-15, distinct from the earlier local-loopback ornith server. The stack, as reported by Hermes at 11:09, is: "nginx is up on 8080, model server healthy on 8100, Tailscale reachable from Mac." ^[raw/inbox/2026-09-15.md] It sits behind Tailscale (reachable from the Mac), fronts the model server through nginx, and serves the ornith model through a corrected context length of 65536.

This grows out of the remote-host inference-discovery thread documented on 2026-09-13 (cf. [[topics/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]]) — the port-probing and bring-up ritual against the "HP" machine — but now the server is actually up and serving, with a concrete port/endpoint map instead of guessing.

## Incident cluster — 2026-09-15

The path to a healthy stack was noisy:

- 10:12 — A "Flash Next server (PID 1069592) eating 16 GB on GPU 1" was found; Hermes killed it and a new OOM server, then restarted. ^[raw/inbox/2026-09-15.md]
- 11:09 — An earlier background process had "exited code 7 (connection refused)" from a prior check while "Omarchy's server was restarting"; the stack was reported healthy afterward. ^[raw/inbox/2026-09-15.md]
- 13:15 — "Mac's prompt cache is full from accumulated test history"; Hermes restarted fresh. ^[raw/inbox/2026-09-15.md]
- 13:21–13:22 — All background processes complete; an earlier test failure was explained as "the earlier test before ctx was corrected to 65536. All later tests passed." ^[raw/inbox/2026-09-15.md]

## Pain points

- GPU memory contention: a stray process consumed 16 GB on GPU 1, forcing kills and restarts. ^[raw/inbox/2026-09-15.md]
- Prompt-cache saturation: accumulated test history filled the Mac's prompt cache, requiring a restart. ^[raw/inbox/2026-09-15.md]
- Restart churn: multiple background processes exited with connection-refused and OOM codes across the session. ^[raw/inbox/2026-09-15.md]

## Context-length correction

The context length was corrected to 65536; earlier test failures preceded this correction and later tests passed after it. ^[raw/inbox/2026-09-15.md]

## Relation to local-model-serving

This is the remote-hosted evolution of local-model-serving: the same "test the server, wait for ready" ritual now targets an nginx-fronted model server on 8100 behind Tailscale rather than a loopback `mlx_lm` instance. ^[raw/inbox/2026-09-13.md]

Related: [[topics/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]], [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/concepts/local-model-serving|local model serving]], and [[topics/self-file/wiki/entities/hermes|Hermes]].
