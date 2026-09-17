---
title: Senter Agent runtime, SENTER.md and the sandbox
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [repo, spec, plan]
sources:
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md
  - raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/README.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/android-surface/README.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/ANDROID.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/EIKON.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/HERM_FRONTEND.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/PETDEX.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/STS.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/base/CHAT.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/base/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/base/SESSIONS.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/media/MEDIA.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/research/RESEARCH.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/wallet/WALLET.md
confidence: medium
---

# Senter Agent runtime, SENTER.md and the sandbox

## The split
"SENTER.md is the declarative language/context layer. Senter Agent is the agent that interprets and operates on it." Markdown source → Context → Skills → Agents → proposed Loops → Hermes sandbox or explicitly approved runtime. `SENTER.md` "does not grant permissions by itself." ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md] ^[raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md]

## Identity
- **Senter Agent** = the runtime, personified in the Herm TUI by the **three-eyed owl Eikon**.
- **STS auxiliary** = an unnamed, tool-free speech-to-speech task of Senter — "not a separate agent".
- **Herm frontend** = sandboxed UI with the owl Eikon and a live Wiki sidebar. ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md]

## All-caps modules
An all-caps filename (`MEDIA.md`, `WALLET.md`, `RESEARCH.md`) is a user-authored GOOP module and context boundary with `## Purpose / Allowed / Forbidden / Approval / Secret References`. "The Markdown declares policy; Hermes and the sandbox must enforce it." No raw card numbers, CVVs, keys in any module — reference a secret manager. ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/wallet/WALLET.md]

Shipped profiles: `base/` (SENTER, CHAT, SESSIONS building blocks), `media/` (live-video editing, footage slicing, B-roll, graphs, overlays, infographics — preserve source footage, approval before publish/delete), `research/` (never invent citations), `wallet/` (policy-only, no agent). Selected via `GOOP_PROFILE=media` → `SENTER_GOOP_PROFILE`. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/media/MEDIA.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/research/RESEARCH.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/profiles/base/CHAT.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/README.md]

## MVP boundary
"The current implementation parses Markdown and writes a human-editable proposal queue" (`python -m senter_agent.cli . --json --queue .system/proposals.md`). It creates no profiles, skills, crons, webhooks or containers; adapters are approval-gated. Roadmap: reconciliation/redundancy detection, rule manifests, persistent proposal queue + audit trail, Kanban, safe adapters, owl Herm frontend, STS for Android, media pipeline as a topic. ^[raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md]

## Sandbox contract
"Never modify `~/.hermes/hermes-agent/` or the running Hermes installation." Layout: pinned submodules `hermes-agent/`, `herm-sovth/` (Southpaw OpenTUI frontend), `hermes-android/` (prebuilt APK + Termux only, no Gradle source), disposable `hermes-home/`, `goop/`, `docker/`. Image tags `senter-agent:{base,media,wallet,research}`; credentials injected at runtime, never baked. Optional Android emulator sidecar (`docker-android:api-33`, ADB :5555); the bridge allows one approved screenshot/tap/swipe/text per request, 15 s timeout, 10 MB cap, no raw ADB/shell/root. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/README.md]

## Surfaces
- **Herm frontend** (`HERM_FRONTEND.md`): owl default Eikon; sidebar shows SENTER.md context, active topic, related topics, skills, proposed agents/loops, proposal queue, Kanban, unread injections; centre canvas with draggable blocks (`SESSIONS.md`, `CHAT.md`, `SENTER.md`, …). ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/HERM_FRONTEND.md]
- **Eikon** (`EIKON.md`): `owl-animated-24fps`, 192×96, states idle/thinking/speaking; six Herm states alias onto three (listening/working→thinking, error→speaking). "Do not redesign the owl." ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/EIKON.md]
- **Android** (`ANDROID.md`, browser prototype at :8765): side button → compact STS bar; tap = send, double-tap = screenshot (permission-gated), drag up = full canvas with block sidebar. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/ANDROID.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/android-surface/README.md]
- **Petdex** (`PETDEX.md`): presentation-only mascot via `hermes pets …`; falls back to the static owl. Whole-flow map idle→idle, thinking/listening/working→run, speaking→done, error→error. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/PETDEX.md]
- **STS** (`STS.md`): STT/TTS are adapters, not tool runners; audio capture caller-owned. ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/STS.md]

## Integrated status
Unified Wiki `~/.hermes/wiki/` implemented; runtime + planner implemented (planner "constrained"); Herm TUI built/tested; Android prototype + prebuilt APK exercised on emulator; STS specified. Blockers: no Gradle tree; owl reference HTML missing from checkout. ^[raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md]

Lifecycle everywhere is Collect → Generate → Evaluate → Apply ([[wiki-topics/senter-wiki/wiki/concepts/factory-pipeline-gepa|factory pipeline]]); policy-in-Markdown is the [[wiki-topics/senter-wiki/wiki/concepts/markdown-is-the-api|Markdown is the API]] principle. The proposal-only default is the ancestor of today's [[wiki-topics/senter-wiki/wiki/concepts/approval-policy|approval policy]].

Relationship to this topic: this repo-level plan predates the live vault UI; the live [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]] preview pane, corner feed and petdex "running" pets are the surviving expression of the "wiki sidebar" idea. Confidence medium because none of these documents were re-verified on 2026-09-05. ^[raw/sources/knowledge/agent-wiki-repo/INTEGRATED_STATUS.md]
