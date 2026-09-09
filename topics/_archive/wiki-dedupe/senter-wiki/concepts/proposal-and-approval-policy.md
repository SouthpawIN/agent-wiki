---
title: Proposals and approvals: what needs Chris and what auto-applies
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [decision, spec, infra]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
confidence: high
---

# Proposal & approval policy (as of 2026-09-05 17:25)

## Rule
**Only bots and loops** remain `.proposed` with APPROVE/REJECT — *"they cost money and run unattended."* **No approvals for topics, edits, continuity, or skills** — they
auto-apply (5 pending skills were promoted; the topic-worker now writes `SKILL.md` directly). ([[topics/senter-wiki/wiki/decisions/2026-09-05-approvals-only-bots-and-loops|decision]]) ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Surface
Proposals must be *"visible in the wiki — rows in SKILLS/BOTS/LOOPS marked proposed, so you can see them get proposed."* Proposed rows show a hollow ring + PROPOSED tag;
the pinned card gets **APPROVE** (attention yellow) / **REJECT**. Each pitch is one card — *"one card per proposal so the feed moves constantly."* Bridge `POST /approve` does
exactly two things: drop `.proposed` or delete. Skill: `senter-proposal-pipeline`. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

## Pending on Chris at 17:14
5 skills (since auto-applied), 1 bot (`senter-wiki-bot`), 1 merge (senter-wiki → senter), 2 dedupes. *"Your call on the merge especially — the umbrella says one subject,
I kept them apart."* Veto → `topics/_global/.system/keep-separate.md`. See [[topics/senter-wiki/wiki/decisions/keep-senter-and-senter-wiki-separate|the merge question]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Lineage
Spec (July): every factory output proposal-gated; `SENTER_AGENT.md` MVP was *"deliberately proposal-only."* 09-05 relaxed it for cheap, reversible artifacts and kept the gate
where money and unattended execution start. Not done: kanban claims (lock files for now); `hermes serve approval.*` transport (bridge `/approve` is the stand-in);
sidebar SOUL rewrite (text proposed in `agents/README.md`). ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

Related: [[topics/senter-wiki/wiki/entities/umbrella|umbrella]], [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]].
