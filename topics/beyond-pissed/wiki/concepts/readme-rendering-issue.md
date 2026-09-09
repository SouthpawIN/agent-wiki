---
title: README Rendering Issue
created: 2026-09-06
updated: 2026-09-08
type: concept
tags: [pain, tool, infra]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md]
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
Hermes verified the vault-live.html's `loadLive` function by checking the current state of the file and testing if it can load the data^[raw/inbox/2026-09-08.md].

## Scan to Update .system-live.json
A scan is needed to update `.system-live.json`; Hermes checked if `scan-topics.py` exists and will run it^[raw/inbox/2026-09-08.md].

See also: [[topics/beyond-pissed/wiki/decisions/ship-today|Ship Today]], [[topics/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]], [[topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]]
