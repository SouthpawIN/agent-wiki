---
title: life-links
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# life-links

Last updated: 2026-09-17 | Total pages: 5

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Concepts

- [clickable integrations](wiki/clickable-integrations.md) — *Concept* — Chris's pain that a page's integrations render as a non-clickable JSON list, and the proposed resolution to render them as clickable links while kee
- [front-matter integrations property](wiki/front-matter-integrations.md) — *Concept* — The proposal to make a page's integrations an explicit property inside the wiki page's YAML front matter.
- [life links](wiki/life-links.md) — *Concept* — Chris's idea of representing a page's external connections ("life links" / integrations) as structured, prominent data in the wiki rather than as sc

### Decisions

- [integrations block moved above overview](wiki/integrations-above-overview.md) — *Decision* — Reorganize a wiki page so the integrations section (together with repositories and a table) sits above the overview, reading almost like part of th

### Queries

- [can life links live in the front matter?](wiki/life-links-in-front-matter.md) — *Query* — Chris opened this as a question, not a decision: whether a wiki page's "life links" (integrations) can be represented inside the front matter.

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[clickable-integrations](agents/clickable-integrations.md.proposed) — **I see you're frustrated that your page integrations show as a non-clickable JSON list — want a bot that renders them as clickable links while keepin
- **[front-matter-clickable-render](agents/front-matter-clickable-render.md.proposed) — **Want me to look into how the Senter wiki UI would render integrations as clickable links, and whether front-matter integrations can be surfaced that
- **[integrations-above-overview](agents/integrations-above-overview.md.proposed) — **I see you want the integrations/repositories/table block to sit above the overview and read index-like — want a bot that reorders a page's sections 
- **[integrations-maintainer](agents/integrations-maintainer.md.proposed) — **I see you're talking about making integrations a structured front-matter property — want a bot that maintains the `integrations:` property on wiki p


---

## LOOPS

Proposed loops:

- **[integrations-order-audit](loops/integrations-order-audit.md.proposed) — owner: integrations-above-overview · cadence: weekly · status: SUGGESTED
- **[integrations-reconcile](loops/integrations-reconcile.md.proposed) — owner: integrations-maintainer · cadence: daily · status: SUGGESTED
