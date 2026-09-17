---
title: Decision 2026-09-09 — git repo initialized in the vault
created: 2026-09-09
updated: 2026-09-09
type: decision
tags: [decision, repo, infra, git]
sources:
  - raw/inbox/2026-09-09.md
confidence: high
---

# Decision 2026-09-09 — git repository initialized in the Senter vault

**What.** The `~/Documents/Projects/Projects/` vault (hosting `topics/`, `vault-live.html`, and the live Senter Wiki) was **not** a git repository, causing Chris's update failures. The root cause was diagnosed:

> "The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' — there's no git to track or push changes. The user wants to be able to update AND keep the project (which is the wiki/vault)." ^[raw/inbox/2026-09-09.md]

Hermes initialized git, added the remote origin `https://github.com/SouthpawIN/agent-wiki`, created a `.gitignore` for generated files, and committed 2607 files to establish version control for the vault. ^[raw/inbox/2026-09-09.md]

**Why.** Without git, the vault had no history tracking, no push/pull capability, and no way for "updates" to resolve — Chris's workflow expects to see changes land and be tracked, and the fleet's own compile loops write markdown into the wiki. Git is the backbone for that contract. ^[raw/inbox/2026-09-09.md]

## Remote and repo target

The remote is `https://github.com/SouthpawIN/agent-wiki`, which was consolidated into `SouthpawIN/Senter` on 2026-08-29 ([[topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|decision 2026-08-29]]). The agent-wiki repo is the theoretical backbone of the Senter Wiki; vault-live.html carries a footer backlink to it. ^[raw/inbox/2026-09-09.md] ^[raw/sources/knowledge/agent-wiki-repo/README.md]

## `.gitignore`

Generated files and transient state are excluded: `.system-live.json`, `assets/avatars/` cache, `.system-live.json` size-bypass target (see [[topics/senter-wiki/wiki/entities/file-cap-bypass|bridge FILE_CAP fix]]). ^[raw/inbox/2026-09-09.md]

## Related

- [[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo → Senter]]
- [[topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|Decision 2026-08-29: consolidate repos]]

## Contested

The remote was set to `https://github.com/SouthpawIN/agent-wiki`, but the 2026-08-29 consolidation decision renamed the repo to `SouthpawIN/Senter`. The footer backlink in vault-live.html also points to `agent-wiki`. This discrepancy is unresolved — Chris may want the remote updated to `SouthpawIN/Senter` to match the consolidation. ^[raw/inbox/2026-09-09.md]