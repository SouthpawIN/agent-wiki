---
title: "2026-09-05 — Per-message watcher, not per-session (\"like Cursor\")"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, loop, timeline]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-05 — Per-message watcher, not per-session ("like Cursor")

**What.** Asked "Watcher granularity: every message, or session-end summaries + tool results?", Chris (16:35) answered: **"I want this to be fast paced… live editing just like cursor. So everything that I talk to in the sidebar, I should be able to watch the wiki move around on its own, edit on its own, skills and bots and loops getting proposed all the time. So, not per session, I want to per message, just like when you talk to cursor every message at its code base… this is like a auto wiki, a live acting second brain."** ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Result (16:37).** The [[wiki-topics/senter/wiki/entities/watcher|watcher]] went live as a launchd service tailing Hermes's message table per message, filing under the best topic with a feed card, parking misfits in `_inbox/unsorted.md`, proposing a skill every 12 filings. The inbox header of this very raw file records it: "Filed by the watcher per message (Chris 2026-09-05: 'per message, like Cursor')."

**Companion choices made the same turn.** Per-topic async workers (`hermes -p senter <topic>`) + one opinionated umbrella senter cron; `hermes kanban` claims prevent collisions; skills drafted as real `.proposed` files until approved; approvals via `hermes serve` next. Chris: "build out Senter Wiki per all the context, resources, links, and your understanding of it so far." Then 17:01: "you need to continue going. You're not done yet."

**Why.** Cadence is the product: Chris wants to see the second brain act while he speaks ([[wiki-topics/senter/wiki/concepts/cursor-for-markdown|Cursor for markdown]]). Slower loops (REFLECT every 2 h, session-end exports) remain as complements, not the primary path.

**Tightened 17:18.** Proposals must come even faster and reach bots: "bots need to trigger a lot sooner… if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it." See [[wiki-topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|flywheel]].
