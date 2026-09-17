---
title: Wiki orientation procedure (resuming an existing wiki)
created: 2026-09-16
updated: 2026-09-16
type: concept
tags:
  - skill
  - preference
  - infra
sources:
  - raw/inbox/2026-09-14.md
  - raw/inbox/2026-09-16.md
confidence: high
---

# Wiki orientation procedure (resuming an existing wiki)

A standing rule for the kashik compile loop: always orient before ingesting, querying, or linting. The procedure is repeated verbatim in the watcher's filings, which is what makes it a rule rather than a one-off tip.

## What Chris said

The filing states: *"Resuming an Existing Wiki (CRITICAL — do this every session)"* and spells out the order:

① **Read `SCHEMA.md`** — understand the domain, conventions, and tag taxonomy.
② **Read `index.md`** — learn what pages exist and their summaries.
③ **Scan recent `log.md`** — read the last 20-30 entries to understand recent activity.

Only after orientation should the agent *"ingest, query, or lint."* ^[raw/inbox/2026-09-16.md]

For large wikis (100+ pages), also run a quick `search_files` for the topic at hand before creating anything new. ^[raw/inbox/2026-09-16.md]

## Why

Orientation prevents four specific failures:

- Creating duplicate pages for entities that already exist
- Missing cross-references to existing content
- Contradicting the schema's conventions
- Repeating work already logged ^[raw/inbox/2026-09-16.md]

## Layering note

The filing frames the wiki as layered; the schema sits at **"Layer 3 — The Schema: `SCHEMA.md` defines structure, conventions, and tag taxonomy."** ^[raw/inbox/2026-09-16.md] (This is the only layering terminology present in the raw — treat it as a label, not a full taxonomy.)

## Companion procedure (incomplete in source)

The same filing carries an **"Initializing a New Wiki"** section that opens *"When the user asks to create or start a wiki:"* and then stops at step 1 — an unfinished procedure, not yet filled in. ^[raw/inbox/2026-09-16.md]

## Related

- [[wiki/entities/kashik|kashik]]
- [[wiki/concepts/llm-wiki|llm-wiki]]
- [[wiki/concepts/librarian-concept|Librarian concept]]
- [[wiki/decisions/topic-discovery-governance|Topic discovery governance]]
