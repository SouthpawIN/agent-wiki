---
title: "Hermes fallback causes"
created: 2026-09-06
updated: 2026-09-06
type: entity
tags:
  - tool
  - infra
  - pain
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
confidence: high
---

# Hermes fallback causes

## What Chris observed
The runtime loaded a backup model instead of the explicitly chosen one, and later records showed automatic model changes during the session.

> "No, that's still not the right one. That one's like the backup model." ^[raw/inbox/2026-09-06.md]

## Technical causes
Klerik traced two specific causes: the active model appearing from a fallback list, and a deterministic fallback triggered because the LLM context summarizer was unavailable.

> "The `stepfun/step-3.7-flash` in the system message context was coming from the fallback list" ^[raw/inbox/2026-09-06-from-klerik.md]

^[raw/inbox/2026-09-06.md]

> "Recovered from a deterministic fallback because the LLM context summarizer was unavailable." ^[raw/inbox/2026-09-06.md]

## Related
- [[wiki-topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[wiki-topics/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
- [[wiki-topics/back-where/wiki/entities/recovery-background-process|Recovery background process mid-run]]
