---
title: Simplify filesystem structure
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - infra
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Simplify filesystem structure

Chris decided to simplify the topic filesystem using frontmatter-based progressive disclosure rather than maintaining deep nested topic folders.

## What changed

Instead of relying on folder hierarchy for discovery and routing, the topic will rely more heavily on structured frontmatter metadata. ^[raw/inbox/2026-09-07.md]

## Why

Deep nested folders made navigation and agent routing harder to maintain. Frontmatter keeps metadata close to the content, human-readable, and machine-consumable.

## Next action

Chris stated he would make the edits and verify live preview. That means edits are pending execution and verification, not already complete.

## Related

- [[wiki/concepts/progressive-disclosure-frontmatter|Progressive disclosure frontmatter]]
- [[wiki/entities/kashik|kashik]]
