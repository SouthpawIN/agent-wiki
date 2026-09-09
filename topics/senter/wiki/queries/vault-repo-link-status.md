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

- [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] version is tracked in
  `topics/senter-wiki/README.md`; git tracking depends on the working directory
  being a real checkout of `agent-wiki`, not a loose copy.
- The [[topics/senter/wiki/entities/senter-bridge|senter-bridge]] plugin is mirrored at
  `assets/senter-bridge/` in the vault — if the vault diverges from the repo,
  changes drift.
- [[topics/senter/wiki/entities/topic-agent|topic-agent]] runs `hermes kanban` claims,
  and dispatch/sentinel status depends on a coherent git working tree per the
  [[topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]].

## what to check

1. Is `~/Documents/Projects/Projects` a git repo? (`git -C ~/Documents/Projects/Projects rev-parse --show-toplevel`)
2. Is it a symlink to `gh-sync/agent-wiki`? (`readlink`, `ls -la ~/Documents/Projects`)
3. Is there git remote config tying the working directory to the `agent-wiki` repo URL?

## related

- [[topics/senter/wiki/concepts/vault-repo-mapping|vault-to-repo mapping]]
- [[topics/senter/wiki/entities/senter-repo|senter repo]]
- [[topics/senter/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]]
- [[topics/senter/wiki/queries/verify-apply-paths-and-watchpaths-landed|verify apply paths and WatchPaths landed]]
