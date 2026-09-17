---
title: looked-image
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# looked-image

Last updated: 2026-09-17 | Total pages: 11

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [131K optimization target](wiki/131k-optimization-target.md) — An explicit size/resource constraint introduced by Chris for an unnamed artifact.^[raw/inbox/2026-09-07.md]
- [Memory shard](wiki/memory-shard.md) — A Chris-coined term for a surviving local copy that can be used to reconstruct a desired state after something went wrong.
- [Screenshot 2026-09-05 4.38.59 PM](wiki/screenshot-2026-09-05-4-38-59-pm.md) — Visual content of this file was not successfully analyzed for this compile, so this page records known provenance and Chris’s use of it as a target reference.
- [Visual Reference section (Rules, Skills)](wiki/visual-reference-section-rules-skills.md) — A fragment captured from Hermes state on 2026-09-17 that lists a "Visual Reference" section followed by numbered items 10. Rules, 11. Skills, 12. (truncated).^[

### Concepts

- [Visual revert target](wiki/visual-revert-target.md) — A concept introduced by this topic: restore a broken or incorrect state by reference to a known-good visual artifact instead of verbal description.

### Decisions

- [Recovery before recreation](wiki/recovery-before-recreation.md) — When a state has diverged from a known-good screenshot, the first action is to search for a local memory shard; only if no shard exists should the state be rebu
- [Research optimization before rebuild](wiki/research-optimization-before-rebuild.md) — When an artifact must meet a size/resource target, prefer researching applicable optimization flags or quantization paths before rebuilding.
- [Revert-or-recreate decision](wiki/revert-or-recreate.md) — Prefer reverting to a known good visual state when possible; if revert is not possible, recreate it to match the screenshot.

### Comparisons

- [131K abstract vs Stafford-Douglasal](wiki/131k-abstract-vs-stafford-douglasal.md) — The 131K target is not yet pinned to one definition. It appears first as a generic artifact constraint, then as a local benchmark at Stafford-Douglasal Science

### Queries

- [Locate memory shard for revert target](wiki/locate-memory-shard.md) — Is there a local memory shard for the desired UI state that can be used to revert instead of recreating from scratch?
- [Meet 131K with optimization](wiki/meet-131k-with-optimization.md) — Can the current artifact meet the 131K target through further optimization research, rather than rebuilding?

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[looker-131k-research](agents/looker-131k-research.md.proposed) — **I see you're trying to hit a 131K target — want a bot that researches applicable optimization flags and verifies actual artifact size reduction?**
- **[looker](agents/looker.md.proposed) — **I see you're trying to recover a broken UI state from a screenshot — want a bot that can find and verify local memory shards and compare the live st


---

## LOOPS

Proposed loops:

- **[memory-shard-scan](loops/memory-shard-scan.md.proposed) — owner: looker · cadence: daily · status: SUGGESTED
- **[optimization-flag-scan](loops/optimization-flag-scan.md.proposed) — owner: looker · cadence: human phrase · status: SUGGESTED
