---
title: Verify vault-to-repo link status (gh-sync / agent-wiki)
created: 2026-09-09
updated: 2026-09-09
type: query
tags: [repo, infra, query, verification]
sources: [raw/inbox/2026-09-09.md]
confidence: low
---

# Verify vault-to-repo link status (gh-sync / agent-wiki)

## the question

Hermes observed on 2026-09-09 13:15 that a `gh-sync` directory contains
three repos: `agent-wiki`, `klerik`, and `senter`. He then noted:

> But the user's working directory is `~/Documents/Projects/Projects`.
> This might be a symlink, or the Projects folder might be a different
> location. Let me check what the actual relationship should be and
> initialize git if needed for updates.

Following up at 13:17:

> Looking at the README, the Projects folder should be the agent-wiki
> Senter codebase. Let me initialize it as git and connect it to the
> remote.

The investigation was in progress at filing time; the relationship between
`~/Documents/Projects/Projects` and `gh-sync/agent-wiki` was not resolved.

## why it matters

- [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] version is tracked in
  `wiki-topics/senter-wiki/README.md`; git tracking depends on the working directory
  being a real checkout of `agent-wiki`, not a loose copy.
- The [[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]] plugin is mirrored at
  `assets/senter-bridge/` in the vault — if the vault diverges from the repo,
  changes drift.
- [[wiki-topics/senter/wiki/entities/topic-agent|topic-agent]] runs `hermes kanban` claims,
  and dispatch/sentinel status depends on a coherent git working tree per the
  [[wiki-topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]].

## status (2026-09-09 13:17+ resolution)
Hermes diagnosed: *\"The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' — there's no git to track or push changes. The user wants to be able to update AND keep the project (which is the wiki/vault).\"* ^[raw/inbox/2026-09-09-from-senter-wiki.md]

Hermes then **initialized git** and connected it to the remote `https://github.com/SouthpawIN/agent-wiki` ^[raw/inbox/2026-09-09.md]. Verified at session end:
- `~/Documents/Projects/Projects` is a real git repo (not a symlink — `readlink -f` resolves to itself)
- Remote: `origin https://github.com/SouthpawIN/agent-wiki`
- Git initialized **resolves the "updates keep failing" root cause**: the bridge/file-serving path and wiki writes can now be tracked and committed

### What remains unresolved
The exact relationship between the working directory and the `gh-sync` directory's three repos (`agent-wiki`, `klerik`, `senter`) — whether the vault is a worktree, clone, or loose copy of `agent-wiki`. Hermes noted at 13:15: *\"This might be a symlink, or the Projects folder might be a different location\"* — confirmed it is NOT a symlink, but the sync mechanism to the gh-sync repos is not recorded.

## related
|- [[wiki-topics/senter/wiki/concepts/vault-repo-mapping|vault-to-repo mapping]]
|- [[wiki-topics/senter/wiki/entities/senter-repo|senter repo]]
|- [[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]] — bridge health verification 2026-09-09 (35 topics / 69 bots / 201 skills / 81 loops)
|- [[wiki-topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]]
|- [[wiki-topics/senter/wiki/queries/verify-apply-paths-and-watchpaths-landed|verify apply paths and WatchPaths landed]]
