---
title: Fix Discrepancy to Updates
created: 2026-09-09
updated: 2026-09-10
type: decision
tags: [decision, plan, preference, question]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Fix Discrepancy to Updates

Chris stated: "I want the updates to go as their plan" and emphasized he wants to be able to update without losing the project.

> Now, I don't want to lose either I want the updates to go as their plan. I want to be able to just update But I don't want to lose the project so try to fix whatever the discrepancy is between there and Get this updated and then do everything else that I've asked in this session ^[raw/inbox/2026-09-09.md]

As of 2026-09-10, the git repository at `~/Documents/Projects/Projects` is confirmed on `main` with origin `https://github.com/SouthpawIN/agent-wiki`, and Hermes continued verifying the git state and `.system-live.json` directly through the `/file` route — confirming the remaining blocker is state drift and sync mechanics, not repo absence^[raw/inbox/2026-09-10.md]. On 2026-09-10 the repo briefly disappeared and was restored, and the `main` branch was found to have no upstream set^[raw/inbox/2026-09-10.md]. See [[topics/beyond-pissed/wiki/queries/git-upstream-not-set|Git Upstream Not Set on main Branch]] and [[topics/beyond-pissed/wiki/decisions/git-state-drift-recovery|Git State Drift Recovery]] for details.

## Root Cause of the Update Failure (2026-09-10)

The update pipeline (`hermes update --branch main`) was failing in its `pre_update_backup` step. The culprit was `_prepare_checkout_for_update`, which **refuses to switch branches while the working tree is dirty and the parked branch is not merge-safe**, exiting with code 1 — so the update never got far enough to actually run. The fix was to get onto a clean `main` (the uncommitted kanban files were stashed/committed first), after which the update check reported "Already up to date"^[raw/inbox/2026-09-10.md]. This ties the abstract "discrepancy" into a concrete mechanism: the working tree had uncommitted changes + a parked branch, which the update guard would not cross.

## Key Concerns

- **Preservation**: Must not lose the project during updates
- **Discrepancy**: There is a discrepancy between "there" (current state) and "update" target state
- **Prioritization**: Get the update fixed first, then proceed with other session requests
- **Plan Integrity**: Updates should follow the established plan

See also: [[topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics/beyond-pissed/wiki/entities/agent-wiki|Agent Wiki]], [[topics/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]], [[topics/beyond-pissed/wiki/decisions/finish-center-wiki-and-orchestrate|Finish Center Wiki and Orchestrate]], [[topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]]
