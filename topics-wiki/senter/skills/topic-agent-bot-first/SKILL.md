---
name: topic-agent-bot-first
description: Use when a topic worker distils inbox context. One agent per topic rewrites context into the wiki, then proposes bots FIRST, loops next — no skill-count gate.
version: 0.1.0
distilled: 2026-09-05 17:48
topic: senter
---
# topic-agent-bot-first
# Topic agent: bot-first proposals (Chris 2026-09-05 17:46)

Supersedes the 'wait for >=3 related skills before proposing a bot' gate for PROPOSALS (the gate stays for silent creation).

## Steps per tick
1. Read `topics-wiki/<t>/.system/inbox.md` (watcher-cut pieces of the live sidebar session). Do not expect a hand-off.
2. Rewrite ALL inbound context into the topic's structured wiki (llm-wiki style pages), never a one-line summary.
3. Immediately propose ACTION as sidebar cards, in this order: (a) research offer for a new subject, (b) a bot that could own the craft ('I see you're talking about video creation — want something that edits / makes shorts?'), (c) a loop once the bot has a stable workflow. Skills are recorded as they fall out of the bot's work.
4. Reuse before create: an existing researcher/bot is refined, not duplicated.

## Rules
- ONE agent owns the topic lifecycle end-to-end; no umbrella/worker split ('I don't like the separation').
- Proposals are suggestions surfaced to the user, never silent spawns; no approval needed for wiki self-edits, only spend/delete/publish.
- Fire on first appearance of a subject; do not wait for recurrence or skill counts.
- Chris's examples are illustrations of tone, not literal build orders.

## Evidence
> I don't like the separation. How I imagine that it should happen is that the watcher is watching my conversation with the sidebar, watching the session's live, and is just cutting out pieces that are by topic
> We shouldn't have to wait till there's a bunch of skills. The bots is how it should suggest action, bots and then loops.
> I want to be sending the user notifications like, hey, do you want to research this? Do you want to create a bot that's able to do this kind of thing
> skills and bots and loops getting proposed all the time
