---
title: "TTS failure during credit outage"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags:
  - tool
  - pain
  - infra
sources:
  - raw/inbox/2026-09-06.md
confidence: high
---

# TTS failure during credit outage

## What happened
TTS stopped working because the image-analysis model ran out of credits. Chris noted that a $2,000 top-up had been added, so enough balance should exist, yet TTS remained unavailable.

> "Also, the TTS is failing. Since there's something wrong with my credits, there was $2,000 added to my credits. We've used some of it, but there should be enough on there. So please get that fixed because it's grown up the project." ^[raw/inbox/2026-09-06.md]

## Technical diagnosis
The image-analysis credit exhaustion triggered a downstream TTS entitlement check, but the failure mode was stale cached auth state rather than true balance shortage. Klerik identified that the account-info cache or JWT had been captured before the $2,000 credit top-up, so entitlement checks returned a negative result even after payment.

The proposed code fix is in the TTS audio-client resolution path: retry with `force_fresh=True` when the initial entitlement check fails. `managed_nous_tools_enabled()` already exposes `force_fresh`, but the TTS path was not passing it.

^[raw/inbox/2026-09-06-from-klerik.md]

## Related
- [[topics-wiki/back-where/wiki/queries/restoration-and-billing|Restoration and billing]]
- [[topics-wiki/back-where/wiki/concepts/tts-cache-freshness|TTS cache-freshness failure]]
