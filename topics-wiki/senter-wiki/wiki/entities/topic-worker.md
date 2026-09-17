---
title: topic-worker — per-topic GEPA proposal loop
aliases:
  - topic-worker.py and topic-wiki.py
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [loop, infra, tool]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05.md
confidence: high
---

# topic-worker — per-topic GEPA proposal loop

## What it is
`assets/topic-worker.py`, launchd every 5 min: one real `hermes -p senter` run per topic over the [[topics-wiki/senter-wiki/wiki/entities/senter-watcher|watcher's]] inbox, running the GEPA cycle collect → generate → evaluate → apply ([[topics-wiki/senter-wiki/wiki/concepts/factory-pipeline-gepa|factory pipeline]]). Originally wrote `.proposed` files only. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## First real pass (2026-09-05)
On Chris's actual messages it produced 5 skill proposals — e.g. `sidebar-rubber-duck` "quotes you verbatim as evidence and reads as a real SKILL.md" — and 8 continuity lines. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Policy change same day
After [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-approvals-only-bots-and-loops|approvals only for bots and loops]], the topic-worker writes `SKILL.md` directly (the 5 pending skills were promoted). Only bots and loops stay `.proposed`. Every worker skill/continuity write emits a `/stage` event. ^[raw/inbox/2026-09-05-legacy-inbox.md]
Also stages every edit/proposal as a `wiki` event ([[topics-wiki/senter-wiki/wiki/concepts/approval-policy|approval policy]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Staged status
Listed as PROPOSED in the loops lane when the topic was built (16:51), running by 17:14 ("The flywheel is running end to end"). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Folded from `topic-worker-and-topic-wiki-compiler`

Two backend passes built 2026-09-05, both run as `hermes -p senter` over a topic's unprocessed raw. ^[raw/inbox/2026-09-05-legacy-inbox.md]

### topic-wiki compile (`assets/topic-wiki.py`, launchd `com.senter.topic-wiki`, every 15 min)
*"Every topic is now a Karpathy-style LLM wiki"*: one senter run per topic over unprocessed raw items → pages created/updated → `index.md` rebuilt →
feed card + the wiki visibly opens that topic. All 19 topics initialised; the first two real compiles (senter, senter-wiki — 5 MB of raw) ran in the
background, *"several minutes each."* Full session transcripts are NOT compiled per pass — grepped on demand. ^[raw/inbox/2026-09-05.md]

### Superseded by topic-agent
Loop page `triggers-loops/topic-agent.md`: ONE agent per topic owns the lifecycle — rewrites raw into `wiki/`, then immediately pitches action (bots → loops → research)
as one card each. Replaces topic-worker + the compile loop. ^[raw/inbox/2026-09-05.md]

See also [[topics-wiki/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]].

Related: [[topics-wiki/senter-wiki/wiki/entities/umbrella|umbrella]] (cross-topic), [[topics-wiki/senter-wiki/wiki/entities/topic-wiki-compile-loop|topic-wiki compile loop]] (Layer-2 compile), [[topics-wiki/senter-wiki/wiki/entities/senter-agent-sandbox|Senter Agent runtime]] for the original proposal-only MVP boundary this descends from.

## Absorbed
- `entities/topic-worker-and-topic-wiki-compiler` — 2026-09-05 → archived at `topics-wiki/_archive/wiki-dedupe/senter-wiki/entities/topic-worker-and-topic-wiki-compiler.md`
