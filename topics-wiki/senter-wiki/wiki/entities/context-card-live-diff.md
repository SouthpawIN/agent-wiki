---
title: "Context card live diff — watching the topic agent edit the wiki (+N −M, green/red lines)"
created: 2026-09-05
updated: 2026-09-06
type: entity
tags: [ui, spec, tool]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-06.md
confidence: high
---

# Context card live diff

The CONTEXT card of a topic row, after the 19:06 decision ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|CONTEXT is the wiki with live diffs]]). It replaces the `index.md` listing and the page/raw counts.

## What it renders
The topic's actual `wiki/` pages, grouped by section — ENTITIES / CONCEPTS / DECISIONS / COMPARISONS / QUERIES — each page as its title plus rendered markdown, fetched through the [[topics-wiki/senter-wiki/wiki/entities/senter-bridge|bridge]] when the card opens. No counts, no index list. ^[raw/inbox/2026-09-05.md]

## How a diff arrives (as reported 19:12, "DOM-proven")
1. The topic agent ([[topics-wiki/senter-wiki/wiki/entities/topic-wiki-compile-loop|compile loop]]) snapshots the wiki before its run and diffs every changed page after.
2. Each changed page becomes a `diff` event into the UI.
3. The UI scrolls that page into view and repaints it: removed lines red and struck through, added lines green; a `+N −M` badge on the page and a running badge beside the card title — Chris's *"plus-minus lines in the red and green like what you would see on like Github."*
4. It settles to plain text after **6 s**.
5. If the card is closed it **peeks open for the edit (9 s)** — unless Chris has a card pinned. ^[raw/inbox/2026-09-05.md]

## Geometry
The card's right edge stops near the side chat so the feed and the player stay live while he reads — [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-content-card-stops-at-side-chat|decision]]. The recent closed-chat gutter is `right:4px`. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-06.md]

## Row diff badges + 24h persistence
`mkTopic` and `refreshWikiOrbs` now render `.usage` and `.diffbadge` before `.tname`; `.rdiff` is a fixed 44px slot between usage and the dots so nothing shifts. Diff state persists 24h via `localStorage('sw.diffs')`; default sort is `decayedDiff` → usage → updated date. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-06.md]

## Open on this element
- Wiki topic bodies are baked HTML at build time. If README.md changes, baked `.tbody-inner` does not refresh until the next build; a live `mdRender` re-render step in `openEditor` is still needed for true live markdown in the card. ^[raw/inbox/2026-09-06.md]
