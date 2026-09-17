---
title: Update failure — vault not a git repository
created: 2026-09-09
updated: 2026-09-09
type: decision
tags: [decision, infra, git, update]
sources:
  - raw/inbox/2026-09-09.md
confidence: high
---

# Decision 2026-09-09: Update failure root cause — vault not a git repository

## What

The vault at `~/Documents/Projects/Projects/` was **not** a git repository, causing Chris's "updates keep failing" errors. The root cause was diagnosed as:

> "The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' — there's no git to track or push changes. The user wants to be able to update AND keep the project (which is the wiki/vault)."
> — chris · 2026-09-09 13:01 ^[raw/inbox/2026-09-09.md]

## Resolution

Hermes initialized a git repository, added the remote origin `https://github.com/SouthpawIN/agent-wiki`, created a `.gitignore` for generated files, and committed 2607 files to establish version control.

## Why

Without git, the vault had no history tracking, no push/pull capability, and no way for "updates" to resolve. Chris's workflow expects to see changes land and be tracked. The fleet's compile loops write markdown into the wiki, and git is the backbone for that contract.

## Evidence

- "The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' — there's no git to track or push changes." — 2026-09-09 13:01 ^[raw/inbox/2026-09-09.md]
- "Initialized git, added remote origin: https://github.com/SouthpawIN/agent-wiki, created .gitignore for generated files (.system-live.json, dashboard.html, logs), committed 2607 files enabling future updates" — 2026-09-09 20:07 ^[raw/inbox/2026-09-09.md]

## Related

- [[topics-wiki/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[topics-wiki/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[topics-wiki/senter-wiki/wiki/entities/file-cap-bypass|FILE_CAP bypass for .system-live.json]]
- [[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-orb-rename-completion|Orb label rename completion]]