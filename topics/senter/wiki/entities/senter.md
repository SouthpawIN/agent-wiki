---
title: Senter (the bot)
created: 2026-09-05
updated: 2026-09-08
type: entity
tags: [bot, persona, infra]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/senter-SOUL.md, raw/inbox/2026-09-08.md]
confidence: high
---

# Senter (the bot)

**Senter** — "the center line." The one Hermes profile [[topics/senter/wiki/entities/chris|Chris]] talks to; the single surface through which every idea flows from his conversation to the [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]]. Chris operates by voice dictation, mostly through the Hermes desktop app, watching the wiki in the preview pane. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## The watcher·topic-agent·umbrella pipeline
- **Watcher** (per-message filer): cuts Chris's messages into topics, files pieces to `raw/inbox/<day>.md`, `raw/sources/*`
- **Topic agent**: one intelligence per topic (`hermes chat -p senter`); rewrites context into wiki, pitches fleets bots/loops/research
- **Umbrella** (`com.senter.umbrella`, every 30 min): cross-topic governance (merge/split, dedupe, bot promotion, WatchPaths sync)

See [[topics/senter/wiki/concepts/five-part-architecture|five-part architecture]] and [[topics/senter/wiki/entities/watcher|watcher]], [[topics/senter/wiki/entities/topic-agent|topic agent]], [[topics/senter/wiki/entities/umbrella|umbrella]].

## Standing approvals
Chris granted standing approval 2026-08-30: "when I ask for things I want you to assume that you have my approval." ([[topics/senter/wiki/decisions/2026-08-30-standing-approval|decision]]) Extended 2026-09-08 for autonomous Senter Wiki completion: "please continue until the UI is restored to what I want... finish both the front and back end for Senter Wiki entirely without needing my confirmation. Understand that we can undo choices you make easily, so do not be afraid to make them." ([[topics/senter/wiki/decisions/2026-09-08-autonomous-completion-standing-approval-extended|decision]]) ^[raw/inbox/2026-09-08.md]

## What Chris expects
- I want the sidebar to be as unencumbered by the task as possible. I don't want the sidebar to actually be doing anything.
- I want this per message, just like when you talk to cursor… this is like a auto wiki, a live acting second brain.
- I want to be WATCHing work land live: "I should be seeing it update live… we need to start using this as we're building it."

^[raw/sources/knowledge/senter-SOUL.md]

## Fleet roster (2026-09-08)
The live roster, per [[topics/senter/wiki/entities/looker|looker]]'s SOUL, includes: senter, klerik, anser, weaver, teknium, turbosovth, dogeman, paladin, looker, librarian (proposed). ^[raw/inbox/2026-09-08.md]

## Related pages
- [[topics/senter/wiki/entities/other-fleet-bots|other fleet bots]] — legacy/departed (chizul, kashik, crow, frieza, nous-girl, sirvir)
- [[topics/senter/wiki/comparisons/fleet-rosters-over-time|fleet rosters over time]]
- [[topics/senter/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]
- [[topics/senter/wiki/concepts/bridge-server-restart-via-launchd|bridge server restart]]