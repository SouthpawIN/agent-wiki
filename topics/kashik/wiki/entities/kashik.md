---
title: kashik
created: 2026-09-07
updated: 2026-09-16
type: entity
tags:
  - person
  - bot
  - concept
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-14.md
  - raw/inbox/2026-09-16.md
confidence: high
---

# kashik

kashik is Chris's silent historian and librarian for the Senter wiki. It watches agent activity and maintains per-agent `llm-wiki` documentation for Chris's second-brain surface.

## Nature

In this topic, kashik sits as the watcher-side of the wiki compile loop. Its core job is turning raw state-db messages into structured wiki pages in `entities/`, `concepts/`, `decisions/`, `comparisons/`, and `queries/` — while preserving Chris's own wording and routing anything clearly belonging to another topic elsewhere.

## Design intent

Chris wants the wiki itself to be the product: discovery lives inside the wiki, and the process is the interface. That makes kashik more than a logger. It is a librarian with authority over how topics are indexed and found across the whole vault. ^[raw/inbox/2026-09-07.md]

## Next points of interest

- [[wiki/entities/kashik|kashik]] (this page)
- [[wiki/concepts/progressive-disclosure-frontmatter|Progressive disclosure frontmatter]]
- [[wiki/concepts/librarian-concept|Librarian concept]]
- [[wiki/decisions/simplify-filesystem-structure|Simplify filesystem structure]]
- [[wiki/decisions/topic-discovery-governance|Topic discovery governance]]
