---
title: Git remote naming conflict — agent-wiki vs Senter consolidation
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [infra, repo, decision, contested]
sources:
  - raw/inbox/2026-09-08.md
  - raw/inbox/2026-09-09.md
confidence: high
contested: true
---

# Git remote naming conflict

## What happened
On 2026-09-09, git was initialized in `~/Documents/Projects/Projects/` because the vault had no `.git` folder, causing "My updates keep failing" — there was no git to track or push changes.
^[raw/inbox/2026-09-09.md]

The remote origin was set to `https://github.com/SouthpawIN/agent-wiki`.
A footer backlink was added: "Theoretical backbone: https://github.com/SouthpawIN/agent-wiki".
^[raw/inbox/2026-09-08.md]

## The conflict
- **2026-08-29 decision**: Chris consolidated the org — "this should combine senter, agent wiki, and klerik … replace all with **Senter**." The repo should be renamed to `SouthpawIN/senter`.
  ^[raw/inbox/2026-09-09.md]
- **2026-09-09 action**: git remote was set to `https://github.com/SouthpawIN/agent-wiki` — the OLD name, not `Senter`.
- This is flagged `contested: true` — the agent-wiki remote does not reflect the 2026-08-29 consolidation to Senter. The footer backlink also uses the old `agent-wiki` name.

## Resolution needed
Either:
1. Rename the remote to `https://github.com/SouthpawIN/senter` to match the consolidation, or
2. Confirm the `agent-wiki` name is intentionally kept as the "permanent, unchanging theoretical backbone" per the turbofit constraints.
  ^[raw/inbox/2026-09-09-from-turbofit.md]

The turbofit raw item explicitly states: "User's agent wiki GitHub repository is a permanent, unchanging theoretical backbone for Senter wiki theory" — so the name may be intentionally retained despite the 2026-08-29 consolidation directive.

## See also
- [[topics/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|Vault git init]]
- [[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|Consolidate repos into Senter]]
