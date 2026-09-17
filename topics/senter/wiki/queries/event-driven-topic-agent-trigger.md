---
title: Event-driven topic-agent trigger verification (2026-09-09)
created: 2026-09-09
updated: 2026-09-09
type: query
tags: [query, infra, bot, loop, gap, verification]
sources: [raw/inbox/2026-09-09.md]
confidence: low
---

# Event-driven topic-agent trigger verification (2026-09-09)

**The question.** The topic agent (`assets/topic-agent.py`) still fires on a 5-min timer, not on WatchPaths-triggered new inbox writes. This gap, identified at 2026-09-05 18:18, remains unresolved.

## What's needed

A loop or mechanism that triggers `topic-agent.py` on new `raw/inbox/<day>.md` writes instead of the timer. The watcher's WatchPaths mechanism could emit an event when a new topic is scaffolded, but the topic agent itself needs an event-driven trigger.

## Evidence from 2026-09-09

From `raw/inbox/2026-09-09.md`:

> "Let me verify the bridge server is still running correctly and check if there are any other pending issues"

> "Live Data Pipeline Verified
- Bridge server is running and healthy
- `/system-live.json` is served correctly via `/file` endpoint
- Data shows: 35 topics, 69 bots, 201 skills, 81 loops
- senter-wiki topic now properly populated"

The bridge health verification confirms the pipeline is working, but does not address the topic-agent trigger mechanism.

## Status

**Open.** The event-driven topic-agent trigger has not landed. See also [[topics/senter/wiki/queries/verify-apply-paths-and-watchpaths-landed|verify apply paths and WatchPaths landed]].

## Related

- [[topics/senter/wiki/entities/topic-agent|topic agent]]
- [[topics/senter/wiki/entities/watcher|watcher]]
- [[topics/senter/wiki/concepts/watcher-as-cutter|watcher as cutter]]
- [[topics/senter/wiki/entities/umbrella|umbrella]] (syncs WatchPaths with new topics)
- [[topics/senter/wiki/concepts/event-driven-trigger-gaps-2026-09-07|event-driven trigger gaps 2026-09-07]]
- [[topics/senter/wiki/concepts/event-driven-trigger-gaps-2026-09-08|event-driven trigger gaps 2026-09-08]]