---
title: "Active Model / Provider Churn"
created: 2026-09-13
updated: 2026-09-17
type: concept
tags: [tool, preference, infra, contested, timeline]
sources: ["raw/inbox/2026-09-07.md", "raw/inbox/2026-09-10.md", "raw/inbox/2026-09-11.md", "raw/inbox/2026-09-12.md", "raw/inbox/2026-09-13.md", "raw/inbox/2026-09-15.md", "raw/inbox/2026-09-16.md", "raw/inbox/2026-09-17.md"]
confidence: high
---

# Active Model / Provider Churn

Across consecutive sessions the active Hermes model and provider never settled — the same session id was reused with a different provider each time. That is the strongest live evidence that no provider lock is final until a verified config write and restart confirm both the exact model variant and the throughput target.^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-10.md] ^[raw/inbox/2026-09-11.md]

## Timeline of active-model changes
- `2026-09-07` — provisional `Unleashed + DFlash2` lock at `131K`, then a competing `Ornith` proposal; runtime changes to `upstage/solar-pro4:free` and `inclusionai/ling-3.0-flash-sante:free` (both provider `nous`).^[raw/inbox/2026-09-07.md]
- `2026-09-10 10:06` — system: active model → `grok-4.6` via provider `xai`.^[raw/inbox/2026-09-10.md]
- `2026-09-10 15:07` — system: active model → `meituan/longcat-2.0:free` via provider `nous`.^[raw/inbox/2026-09-10.md]
- `2026-09-10 15:19–15:22` — toggles back to `grok-4.6` (xai), then again `longcat-2.0:free` (nous).^[raw/inbox/2026-09-10.md]
- `2026-09-11 18:04–18:06` — `grok-4.6` (xai) → `deepseek-v4-flash-free` (opencode-free) → `longcat-2.0:free` (nous).^[raw/inbox/2026-09-11.md]
- `2026-09-12 14:12` — `grok-4.6` (xai), then `longcat-2.0:free` (nous).^[raw/inbox/2026-09-12.md]
- `2026-09-13 16:43/16:52/16:53` — `ornith-1-5-35a3b` via provider `xai`.
- `2026-09-13 16:44/16:53` — toggles back to `longcat-2.0:free` via nous.
- `2026-09-14 20:38` — session `20260914_200308_f9b029`, `sim 0.06`, operation interrupted (hermes).^[raw/inbox/2026-09-14.md]
- `2026-09-15 02:14` — `[System]` active model → `meituan/longcat-2.0:free` via provider `nous` (session `20260914_222247_d630dd`, `sim 0.17`).^[raw/inbox/2026-09-15.md]
- `2026-09-15 09:18` — `[System]` active model → `meituan/longcat-2.0:free` via provider `nous` (session `20260914_200308_f9b029`, `sim 0.17`). Same provider as the 262K/81.2 tok/s run later that day.^[raw/inbox/2026-09-15.md]
- `2026-09-15 13:04` — same session `20260914_200308_f9b029`: after the `81.2 tok/s @ 262K` MTP run, Hermes switched the draft model from MTP to `DFlash2` to test it through Hermes (MTP "works through Hermes (26s)").^[raw/inbox/2026-09-15.md]
- `2026-09-15 16:33` — operation interrupted; `16:50` Hermes: "Let me get everything stable and verify the full setup" (session still settling).^[raw/inbox/2026-09-15.md]
|- `2026-09-15 12:41` — Hermes observed its own config: model set to `"auto"`, provider `"custom"` (the runtime picks the underlying model).^[raw/inbox/2026-09-15.md]
- `2026-09-16 23:35` — `[System]` active model → `inclusionai/ling-3.0-flash-sante:free` via provider `nous` (session `20260914_200308_f9b029`, `sim 0.16`). Continues the churn; the same session id reappears with a different free nous model.^[raw/inbox/2026-09-16.md]
- `2026-09-17 08:37` — `[System]` active model → `meituan/longcat-2.0:free` via provider `nous` (session `20260914_200308_f9b029`, `sim 0.17`). Same session id flips again to yet another free nous model — the never-settling free-nous churn continues.^[raw/inbox/2026-09-17.md]

## What it means
- The lock was never stable or cleanly applied, despite multiple Hermes-side lock attempts.^[raw/inbox/2026-09-07.md]
- The same session id (`20260903_001447_7bc70a`) is reused across evaluation windows with different active providers and similarity values, so the `sim 0.09` reading from `2026-09-10 10:06` is not comparable to the `Qwen 3.8 27B` run from 2026-09-07. The similarity trajectory stays provisional until Chris confirms which run the `0.09` belongs to.^[raw/inbox/2026-09-10.md] ^[raw/inbox/2026-09-13.md]
- Reinforces the provisional-lock rule: competing runtime model proposals in the same session make any recorded lock provisional until a verified config write and restart confirm both the exact model variant and throughput target.^[raw/inbox/2026-09-07.md]

## Ornith placement correction
- `2026-09-13 16:43` — Chris: "The only thing is you put ornith under xai not turbo fed you put under the wrong provider."^[raw/inbox/2026-09-13.md]
- `ornith-1-5-35a3b` is to be treated as an `xai`-provider model, correcting an earlier placement under a TurboFit-style ("turbo fed") provider. See [[topics/hermes-agent/wiki/decisions/ornith-provider-placement-2026-09-13|Ornith Provider Placement — 2026-09-13]].

## Related
- [[topics/hermes-agent/wiki/decisions/provider-lock-review-2026-09-07|Provider Lock Review — 2026-09-07]]
- [[topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics/hermes-agent/wiki/entities/session-20260910-sim-009|Similarity Observation — 2026-09-10 sim 0.09]]
- [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
