---
title: Senter Self-Model Schema
created: 2026-08-31
type: selfmodel-schema
source: Anser founding audit (founding-audit-anser-20260901.md)
---

# SCHEMA — Senter's Declarative Self-Model

This directory is Senter's structured self-knowledge layer, per Anser's audit verdict:
the agent-wiki fills the gap Hermes leaves — a **structured, interlinked, queryable
declarative self-model**. Rules (non-negotiable):

1. **Query-on-demand, never injected verbatim.** This dir stays OUT of context-file
   discovery paths. Distilled one-liners get flushed into `memory` instead.
2. **Curator lifecycle.** Every page gets `updated:` frontmatter; stale pages are
   archived (never deleted); consolidation replaces sprawl.
3. **Wikilinks over duplication.** One fact, one page; link to it.
4. **Provenance always.** Every claim links to its evidence (session, file, tool output).
5. **Anser gate.** Before adding a NEW page type, consult @anser — does Hermes
   built-in already cover it?

## Page types

| File | Axis | Contents |
|---|---|---|
| `capabilities.md` | inventory | What Senter can do: tools, skills, authority limits, delegation reach |
| `decisions.md` | decision log | Decisions WITH rationale + date + who approved; append-only |
| `lessons.md` | lessons | Distilled operational lessons; each links to its evidence |
| `relationships.md` | graph | Fleet roster + vault topics + external systems Senter touches |
| `open-questions.md` | contradictions | Flagged uncertainties, contradictions between beliefs, unresolved debates |
| `founding-audit-anser-20260901.md` | provenance | The audit that established this layer (2026-08-31) |

## Lifecycle

- **Update trigger:** after any decision, lesson, or capability change in a session.
- **Flush:** monthly (or on major change) distill to memory one-liners.
- **Review:** Anser audits quarterly for overlap with Hermes built-ins.
- **Archive:** superseded content moves to `.system/selfmodel/archive/` with date prefix.
