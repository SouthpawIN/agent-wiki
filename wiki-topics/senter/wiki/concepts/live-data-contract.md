---
title: Live-data contract ("spawn = visible", no timers)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, ui, infra, decision]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Live-data contract ("spawn = visible", no timers)

Two of Chris's hard rules for the [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] and its daemons. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## No BAKED collections — "spawn = visible"
The BOTS page missed weaver and paladin for hours because `LIVE_BOTS`/`LIVE_SKILLS` were constants baked into the HTML at v10 while integrations had already moved to a live loader. Rule: any list the wiki shows (topics, skills, bots, loops, integrations) loads from `.system-live.json` via the [[wiki-topics/senter/wiki/entities/senter-bridge|bridge]]; the scan re-runs on a filesystem `fleet/changed` event, not by hand; fallback is a labeled `cached · <age>` copy, never a static list. When Chris says "the new X aren't showing up," grep the product file for `const LIVE_` / hardcoded arrays FIRST. Details: skill `references/live-data-contract.md`.

## No dummy data
"No dummy data" is a hard rule: render from the live source; label any static fallback `static · fallback`; "on disk" ≠ "connected", "present" ≠ "usable" — the integration scan once omitted the nous OAuth (the provider everything runs on) and counted unconfigured plugins as available. Chris on 2026-09-05: "Not a demo playthrough I want to actually be live to the music." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## "Live live live — no timed loaders"
Inventory every timer and convert each to an event; survivors must be labeled fallbacks. Found: 5 wiki intervals (12 s demo hero rotate, 9 s demo twinkles, 60 s reload heartbeat, 15 s age stamp, an unexplained 1.2 s `apply`) + feed POLL 300 s, dispatch 5 s, sentinel 30 s. Rule (in `wiki-topics/senter/process/build-loop.md`): filesystem change → watcher → SSE; provider event → webhook/WebSub/ETag long-poll → SSE; bot action → hook → SSE. A timer may remain only if it (a) engages when the push channel is down, (b) is labeled in the UI (`fallback · polling`), (c) is listed with its justification; the [[wiki-topics/senter/wiki/concepts/reflect-loop|REFLECT loop]] gets a detector for new unlabeled timers. Honest exception: GitHub without a public URL → notifications long-poll honoring `X-Poll-Interval`, labeled. Feeds are event-driven; timed polling only as a labeled fallback.

## Why it matters
It is what lets Chris "watch the wiki move around on its own" — the [[wiki-topics/senter/wiki/entities/watcher|watcher]] files per message and the UI must reflect it without a refresh.
