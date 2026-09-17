---
title: Decision 2026-08-29: consolidate agent-wiki + klerik + senter into one repo, Senter
created: 2026-08-29
updated: 2026-09-05
type: decision
tags: [decision, repo, timeline]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Decision 2026-08-29: consolidate repos into Senter

## What
Chris: "this should combine senter, agent wiki, and klerik … replace all with Senter." `agent-wiki` + `klerik` + `senter` → one GitHub repo **Senter**. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Procedure that worked
Vault: `wiki-topics/agent-wiki` → `wiki-topics/senter` (archive the old senter README as `fleet-orchestrator-profile.md`, klerik's as `klerik-profile.md`; keep old `.system/` under `.system/archive/<name>-old/`); repoint catalogs (`MERGED into [[wiki-topics/senter/README|senter]]`, `SouthpawIN/agent-wiki` → `SouthpawIN/Senter`); verify 0 hits for old paths; dated `log.md` line. Repo: shallow clones, merge secondary repos into `profiles/<name>/`, strip usage/lock state, commit with a merge-mapping table, rename via GitHub API PATCH (needs Administration-scope PAT; old URLs redirect). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Effects
The `agent-wiki-vault` skill keeps its name; "Senter vault" = "agent-wiki vault". The repo whose spec this wiki compiles: [[wiki-topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]. Context: [[wiki-topics/senter-wiki/wiki/concepts/senter-wiki-vision|vision]].
