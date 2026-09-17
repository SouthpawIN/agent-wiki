---
title: Event-driven trigger gaps identified 2026-09-07
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [query, infra, bot, loop, gap]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Event-driven trigger gaps identified 2026-09-07

Hermes summarized **still-likely gaps** in the event-driven path on 2026-09-07 18:10. These gaps are work, not questions.

## Remaining gaps

### Topic-agent trigger

**Gap:** The topic agent still fires on a 5-minute timer, not on WatchPaths-triggered new inbox writes. The desired event-driven switch has not landed.

**What's needed:** A loop that triggers `topic-agent.py` on new `raw/inbox/<day>.md` writes instead of the timer. The watcher's WatchPaths mechanism could emit an event when a new topic is scaffolded (per [[topics/senter/wiki/entities/umbrella|umbrella]]), but the topic agent itself needs a trigger.

**Status:** Documented. See [[topics/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|2026-09-08 query]] for reaffirmation.

### Bot/research apply paths verification

**Gap:** Only the loop path is proven landed (cron `e6e20c22e1b9` on klerik, 2026-09-05 18:20). The bot and research paths exist in [[topics/senter/wiki/concepts/approval-apply-paths|approval apply paths]], but their full execution has not been landed and verified.

**Bot path:** Does `hermes profile create` + SOUL/AGENTS write correctly and land in the wiki? Has this been end-to-end tested?

**Research path:** Does looker actually write answers into the wiki page the question came from? Has this been proven?

## Related pages

- [[topics/senter/wiki/entities/topic-agent|topic agent]]
- [[topics/senter/wiki/entities/watcher|watcher]]
- [[topics/senter/wiki/concepts/approval-apply-paths|approval apply paths]]
- [[topics/senter/wiki/entities/umbrella|umbrella]]
- [[topics/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]]

^[raw/inbox/2026-09-07.md]