---
title: senter-wiki topic skills (senter-watcher, progressive-disclosure, wiki-ui-knobs)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [skill]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# senter-wiki topic skills

Three SKILL.md files created in `topics-wiki/senter-wiki/skills-capabilities/` on 2026-09-05 when the topic was built "per the agent-wiki spec, all real files" (LOOPS went 13 → 16 in the wiki at the same time). ^[raw/inbox/2026-09-05-legacy-inbox.md]

| Skill | Purpose |
|---|---|
| `senter-watcher` | operate / replay / tune the [[topics-wiki/senter-wiki/wiki/entities/senter-watcher|watcher]] |
| `progressive-disclosure` | INDEX → file → section reading protocol for the [[topics-wiki/senter-wiki/wiki/entities/sidebar-agent|sidebar]] |
| `wiki-ui-knobs` | every UI knob with Chris's tuned value and the rule that owns it — "13 named + all `--*` vars extracted from the HTML" (compiled here as [[topics-wiki/senter-wiki/wiki/queries/ui-knob-registry|UI knob registry]]) |

## Older, profile-level skill
`agent-wiki-vault` (in `~/.hermes/.../skills`, v1.0.0) is the master skill for working in the vault and doing `vault-live.html` surgery; its body is the largest raw source of this wiki and the origin of [[topics-wiki/senter-wiki/wiki/concepts/chris-ui-working-rules|Chris's UI working rules]]. It keeps the `agent-wiki-vault` name for compatibility after the Senter rename. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Why these are rows
The [[topics-wiki/senter-wiki/wiki/entities/scan-topics|scanner]] was fixed the same day to scan `topics-wiki/*/skills-capabilities/` — before that "the spec's primary skill location was invisible". Skills now auto-apply without approval ([[topics-wiki/senter-wiki/wiki/concepts/approval-policy|approval policy]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
