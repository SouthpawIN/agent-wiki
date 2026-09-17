---
title: Sandbox & safety contract (repo)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, infra, plan]
sources:
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/README.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/ANDROID.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/EIKON.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/HERM_FRONTEND.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/PETDEX.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/STS.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/wallet/WALLET.md
confidence: medium
---

# Sandbox & safety contract

From the [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]: *"SENTER.md is never permission to modify the live Hermes installation. All Herm TUI and Hermes-Agent development
happens in a disposable, separate sandbox."* ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md]

## Boundaries
- Live Hermes protected; sandbox = clean Hermes-Agent + Herm frontend checkouts, disposable `HERMES_HOME`, Docker images `senter-agent:{base,media,wallet,research}` with GOOP
  modules mounted; *"must not contain host credentials or live session databases."* ^[raw/sources/knowledge/agent-wiki-repo/sandbox/README.md]
- **WALLET.md** pattern: Allowed (masked metadata, reports) / Forbidden (full card numbers, CVVs, purchases without approval, credentials in Markdown/images/logs/chat) /
  Approval (any transaction, external transmission, secret modification) / `secret-manager://wallet/cards`. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/wallet/WALLET.md]
- **Android** (`ANDROID.md`): side-button compact STS overlay; same icon tap-to-send / double-tap-screenshot / drag-up to expand; canvas with building blocks `SESSIONS.md`,
  `CHAT.md`, `SENTER.md`, current topic, proposal queue, Kanban. Phone operations permission-gated; never host credentials. Bridge: one approved action per request,
  15 s timeout, 10 MB cap. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/ANDROID.md]
- **EIKON.md**: the owl player `owl-animated-24fps` (idle/thinking/speaking, 192×96) is the accepted reference — *"Do not redesign the owl."* Six Herm states alias to three
  clips (listening/working→thinking, error→speaking). Malformed source fails closed. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/EIKON.md]
- **HERM_FRONTEND.md**: sandbox-only modified Herm TUI with the owl as default Eikon and a Wiki sidebar (SENTER.md context, active topic, skills, proposed agents/loops,
  queue, Kanban, unread injections); build only in `sandbox/herm-sovth/`; existing Herm tests stay green. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/HERM_FRONTEND.md]
- **PETDEX.md**: presentation-only mascot, profile-scoped under `<HERMES_HOME>/pets/`, never grants execution; falls back to the static owl. (The live wiki's running
  indicator = petdex pets bottom-left ×N.) ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/PETDEX.md]
- **STS.md**: STT/TTS are adapters, not tool runners; no shell/ADB/network/credential access. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/STS.md]

Related: [[topics/senter-wiki/wiki/concepts/goop-four-primitives|GOOP primitives]].
