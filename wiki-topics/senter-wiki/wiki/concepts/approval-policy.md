---
title: Approval policy — only bots and loops need APPROVE; everything else auto-applies
aliases:
  - "Proposals and approvals: what needs Chris and what auto-applies"
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [decision, spec, infra]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Approval policy — only bots and loops need APPROVE

## Current rule (Chris, 2026-09-05 ~17:19)
"No approvals for topics, edits, continuity, or skills — they auto-apply … Only bots and loops remain `.proposed` with APPROVE/REJECT — they cost money and run unattended." Formalised in [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-approvals-only-bots-and-loops|decision]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Mechanics
- Proposals are `.proposed` files in the topic lanes; the [[wiki-topics/senter-wiki/wiki/entities/scan-topics|scanner]] renders them as rows with a hollow ring + PROPOSED tag in SKILLS/BOTS/LOOPS; the pinned card gets **APPROVE** (`#FFE45A`) / **REJECT**. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|Bridge]] `POST /approve` "does exactly two things — drop `.proposed` or delete." `hermes serve approval.*` transport is the eventual path; the bridge is the stand-in. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- "Each pitch is one card with APPROVE/REJECT" in the [[wiki-topics/senter-wiki/wiki/entities/corner-feed|corner feed]]; one card per proposal so the feed moves constantly. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Topic-merge vetoes go in `wiki-topics/_global/.system/keep-separate.md`. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Lineage
Spec-era: the Senter Agent planner was "read-only and proposal-only"; profile creation, cron/webhook deployment and live skill writes "require a later approval/enforcement layer". ^[raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md] The 09-05 rule is that layer, narrowed to the two costly primitives.

## Standing user authority
Chris's memory-level rule: act first; confirm only spending, deletion, publishing. Scanner restarts (kill running agents) still need his approval each time. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## What was waiting on him at 17:14
5 skills (auto-promoted minutes later), 1 bot (`senter-wiki-bot`), 1 merge (senter-wiki → senter), 2 dedupes. See [[wiki-topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Folded from `proposal-and-approval-policy`
(as of 2026-09-05 17:25)

- Rule detail: skills auto-apply — 5 pending skills were promoted; the topic-worker now writes `SKILL.md` directly. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Surface: proposals must be *"visible in the wiki — rows in SKILLS/BOTS/LOOPS marked proposed, so you can see them get proposed."* Skill: `senter-proposal-pipeline`. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]
- Pending at 17:14, the merge question: *"Your call on the merge especially — the umbrella says one subject, I kept them apart."* See [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|the merge question]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Lineage: Spec (July): every factory output proposal-gated; `SENTER_AGENT.md` MVP was *"deliberately proposal-only."* 09-05 relaxed it for cheap, reversible artifacts and kept the gate where money and unattended execution start. Not done: kanban claims (lock files for now); `hermes serve approval.*` transport (bridge `/approve` is the stand-in); sidebar SOUL rewrite (text proposed in `agents/README.md`). ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

Related: [[wiki-topics/senter-wiki/wiki/entities/umbrella|umbrella]], [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]].

## Absorbed
- `concepts/proposal-and-approval-policy` — 2026-09-05 → archived at `wiki-topics/_archive/wiki-dedupe/senter-wiki/concepts/proposal-and-approval-policy.md`
