---
title: "Model Check — 20260903_001447_7bc70a"
created: 2026-09-06
updated: 2026-09-13
type: entity
tags: [person, tool, decision, question, contested]
sources: ["raw/inbox/2026-09-06.md", "raw/inbox/2026-09-07.md", "raw/inbox/2026-09-10.md", "raw/inbox/2026-09-13.md"]
confidence: medium
contested: true
---

# Model Check — 20260903_001447_7bc70a

Chris is actively checking a specific model/session by id `20260903_001447_7bc70a` against realistic compression behavior.^[raw/inbox/2026-09-06.md] ^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-10.md]

## Session identifier
- session: `20260903_001447_7bc70a`

## Environment cleanup requirement
- `2026-09-07 00:08` — Chris: "I would really rather you be testing this 27B with as clean of a hard drive as you can... take off maple... delete that if it's still here."^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:02` — same cleanup request repeated verbatim.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:03` — same cleanup request repeated verbatim again.^[raw/inbox/2026-09-07.md]

## Performance — 2026-09-07
- Model: `MTPLX Qwen 3.8 27B`
- Hardware: `M1 MacBook 32GB`
- Context tested: `44 tokens → 10K+`
- Results:
  - `44 tokens` → `8.7 tok/s` ✅
  - `3K tokens` → `1.0 tok/s` ✅
  - `4K tokens` → `2.2 tok/s` ✅
  - `5K tokens` → `0.3 tok/s` ✅
  - `8K tokens` → `0.4 tok/s` ✅
  - `10K+ tokens` → `507 OOM` ❌
- Root cause: MTPLX loads at ~20GB, KV cache at 131K needs ~12GB. Combined 32GB leaves zero room for macOS or Hermes Agent.^[raw/inbox/2026-09-07.md]
- Stable on this box: `65K context` at `10-12 tok/s`, no OOM.^[raw/inbox/2026-09-07.md]
- Hermes Agent overhead: ~`2-4GB`.^[raw/inbox/2026-09-07.md]
- Comparison point: `M5 Max` achieves `58 tok/s` under the same model because of faster memory bus and idle system.^[raw/inbox/2026-09-07.md]
- Hermes recommendation: lock in `65K context` as main provider; retain catalog entry for future `64GB+` Mac upgrade.^[raw/inbox/2026-09-07.md]
- Accuracy note: separate prompt processing from generation for true tok/s; streamed measurement was identified as needed on session `20260907_023254_23b249`.^[raw/inbox/2026-09-07.md]
- Stale-process clarification: an OOM during testing may come from a stale wrong-flag attempt; verify active server pid before treating it as a model/host failure.^[raw/inbox/2026-09-07.md]
- Memory math: `Qwen 3.8 27B Q3_K_XL = 12.3GB`, `131K KV cache with q8 = ~8GB`, `DFlash2 draft = 1GB`, `macOS + Hermes Agent = 6-8GB`. Total exceeds 32GB on M1.^[raw/inbox/2026-09-07.md]
- Unsettled lock-in: despite Hermes-side provider lock attempts, the active provider/model changed multiple times during the session, indicating the lock was not stable or cleanly applied.^[raw/inbox/2026-09-07.md]
- Ornith proposal: at `2026-09-07 10:12`, Hermes proposed stopping Tiel-Coder and locking in Ornith as main provider, contradicting the earlier Unleashed + DFlash2 lock.^[raw/inbox/2026-09-07.md]
- Config-write friction: at `2026-09-07 13:51`, Hermes reported the tool was refusing to write to the Hermes config and needed to use the Hermes CLI instead.^[raw/inbox/2026-09-07.md]
- Runtime model changes: system logged active-model changes to `upstage/solar-pro4:free via provider nous` at `11:19`, `12:02`, `13:59`, and `inclusionai/ling-3.0-flash-sante:free via provider nous` at `14:03`.^[raw/inbox/2026-09-07.md]

