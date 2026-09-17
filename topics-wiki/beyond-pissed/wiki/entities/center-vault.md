---
title: Center Vault
created: 2026-09-06
updated: 2026-09-10
type: entity
tags: [tool, repo, infra]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Center Vault

The central repository/vault Chris says must be reviewed to understand how the current work is built, worked, and used in the current fix process. Chris works directly in `~/Documents/Projects/Projects`, which is the active vault root.

> You need to look through the center vault and see how this whole thing will be built and how it's supposed to be worked and how it's supposed to be used in that process right now in the fixes. ^[raw/inbox/2026-09-06.md]

## Repository Structure Discrepancy

Hermes discovered that `~/Documents/Projects/Projects` was **not a git repository** — there was no `.git` directory — and that caused updates to fail^[raw/inbox/2026-09-09.md]. The `agent-wiki` repo exists at `~/gh-sync/agent-wiki` with git, but `Projects` is **not a submodule** of it^[raw/inbox/2026-09-09.md].

## Current System State (2026-09-09)

Current file/system state is now the source of truth^[raw/inbox/2026-09-08.md]. On 2026-09-09:

- `~/Documents/Projects/Projects` is **a git repository on `main`** with remote `origin` pointing to `https://github.com/SouthpawIN/agent-wiki`^[raw/inbox/2026-09-09.md].
> ~/gh-sync/agent-wiki` is also on `main` with the same origin^[raw/inbox/2026-09-09.md].
>- Both repos are on the same lineage, but the working tree has many uncommitted changes^[raw/inbox/2026-09-09.md].
>- A continuous `scan-topics.py --watch 20` loop is repacking data every 20 seconds^[raw/inbox/2026-09-09.md].
>- See [[topics-wiki/beyond-pissed/wiki/decisions/git-state-drift-recovery|Git State Drift Recovery]] for the 2026-09-10 state where the repo briefly disappeared, was restored, upstream tracking is missing, and the scan loop uses stale code^[raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md].

So the new blocker is **state drift / scan-loop staleness**, not a missing repo or a blocked network fetch.

## Hermes Evidence Stream

Hermes diagnosed the missing git repository, examined whether `Projects` is a submodule of `agent-wiki` (it is not), looked at `gh-sync` as the likely git home, and then initialized/connected the repo^[raw/inbox/2026-09-09.md]. Later evidence shows Hermes inspected `vault-live.html` load behavior, the BOTS view, the `loadLive` function, the `/file` route, and `.system-live.json` update mechanics^[raw/inbox/2026-09-09.md].

## System State

Chris emphasized using "current file/system state for exact details"^[raw/inbox/2026-09-08.md]. The token used by Hermes changes when `--new-token` is invoked, requiring reads of the new token for continued system state synchronization^[raw/inbox/2026-09-08.md]. On 2026-09-10 Hermes confirmed the live repo is on `main` with origin `https://github.com/SouthpawIN/agent-wiki` and that the working tree carries many uncommitted changes; the `.system-live.json` file was verified directly through the `/file` route alongside the git state^[raw/inbox/2026-09-10.md].

See also: [[topics-wiki/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics-wiki/beyond-pissed/wiki/entities/agent-wiki|Agent Wiki]], [[topics-wiki/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]], [[topics-wiki/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]]
