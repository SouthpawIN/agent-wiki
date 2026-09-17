---
title: Git remote naming conflict — agent-wiki vs Senter
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [infra, decision, repo, contested]
sources:
  - raw/inbox/2026-09-09.md
confidence: high
contested: true
---

# Git remote naming conflict — agent-wiki vs Senter

## The issue

When git was initialized in the vault on 2026-09-09, the remote origin was set to `https://github.com/SouthpawIN/agent-wiki` and the
footer backlink in `vault-live.html` was added pointing to the same URL. However, on 2026-08-29 Chris decided to consolidate the
`agent-wiki` + `klerik` + `senter` repos into a single repo named `Senter` ([[wiki-topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|decision 2026-08-29]]).

> "this should combine senter, agent wiki, and klerik … replace all with Senter" ^[raw/inbox/2026-09-05-legacy-inbox.md]

The git remote and footer backlink should therefore point to `https://github.com/SouthpawIN/Senter`, not `agent-wiki`.

## Evidence

- 2026-09-09 13:17: "The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing'
  — there's no git to track or push changes." ^[raw/inbox/2026-09-09.md]
- Git was initialized with remote `https://github.com/SouthpawIN/agent-wiki` (2026-09-09 commit `6b217cb`).
- Footer backlink added: "Theoretical backbone: https://github.com/SouthpawIN/agent-wiki" ^[raw/inbox/2026-09-09.md]
- The 2026-08-29 consolidation renamed the repo to `SouthpawIN/Senter`.

## Status: waiting on Chris

This discrepancy is unresolved. Chris may want the remote updated to `SouthpawIN/Senter` to match the consolidation decision.

## Related

- [[wiki-topics/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|vault git init decision]]
- [[wiki-topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|repo consolidation decision]]
- [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
