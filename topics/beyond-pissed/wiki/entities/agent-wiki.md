---
title: Agent Wiki
created: 2026-09-09
updated: 2026-09-09
type: entity
tags: [repo, tool, infra]
sources: [raw/inbox/2026-09-09.md]
confidence: high
---

# Agent Wiki

The `agent-wiki` repo at `~/gh-sync/agent-wiki`, a git repository that is structurally related to but not currently connected to the center vault at `~/Documents/Projects/Projects`.

## Repository Relationship

The `agent-wiki` repo has **submodules**, but `Projects` is not one of them. Chris works in `~/Documents/Projects/Projects` (the center vault) but the intended relationship between that directory and `agent-wiki` at `~/gh-sync/agent-wiki` is ambiguous — the directory is not a submodule, not a symlink, and not otherwise connected^[raw/inbox/2026-09-09.md].

> The agent-wiki repo has submodules, but `Projects` is not a submodule. The user is working in `~/Documents/Projects/Projects` which should be the same as or connected to the agent-wiki repo. Let me check if Projects is supposed to be synced with agent-wiki. There's a `gh-sync` directory which seems to be the git repo. ^[raw/inbox/2026-09-09.md]

## Intended Architecture

Chris wants the center wiki to orchestrate across this and other projects. The `agent-wiki` repo at `~/gh-sync/agent-wiki` is the git-side home; the center vault at `~/Documents/Projects/Projects` is the active working copy^[raw/inbox/2026-09-09.md]. Both repos are on `main`, both point to the same GitHub origin (`https://github.com/SouthpawIN/agent-wiki`), and the vault now has git initialized^[raw/inbox/2026-09-09.md]. The remaining gap is sync mechanics and current state drift, not remote access.

See also: [[topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]], [[topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]]
