---
title: String split slug generation
created: 2026-09-08
updated: 2026-09-08
type: decision
tags:
  - decision
  - infra
sources:
  - raw/inbox/2026-09-08.md
confidence: medium
---

# String split slug generation

A decision about how wiki page slugs are derived from filenames.

## What Chris decided

Chris confirmed the slug generation logic for progressive disclosure frontmatter: filenames are split on `.md` to produce the wiki slug. The pattern `.split(".md")[0]` correctly converts `context-fallback-pin.md` to `context-fallback-pin` and `librarian.md` to `librarian`. ^[raw/inbox/2026-09-08.md]

## Context

This was part of Chris's work simplifying the topic filesystem using frontmatter-based progressive disclosure. The slug generation is the mechanism that bridges filename conventions to wiki link targets.

## Status

Verified working — Chris's test confirmed the split should work.

## Related
- [[wiki/concepts/progressive-disclosure-frontmatter|Progressive disclosure frontmatter]]
- [[wiki/concepts/llm-wiki|llm-wiki]]
- [[wiki/entities/kashik|kashik]]
- [[wiki/queries/clone-official-repos-to-read-docs|Clone official repos to read documentation]]