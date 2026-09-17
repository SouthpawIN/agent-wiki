---
title: "Remote inference stack converged — 2026-09-15"
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, infra, plan]
sources: [raw/inbox/2026-09-15.md]
confidence: medium
contested: true
---

# Remote inference stack converged — 2026-09-15

On 2026-09-15 Hermes reported the remote inference stack healthy after a session of GPU-memory kills and restarts: "nginx is up on 8080, model server healthy on 8100, Tailscale reachable from Mac." ^[raw/inbox/2026-09-15.md] This supersedes the earlier local-loopback ornith-only serving model as the operational inference path.

## Evidence

- 10:12 — "There's still a Flash Next server (PID 1069592) eating 16 GB on GPU 1. Let me kill it and the new OOM server, then use a proper approach." ^[raw/inbox/2026-09-15.md]
- 11:09 — "The background process exited code 7 (connection refused) — that was from an earlier check while Omarchy's server was restarting. It's since been fixed: nginx is up on 8080, model server healthy on 8100, Tailscale reachable from Mac." ^[raw/inbox/2026-09-15.md]
- 13:15 — "Mac's prompt cache is full from accumulated test history. Let me restart fresh." ^[raw/inbox/2026-09-15.md]
- 13:22 — "Already fixed — that was the earlier test before ctx was corrected to 65536. All later tests passed." ^[raw/inbox/2026-09-15.md]

## Outcome

The operational inference endpoint map became: nginx :8080 → model server :8100, reachable from the Mac over Tailscale, serving the ornith model at a corrected context length of 65536. The stack remains contested: true pending live confirmation of the :8080/:8100 endpoints and Tailscale reachability. At 16:28 Hermes reported the session's final state stable ("All background processes complete. Current state stable."), the last logged confirmation of the converged stack. ^[raw/inbox/2026-09-15.md]

Related: [[topics/self-file/wiki/entities/ornith-server|ornith server]], [[topics/self-file/wiki/concepts/remote-inference-stack-2026-09-15|Remote inference stack — 2026-09-15]], [[topics/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]], [[topics/self-file/wiki/entities/hermes|Hermes]], and [[topics/self-file/wiki/queries/mlx-lm-large-prompt-kill-causes|mlx_lm SIGKILL causes]].
