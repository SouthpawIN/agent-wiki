---
title: Skill Registry
created: 2026-07-07
updated: 2026-11-07
type: catalog
tags: [skills, registry]
---

# Skill Registry

Every skill, grouped by the bot that loads it. 28 skills across 9 bots.

| Bot | Skills |
|---|---|
| bot-wiki | `bot-authoring`, `bot-reconcile`, `bot-promote` |
| youtube | `rant-segmentation`, `clip-assembly`, `package-and-chapters` |
| pocketshop | `draft-listing-pipeline`, `restock-ev-pick`, `sale-ledger` |
| turbofit | `support-verify`, `model-matrix-add`, `fit-list-sync`, `artifact-audit` |
| kart-racer | `unity-kart-prototype`, `nrcu-roster-import`, `track-kit` |
| ai-daw | `daw-plugin-scaffold`, `music-model-adapter`, `lego-arrangement` |
| anser | `grounded-answer`, `x-corpus-refresh`, `mod-escalation` |
| hermes | `webapp-on-tailnet`, `device-onboarding`, `bot-mode-profiles` |
| ssi | `document-intake`, `form-drafting`, `notice-response` |

## What qualifies as a skill

An executor with no context can follow it and produce a named artifact at a
predicted path. If it reads like a description of the domain, it is prose and
belongs in `.system/continuity.md`.

## Creating a skill

File `[SKILLS]` in the owning bot's `.system/queue.md`, or write
`skills/<slug>/SKILL.md` directly and note it in the bot's log. Skills factory
materializes the rest.
