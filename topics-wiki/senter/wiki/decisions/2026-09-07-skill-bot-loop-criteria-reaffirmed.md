---
title: Skill-vs-bot-vs-loop decision criteria (reaffirmed 2026-09-07)
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, bot, loop, skill, spec]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-05.md]
confidence: high
---

# Skill-vs-bot-vs-loop decision criteria (reaffirmed 2026-09-07)

The five-part architecture already defines these four tiers explicitly. On 2026-09-07, Hermes noted the need to add them explicitly to the architecture and topic-agent wording; the content is already decided, so this page preserves the canonical wording rather than reopening it. ^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-05.md]

## Canonical criteria

- **Skill** — reusable ability that belongs on an existing bot or in Hermes itself. If it is narrow, repeatable, and does not need its own memory/profile, it is a skill.
- **Bot** — needs its own persistent identity, memory, or runtime. If it must remember prior turns, own a schedule, or spend money/resources unattended, it is a bot.
- **Loop** — time/event-driven workflow owned by a bot. If it runs on cron/kanban and produces artifacts without Chris in the loop, it is a loop.
- **Wiki** — the topic's full knowledge layer; everything the topic knows about itself, including transcripts, decisions, and references.

## History

- 2026-09-05 17:18 and later sessions used these exact tiers while Chris corrected the order from skills-first to bots-first for proposals.
- 2026-09-07 18:10–18:16 surfaced the rename/restructure question without changing the criteria themselves.

## Contested point

The 2026-09-05 evening revision still stands: proposals should fire bot/loop first, not wait for skills to accumulate (see [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]], contested section).

## Related
- [[topics-wiki/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|One agent per topic, no separation]]
- [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]]
