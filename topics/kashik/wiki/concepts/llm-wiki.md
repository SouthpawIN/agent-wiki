---
title: llm-wiki
created: 2026-09-08
updated: 2026-09-08
type: concept
tags:
  - tool
  - skill
  - infra
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# llm-wiki

The per-agent wiki documentation convention Chris has adopted for the Senter vault.

## What Chris said

kashik maintains per-agent `llm-wiki` documentation. Chris was debugging the slug generation logic where a topic agent takes a filename like `context-fallback-pin.md` and derives the wiki slug `context-fallback-pin`. His test confirmed the split logic works: `"context-fallback-pin.md".split(".md")[0]` yields `"context-fallback-pin"` and `"librarian.md".split(".md")[0]` yields `"librarian"`. ^[raw/inbox/2026-09-08.md]

## Technical detail

Chris verified that the `.md` extension splitting mechanism used for progressive disclosure frontmatter slug generation functions correctly. After initial doubt ("Wait, that's not right. Let me test:"), he confirmed the split should work and checked what was happening.

## Purpose

Each agent (kashik, weaver, teknium, etc.) maintains its own `llm-wiki` documentation folder, keeping agent-specific knowledge isolated while allowing the librarian to link across topics.

## Related
- [[wiki/entities/kashik|kashik]]
- [[wiki/concepts/progressive-disclosure-frontmatter|Progressive disclosure frontmatter]]
- [[wiki/concepts/librarian-concept|Librarian concept]]