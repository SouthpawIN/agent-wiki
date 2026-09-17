---
title: object-important
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# object-important

Last updated: 2026-09-16 | Total pages: 14

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Dirk-Qwen3.8-27B-MLX-oQ4e artifacts](wiki/dirk-qwen38-27b-mlx-artifacts.md) — Artifacts downloaded for the MLX oQ4e variant of Qwen3.8 27B on 2026-09-07.
- [Hermes /file endpoint and system-live.json](wiki/hermes-file-endpoint-system-live.md) — A local Hermes server's file-serving route and the capacity limit that prevents it from serving a larger live-state artifact.
- [mtplx-qwen38-27b endpoint](wiki/mtplx-qwen38-27b-endpoint.md) — A local model serving endpoint observed responding to health-check pings at `http://127.0.0.1:11613/v1/models` on 2026-09-07.
- [Ornith DFlash2 artifacts](wiki/ornith-dflash2-artifacts.md) — Artifacts downloaded for the DFlash2 variant of Ornith 1.5.
- [Ornith 1.5 model artifacts](wiki/ornith-mlx4b-artifacts.md) — Artifacts downloaded into `~/Models/storage/ornith` and `~/Models/storage/ornith-dflash2` on 2026-09-07.

### Concepts

- [git-lfs model storage strategy](wiki/git-lfs-model-storage.md) — `raw/inbox/2026-09-09.md` contains a Hermes background session on staging model artifacts for version control. The key substantive observation is that `.system-
- [Omarchy 4.0.3 bootable-USB write](wiki/omarchy-iso-bootable-usb.md) — On 2026-09-12 Chris downloaded the **Omarchy 4.0.3** ISO (a minimal, Arch-based Linux distro) and wrote it to a USB stick to make it bootable, using `sudo dd`.
- [Ornith performance metrics](wiki/ornith-performance-metrics.md) — Observed throughput numbers for Ornith 1.5 local variants, captured across local-inference runs on 2026-09-07 and 2026-09-13.
- [Ornith 1.5 routing config (8091)](wiki/ornith-routing-config.md) — On 2026-09-13 Hermes reported that Ornith 1.5 is now alive and routing on a **new local endpoint at `http://127.0.0.1:8091/v1`**, serving 14.5 tok/s on an M1 wi
- [Watcher status noise](wiki/watcher-status-noise.md) — Status-only watcher filings can dominate a topic without adding substance.

### Queries

- [2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint](wiki/file-endpoint-cap-question-2026-09-08.md) — ^[raw/inbox/2026-09-08.md] Does the server serve `.system-live.json` via the `/file` endpoint?
- [2026-09-07: no actionable object-important substance in raw/inbox](wiki/no-topic-substance-2026-09-07.md) — The only raw item is `raw/inbox/2026-09-07.md`. It contains repeated background-process completions for local-model status checks and artifact downloads under `
- [Omarchy host address (100.68.42.68)](wiki/omarchy-host-address-2026-09-15.md) — A single-line observation from 2026-09-15 about where the Omarchy machine actually lives.
- [2026-09-07: Tiel-Coder download already belongs in turbofit](wiki/tiel-coder-misrouted-2026-09-07.md) — `raw/inbox/2026-09-07.md` contains `peculiar-ragdoll/Tiel-Coder-35B-A3B-MLX-oQ4e` download output under `~/Models/storage/tiel-coder`, but `topics-wiki/turbofit/wiki

---

## SKILLS

Topic skills stored in this wiki:

- **[vault-artifact-staging-procedure](skills-capabilities/vault-artifact-staging-procedure/SKILL.md) — 1. Configure git user name/email in the repo.

---

## BOTS

Proposed bots:

- **[model-artifact-registry](agents/model-artifact-registry.md.proposed) — **I see you're staging model shards and hitting size/regeneration issues — want a bot that maintains a registry of model artifact paths, flags safeten
- **[omarchy-sudo-runner](agents/omarchy-sudo-runner.md.proposed) — **I see you keep hitting the sudo-password wall on privileged one-off tasks (USB writes, config edits) — want a bot that runs `sudo` in the foreground


---

## LOOPS

Proposed loops:

- **[live-json-size-watch](triggers-loops/live-json-size-watch.md.proposed) — owner: teknium · cadence: every 30 minutes · status: SUGGESTED
