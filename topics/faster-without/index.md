---
title: faster-without
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# faster-without

Last updated: 2026-09-17 | Total pages: 15

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [27B Model](wiki/27b-model.md) — The 27B model is the concrete inference target in this topic. Chris’s standing requirement is that it run at a minimum 131K context length, even if D-flash is r
- [81 tok/s Build (Checkpoint)](wiki/81-tok-s-build.md) — A build reported at **81 tokens per second** — described by Chris as "excellent" — that he wanted captured as a **checkpoint before attempting any DFlash2 specu
- [D-Flash](wiki/d-flash.md) — D-flash is the feature under review for removal to improve inference speed. Chris asked, "Would it be faster without it?" and later clarified: "By faster, I mea
- [DFlash2](wiki/d-flash2.md) — DFlash2 appears in a live setup labeled `Unleashed + DFlash2`, which is reported up at 131K and intended for speed testing against a separate `Unleashed` server
- [Unleashed](wiki/unleashed.md) — Unleashed is a speed reference point in Chris’s comparison. A measured state of 8.4 tok/s for 1000 tokens was described as faster than Unleashed. ^[raw/inbox/20

### Concepts

- [Save Checkpoint Before Experiment](wiki/checkpoint-before-experiment.md) — Chris's working rule before any speculative-decode change: **capture the current good build as a checkpoint first, so it can be restored if the experiment regre
- [D-Flash Tradeoff](wiki/d-flash-tradeoff.md) — Chris questions whether D-flash is why current speeds are lower than he remembers. ^[raw/inbox/2026-09-06.md#L7] He wants to know whether removing it would make
- [Measured Performance](wiki/measured-performance.md) — Chris recalled earlier speeds being much higher than current performance. The only explicit benchmark captured so far is 8.4 tok/s for 1000 tokens, described as
- [27B at 131K](wiki/performance-target.md) — Chris’s explicit requirement is that the 27B model run at a minimum 131K context length. ^[raw/inbox/2026-09-06.md#L17] This target holds even when reconsiderin

### Decisions

- [Fix Tables Then Checkpoint](wiki/fix-tables-then-checkpoint.md) — On **2026-09-16**, Chris gave a **sequencing rule** for what to finish before the topic moves on: fix the wiki's tables first, then rebuild the checkpoint to ma
- [Retain 131K Context](wiki/retain-131k-context.md) — Chris decided that any speed change must preserve the hard floor of 131K context length for the 27B model. ^[raw/inbox/2026-09-06.md#L17]

### Comparisons

- [DFlash2 Without D-Flash — Full Responses at High Speed](wiki/dflash2-without-dflash-high-speed.md) — With D-flash **disabled**, "**both MTP and DFlash2 produce full responses at high speed**." ^[raw/inbox/2026-09-15.md#L16] This is the first measured outcome of
- [Unleashed vs DFlash2](wiki/unleashed-vs-dflash2.md) — A planned head-to-head performance comparison between the separate `Unleashed` server and the `Unleashed + DFlash2` setup. Both are reported running, and the st
- [With vs Without D-Flash](wiki/with-without-d-flash.md) — Chris is comparing the current D-flash-enabled state against a hypothetical faster state without it. He recalls earlier speeds being much higher and suspects D-

### Queries

- [How to Hook Up DFlash2 Speculative Decoder](wiki/dflash2-spec-draft-hookup.md) — Two open questions about wiring **DFlash2**, a speculative decoder, for the Unleashed model: **how D-flash 2 is "supposed to be hooked up,"** and the mechanics

---

## SKILLS

Topic skills stored in this wiki:

- **[d-flash-131k-benchmark](skills/d-flash-131k-benchmark/SKILL.md) — 1. Confirm both Unleashed and Unleashed+DFlash2 servers are running at 131K context.

---

## BOTS

Proposed bots:

- **[d-flash-benchmarker](agents/d-flash-benchmarker.md.proposed) — **I see you're weighing D-flash removal for speed — want a bot that benchmarks 27B@131K with/without D-flash and reports whether the 131K target still
- **[d-flash-checkpoint](agents/d-flash-checkpoint.md.proposed) — **I see you're about to engage the DFlash2 spec-draft but the 81 tok/s checkpoint save is unconfirmed and you said don't move further until the curren
- **[d-flash2-benchmark](agents/d-flash2-benchmark.md.proposed) — **I see the DFlash2 high-speed result ('both MTP and DFlash2 produce full responses at high speed') has no tok/s number — want a bot that benchmarks t
- **[d-flash2-setup-research](agents/d-flash2-setup-research.md.proposed) — **Want me to look into exactly how DFlash2's spec-draft is configured for qwen4 at 131K — the precise setup requirements the 09-15 run left open?**


---

## LOOPS

Proposed loops:

- **[d-flash2-checkpoint-watch](loops/d-flash2-checkpoint-watch.md.proposed) — owner: d-flash-benchmarker · cadence: every morning · status: SUGGESTED
- **[d-flash2-daily-speed-watch](loops/d-flash2-daily-speed-watch.md.proposed) — owner: d-flash-benchmarker · cadence: daily · status: SUGGESTED
- **[daily-131k-speed-check](loops/daily-131k-speed-check.md.proposed) — owner: teknium · cadence: daily · status: SUGGESTED
