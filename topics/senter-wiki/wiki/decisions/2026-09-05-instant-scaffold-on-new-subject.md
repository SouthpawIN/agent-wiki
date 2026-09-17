---
title: Decision 2026-09-05: a new subject scaffolds a topic and dispatches research immediately
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, loop, bot]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# Decision 2026-09-05: new subject → immediate scaffold + research dispatch

## What
"(2) a new subject triggers immediate scaffold + research dispatch to an existing bot." Detail: "a substantive message that fits no topic → watcher scaffolds `topics/<slug>/` (README, `.system`, skills/agents/loops) *and* dispatches a research run to an existing bot (looker) that writes `.system/research.md` + a Status line. No card, no waiting." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Why
Chris's standing expectation of first action in seconds and no queues; "routed/queued" reads as stalling (memory). A topic exists the moment he mentions a new domain, consistent with [[topics/senter-wiki/wiki/concepts/senter-wiki-vision|everything you talk about gets captured as Topics]].

## Actors
[[topics/senter-wiki/wiki/entities/senter-watcher|watcher]] (detect + scaffold), looker from [[topics/senter-wiki/wiki/entities/fleet-bots|fleet bots]] (research). With the LLM-wiki layer the scaffold also gets `raw/ wiki/ SCHEMA.md index.md log.md` ([[topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|layout]]).
