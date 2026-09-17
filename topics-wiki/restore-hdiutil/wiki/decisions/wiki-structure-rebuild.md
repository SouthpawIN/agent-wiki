---
title: 2026-09-16 wiki structure rebuild
created: 2026-09-16
updated: 2026-09-16
type: decision
tags: [decision, spec, infra, timeline]
sources: [raw/inbox/2026-09-16.md]
confidence: high
---

# 2026-09-16 wiki structure rebuild

The topic's wiki scaffolding was rebuilt on 2026-09-16 after hermes reported the structure was wrong. [^raw1]

## What chris said (build instructions)
- "Write `SCHEMA.md` customized to the domain (see template below)" — the step list continued: "5. Write initial `index.md` with sectioned header", "6. Write initial `log.md` with creation entry", "7." [^raw1]
- These are the topic-wiki build recipe: SCHEMA.md, index.md, and log.md are the three files that scaffold a topic.

## What hermes did
- 13:37 — "Downloads failed - wrong command format. Let me fix:" [^raw1]
- 22:13 — "The structure is still wrong. Let me restore from git and do this cleanly with one comprehensive rewrite:" [^raw1]
- 22:15 — "The table extraction failed. Let me restore and extract the actual tables properly" [^raw1]

## Status
SCHEMA.md, index.md, and log.md all exist and are current. SCHEMA.md is per-domain (custom tag taxonomy, page thresholds, the `<!-- chris -->` rule). The restructure was a **wiki-scaffolding operation** — it did not change the topic's subject content (hdiutil restore failure, Omarchy ISO flash, USB instability). [^raw1]

## Related
- [[topics-wiki/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — the topic's subject content, unchanged by the rebuild.
- [[topics-wiki/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — the subject content.

---
[^raw1]: [raw/inbox/2026-09-16.md](raw/inbox/2026-09-16.md).
