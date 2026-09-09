---
title: "Bots terminology"
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [concept, preference, infra]
sources: [raw/inbox/2026-09-08.md, README.md]
confidence: high
---

# Bots terminology

Across the Hermes/Senter fleet the user-facing term is **"bots"**, not
"agents". The word "agents" survives only in internal code as a reflection
of the legacy `agents/` directory on disk. ^[raw/inbox/2026-09-08.md]

## Fleet convention

> "Crow — deep research agent for Hermes Agent."
> ^[README.md]

Even though Chris sometimes calls Crow the "deep research **agent**", the
canonical fleet vocabulary (see [[topics/crow/../../senter/BRIEF.md|Senter BRIEF]])
and the wiki UI itself use **"bots"**. The distinction is documented in:

- [[topics/crow/wiki/decisions/agents-to-bots-terminology.md|Agents-to-bots terminology decision]]

## Key distinction

| Layer | Term | Reason |
|-------|------|--------|
| UI / prose | bots | matches fleet vocabulary |
| Internal JS vars | agents | maps to `agents/` dir on disk |

## See also

- [[topics/crow/wiki/decisions/agents-to-bots-terminology.md|Terminology decision]]
- [[topics/crow/README.md|crow README]]
