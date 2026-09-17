---
title: "2026-09-02 — Process artifacts are the product"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, preference]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-02 — Process artifacts are the product

**What.** Chris: **"this is exactly how I intend people to use this product… as we fix things we need to be bolstering it in the wiki."** A lesson written only into `log.md` is invisible to an adopter, so every repeat correction becomes a rule in the owning topic's `process/` doc: pipeline/verification rules → `wiki-topics/senter/process/build-loop.md`; how-to-write-a-bot rules → `wiki-topics/klerik/process/agent-authoring-rules.md` (12 rules, each traced to a correction; klerik owns and applies it to every SOUL/AGENTS). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Corollaries stated with it.**
- Visual UI work must use vision and be captured as skills-capabilities/bots — "use the workflow we're building"; "write this as a skill and maybe a bot" → the `wiki-look-verify` skill and [[wiki-topics/senter/wiki/entities/looker|looker]].
- "No dummy data" is a hard rule ([[wiki-topics/senter/wiki/concepts/live-data-contract|live-data contract]]).
- Every standing rule Chris states goes into the owning bot's SOUL the same turn.

**Why.** The Senter system is meant to ship to others; the vault + process docs are the deliverable, not a by-product. Chris's 2026-09-05 words: the wiki is "a funnel for all of the contacts for everything that the user cares or worries about" — a product for *users*, not just for him. ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Related.** [[wiki-topics/senter/wiki/concepts/markdown-is-the-api|Markdown is the API]]; [[wiki-topics/senter/wiki/concepts/reflect-loop|REFLECT loop]] (automates repeat-correction → rule).
