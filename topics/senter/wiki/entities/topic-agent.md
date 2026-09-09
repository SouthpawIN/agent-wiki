---
title: Topic agent (assets/topic-agent.py — one intelligence per topic)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, loop, bot, infra, spec]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: high
---

# Topic agent (`assets/topic-agent.py`)

The **topic agent** is the single intelligence that owns one vault topic end to end. Introduced 2026-09-05 17:53 as the direct answer to [[topics/senter/wiki/entities/chris|Chris]]'s "I don't like the separation" ([[topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|decision]]): it replaces both the per-topic worker (inbox → proposed skills) and the wiki compiler that Hermes had sketched at 16:37. ^[raw/inbox/2026-09-05.md]

## What Chris asked for
> "each individual topic will have its own agent that will rewrite all of that inbound context as a structured wiki. And then set that out the skills and bots and loops out of that context… when a subject is made, I want this to be very proactive."

## What was built (Hermes, 17:53)
- Lives at `~/Documents/Projects/Projects/assets/topic-agent.py`; runs **every 5 min**; one `senter` run per topic.
- Step 1 — **rewrite**: new watcher cuts (`raw/inbox/<day>.md`) + sources (`raw/sources/…`) become structured wiki pages (entities/concepts/decisions, provenance `^[raw/…]`, index), per the llm-wiki conventions in this topic's `SCHEMA.md` and the [[topics/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|CONTEXT = full LLM wiki decision]].
- Step 2 — **pitch action** from what it just read, in Chris's order: bots first ("I see you're talking about X — want a bot that does Y?"), reusing a fleet bot when one fits (dogeman for video was the worked example), then loops, then research questions. See [[topics/senter/wiki/concepts/proactive-suggestion-doctrine|proactive suggestion doctrine]].
- Skills are written when a repeatable procedure is evident; no approval is needed for wiki edits or skills ([[topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]).

## Inputs and outputs
- In: the [[topics/senter/wiki/concepts/watcher-as-cutter|cutter]]'s filings, `raw/sources/knowledge/*`, `SCHEMA.md`, `index.md`, `log.md`, and — since 19:23 — the topic's `BRIEF.md` as pre-prompt ([[topics/senter/wiki/concepts/topic-brief-pre-prompting|topic BRIEF pre-prompting]]: scope, anti-scope, lens, standing preferences).
- Out: `wiki/<section>/<slug>.md` pages, a `## [date] compile | …` line in `log.md`, and a JSON block of pitches (bots / loops / research / skills) that the wiki turns into sidebar cards; since 19:23 also `misrouted` (cuts that belong to another topic per the anti-scope) and `brief` (one-line learnings appended to BRIEF.md "## Learned").

## Relationship to the rest of the fleet
The topic agent is the per-topic form of what [[topics/senter/wiki/entities/senter|Senter]] did by hand under the 2026-08-30 conversation-first model (detect interest → sort → propose). Bot creation it proposes still goes through klerik; redundancy through anser; UI through weaver — it proposes, it does not spawn ("never spawned silently").

## Tension to watch — resolved 18:18
A 5-minute cadence is a timer. Chris's standing rules are "per message, just like when you talk to cursor" and "live live live — no timed loaders" ([[topics/senter/wiki/concepts/live-data-contract|live-data contract]]). Firing on new inbox writes instead of on a clock would satisfy both. ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Decided without a card, 18:18.** After Chris's 18:16 "Preempt decision, stop asking me for so many decisions… looking for things that aren't complete yet and complete them" ([[topics/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]), Hermes named this as one of two gaps it already knew about — "event-driven instead of 5-min timer; governance orphaned" — and took it as work: "Do them myself rather than via cards." Target state: the topic agent fires on a new `raw/inbox/<day>.md` write, not on a clock. Whether the change landed is not recorded in the raw item. ^[raw/inbox/2026-09-05.md]

## First pitches, and what they taught
The first agent run pitched exactly what Hermes already knew was missing. That is the correct output and the wrong channel: a known gap is work, not a question. The 18:16 ruling turns this into the agent's pre-pitch test — *does the wiki already answer this? then do it.* The first completion under the new rule was the [[topics/senter/wiki/concepts/loop-apply-path|loop apply path]] (approve → real cron on klerik). ^[raw/inbox/2026-09-05.md]

## The agent's memory is this wiki — and it was wrong once (18:53)
The agent "keeps pitching 'governance has no owner' — because the wiki (its memory) says the umbrella was deleted, when in fact it still runs." The [[topics/senter/wiki/entities/umbrella|umbrella]] (`com.senter.umbrella`, 30 min) was never removed; only worker + compiler were. The fix was a raw correction + recompile, not a pitch filter: [[topics/senter/wiki/concepts/fix-the-record-not-the-pitch|fix the record, not the pitch]]. Also from the same correction: the umbrella syncs this agent's launchd **WatchPaths** when the watcher scaffolds a new topic — so "event-driven on new inbox writes" is the mechanism (WatchPaths), and new topics join it automatically. ^[raw/sources/2026-09-05-umbrella-still-runs.md]

What an approved pitch now does is fixed too: loop → `hermes cron create`, bot → profile + SOUL/AGENTS, research → looker writes into the page ([[topics/senter/wiki/concepts/approval-apply-paths|approval apply paths]]).

## Prompt caps (18:58)
After the first passes flooded Chris with cards about the pipeline itself, the prompt was capped: **1 bot / 2 loops / 1 research per pass, zero infrastructure pitches, `hermes:` raw lines are evidence not requests.** 13 self-referential proposals were pruned; two useful ones kept and approved. Details: [[topics/senter/wiki/concepts/topic-agent-pitch-caps|pitch caps]]. ^[raw/inbox/2026-09-05.md]

## How it is told to think (19:23)
"Each topic declares what belongs to it and how to think about it, and the cutter/agent read it." The agent's prompt now opens with the topic's `BRIEF.md` — Chris-editable, `<!-- chris -->` lines never rewritten — so its memory has two layers: the wiki (what is known) and the BRIEF (how to read what arrives). Details in [[topics/senter/wiki/concepts/topic-brief-pre-prompting|topic BRIEF pre-prompting]]. ^[raw/inbox/2026-09-05.md]

## What it runs on (19:12)
Per Chris's 19:06 "just built in Hermes commands and markdown" ([[topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]]), the agent is already native: "the topic agent is `hermes chat -p senter` over markdown." Its pages are served to the wiki pane through the bridge `/file` allowlist, widened at 19:09 to `topics/*/wiki/*` ([[topics/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom]]). ^[raw/inbox/2026-09-05.md]
