---
title: self-file
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# self-file

Last updated: 2026-09-15 | Total pages: 17

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Colibri](wiki/colibri.md) — A local inference target evaluated on 2026-09-07 and ruled out for standard `mlx_lm` because it requires custom Maple MLX code. Hermes recorded, "Colibri requir
- [Hermes](wiki/hermes.md) — The AI agent framework Chris uses. On 2026-09-07 it surfaced the server-testing intent and reported the background process exit for the ornith server. ^[raw/inb
- [MTPLX server](wiki/mltplx-server.md) — A local inference server observed on `127.0.0.1:11613`. On 2026-09-07 Hermes noted, "The server on 11613 is MTPLX." ^[raw/inbox/2026-09-07.md]
- [ornith server — mlx_lm local instance](wiki/ornith-server.md) — Local `mlx_lm` server instance serving the `ornith` model from `/tmp/mlx-lm-deepgrove`, bound to `127.0.0.1` with a contested port. Chris said at 2026-09-07 14:

### Concepts

- [local model serving](wiki/local-model-serving.md) — Running LLM inference locally on Chris's machine, rather than via remote API. On 2026-09-07 Chris said, "I have good info on the current setup. Let me test both
- [remote-host inference discovery](wiki/remote-host-inference-discovery.md) — The practice of locating and bringing up a local-inference server on a remote compute box in Chris's setup — a machine Chris calls the "HP" (with a related `oma
- [Remote inference stack — 2026-09-15](wiki/remote-inference-stack-2026-09-15.md) — A remote inference deployment Chris's setup converged on by 2026-09-15, distinct from the earlier local-loopback ornith server. The stack, as reported by Hermes
- [scan-topics.py JSON schema — skills field](wiki/scan-json-schema.md) — A `skills` field schema mismatch surfaced in the raw→wiki compilation loop on 2026-09-09. The scan's PRINT output reported `skills=0` (an integer count) while t
- [server compatibility constraints](wiki/server-compatibility-constraints.md) — Constraints that determine whether a local inference target can actually run on Chris's existing `mlx_lm` setup, as opposed to requiring a different server fram

### Decisions

- [Colibri ruling — 2026-09-07](wiki/colibri-ruling-2026-09-07.md) — On 2026-09-07, after downloading and attempting to use Colibri, Hermes decided it was not compatible with standard `mlx_lm` and switched back to ornith. Hermes
- [Remote inference stack converged — 2026-09-15](wiki/remote-stack-converged-2026-09-15.md) — On 2026-09-15 Hermes reported the remote inference stack healthy after a session of GPU-memory kills and restarts: "nginx is up on 8080, model server healthy on
- [Server exploration note — 2026-09-07](wiki/server-exploration-2026-09-07.md) — On 2026-09-07 Chris said he had good info on the current setup and intended to test both existing servers and explore other options. ^[raw/inbox/2026-09-07.md]
- [Token desync — 2026-09-08 server restart](wiki/token-desync-2026-09-08.md) — On 2026-09-08, after both local servers came back up, Hermes found the `/token` endpoint returning a stale value different from the newly written token file. Th
- [Watch process data-overwrite restart — 2026-09-09](wiki/watch-process-overwrite-2026-09-09.md) — On 2026-09-09, Hermes observed that a running watch process was overwriting files with old data, creating a stale-data consistency issue in the raw→wiki compila

### Comparisons

- [Local servers — 2026-09-07](wiki/local-servers-2026-09-07.md) — | Server | Port evidence | Status notes | Source |

### Queries

- [Bonsai MLX viability](wiki/bonsai-mlx-viability.md) — After Colibri was ruled out for standard `mlx_lm`, Hermes said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md] On 2026-09-08, Herm
- [What triggers SIGKILL in mlx_lm server during long prompt processing: cache limits, memory pressure, or timeout?](wiki/mlx-lm-large-prompt-kill-causes.md) — Chris hit a hard kill after 40k tokens on the ornith `mlx_lm` server; knowing the cause informs whether to tune cache, add swap, or switch servers.

---

## SKILLS

Topic skills stored in this wiki:

- **[stale-process-kill-rescan](skills/stale-process-kill-rescan/SKILL.md) — Use when a watch/scan process is overwriting files with old data after a code update, or when scan output JSON diverges from PRINT output (e.g. skills

---

## BOTS

Proposed bots:

- **[bonsai-mlx-probe](agents/bonsai-mlx-probe.md.proposed) — **I see you've been chasing a local inference backend that isn't standard mlx_lm — want a bot that probes Bonsai MLX against the ornith model and repo
- **[gpu-memory-tuner](agents/gpu-memory-tuner.md.proposed) — **I see your local and remote inference keeps hitting GPU memory walls — want a bot that profiles mlx_lm and Flash Next memory use and tunes context/c
- **[local-inference-monitor](agents/local-inference-monitor.md.proposed) — **I see you're testing local inference endpoints and hitting SIGKILL on large prompts — want a bot that monitors mlx_lm server health, port drift, and
- **[local-inference-porter](agents/local-inference-porter.md.proposed) — **I see you're still fighting churn between ornith and MTPLX on 11613 — want a bot that watches your local endpoints and keeps a live port map?**
- **[omarchy-plugin-ui](agents/omarchy-plugin-ui.md.proposed) — **I see you're building a plugin UI for Omarchy's remote inference stack — want a bot that builds that Omarchy plugin UI fronting nginx :8080 → model 
- **[prompt-cache-cleanup](agents/prompt-cache-cleanup.md.proposed) — **I see your Mac's prompt cache fills from accumulated test history and forces restarts — want a bot that clears and schedules prompt-cache maintenanc
- **[remote-stack-watchdog](agents/remote-stack-watchdog.md.proposed) — **I see you now run inference over a remote stack (nginx :8080, model server :8100, Tailscale) — want a bot that watches those endpoints plus GPU memo


---

## LOOPS

Proposed loops:

- **[gpu-memory-watch](loops/gpu-memory-watch.md.proposed) — owner: local-inference-monitor · cadence: hourly · status: SUGGESTED
- **[large-prompt-regression](loops/large-prompt-regression.md.proposed) — owner: teknium · cadence: once per server config change · status: SUGGESTED
- **[local-endpoint-verification](loops/local-endpoint-verification.md.proposed) — owner: local-inference-monitor · cadence: every 30m · status: SUGGESTED
- **[local-server-health-check](loops/local-server-health-check.md.proposed) — owner: looker · cadence: every 30 minutes while servers are expected up · status: SUGGESTED
- **[local-watch-process-monitor](loops/local-watch-process-monitor.md.proposed) — owner: klerik · cadence: every 10m · status: SUGGESTED
- **[remote-stack-health-tick](loops/remote-stack-health-tick.md.proposed) — owner: local-server-health-check · cadence: every 30m · status: SUGGESTED
