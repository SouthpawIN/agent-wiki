---
title: Usage strip (GitHub-style heat dots per row)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui]
sources:
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Usage strip (GitHub-style heat dots per row)

## Chris's ask
"GitHub usage chart … like a diffusion map … tiny dots"; "I like the dot element, tiny dots." ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Data
`scan_usage()` in [[wiki-topics/senter-wiki/wiki/entities/scan-topics|scan-topics.py]] → `LIVE.usage = {days:98, end, topics:{name:[98 ints]}, bots:{}, skills:{}}` — one int per local day = rows in `~/.hermes/state.db` `messages` whose rowid matches `messages_fts MATCH "name"`; read-only sqlite. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Paint
`window.paintUsage()` after `live/loaded` and called from INSIDE `rerenderAll` (a monkey-patch wrapper installed before `rerenderAll` existed never attached → charts vanished on every re-render; Chris: "I'm not seeing the usage dots … those were pretty locked in"). Per row picks kind by `data-bot/data-skill/data-topic`; shows last `WEEKS=10` × 7 as `<i style="--a:…">` 3px circles, alpha `0.15+0.85*sqrt(n/rowMax)`, empty `.06`; `cell.title` = total. CSS `.thead .usage { flex:0 0 var(--usageW,140px); display:grid; grid-template-rows:repeat(7,1fr) }`. Knobs `--usageW`, `WEEKS`, dot 3px. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## It also orders the list
Default list order = usage, highest first; one `usageOf(kind,name)` feeds both the chart and `rankBy` "so chart and order can never disagree" ([[wiki-topics/senter-wiki/wiki/concepts/similarity-ranking|similarity and ranking]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Position in the row: fixed 140px pushed against the dots (`margin-left:auto`) so all rows share both edges — [[wiki-topics/senter-wiki/wiki/concepts/standard-row-anatomy|standard row anatomy]]. Short titles leave air before the chart by design; Chris OK'd. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
