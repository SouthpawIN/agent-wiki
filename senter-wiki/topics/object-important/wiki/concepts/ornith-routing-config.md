---
title: "Ornith 1.5 routing config (8091)"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [tool, plan, pain, infra]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# Ornith 1.5 routing config (8091)

On 2026-09-13 Hermes reported that Ornith 1.5 is now alive and routing on a **new local endpoint at `http://127.0.0.1:8091/v1`**, serving 14.5 tok/s on an M1 with a Q4_K_M quantizer. The outstanding task is to point Hermes's own config at that endpoint.

## The config change

^[raw/inbox/2026-09-13.md] Hermes cannot edit the config itself ("I can't edit the Hermes config directly from here. You'll need to make two changes"). The one concrete change it names, on three repeated filings:

> Change line 8: `api: http://127.0.0.1:11613/v1` → `api: http://127.0.0.1:8091/v1`

in `~/.hermes/config.yaml`. (Each filing is cut off at "2." / "3." — the remaining items are truncated in the raw, but the line-8 swap is the repeatable, unambiguous instruction.) The old target was `11613`, the same port the mtplx-qwen38-27b endpoint answered on in 2026-09-07 — so this swap repoints Hermes from the previous local model to Ornith 1.5.

## Status / pain

^[raw/inbox/2026-09-13.md] The change is **unconfirmed and outstanding** as of the last filing (16:39). The filings repeat the same "I can't edit the config" message verbatim several times, so the edit has not been executed in the captured session.

^[raw/inbox/2026-09-15.md] On 2026-09-15 at 16:58 a background health check ran `curl -s --max-time 3 http://127.0.0.1:8091/health` (with `/tmp/check_models2.py`) and matched `ok:true` — direct evidence the 8091 endpoint is actually alive. So the endpoint itself is now **verified live**, but the `~/.hermes/config.yaml` line-8 repoint (11613 → 8091) still has not been made; Hermes continues to point at the old target.

## Related
- [[wiki/concepts/ornith-performance-metrics|Ornith performance metrics]] — the 14.5 tok/s Q4_K_M figure that motivated the routing change.
- [[wiki/entities/mtplx-qwen38-27b-endpoint|mtplx-qwen38-27b endpoint]] — the 11613 port being replaced on line 8.
