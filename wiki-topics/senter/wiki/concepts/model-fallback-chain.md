---
title: Model fallback chain (user's pick stays sticky until an actual error)
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [infra, config, pain, decision]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-06-from-youtube.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Model fallback chain (user's pick stays sticky until an actual error)

How Hermes selects a model when the user's chosen model or provider fails — and the rule Chris wants it to follow: **the model picker's choice must stay in place until an actual error forces a fall**, not a silent auto-switch to `stepfun/step-3.7-flash:free`. ^[raw/inbox/2026-09-06.md]

## How it works (Hermes, 02:22)

The `model.default` field in `config.yaml` sets the preferred model. The `fallback_providers` block lists providers and their fallback models tried in order when the default fails. At 2026-09-06 02:22, the chain was:

1. **`turbofit`** — local llama.cpp server on the user's Mac
2. **`nous`** with `stepfun/step-3.7-flash:free` as the first fallback

When the turbofit local server was not running, the chain fell straight through to `stepfun/step-3.7-flash:free` — a free-tier provider that Chris never picked and does not want as a default. ^[raw/inbox/2026-09-06.md]

## The bug

The user's explicit default model (`z-ai/glm-5.3-flash`) was **not in the fallback chain at all**. The fallback went `turbofit → stepfun/step-3.7-flash:free`, skipping the user's preference entirely. Additionally, `auxiliary.compression.provider: auto` let the context summarizer auto-select `stepfun/step-3.7-flash` on its own. ^[raw/inbox/2026-09-06.md]

## The fix (applied 02:25)

1. **`z-ai/glm-5.3-flash` placed first in the fallback chain** — so the user's picked model is the first fallback, not `stepfun/step-3.7-flash:free`.
2. **`auxiliary.compression` set explicitly** to `nous` / `z-ai/glm-5.3-flash` instead of `auto`.

## The rule (Chris, 01:51)

> "If I pick a model from The model picker that it should stay with that model until it needs to fall back."

The picked model must be **sticky** — it stays until an actual provider error occurs, not when the top-of-chain provider happens to be down. See [[wiki-topics/senter/wiki/decisions/2026-09-06-model-picker-sticky-and-tts-gateway|decision]] and [[wiki-topics/senter/wiki/entities/chris|Chris preferences]].

## Session boundary

The **main-model switch takes effect in a new session**; the current session stays on its current model. Sticky-model enforcement is therefore a per-session rule: once a session is on `z-ai/glm-5.3-flash` after the fix, it should not silently flip to `stepfun/step-3.7-flash:free` mid-session due to fallback ordering or `auxiliary.compression.provider: auto`. ^[raw/inbox/2026-09-06-from-youtube.md]

## Why turbofit is at the top

The `turbofit` provider sits first in `fallback_providers` because Chris wants local inference as the fast lane when available ([[wiki-topics/senter/wiki/entities/turbosovth|turbosovth]]). When the local server is down, the chain should fall to the user's preferred cloud model, not to a free-tier default. The config fix moves the user's preference ahead of `stepfun` in the chain. ^[raw/inbox/2026-09-06.md]

## Related

[[wiki-topics/senter/wiki/entities/hermes-agent|Hermes Agent]] already records the companion fact: "Profiles don't inherit root `auxiliary.vision` config — pin it in every profile." The same inheritance problem applies to `fallback_providers` — each profile needs its fallback chain to list the user's preferred model first. ^[raw/inbox/2026-09-06.md]
