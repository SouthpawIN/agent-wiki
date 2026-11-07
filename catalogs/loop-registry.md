---
title: Loop Registry
created: 2026-07-07
updated: 2026-11-07
type: catalog
tags: [loops, registry, cron]
---

# Loop Registry

Every loop in the fleet. `live` means armed in Hermes cron; `spec` means the
procedure is written and awaiting a manual pass.

| Loop | Bot | Schedule | Skill | State |
|---|---|---|---|---|
| [[bots/bot-wiki/loops/fleet-reconcile\|fleet-reconcile]] | bot-wiki | daily 06:00 | bot-reconcile | live |
| [[bots/youtube/loops/nightly-ingest\|nightly-ingest]] | youtube | daily 02:00 | rant-segmentation | spec |
| [[bots/youtube/loops/weekly-cut\|weekly-cut]] | youtube | Sun 10:00 | clip-assembly | spec |
| [[bots/pocketshop/loops/ev-discovery\|ev-discovery]] | pocketshop | daily 09:00 | restock-ev-pick | spec |
| [[bots/pocketshop/loops/sale-watch\|sale-watch]] | pocketshop | hourly 08–23 | sale-ledger | spec |
| [[bots/turbofit/loops/artifact-audit\|artifact-audit]] | turbofit | Mon 07:00 | artifact-audit | spec |
| [[bots/turbofit/loops/release-gate\|release-gate]] | turbofit | on tag | fit-list-sync | spec |
| [[bots/kart-racer/loops/roster-sync\|roster-sync]] | kart-racer | Mon 08:00 | nrcu-roster-import | spec |
| [[bots/ai-daw/loops/engine-watch\|engine-watch]] | ai-daw | monthly | music-model-adapter | spec |
| [[bots/anser/loops/corpus-refresh\|corpus-refresh]] | anser | daily 07:30 | x-corpus-refresh | spec |
| [[bots/hermes/loops/mesh-health\|mesh-health]] | hermes | daily 06:30 | webapp-on-tailnet | spec |
| [[bots/ssi/loops/deadline-watch\|deadline-watch]] | ssi | daily 07:00 | notice-response | spec |

## Promotion rule

`spec → live` only after the procedure has been run by hand once, produced its
artifact where the BOT.md predicted, and been proven idempotent. See
[[bots/bot-wiki/skills/bot-promote/SKILL|bot-promote]].

## Demotion

Two consecutive failures demote a live loop back to `spec`. Fix it out of prod.
