---
name: tts-fresh-entitlement-retry
description: Use when TTS fails after a credit top-up or entitlement error. Retry audio-client resolution with fresh account info instead of cached state.
version: 0.1.0
distilled: 2026-09-06 21:51
topic: back-where
---
# tts-fresh-entitlement-retry
When TTS entitlement resolution fails with an entitlement/cache error:
1. Re-run the audio client config check with `force_fresh=True` on the account-info lookup.
2. Retry the TTS request with the refreshed config.
3. If it still fails, surface the exact entitlement error and do not silently switch providers or declare done without a successful Hermes test.

## Evidence
> The fix should be in the TTS openai resolution to retry with `force_fresh=True` when the first attempt fails with an entitlement error.
> Let me fix `_resolve_openai_audio_client_config` to retry with fresh account info
