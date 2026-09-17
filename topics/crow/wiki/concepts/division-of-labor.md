---
title: "Division of labor"
created: 2026-09-16
updated: 2026-09-17
type: concept
tags: [concept, preference]
sources: [raw/inbox/2026-09-16.md, README.md]
confidence: medium
---

# Division of labor

Crow's operating model is a split between the human and the agent. ^[raw/inbox/2026-09-16.md]

> "The human curates sources and directs analysis. The agent
> summarizes, cross-references, files, and maintains consistency."
> ^[raw/inbox/2026-09-16.md]

## Roles

- **Human (Chris):** curates sources, directs analysis.
- **Agent (crow):** summarizes, cross-references, files, maintains consistency.

This pairs with crow's stated function — "Produces lore via web search,
extraction, and llm-wiki structure" — as the agent's side of the split.
^[README.md]

## Live-reload workflow

The agent updates pages as findings arrive and reloads the viewer so changes
appear live:

> "As we work, I'll update model pages with new findings and reload Obsidian so
> you see changes live."
> ^[raw/inbox/2026-09-16.md]

## Wiki location

The wiki path is set via the `WIKI_PATH` environment variable (e.g. in
`${HERMES_HOME:-~/.hermes}/.env`); if unset it defaults to `~/wiki`.
^[raw/inbox/2026-09-16.md]

## Skill activation

Crow's wiki skill fires on five documented triggers — act (create / ingest /
lint) rather than merely log when the user: creates/builds/starts a wiki,
ingests or processes a source, asks a question with a wiki present at
`WIKI_PATH`, asks to lint/audit/health-check the wiki, or references the wiki in
a research context. ^[raw/inbox/2026-09-16.md] See
[[topics/crow/wiki/concepts/wiki-skill-activation|Wiki skill activation]].

## Operational notes

- 2026-09-16 21:11 (hermes): the queries loop wrote to the wrong variable; fixed
  and recombined. ^[raw/inbox/2026-09-16.md]

## See also

- [[topics/crow/wiki/concepts/wiki-skill-activation|Wiki skill activation]]
- [[topics/crow/wiki/decisions/agents-to-bots-terminology|Agents-to-bots terminology decision]]
- [[topics/crow/wiki/concepts/bots-terminology|Bots terminology]]
- [[topics/crow/README.md|crow README]]
