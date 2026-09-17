---
title: "2026-09-06 — Model picker must stay sticky; TTS managed-gateway cache must be force-fresh"
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, pain, infra, preference, timeline]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-06-from-youtube.md]
confidence: high
---

# 2026-09-06 — Model picker must stay sticky; TTS managed-gateway cache must be force-fresh

**What.** Two runtime config problems surfaced together at 01:51 on 2026-09-06 and were diagnosed through 02:31 by [[topics-wiki/senter/wiki/entities/hermes-agent|Hermes Agent]]. ^[raw/inbox/2026-09-06.md]

> **Model:** "my model keeps switching the step 3.7 flash And that keeps screwing out my project. So we need to make the model stop auto switching I don't know if that's a turbo fifth thing, but if it is that's something that needs to be fixed. If I pick a model from The model picker that it should stay with that model until it needs to fall back."

> **TTS:** "Also, the TTS is failing."

## Model auto-switching — root cause and fix

**Root cause (Hermes, 02:22).** The `fallback_providers` block in config.yaml has the `turbofit` provider at the top (lines 6-18); when it fails or isn't active (local server not running), it falls back to the `nous` provider with `stepfun/step-3.7-flash:free` as the **first** fallback. The user's explicit default model (`z-ai/glm-5.3-flash`) was not in the fallback chain at all. The `auxiliary.compression.provider: auto` with an empty model meant compression auto-selected — likely `stepfun/step-3.7-flash` for the context summarizer.

**Fix applied (02:25):**
1. `z-ai/glm-5.3-flash` placed first in the fallback chain (not `stepfun/step-3.7-flash:free`).
2. `auxiliary.compression` set explicitly to `nous` / `z-ai/glm-5.3-flash` instead of `auto`.

**The rule Chris stated.** "If I pick a model from The model picker that it should stay with that model until it needs to fall back." The model picker's chosen model must be the **first** fallback, so explicit user choice is preserved until an actual error forces a fall. See [[topics-wiki/senter/wiki/concepts/model-fallback-chain|model fallback chain]].

**Connection to turbofit.** The `turbofit` provider sits atop `fallback_providers` — when its local server isn't running, the chain falls through to `stepfun`. This is not a turbofit inference issue per se; it is a **fallback ordering** issue that affects which provider the ladder resolves to. The [[topics-wiki/senter/wiki/entities/turbosovth|turbosovth]] profile owns the local runtime; the config ordering is fleet infrastructure. ^[raw/inbox/2026-09-06.md]

## TTS failure — root cause and fix

**Root cause (Hermes, 02:26–02:31).** Config shows `tts.provider: nous`, which maps to the OpenAI path through the managed Nous gateway (`resolve_managed_tool_gateway("openai-audio")`). The gateway resolves via `managed_nous_tools_enabled()` + `read_nous_access_token()`. When Chris's "$2,000 was added to my credits," the JWT-based entitlement cache (60s TTL) still says "not entitled" because the JWT was minted before the credits were added. The error: "the Nous Tool Gateway is not available (not entitled or unreachable)."

**Fix identified (02:31).** Make `resolve_managed_tool_gateway` use `force_fresh=True` when doing TTS resolution, so it fetches fresh account info reflecting the newly-added credits. The patch targets `_managed_openai_audio_route()` in the Hermes CLI core → [[topics-wiki/senter/wiki/entities/teknium|teknium]] for the upstream/PR treatment.

## Vision provider — out of credits

**Incident (01:53, 02:53).** "I can't analyze the screenshot because the vision provider is out of credits." The `auxiliary.vision.provider: auto` picks a free-tier model that times out and retries — the same class of problem already documented in [[topics-wiki/senter/wiki/entities/hermes-agent|Hermes Agent]] ("pin `auxiliary.vision` in every profile") and [[topics-wiki/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch + sentinel]] (round 5: 84% of fleet tool time). The 15:27 status update records the workaround ("Vision switched to free StepFun model"), but the root-cause fix (pinning a timed model in every profile config) was identified at 2026-09-02 and remains an open action.

## Relationship to standing preferences

Chris's 18:16 ruling — "Preempt decision, stop asking me for so many decisions. I've told you everything that I want this to be so far Continue building looking for things that aren't complete yet and complete them" ([[topics-wiki/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]) — means the model-switching fix (22:25) was applied as work, not carded back. The model-picker stickiness rule is now a standing preference: see [[topics-wiki/senter/wiki/entities/chris|Chris]] preferences and [[topics-wiki/senter/wiki/concepts/model-fallback-chain|fallback chain]]. ^[raw/inbox/2026-09-06.md]

## Status

- Model fallback chain: **fix applied** (z-ai/glm-5.3-flash first; compression explicit); session boundary noted — model switches only apply in new sessions. ^[raw/inbox/2026-09-06-from-youtube.md]
- Vision provider: **workaround applied** (StepFun); root-cause fix (pin in every profile) still open.
- TTS gateway: **fix identified, not yet applied** — needs `force_fresh=True` in `_managed_openai_audio_route`.
- The vault-live.html backup/recovery subagent result (01:35–01:54) is filed under [[topics-wiki/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] — the wiki pane's HTML file integrity, not the sidebar's backend.
