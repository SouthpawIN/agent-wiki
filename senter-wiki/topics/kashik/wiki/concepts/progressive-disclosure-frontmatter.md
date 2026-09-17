---
title: Progressive disclosure frontmatter
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - idea
  - infra
  - preference
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Progressive disclosure frontmatter

A filesystem-simplification strategy: put key discovery information into page frontmatter so deeper nested folders can be reduced or removed.

## Chris's intent

Chris explicitly framed this as replacing deep folder nesting with frontmatter-driven progressive disclosure. The goal is cleaner topic directories without losing access to metadata that the watcher, cutter, and topic agents need. ^[raw/inbox/2026-09-07.md]

## Rationale

Flat or shallow topic structures are easier to read, route, and revise. Frontmatter becomes the machine-readable index that previously required folder depth. This also matches Chris's standing preference for markdown-native tools over custom code.

## Open implications

- Pages must stay consistent with SCHEMA's frontmatter contract.
- This only works if every agent reads frontmatter before loading whole topic subfolders.
- Future reorganization should be tested against watcher routing and wiki compilation paths.

## Related

- [[wiki/entities/kashik|kashik]]
- [[wiki/decisions/simplify-filesystem-structure|Simplify filesystem structure]]
