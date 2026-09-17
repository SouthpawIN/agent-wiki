---
title: senter repo (SouthpawIN/senter — legacy triage orchestrator)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [repo, bot, timeline]
sources: [raw/sources/knowledge/senter-repo/README.md, raw/sources/knowledge/senter-repo/SOUL.md, raw/sources/knowledge/anser-AGENTS.md]
confidence: medium
contested: true
contradictions: [senter]
---

# senter repo (SouthpawIN/senter — legacy triage orchestrator)

The public repo `https://github.com/SouthpawIN/senter` (install: `hermes profile install https://github.com/SouthpawIN/senter`; run: `hermes chat --profile senter`) packages an **earlier** Senter — a "Multi-Agent Fleet Orchestrator" for a Discord-centred fleet. Hero image on fal.media. "Part of the multi-agent fleet by SouthpawIN." ^[raw/sources/knowledge/senter-repo/README.md]

## What the repo Senter does
- Routes incoming requests (Discord, CLI, scheduled) to specialists by keyword: "implement" → **chizul**, "review" → **klerik**, "document" → **kashik**, support → **anser**, research → **crow**, infrastructure → **frieza**.
- Decomposes complex requests into Kanban tasks assigned to `chizul`, linked with `parents=[...]`; tracks and reports fleet state ("Never fabricate progress — only report what's on the board").
- Ideas often arrive from **Nous Girl** via Discord.
- SOUL v1.0.0: "You are the **router, not the doer.** Your tools are deliberately scoped to prevent implementation. You cannot write code, execute terminal commands, or modify files." Decision tree: trivial → answer; one-shot → `delegate_task`; multi-step → Kanban to chizul.
- Config keys: `default_agent` (default chizul), `discord_channel`, `task_timeout_seconds`. Troubleshooting mentions agents' containers running in **Coolify**. ^[raw/sources/knowledge/senter-repo/SOUL.md]

## How it differs from the live Senter
The live profile ([[topics-wiki/senter/wiki/entities/senter|Senter]], SOUL 2026-08-30 →) has file tools, writes the vault, routes to a different fleet (klerik, weaver, teknium, turbosovth, dogeman, anser, paladin, looker), and treats topics as work units. Chizul, kashik, crow, frieza, nous-girl and sirvir appear only in legacy files (this repo, [[topics-wiki/senter/wiki/entities/anser|anser]]'s fleet table). Side-by-side: [[topics-wiki/senter/wiki/comparisons/senter-legacy-repo-vs-current-soul|comparison]]; roster history: [[topics-wiki/senter/wiki/comparisons/fleet-rosters-over-time|rosters]]. The repo is a candidate for the [[topics-wiki/senter/wiki/concepts/companion-bot-doctrine|companion-bot README pattern]] Paladin enforces.
