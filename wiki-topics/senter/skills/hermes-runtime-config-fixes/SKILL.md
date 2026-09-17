---
name: hermes-runtime-config-fixes
description: Use when fixing Hermes runtime config issues for model-picker stickiness, TTS gateway entitlement, or vision provider pinning.
version: 0.1.0
distilled: 2026-09-06 22:54
topic: senter
---
# hermes-runtime-config-fixes
1. Check fallback_providers: the user's picked model must be first; if turbofit is unavailable, fall to the user preference, not a free-tier default. 2. Pin auxiliary.compression.provider/model explicitly; never leave as auto. 3. Pin auxiliary.vision.provider in root config AND every profile with a timeout. 4. For TTS failures after credits: managed_nous_tools_enabled() may read a 60s JWT cache; confirm whether resolve_managed_tool_gateway uses force_fresh=True for TTS resolution. 5. Remember: main-model switches apply in new sessions; sticky-model enforcement is per-session.

## Evidence
> The fallback went `turbofit → stepfun/step-3.7-flash:free`, skipping the user's preference entirely.
> The `force_fresh=True` patch was identified at 02:31 but the raw does not record its application.
> main-model switch takes effect in a new session; this one stays on its current model.
