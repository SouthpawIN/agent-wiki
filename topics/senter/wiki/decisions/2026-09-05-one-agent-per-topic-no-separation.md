---
title: 2026-09-05 — One agent per topic; the watcher cuts; bots first, no thresholds ("I don't like the separation")
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, loop, bot, plan, preference]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: high
contested: true
---

# 2026-09-05 — One agent per topic; the watcher cuts; bots first, no thresholds

**What.** At 17:46 [[topics/senter/wiki/entities/chris|Chris]] rejected the umbrella/worker/compiler split Hermes had built earlier in the afternoon: **"I don't like the separation."** He replaced it with a three-role picture — a [[topics/senter/wiki/concepts/watcher-as-cutter|watcher that cuts]] the live sidebar session into per-topic pieces, **one agent per topic** that rewrites everything inbound into a structured wiki *and* derives skills/bots/loops from it, and a proposal order of **bots first, then loops** with no waiting for skill counts. ^[raw/inbox/2026-09-05.md]

> "How I imagine that it should happen is that the watcher is watching my conversation with the sidebar, watching the session's live, and is just cutting out pieces that are by topic and sorting those into their topic. And then each individual topic will have its own agent that will rewrite all of that inbound context as a structured wiki. And then set that out the skills and bots and loops out of that context."

> "I was thinking that the bots has taken a little slow to be created or used. We shouldn't have to wait till there's a bunch of skills. The bots is how it should suggest action, bots and then loops."

**Why.** Two pains, both voiced the same afternoon: the pipeline felt slow ("the bots has taken a little slow to be created or used"; at 17:18 "bots need to trigger a lot sooner"), and the UI wasn't visibly moving ("I'm not seeing things move in the UI like I thought that I would"). A separate worker + compiler + umbrella meant more hand-offs and more waiting before anything was proposed. ^[raw/inbox/2026-09-05-legacy-inbox.md]

**How Hermes implemented it (17:47–17:53).** ^[raw/inbox/2026-09-05.md]
- Watcher → the cutter: each message is split at subject changes (sentence groups classified individually, re-joined when consecutive pieces agree) and each cut filed into its topic's `raw/inbox/<day>.md`. Verified on Chris's 17:46 message itself: the wiki-architecture part stayed in `senter`, the video-creation part went to `youtube`.
- New subject → immediate cards: "Want me to research it?" and "Want a bot for this?" — no thresholds.
- [[topics/senter/wiki/entities/topic-agent|`assets/topic-agent.py`]], every 5 min, replaces both the per-topic worker and the wiki compiler: one senter run that (1) rewrites new cuts + sources into the structured wiki and (2) pitches action — bots first, reusing a fleet bot when one fits (e.g. dogeman for video), then loops, then research questions.

**What it supersedes / conflicts with.**
- The 16:37 shape "per-topic workers running asynchronously, plus one opinionated umbrella" (see [[topics/senter/wiki/concepts/five-part-architecture|five-part architecture]]) — the umbrella/worker/compiler roles collapse into the topic agent. Governance (merge/split at the locked .35/.50 thresholds) is not mentioned again in the raw; where it lives now is an open question. **Corrected 18:53:** only worker + compiler collapsed; the [[topics/senter/wiki/entities/umbrella|umbrella]] (`com.senter.umbrella`, 30 min) was kept and still owns governance. ^[raw/sources/2026-09-05-umbrella-still-runs.md]
- The 16:29 flywheel sequencing "when there's enough related skills… then it groups those into a bot" is contested by 17:46 "We shouldn't have to wait till there's a bunch of skills" — recorded on [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|the flywheel page]] with `contested: true`.
- The watcher's "every 12 filings proposes a skill candidate" rule from 16:37 is dead: proposals fire on first appearance of a subject.

**Guardrail Chris attached.** The examples he gave are illustrations, not orders: "These are just suggestions. I'm not asking for these literally. These are suggestions of how I want the workflow to go." See [[topics/senter/wiki/concepts/proactive-suggestion-doctrine|proactive suggestion doctrine]].

**Status.** Built 17:53; this compile is the first output of the new topic agent for `senter`. Still open: whether 5-minute polling satisfies "per message, like Cursor" ([[topics/senter/wiki/decisions/2026-09-05-per-message-watcher|decision]]) and the [[topics/senter/wiki/concepts/live-data-contract|no-timers rule]].
