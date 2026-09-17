---
name: wiki-orientation-procedure
description: Use before ingesting, querying, or linting an existing topic wiki. Always orient first: read SCHEMA.md, then index.md, then the last 20-30 log.md entries, then act; run search_files for wikis with 100+ pages.
version: 0.1.0
distilled: 2026-09-17 04:33
topic: kashik
---
# wiki-orientation-procedure
# Wiki orientation procedure

Always orient before ingesting, querying, or linting an existing topic wiki. Standing rule — stated "CRITICAL — do this every session" and repeated verbatim in the watcher's filings.

## Steps
1. Read SCHEMA.md — domain, conventions, tag taxonomy.
2. Read index.md — what pages exist and their summaries.
3. Scan the last 20-30 entries of log.md — recent activity.
4. Only after (1)-(3) complete: ingest, query, or lint.
5. For wikis with 100+ pages: also run a quick search_files for the topic at hand before creating anything new.

## Why
Prevents: duplicate pages for entities that already exist, missing cross-references, contradicting the schema's conventions, repeating work already logged.

## Pitfalls
- The companion "Initializing a New Wiki" procedure is still incomplete in source (opens, then stops at step 1). Do not assume it exists; fill it in when Chris actually starts a new topic wiki.
- Orient even when you think you know the topic — a raw item can belong to a wiki that already has pages.
- raw/ is immutable; never edit raw to "fix" a duplicate filing.

## Evidence
> "Resuming an Existing Wiki (CRITICAL — do this every session)" and spells out the order: ① Read SCHEMA.md ② Read index.md ③ Scan recent log.md
> Only after orientation should the agent "ingest, query, or lint."
> For large wikis (100+ pages), also run a quick search_files for the topic at hand before creating anything new.
