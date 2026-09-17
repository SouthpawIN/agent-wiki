---
title: "Wiki skill activation"
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [skill, preference]
sources: [raw/inbox/2026-09-16.md]
confidence: medium
---

# Wiki skill activation

Crow's wiki skill has a documented set of conditions under which it activates.
These are the triggers that tell the agent to *act* (create / ingest / lint)
rather than merely log a pass. ^[raw/inbox/2026-09-16.md]

> "Use this skill when the user:
> - Asks to create, build, or start a wiki or knowledge base
> - Asks to ingest, add, or process a source into their wiki
> - Asks a question and an existing wiki is present at the configured path
> - Asks to lint, audit, or health-check their wiki
> - References their wiki, knowledge base, or 'notes' in a research context"
> ^[raw/inbox/2026-09-16.md]

## The five triggers

1. **Create / build / start** a wiki or knowledge base.
2. **Ingest / add / process** a source into the wiki.
3. **Answer a question** when an existing wiki is present at the configured
   path (`WIKI_PATH`).
4. **Lint, audit, or health-check** the wiki.
5. **Reference the wiki / knowledge base / "notes"** in a research context.

## Context

This sits on top of crow's division of labor — the human curates sources and
directs analysis; the agent summarizes, cross-references, files, and maintains
consistency — and crow's live-reload workflow (update pages as findings arrive,
then reload Obsidian so changes show live). ^[raw/inbox/2026-09-16.md]

## See also

- [[topics-wiki/crow/wiki/concepts/division-of-labor|Division of labor]]
- [[topics-wiki/crow/wiki/concepts/bots-terminology|Bots terminology]]
- [[topics-wiki/crow/wiki/decisions/agents-to-bots-terminology|Agents-to-bots terminology decision]]
- [[topics-wiki/crow/README.md|crow README]]
