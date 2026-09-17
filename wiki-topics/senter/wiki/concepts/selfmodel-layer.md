---
title: Self-model layer (wiki-topics/senter/.system/selfmodel)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, plan, tool]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Self-model layer (wiki-topics/senter/.system/selfmodel)

Built **2026-08-31** per [[wiki-topics/senter/wiki/entities/anser|anser]]'s audit: Senter's declarative self-knowledge, separate from Hermes built-ins. Files: `SCHEMA.md` (page types + lifecycle), `decisions.md` (append-only, rationale + approver), `lessons.md` (evidence-linked; #1–28 by 2026-09-02), `capabilities.md`, `relationships.md`, `open-questions.md`, `founding-audit`. Reference: skill `references/vault-ui-architecture.md`. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Anser's 5 rules (all adopted)
1. **Query-on-demand, NEVER injected verbatim into context** — flush distilled one-liners into `memory` instead.
2. Curator lifecycle: `updated:` frontmatter, archive-never-delete.
3. Wikilinks over duplication.
4. Provenance on every claim.
5. Consult anser before creating a NEW page type — Hermes built-ins may already cover it: memory = flat facts, skills = procedures, session_search = raw episodes, SOUL/AGENTS = fixed contracts; "the vault = the structured growing self-model none of them provide."

Update the selfmodel after any decision, lesson, or capability change.

## Relation to this wiki
The selfmodel was the first "memory layer" for Senter; on 2026-09-05 Chris generalized the idea to every topic — "this is supposed to be basically a memory layer for Hermes agent" — with [[wiki-topics/senter/wiki/concepts/progressive-disclosure|progressive disclosure]] as the read path and full LLM wikis (this one) as the store ([[wiki-topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|decision]], [[wiki-topics/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|decision]]). Rule 1 ("never injected verbatim") is exactly the disclosure principle. ^[raw/inbox/2026-09-05-legacy-inbox.md]
