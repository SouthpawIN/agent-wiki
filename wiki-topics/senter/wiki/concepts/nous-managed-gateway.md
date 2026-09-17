---
title: Nous managed gateway (TTS / tool proxy with JWT entitlement cache)
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [infra, gateway, pain, tool]
sources: [raw/inbox/2026-09-06.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: medium
---

# Nous managed gateway (TTS / tool proxy with JWT entitlement cache)

The managed gateway that lets Hermes access Nous-provided tools (TTS via the OpenAI audio proxy, vision, etc.) using the user's Nous account — and the staleness bug that breaks it after credits are added. ^[raw/inbox/2026-09-06.md]

## How it resolves (Hermes, 02:26–02:28)

When `tts.provider: nous` is selected, the TTS tool uses `_managed_openai_audio_route()`, which calls `resolve_managed_tool_gateway("openai-audio")`. That in turn calls `managed_nous_tools_enabled()` + `read_nous_access_token()`.

`managed_nous_tools_enabled()` calls `get_nous_portal_account_info()`, which checks `tool_gateway_entitled`. The entitlement is read from a **JWT-based cache** with a 60-second TTL. The `force_fresh=True` code path always calls `/api/oauth/account` directly. ^[raw/inbox/2026-09-06.md]

## The bug — stale cache after credits

**Symptoms (01:51, 02:25).** Chris: "the TTS is failing." Config shows `tts.provider: nous`. The error: "the Nous Tool Gateway is not available (not entitled or unreachable)." Chris says "$2,000 was added to my credits."

**Root cause (02:28–02:31).** When credits were just added, the JWT-based entitlement cache (60s TTL) still says "not entitled" because the JWT was minted **before** the credits were added. `resolve_managed_tool_gateway` calls `managed_nous_tools_enabled()` **without** `force_fresh`, so it reads the stale cache and returns `None`. The gateway resolution fails, and TTS fails — even though the user's account now has credits.

**Fix identified (02:31).** Make `resolve_managed_tool_gateway` use `force_fresh=True` when doing TTS resolution, so it fetches fresh account info that reflects the newly-added credits. The patch targets `_managed_openai_audio_route()`.

## Why it matters

The managed gateway is the path for all Nous-provided tools — TTS, vision, and potentially others. A stale entitlement cache means any tool that depends on `managed_nous_tools_enabled()` fails silently for up to 60 seconds after the user's account status changes. This is a fleet-infrastructure gap: [[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]] serves approval cards and done-signals, but the tool-gateway entitlement is resolved in the Hermes CLI core itself → [[wiki-topics/senter/wiki/entities/teknium|teknium]] for the patch + PR-ledger treatment.

## Related

[[wiki-topics/senter/wiki/entities/hermes-agent|Hermes Agent]] records the companion fact: "Sanitized repo configs (`***`) crash YAML → silent fallback." The gateway has no such config crash, but has an analogous staleness problem: cached entitlements that don't reflect a recent account change.

## Open

The `force_fresh=True` patch was identified at 02:31 but the raw does not record its application. Whether it was patched in the user's fork (`SouthpawIN/hermes-agent`) or a PR was filed to the ledger ([[wiki-topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]]) is not recorded in this topic's raw.
