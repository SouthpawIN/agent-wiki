---
title: GOOP v1 whitepaper vs Agent Wiki vs what runs today
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [spec, infra, timeline]
sources:
  - raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
confidence: high
---

# GOOP v1 → Agent Wiki → today's flywheel

| Dimension | GOOP v1 (2026-07-04, Anser + sovthpaw) | Agent Wiki spec (2026-07-07) | Running 2026-09-05 |
|---|---|---|---|
| Profiles | 6 persistent | Senter + STS auxiliary + 4 cron factories | one `senter` profile runs every loop; per-topic bots only when earned |
| Continuity | separate JSONL daemon | Hermes session DB | watcher tails `state.db` → `raw/inbox/<day>.md` per message |
| Injection | bespoke plugin | `.system/injections.md` + system prompt | feed cards via bridge `/post` + `wiki` stage events |
| Factories | named agents with memory | cron-triggered `delegate_task` roles | topic-worker (5 min) → topic-agent; umbrella (30 min); compile (15 min) |
| Primitives | 3 (Skills, Agents, Loops) | 4 (+ Context) | 4, Context = two-layer LLM wiki with `index.md` as the row |
| Approval | — | every factory output gated | only bots and loops gated; skills-capabilities/edits auto-apply |
| Build time | 3 months, 8 phases | *"~1 hour to wire up"* | one afternoon (09-05) for watcher→worker→umbrella→approvals→stage |
| State store | separate | *"Filesystem IS the database"* | `.system-live.json` snapshot over the vault + bridge events |
^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md] ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

Reading: the spec's promises held (markdown API, thin factories, filesystem as state); what changed in practice is *where the gate sits* and *how visibility is delivered*
(motion in the UI, not injected prose). See [[topics-wiki/senter-wiki/wiki/concepts/goop-four-primitives|GOOP primitives]], [[topics-wiki/senter-wiki/wiki/concepts/approval-policy|approval policy]].
