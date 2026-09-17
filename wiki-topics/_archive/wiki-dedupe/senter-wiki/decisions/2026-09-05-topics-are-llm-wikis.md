---
title: Decision: every topic is a two-layer LLM wiki; CONTEXT renders index.md
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, infra]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
contested: true
---

# Topics are LLM wikis; CONTEXT = index.md (2026-09-05 17:42–17:43)

> **Superseded in part, 19:06.** The two-layer wiki stands; the *rendering* half ("CONTEXT renders the full `index.md`; context orb = page count") was rejected by Chris the same evening — *"I don't want any numbers indicating what's in the wiki, I want to just see the wiki."* Current rule: [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|CONTEXT is the wiki itself with live diffs]]. ^[raw/inbox/2026-09-05.md]

**What.** Chris pushed back on "context" being a 220-char summary and pointed at the `llm-wiki` skill. Root fix: `raw/` (immutable inbox + sources), `wiki/` five sections
with provenance, `SCHEMA.md`/`index.md`/`log.md`; the row's CONTEXT section renders the **full `index.md`**, the context orb = page count; compile loop every 15 min then
`topic-agent`. ^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Why.** *"I'd been misreading 'context' as a summary line."* Context is the outermost GOOP primitive — it must be the topic's structured understanding, not a blurb.
**Scope.** All 19 topics initialised; transcripts grepped on demand, not compiled. See [[wiki-topics/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]],
[[wiki-topics/senter-wiki/wiki/entities/topic-worker|compiler]].
