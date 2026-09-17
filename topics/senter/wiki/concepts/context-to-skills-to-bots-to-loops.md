---
title: Context → skills → bots → loops (the flywheel)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, loop, skill, bot, idea]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-05.md, raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
contested: true
---

# Context → skills → bots → loops (the flywheel)

The four lanes of Chris's agent-wiki spec (Context/Topics → Skills → Bots → Loops) read as a *process*: each topic runs a loop that turns raw context into skills, clusters skills into a bot, and lets a stable bot suggest its own loop. Chris, 2026-09-05: ^[raw/inbox/2026-09-05-legacy-inbox.md]

> "each of these topics are going to have their own loops where they turn context into skills, just like Hermes agent already does. And then when there's enough related skills where there needs to be an intelligence around that craft, then it groups those into a bot. When the bot is optimized where it has a workflow, then it should suggest a loop. And all of this, all the approvals need to go to the sidebar chat."

## The stages
1. **Context** — everything filed per message by the [[topics/senter/wiki/entities/watcher|watcher]] into a topic's raw/ (plus exported sessions, SOULs, specs).
2. **Skills** — recurring rules distilled into `skills/<name>/SKILL.md` drafts (written as `.proposed` until approved); the watcher proposes a candidate every 12 filings; Hermes already does this from sessions.
3. **Bots** — "when there's enough related skills where there needs to be an intelligence around that craft"; created via [[topics/senter/wiki/entities/klerik|klerik]] with the [[topics/senter/wiki/concepts/profile-setup-checklist|setup checklist]]; gated by [[topics/senter/wiki/entities/anser|anser]] for redundancy.
4. **Loops** — a bot with a stable workflow suggests a loop (`hermes cron`); loops can also be QA (looker), reflection ([[topics/senter/wiki/concepts/reflect-loop|REFLECT]]) or umbrella governance.

## Chris's tempo requirement (17:18)
"bots need to trigger a lot sooner… if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it… use maybe a bot that we've used before to research a different subject, or create a new one… I want the user to only have to be able to talk about their ideas to the site chat and this entire agentic, fleet and knowledge-based coordination self-edits and proposes."

## Contested: does a bot wait for skills? (16:29 vs 17:46, same day)
- **16:29:** "when there's enough related skills where there needs to be an intelligence around that craft, then it groups those into a bot" — skills accumulate first, bots emerge from clusters.
- **17:46:** "We shouldn't have to wait till there's a bunch of skills. The bots is how it should suggest action, bots and then loops." — bots are *proposed* on first sight of a subject; skills fall out as the bot works. ^[raw/inbox/2026-09-05.md]

Reading that reconciles them: the 16:29 order describes how the *artifacts* mature; the 17:46 order describes how *proposals* fire. Stage 2 (skills) is no longer a gate on stage 3 (bots) for proposals. Later statement wins for behaviour; see [[topics/senter/wiki/concepts/proactive-suggestion-doctrine|proactive suggestion doctrine]] and [[topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|decision]]. Who runs the loop: one [[topics/senter/wiki/entities/topic-agent|topic agent]] per topic, not a worker + compiler + umbrella.

## Earlier form (2026-08-30 SOUL)
"conversation → interest → topic sort → momentum → proposal → Chris approval → bot/loop creation → outcome logged in vault" — same flywheel with Senter doing the detection by hand ([[topics/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|decision]]). The REFLECT loop (anser, 2 h detectors → proposals) is the first automated instance of stage 2→3. ^[raw/sources/knowledge/senter-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

Related: [[topics/senter/wiki/concepts/topics-are-the-work-units|Topics are the work units]], [[topics/senter/wiki/concepts/five-part-architecture|Five-part architecture]].
