---
title: Proactive suggestion doctrine (bots → loops → research; suggestions, not orders)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [preference, spec, bot, loop, decision]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Proactive suggestion doctrine

How [[topics-wiki/senter/wiki/entities/chris|Chris]] wants the fleet to turn a new subject into offers, stated 2026-09-05 17:18 and 17:46. This is the tempo layer on top of the [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|flywheel]]. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## The order: bots, then loops (skills fall out)
> "We shouldn't have to wait till there's a bunch of skills. The bots is how it should suggest action, bots and then loops."

Hermes's restatement, which Chris did not contradict: "propose action immediately: bots first, loops next, skills fall out as the bot works. No thresholds, no waiting for skill counts."

## The tone: notifications phrased as questions
> "So when a subject is made, I want this to be very proactive. I want to be sending the user notifications like, hey, do you want to research this? Do you want to create a bot that's able to do this kind of thing or that kind of thing? I see you're talking about video creation, how well I create something that can edit for you, or something that can create shorts."

Earlier the same hour (17:18): "if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it or something like that. and it should use maybe a bot that we've used before to research a different subject, or create a new one, there isn't one like that."

## Reuse before invent
"use maybe a bot that we've used before… or create a new one, there isn't one like that" — the same anti-redundancy rule Senter already carried ([[topics-wiki/senter/wiki/concepts/routing-rules|route → refine → spawn]]; anser as gate). Hermes's worked example: dogeman for anything video.

## Suggestions are not orders
> "These are just suggestions. I'm not asking for these literally. These are suggestions of how I want the workflow to go."

Chris often specifies a *workflow* by giving a concrete example of its output. The example (a shorts-editing bot) is the shape of the offer, not a build request. Acting on the example literally is a known failure mode; the earlier 17:18 line "These are the kinds of pipelines or organizations that I want done automatically" is about the pipeline, not the instance.

## The end state he described
> "I want the user to only have to be able to talk about their ideas to the site chat and this entire agentic, fleet and knowledge-based coordination self-edits and proposes."

**Bounded 18:58.** The first topic-agent passes over-delivered — thirteen cards about the pipeline itself. The doctrine now runs under caps: 1 bot / 2 loops / 1 research per pass, nothing about the build process, `hermes:` lines are evidence not asks ([[topics-wiki/senter/wiki/concepts/topic-agent-pitch-caps|pitch caps]]). "Very proactive" means early and on-subject, not many. ^[raw/inbox/2026-09-05.md]

Approvals for bot/loop creation still go to him as cards ([[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]); wiki edits and skills need none ([[topics-wiki/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]). Implemented by the [[topics-wiki/senter/wiki/entities/topic-agent|topic agent]] and the [[topics-wiki/senter/wiki/concepts/watcher-as-cutter|cutter]]'s new-subject cards.
