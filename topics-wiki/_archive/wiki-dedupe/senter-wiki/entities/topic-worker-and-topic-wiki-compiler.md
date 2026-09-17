---
title: topic-worker.py and topic-wiki.py
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, infra]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
confidence: high
---

# topic-worker.py → topic-wiki.py

Two backend passes built 2026-09-05, both run as `hermes -p senter` over a topic's unprocessed raw. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## topic-worker (`assets/topic-worker.py`, launchd every 5 min)
One real senter run per topic over the watcher's inbox, GEPA **collect → generate → evaluate → apply**. First pass on Chris's actual messages produced
5 skill proposals (e.g. `sidebar-rubber-duck` quoting him verbatim as evidence) and 8 continuity lines. Originally wrote `.proposed` only; after the
policy change it writes `SKILL.md` directly ([[topics-wiki/senter-wiki/wiki/concepts/proposal-and-approval-policy|approval policy]]). Also stages every edit/proposal as a `wiki` event. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## topic-wiki compile (`assets/topic-wiki.py`, launchd `com.senter.topic-wiki`, every 15 min)
*"Every topic is now a Karpathy-style LLM wiki"*: one senter run per topic over unprocessed raw items → pages created/updated → `index.md` rebuilt →
feed card + the wiki visibly opens that topic. All 19 topics initialised; the first two real compiles (senter, senter-wiki — 5 MB of raw) ran in the
background, *"several minutes each."* Full session transcripts are NOT compiled per pass — grepped on demand. ^[raw/inbox/2026-09-05.md]

## Superseded by topic-agent
Loop page `triggers-loops/topic-agent.md`: ONE agent per topic owns the lifecycle — rewrites raw into `wiki/`, then immediately pitches action (bots → loops → research)
as one card each. Replaces topic-worker + the compile loop. ^[raw/inbox/2026-09-05.md]

See also [[topics-wiki/senter-wiki/wiki/entities/umbrella|umbrella]] and [[topics-wiki/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]].
