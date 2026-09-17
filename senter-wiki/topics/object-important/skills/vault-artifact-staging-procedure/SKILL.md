---
name: vault-artifact-staging-procedure
description: Use when staging vault files for commit while excluding generated live-state JSON.
version: 0.1.0
distilled: 2026-09-09 20:23
topic: object-important
---
# vault-artifact-staging-procedure
## Vault artifact staging procedure
1. Configure git user name/email in the repo.
2. Stage important files while excluding generated `.system-live.json`.
3. Review staged count and remaining untracked files.
4. Commit so updates can work.

Pitfall: `.system-live.json` is regenerated at runtime; do not stage it or treat it as source of truth after edits.
Pitfall: large model shards such as `safetensors` files are untracked binaries that need git-lfs if they belong in version control.

## Evidence
> "Set up the user config for git"
> "Stage the important files (excluding .system-live.json which is generated)"
> "Make a commit so updates can work"
> "There are 2608 staged files, plus some untracked ones."
