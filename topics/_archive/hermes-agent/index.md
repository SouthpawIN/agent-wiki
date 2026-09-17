---
title: hermes-agent
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# hermes-agent

Last updated: 2026-09-17 | Total pages: 27

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [Model Check — 20260903_001447_7bc70a](wiki/model-check-20260903.md) — Chris is actively checking a specific model/session by id `20260903_001447_7bc70a` against realistic compression behavior.^[raw/inbox/2026-09-06.md] ^[raw/inbox
- [Session Check — 20260907_030601_6012ee](wiki/session-20260907-030601.md) — On `2026-09-07`, Chris initiated a second live model check under session id `20260907_030601_6012ee`, reiterating the same variant and throughput requirement as
- [Similarity Observation — 2026-09-10 sim 0.09](wiki/session-20260910-sim-009.md) — - `2026-09-10 10:06` — session `20260903_001447_7bc70a`, similarity `sim 0.09`.^[raw/inbox/2026-09-10.md]
- [262K / 81.2 tok/s Milestone — 2026-09-15](wiki/session-20260915-262k-81tok.md) — On `2026-09-15` a new high-throughput large-context result was captured on a GPU-equipped machine: `Unleashed 27B Q3_K_XL` at `262K` context hitting `81.2 tok/s

### Concepts

- [Active Model / Provider Churn](wiki/active-model-provider-churn.md) — Across consecutive sessions the active Hermes model and provider never settled — the same session id was reused with a different provider each time. That is the
- [hermes-agent Repo Git Remotes — 2026-09-10](wiki/hermes-agent-repo-git-remotes.md) — Investigated on `2026-09-10` whether the `gh-sync/agent-wiki` repo is the same as the Hermes Agent checkout. Findings:
- [Hermes Install Broken-Fixed on Omarchy — 2026-09-15](wiki/hermes-install-on-omarchy-2026-09-15.md) — On `2026-09-15`, the Hermes CLI on Chris's **Omarchy** machine was found broken and then repaired. The root cause was a root-owned virtualenv blocking the real
- [DHH Linux Distro with Hermes as Native AI](wiki/hermes-on-dhh-linux-camp.md) — On `2026-09-12`, Chris said he's "looking for the latest Linux distro by DHH" and that "the latest update should have Hermes agent as a native AI."^[raw/inbox/2
- [/hotkeys Slash Command](wiki/hotkeys-slash-command.md) — On `2026-09-15 02:17`, Chris requested a new Hermes-Agent feature: a `/hotkeys` slash command that displays — and, going forward, edits — the combined set of He
- [Model Evaluation — 2026-09-06](wiki/model-evaluation-2026-09-06.md) — Chris uses live Hermes sessions as evaluation environments. On 2026-09-06, he ran a realistic compression test and checked whether the active model worked.^[raw
- [Skills & Bots Progressive Disclosure in the Wiki](wiki/skills-bots-progressive-disclosure.md) — On `2026-09-17 10:45` Chris set out how the wiki should present its skills and bots — as browsable lists where each entry uses progressive disclosure, and where
- [Streaming Throughput Measurement](wiki/streaming-throughput-measurement.md) — Accurate tok/s reporting for local Hermes inference requires separating prompt-processing time from generation time.^[raw/inbox/2026-09-07.md]
- [Topic Index Restructure — 2026-09-16](wiki/topic-index-restructure-2026-09-16.md) — On `2026-09-16 21:09`, Hermes began consolidating the topic's root `index.md` into a clean entry point. This is wiki-structure maintenance (the topic's own inde

### Decisions

- [131K on 32GB Feasibility Decision — 2026-09-07](wiki/131k-on-32gb-feasibility-decision-2026-09-07.md) — **Not-now.** The `10+ tok/s at 131K context` target with `Qwen 3.8 27B` cannot be achieved on `M1 MacBook 32GB`. It requires a hardware upgrade to `64GB+` RAM o
- [Compression Test — 2026-09-06](wiki/compression-test-2026-09-06.md) — On `2026-09-06`, Chris treated a "big essay summarization" task as a realistic compression test for the active Hermes session/stack.^[raw/inbox/2026-09-06.md]
- [Main Provider Lock — 2026-09-07](wiki/main-provider-lock-2026-09-07.md) — On `2026-09-07`, Hermes side locked `Unleashed + DFlash2` as the main provider at `131K` context and instructed a Hermes Agent restart to pick up the change.^[r
- [Model Test Environment Cleanup — 2026-09-07](wiki/model-test-environment-cleanup-2026-09-07.md) — On `2026-09-07`, Chris required that model evaluation for `Qwen 3.8 27B` run only after removing Maple and deleting any remaining uncensored model variant, so t
- [Ornith Provider Placement — 2026-09-13](wiki/ornith-provider-placement-2026-09-13.md) — On `2026-09-13`, Chris corrected that the `ornith-1-5-35a3b` model belongs under provider **xai**, not under a TurboFit-style ("turbo fed") provider.^[raw/inbox
- [Provider Lock Review — 2026-09-07](wiki/provider-lock-review-2026-09-07.md) — On `2026-09-07`, Hermes recorded a provisional provider lock of `Unleashed + DFlash2` at `131K` context. That lock is not accepted as final on this topic: it is
- [Stable Context Lock — 2026-09-07](wiki/stable-context-lock-2026-09-07.md) — On `2026-09-07`, Chris received evidence that `131K` context with `MTPLX Qwen 3.8 27B` is not viable on `M1 MacBook 32GB`, and accepted `65K` context as the sta
- [Targeted 27B at 131K — 2026-09-07](wiki/targeted-27b-131k-2026-09-07.md) — On `2026-09-07`, Chris explicitly required the active provider to be the `Qwen 3.8 27B` variant, with a target of `10+ tok/s` at `131K` context.^[raw/inbox/2026

### Comparisons

- [65K vs 131K Context Comparison](wiki/65k-vs-131k-context.md) — On `M1 MacBook 32GB` with `Qwen 3.8 27B` + `MTPLX` + `DFlash2`, the two context-length options are not interchangeable — `131K` is a hardware ceiling that trigg

### Queries

- [Can Qwen 3.8 27B achieve 10+ tok/s at 131K on M1 32GB with any combination?](wiki/27b-131k-ceiling-confirmation.md) — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [Can 131K context with Qwen 3.8 27B be made stable on M1 32GB?](wiki/32gb-131k-feasibility.md) — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [Is there a viable M-series Mac below 64GB RAM for Qwen 3.8 27B at 131K?](wiki/m1-27b-131k-hardware-floor.md) — **Resolved — answered** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision —
- [Can MTPLX use CPU offload, disk cache, or lower-precision KV to fit 131K on 32GB?](wiki/mtplx-131k-offloading-options.md) — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [What config flags, quantization, or offloading strategies run MTPLX 27B at 131K on 32GB?](wiki/mtplx-131k-optimization.md) — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2

---

## SKILLS

Topic skills stored in this wiki:

- **[clean-environment-model-evaluation](skills/clean-environment-model-evaluation/SKILL.md) — 1. Before any model evaluation run, remove Maple and delete any uncensored model variants; Chris treats this as mandatory, not optional.
- **[live-model-evaluation](skills/live-model-evaluation/SKILL.md) — 1. Confirm the active Hermes provider and session id.
- **[m1-27b-context-lock](skills/m1-27b-context-lock/SKILL.md) — 1. Confirm model variant explicitly before testing: `Qwen 3.8 27B` only. 2. Clean environment first: remove Maple; delete any uncensored model variant
- **[provider-lock-validation](skills/provider-lock-validation/SKILL.md) — 1. Require explicit confirmation of both model variant and throughput target before accepting a lock. 2. If the lock was recorded before Chris's expli

---

## BOTS

Proposed bots:

- **[clean-model-test](agents/clean-model-test.md.proposed) — **I see you're testing the same model path on a dirty stack — want a bot that removes Maple, deletes uncensored variants, verifies the active provider
- **[hermes-agent-bot](agents/hermes-agent-bot.md.proposed) — Owns the `hermes-agent` topic: runs its skills, answers for it, proposes its loops.
- **[hotkeys-command](agents/hotkeys-command.md.proposed) — **I see you asked for a /hotkeys slash command on 2026-09-15 and it's still unbuilt — want teknium to implement it?**
- **[model-evaluator](agents/model-evaluator.md.proposed) — **I see you're running live compression tests to validate model behavior — want a bot that automates the big-essay summarization pass, measures stream
- **[provider-lock-reconciler](agents/provider-lock-reconciler.md.proposed) — **I see you're cycling through Unleashed, DFlash2, Ornith, and nous free models — want a bot that reconciles your wiki's approved provider lock with w


---

## LOOPS

Proposed loops:

- **[daily-model-check](loops/daily-model-check.md.proposed) — owner: looker · cadence: daily during active model testing · status: SUGGESTED
- **[mtplx-config-drift-check](loops/mtplx-config-drift-check.md.proposed) — owner: looker · cadence: every 3 hours · status: SUGGESTED
- **[runtime-provider-drift-watch](loops/runtime-provider-drift-watch.md.proposed) — owner: looker · cadence: every 2h · status: SUGGESTED
