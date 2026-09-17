---
title: Orb label renaming — context to wiki, agents to bots
created: 2026-09-08
updated: 2026-09-10
type: concept
tags: [ui, decision, spec]
sources:
  - raw/inbox/2026-09-08.md
  - raw/inbox/2026-09-09.md
  - raw/inbox/2026-09-10.md
confidence: high
---

# Orb label renaming — context to wiki, agents to bots

## What was changed

**Context → Wiki terminology:**
|- Button: `data-k="context"` → `data-k="wiki"`
|- Button label: "Add context" → "Add to wiki"
|- CSS selector updated accordingly
|- Orb labels: `ctx`/`context` → `wiki`
|- Internal IDs preserved: `#contextChips`, `#popup-context`, `addContext()` function

**Agents → Bots labeling:**
|- Changed `data-k="agents"` → `data-k="bots"` throughout the codebase
|- Bot counts properly set based on actual data
|- Hero meta now shows "skills ×6 · bots ×3"

**Raw Chris quote:** "So one I want to once again rename everything that is context into wiki I think … want that to just be the wiki for that topic. So each topic will have its own wiki It's own skills, its own bots and its own loops." (2026-09-08 08:46) ^[raw/inbox/2026-09-08.md]

## Completion status — 2026-09-09

The static HTML rows were baked with `data-k="wiki"` / `data-label="wiki"` and `data-k="bots"` / `data-label="bots"` (visible on all topic rows in vault-live.html). The JS factory `mkTopic()` at line 1380 still used the old keys `['ctx','skills','agents','loops']` with a ternary that mapped `ctx`→`context` and `agents`→`bots`, so the produced HTML attributes (`data-k="ctx"`, `data-label="context"`, `data-k="agents"`) diverged from the baked rows. ^[raw/inbox/2026-09-09.md]

### Call sites fixed in vault-live.html (2026-09-09 13:33) ^[raw/inbox/2026-09-09.md]

The `mkTopic()` array and all four stale call sites were renamed together:
1. **Line 1380** — key array: `['ctx','skills','agents','loops']` → `['wiki','skills','bots','loops']`, and the `data-label` ternary simplified to just use `k` directly (no more `ctx`→`context` or `agents`→`bots` mapping needed).
2. **Line 1399** (SKILL rows) — `orbs:{ctx:…,skills:1,agents:profs.length,loops:0}` → `orbs:{wiki:1,skills:1,bots:profs.length,loops:0}`
3. **Line 1414** (BOT rows) — `orbs:{ctx:…,skills:cnt,agents:1,loops:0}` → `orbs:{wiki:1,skills:cnt,bots:1,loops:0}`
4. **Line 1646** (Integration rows) — `orbs:{ctx:…,skills:1,agents:1,loops:0}` → `orbs:{wiki:1,skills:1,bots:1,loops:0}`

The four downstream references that were PENDING are now resolved:
|- **Line 1424** `refreshWikiOrbs` — `set('agents',…)` → `set('bots',…)` ^[raw/inbox/2026-09-09.md]
|- **Line 1063** popup header — `if(k==='ctx')` → `if(k==='wiki')` ^[raw/inbox/2026-09-09.md]
|- **Line 1068** popup header — `else if(k==='agents')` → `else if(k==='bots')` ^[raw/inbox/2026-09-09.md]
|- **Lines 1622, 1624, 2264, 2265** — `setOrbActive(topic,'agents',…)` → `setOrbActive(topic,'bots',…)` ^[raw/inbox/2026-09-09.md]

**Root cause:** both the `mkTopic` array AND the downstream references must be renamed together. The 2026-09-08 pass fixed only the call-site object keys, which left the DOM attribute keys (`data-k`) still emitting `ctx`/`agents` while the `set()` and `setOrbActive()` functions were called with `wiki`/`bots` — a mismatch where no element matched the selector. Hermes diagnosed: "The bot row is still using data-k=agents and ctx instead of data-k=wiki and the correct naming." ^[raw/inbox/2026-09-09.md]

## Related
|- [[wiki-topics/senter-wiki/wiki/entities/hero-orbs|Hero orbs]]
|- [[wiki-topics/senter-wiki/wiki/concepts/one-page-navigation-model|One-page navigation model]]
|- [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
|- [[wiki-topics/senter-wiki/wiki/decisions/2026-09-08-senter-wiki-topic-structure-gap|Senter-wiki topic structure gap]]

^[raw/inbox/2026-09-08.md]