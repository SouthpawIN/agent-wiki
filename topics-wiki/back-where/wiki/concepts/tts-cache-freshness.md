---
title: "TTS cache-freshness failure"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags:
  - tool
  - pain
  - infra
sources:
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-06.md
confidence: medium
---

# TTS cache-freshness failure

## What happened
TTS entitlement checks used stale cached account info or a JWT that was minted before the $2,000 credit top-up, so entitlement remained negative even after payment. The result was a voice outage unrelated to actual balance.

> "The issue might be that the JWT was cached BEFORE the credits were added, so it says not entitled." ^[raw/inbox/2026-09-06-from-klerik.md]

> "The user said '$2000 was added to my credits, there should be enough.' So the issue is likely the auth token resolution." ^[raw/inbox/2026-09-06-from-klerik.md]

## Code fix hypothesis
The proposed fix is in the TTS openai resolution path: retry entitlement checks with `force_fresh=True` when the first attempt fails. `managed_nous_tools_enabled()` already exposes `force_fresh`, but the TTS path was not passing it.

> "The fix should be in the TTS openai resolution to retry with `force_fresh=True` when the first attempt fails with an entitlement error." ^[raw/inbox/2026-09-06-from-klerik.md]

## Confidence
Medium: the diagnosis is specific, but the fix is proposed rather than verified end-to-end in these raw items.

## Related
- [[topics-wiki/back-where/wiki/concepts/tts-credit-outage|TTS failure during credit outage]]
- [[topics-wiki/back-where/wiki/queries/restoration-and-billing|Restoration and billing]]
