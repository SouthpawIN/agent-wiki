---
title: "2026-09-05 — The wiki is Hermes's memory layer: all of it, not summaries"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, idea]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-05 — The wiki is Hermes's memory layer: all of it, not summaries

**What.** Chris, 16:22: **"this is supposed to be basically a memory layer for Hermes agent… populate center and center wiki with all of the context that we have so far… these aren't supposed to be summaries going into the context It's supposed to be all of it and then we're… gonna work through making the sidetrack be aware of everything as it goes probably with progressive disclosure."** ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Two shapes floated by Chris.** "either the side chat could be with an auxiliary agents and this whole wiki could be one giant agent that self-managing it that's doing progressive disclosure like how skills are discovered." Hermes's option 3 ("the wiki as one self-managing agent profile (`senter`)") maps to the latter; undecided.

**Done the same hour (16:26).** `topics-wiki/senter-wiki` received 7.4 MB of raw memory (9 full session exports since Aug 27 via `hermes sessions export --format md`, the agent-wiki-vault skill + 10 references, bridge and scanner source, the Anser interview); `topics-wiki/senter` received SOUL + AGENTS for senter/klerik/looker/weaver/paladin/anser and the fleet-coordination skill — i.e. this wiki's `raw/`. `build-index.py` → `.system/INDEX.md` for [[topics-wiki/senter/wiki/concepts/progressive-disclosure|progressive disclosure]]; the `agent-wiki-vault` skill carries "if it isn't in the wiki it isn't remembered."

**Why.** Everything the [[topics-wiki/senter/wiki/entities/senter|sidebar]] and the bots know should live in the topics, readable on demand — the generalization of the 2026-08-31 [[topics-wiki/senter/wiki/concepts/selfmodel-layer|self-model layer]] from Senter alone to every topic.

**Follow-ups.** [[topics-wiki/senter/wiki/decisions/2026-09-05-per-message-watcher|Per-message watcher]] (how memory gets in); [[topics-wiki/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|Context = full LLM wiki]] (how it is compiled and shown). Open: who reads INDEX first automatically (AGENTS.md instruction vs `on_session_finalize` hook vs a self-managing profile).
