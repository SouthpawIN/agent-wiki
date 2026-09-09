---
title: Orb label renaming — context to wiki, agents to bots
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [ui, decision, spec]
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# Orb label renaming — context to wiki, agents to bots

## What was changed

**Context → Wiki terminology:**
- Button: `data-k="context"` → `data-k="wiki"`
- Button label: "Add context" → "Add to wiki"
- CSS selector updated accordingly
- Orb labels: `ctx`/`context` → `wiki`
- Internal IDs preserved: `#contextChips`, `#popup-context`, `addContext()` function

**Agents → Bots labeling:**
- Changed `data-k="agents"` → `data-k="bots"` throughout the codebase
- Bot counts properly set based on actual data
- Hero meta now shows "skills ×6 · bots ×3"

**Raw Chris quote:** "So one I want to once again rename everything that is context into wiki I think … want that to just be the wiki for that topic. So each topic will have its own wiki It's own skills, its own bots and its own loops." (2026-09-08 08:46) ^[raw/inbox/2026-09-08.md]

## Related
- [[topics/senter-wiki/wiki/entities/hero-orbs|Hero orbs]]
- [[topics/senter-wiki/wiki/concepts/one-page-navigation-model|One-page navigation model]]
- [[topics/senter-wiki/wiki/concepts/one-page-navigation-model|One-page navigation]]

^[raw/inbox/2026-09-08.md]