## Session 20260907-030601
- A second live model check was initiated on `2026-09-07 03:06` under session id `20260907_030601_6012ee`.^[raw/inbox/2026-09-07.md]
- Requirements: `Qwen 3.8 27B` variant, `10+ tok/s` at `131K` context, after clean environment.^[raw/inbox/2026-09-07.md]
- Outcome: session interrupted at `05:38` after `20` API calls and `3400.36s` without a summarized conclusion.^[raw/inbox/2026-09-07.md]
- The interrupted session did not change earlier memory-cap evidence; it repeated the same target without producing new measurement data.^[raw/inbox/2026-09-07.md]

## 2026-09-10 — new similarity observation
- `2026-09-10 10:06` — session `20260903_001447_7bc70a`, similarity `sim 0.09`.^[raw/inbox/2026-09-10.md]
- `[System]` — "The active model for this chat has changed to grok-4.6 via provider xai. From this point forward, use this runtime metadata when answering questions about what model/provider is active."^[raw/inbox/2026-09-10.md]
- Note: this session continues to be referenced in new raw items, but the `sim 0.09` value is not yet integrated into the prior `0.07 → 0.06` progression recorded on 2026-09-06. The active model has also shifted to `grok-4.6 via provider xai` as of this entry, which differs from the `Qwen 3.8 27B` under evaluation on 2026-09-07.^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-10.md]
|- Contested: the session id `20260903_001447_7bc70a` is being reused across multiple evaluation windows with differing active providers and similarity measurements; treat the similarity trajectory as provisional until Chris confirms which run the `0.09` value belongs to.

## 2026-09-13 — same id, yet another active model
- The same session id `20260903_001447_7bc70a` is referenced again on `2026-09-13 16:43/16:52` with active model `ornith-1-5-35a3b` via provider `xai`, and `2026-09-13 16:44/16:53` with `longcat-2.0:free` via nous.^[raw/inbox/2026-09-13.md]
- This continues the reuse-of-one-session-id-across-different-providers pattern and further decouples the `sim 0.09` reading from any single comparable run. Reinforces the provisional-lock / provisional-similarity rule.

## Evidence
- `2026-09-06 18:15` — system-side note: "Now a realistic compression test — big essay summarization"^[raw/inbox/2026-09-06.md]
- `2026-09-06 19:34` — Chris: "checking out if this model works"^[raw/inbox/2026-09-06.md]
- `2026-09-07 00:08` — Chris: "I would really rather you be testing this 27B with as clean of a hard drive as you can"; asked to remove Maple and any remaining uncensored variant.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:02` — Chris repeated the same cleanup request verbatim.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:03` — Chris repeated the same cleanup request again, reinforcing it as a standing test precondition.^[raw/inbox/2026-09-07.md]
- `2026-09-07 02:35` — Hermes noted need for streaming measurement: separate prompt processing from generation time for accurate tok/s.^[raw/inbox/2026-09-07.md]
- `2026-09-07 03:06` — Chris: "Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context."^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:35` — Hermes stated `10+ tok/s at 131K` is not achievable on `M1 32GB` with `27B`; recommended `65K at ~7 tok/s` as daily driver and `64GB+` for the 131K target.^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:38` — interrupted evaluation session ended without summary while repeating the same Qwen 3.8 27B / 10+ tok/s at 131K target.^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:42` — Hermes returned to direct memory-cap explanation: `Qwen 3.8 27B Q3_K_XL = 12.3GB`, `131K KV cache = ~8GB`, `DFlash2 = 1GB`, macOS+Hermes = `6-8GB`; total `32GB` budget.^[raw/inbox/2026-09-07.md]
- `2026-09-10 10:06` — session `20260903_001447_7bc70a`, similarity `sim 0.09`; system notes active model changed to `grok-4.6 via provider xai`.^[raw/inbox/2026-09-10.md]

## Related
- [[topics-wiki/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]
- [[topics-wiki/hermes-agent/wiki/decisions/clean-model-test-precondition-2026-09-07|Clean Model Test Precondition — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/concepts/model-evaluation-2026-09-06|Model Evaluation — 2026-09-06]]
- [[topics-wiki/hermes-agent/wiki/decisions/compression-test-2026-09-06|Compression Test — 2026-09-06]]
- [[topics-wiki/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]