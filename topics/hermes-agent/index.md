# hermes-agent — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-17 | Total pages: 26

## Entities
- [[topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]] — Chris is actively checking a specific model/session by id `20260903_001447_7bc70a` against realistic compression behavior.^[raw/inbox/2026-09-06.md] ^[raw/inbox
- [[topics/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]] — On `2026-09-07`, Chris initiated a second live model check under session id `20260907_030601_6012ee`, reiterating the same variant and throughput requirement as
- [[topics/hermes-agent/wiki/entities/session-20260910-sim-009|Similarity Observation — 2026-09-10 sim 0.09]] — - `2026-09-10 10:06` — session `20260903_001447_7bc70a`, similarity `sim 0.09`.^[raw/inbox/2026-09-10.md]
- [[topics/hermes-agent/wiki/entities/session-20260915-262k-81tok|262K / 81.2 tok/s Milestone — 2026-09-15]] — On `2026-09-15` a new high-throughput large-context result was captured on a GPU-equipped machine: `Unleashed 27B Q3_K_XL` at `262K` context hitting `81.2 tok/s

## Concepts
- [[topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]] — Across consecutive sessions the active Hermes model and provider never settled — the same session id was reused with a different provider each time. That is the
- [[topics/hermes-agent/wiki/concepts/hermes-agent-repo-git-remotes|hermes-agent Repo Git Remotes — 2026-09-10]] — Investigated on `2026-09-10` whether the `gh-sync/agent-wiki` repo is the same as the Hermes Agent checkout. Findings:
- [[topics/hermes-agent/wiki/concepts/hermes-install-on-omarchy-2026-09-15|Hermes Install Broken-Fixed on Omarchy — 2026-09-15]] — On `2026-09-15`, the Hermes CLI on Chris's **Omarchy** machine was found broken and then repaired. The root cause was a root-owned virtualenv blocking the real 
- [[topics/hermes-agent/wiki/concepts/hermes-on-dhh-linux-camp|DHH Linux Distro with Hermes as Native AI]] — On `2026-09-12`, Chris said he's "looking for the latest Linux distro by DHH" and that "the latest update should have Hermes agent as a native AI."^[raw/inbox/2
- [[topics/hermes-agent/wiki/concepts/hotkeys-slash-command|/hotkeys Slash Command]] — On `2026-09-15 02:17`, Chris requested a new Hermes-Agent feature: a `/hotkeys` slash command that displays — and, going forward, edits — the combined set of He
- [[topics/hermes-agent/wiki/concepts/model-evaluation-2026-09-06|Model Evaluation — 2026-09-06]] — Chris uses live Hermes sessions as evaluation environments. On 2026-09-06, he ran a realistic compression test and checked whether the active model worked.^[raw
- [[topics/hermes-agent/wiki/concepts/streaming-throughput-measurement|Streaming Throughput Measurement]] — Accurate tok/s reporting for local Hermes inference requires separating prompt-processing time from generation time.^[raw/inbox/2026-09-07.md]
- [[topics/hermes-agent/wiki/concepts/topic-index-restructure-2026-09-16|Topic Index Restructure — 2026-09-16]] — On `2026-09-16 21:09`, Hermes began consolidating the topic's root `index.md` into a clean entry point. This is wiki-structure maintenance (the topic's own inde

## Decisions
- [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]] — **Not-now.** The `10+ tok/s at 131K context` target with `Qwen 3.8 27B` cannot be achieved on `M1 MacBook 32GB`. It requires a hardware upgrade to `64GB+` RAM o
- [[topics/hermes-agent/wiki/decisions/compression-test-2026-09-06|Compression Test — 2026-09-06]] — On `2026-09-06`, Chris treated a "big essay summarization" task as a realistic compression test for the active Hermes session/stack.^[raw/inbox/2026-09-06.md]
- [[topics/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]] — On `2026-09-07`, Hermes side locked `Unleashed + DFlash2` as the main provider at `131K` context and instructed a Hermes Agent restart to pick up the change.^[r
- [[topics/hermes-agent/wiki/decisions/model-test-environment-cleanup-2026-09-07|Model Test Environment Cleanup — 2026-09-07]] — On `2026-09-07`, Chris required that model evaluation for `Qwen 3.8 27B` run only after removing Maple and deleting any remaining uncensored model variant, so t
- [[topics/hermes-agent/wiki/decisions/ornith-provider-placement-2026-09-13|Ornith Provider Placement — 2026-09-13]] — On `2026-09-13`, Chris corrected that the `ornith-1-5-35a3b` model belongs under provider **xai**, not under a TurboFit-style ("turbo fed") provider.^[raw/inbox
- [[topics/hermes-agent/wiki/decisions/provider-lock-review-2026-09-07|Provider Lock Review — 2026-09-07]] — On `2026-09-07`, Hermes recorded a provisional provider lock of `Unleashed + DFlash2` at `131K` context. That lock is not accepted as final on this topic: it is
- [[topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]] — On `2026-09-07`, Chris received evidence that `131K` context with `MTPLX Qwen 3.8 27B` is not viable on `M1 MacBook 32GB`, and accepted `65K` context as the sta
- [[topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]] — On `2026-09-07`, Chris explicitly required the active provider to be the `Qwen 3.8 27B` variant, with a target of `10+ tok/s` at `131K` context.^[raw/inbox/2026

## Comparisons
- [[topics/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]] — On `M1 MacBook 32GB` with `Qwen 3.8 27B` + `MTPLX` + `DFlash2`, the two context-length options are not interchangeable — `131K` is a hardware ceiling that trigg

## Queries
- [[topics/hermes-agent/wiki/queries/27b-131k-ceiling-confirmation|Can Qwen 3.8 27B achieve 10+ tok/s at 131K on M1 32GB with any combination?]] — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [[topics/hermes-agent/wiki/queries/32gb-131k-feasibility|Can 131K context with Qwen 3.8 27B be made stable on M1 32GB?]] — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [[topics/hermes-agent/wiki/queries/m1-27b-131k-hardware-floor|Is there a viable M-series Mac below 64GB RAM for Qwen 3.8 27B at 131K?]] — **Resolved — answered** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 
- [[topics/hermes-agent/wiki/queries/mtplx-131k-offloading-options|Can MTPLX use CPU offload, disk cache, or lower-precision KV to fit 131K on 32GB?]] — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2
- [[topics/hermes-agent/wiki/queries/mtplx-131k-optimization|What config flags, quantization, or offloading strategies run MTPLX 27B at 131K on 32GB?]] — **Resolved — not-now** (2026-09-07). See [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2

