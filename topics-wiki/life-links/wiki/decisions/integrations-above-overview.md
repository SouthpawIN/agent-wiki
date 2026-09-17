---
title: integrations block moved above overview
created: 2026-09-17
updated: 2026-09-17
type: decision
tags: [decision, plan, ui, wiki]
sources: [raw/inbox/2026-09-16.md]
confidence: low
---

# integrations block moved above overview

*Decision* — Reorganize a wiki page so the integrations section (together with repositories and a table) sits above the overview, reading almost like part of the index.

^[raw/inbox/2026-09-16.md] At `2026-09-16 23:24`: "move the integrations with repositories and table to above the overview so that's going to be kind of like you know that should almost be part of the index"

## What

- Move the integrations section, along with the repositories section and a table, to a position above the overview section.
- The intent is for that block to read "almost ... part of the index" — i.e. integrations / repositories become top-level, index-like navigation rather than a lower section.

## Why

- Chris wants integrations to be prominent and structurally first-class. This is the visual-ordering half of the same goal as putting integrations in front matter (see [[topics-wiki/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]]): structured **and** prominent.

## When

- `2026-09-16 23:24`, during a wiki page-structure conversation (message ID `20260914_200308_f9b029`).

## Status

- **Executed (2026-09-17 10:10).** The page body now opens with the integrations block above the overview, labelled "Integrations (frontmatter property + clickable section)" — the prominent half done, now paired with the structured (front-matter) half. The same restructure added two new sections, **Implementation** and **Issues**.
- Per-page rollout: other wiki pages that still carry integrations as a non-clickable JSON list have not yet been updated.

## Related

- [[topics-wiki/life-links/wiki/concepts/life-links|life links]]
- [[topics-wiki/life-links/wiki/concepts/front-matter-integrations|front-matter integrations property]]
- [[topics-wiki/life-links/wiki/queries/life-links-in-front-matter|life links in front matter query]]
