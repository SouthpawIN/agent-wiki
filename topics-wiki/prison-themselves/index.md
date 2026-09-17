---
title: prison-themselves
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# prison-themselves

Last updated: 2026-09-15 | Total pages: 7

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Bonsai MLX](wiki/bonsai-mlx.md) — A local MLX model Chris runs on his Mac, sibling to Ornith MLX in the same running set. [[topics-wiki/prison-themselves/wiki/entities/ornith-mlx|Ornith MLX]] is the
- [Ornith MLX](wiki/ornith-mlx.md) — A local MLX model Chris runs on his Mac. Ornith is one of a family of quantized models he keeps alive on dedicated ports, alongside Bonsai MLX and a ternary var
- [Ternary Bonsai MLX](wiki/ternary-bonsai-mlx.md) — A 2-bit ternary variant of Bonsai MLX that Chris added to his running set on 2026-09-07. His rationale was speed — "it's 2-bit ternary, might be faster."^[raw/i

### Concepts

- [dd Password Write](wiki/dd-password-write.md) — On 2026-09-12 a script was running that typed a password and then ran `dd` to write something to disk. The exact target is not specified in the raw item — only
- [Local MLX Model Fleet](wiki/local-mlx-model-fleet.md) — Chris runs a small fleet of quantized MLX models on his Mac, each on its own dedicated port. The family includes Ornith MLX (`:11613`), Bonsai MLX (`:11623`), a
- [Model Search Expectation](wiki/model-search-expectation.md) — Chris expects deep, thorough searching of model sources (e.g. HuggingFace) before a conclusion is drawn — and calls it out sharply when it isn't done. This is a

### Decisions

- [Model Port Layout](wiki/model-port-layout.md) — **What:** Each local MLX model runs on its own dedicated port so multiple can run at once.

---

## SKILLS

No topic skills yet.

---

## BOTS

Proposed bots:

- **[model-family-researcher](agents/model-family-researcher.md.proposed) — **I see you want thorough coverage of the bonsai/prism MLX model family — want a research bot that maps out every variant, quant, and HuggingFace sour
- **[model-fleet-keeper](agents/model-fleet-keeper.md.proposed) — **I see you're keeping a fleet of MLX models alive on dedicated ports and they keep dropping — want a bot that watches :11613 and :11623 and restarts 


---

## LOOPS

Proposed loops:

- **[fleet-health-tick](triggers-loops/fleet-health-tick.md.proposed) — owner: model-fleet-keeper · cadence: every 30 minutes · status: SUGGESTED
