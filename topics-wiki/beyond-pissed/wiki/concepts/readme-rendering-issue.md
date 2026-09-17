---
title: README Rendering Issue
created: 2026-09-06
updated: 2026-09-10
type: concept
tags: [pain, tool, infra]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: medium
---

# README Rendering Issue

A suspected failure in fetching and re-rendering the live README.md surfaced during Hermes troubleshooting on 2026-09-06.

hermes: Let me check if there's a step that fetches the live README.md and re-renders it with `md()`: ^[raw/inbox/2026-09-06.md]

## Model Catalog Check

Chris's model catalog has entries for `ornith-1-5-35a3b` in the auxiliary_options, but needs to verify if there's a main model entry with `engine: mlx` for Ornith-MLX^[raw/inbox/2026-09-07.md]. The model catalog issue was noted as blocking proper configuration of the orchestrator^[raw/inbox/wiki/queries/ornith-model-catalog.md.proposed].

## System File Route and Token Rotation

Hermes inspects how the `/file` route is handled to understand how `.system-live.json` is served^[raw/inbox/2026-09-08.md]. The token changed because `--new-token` was used^[raw/inbox/2026-09-08.md]; the new token must be read for continued system state synchronization^[raw/inbox/2026-09-08.md].

## README Bot Entry Fix

A note was made to fix the README bot entry (it shouldn't be there as a bot)^[raw/inbox/2026-09-08.md].

## vault-live.html Load Verification

Hermes verified the vault-live.html's `loadLive` function by checking the current state of the file and testing if it can load the data^[raw/inbox/2026-09-08.md]. The CSS is well-structured; Hermes checked the end of the file to see if there's a footer and added the agent-wiki GitHub reference^[raw/inbox/2026-09-08.md].

## Updated Load Function Inspection (2026-09-09)

Hermes checked the JavaScript `loadLive` function to understand the data loading behavior and verified the current UI state by examining the BOTS view and session display in `vault-live.html`^[raw/inbox/2026-09-09.md]. It also inspected the `/file` route serving `.system-live.json` and the relationship between the live data loader and `.system-live.json` updates^[raw/inbox/2026-09-09.md].

## Continuous Scan Loop

A scan is needed to update `.system-live.json`; Hermes checked if `scan-topics.py` exists and will run it^[raw/inbox/2026-09-08.md]. On 2026-09-09, Hermes identified that `assets/scan-topics.py --watch 20` is already running as a continuous watch loop and repacking data every 20 seconds^[raw/inbox/2026-09-09.md]. Hermes also noted potential scan issues: expected `'model'` in bot entries but some bots don't have that field, and it investigated `scan_vault_agents`/`scan_topics` behavior while checking whether the watch process was modifying data between scan and write^[raw/inbox/2026-09-09.md]. The scan-topics.py fix changed `skills` from `[]` to integer `0`, added the `model` field, and fixed `.md` stripping — see [[topics-wiki/beyond-pissed/wiki/concepts/scan-loop-schema-fix|Scan Loop Schema Fix]] and [[topics-wiki/beyond-pissed/wiki/concepts/sys-path-module-confusion|sys.path Module Confusion]]^[raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]. On 2026-09-10 Hermes continued verifying the JSON file directly as part of the live-file-serving investigation^[raw/inbox/2026-09-10.md]. The terminal wrapper sometimes emits `[Command timed out...]` before output arrives — the command still executes. See [[topics-wiki/beyond-pissed/wiki/concepts/execute-code-timeout-behavior|Execute Code Timeout Behavior]] for how this confused fix verification.

See also: [[topics-wiki/beyond-pissed/wiki/decisions/ship-today|Ship Today]], [[topics-wiki/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]], [[topics-wiki/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics-wiki/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]], [[topics-wiki/beyond-pissed/wiki/concepts/scan-loop-schema-fix|Scan Loop Schema Fix]], [[topics-wiki/beyond-pissed/wiki/concepts/sys-path-module-confusion|sys.path Module Confusion]]
