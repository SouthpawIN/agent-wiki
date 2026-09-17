---
title: "Local-model context compression → route to Nous"
created: 2026-09-06
updated: 2026-09-07
type: concept
tags: [tool, decision, pain, infra]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07-from-senter.md]
confidence: low
contested: false
---

# Local-model context compression → route to Nous

This page records a filed support case about Hermes local-model compression slowdown, filed under `anser` on 2026-09-06. Because the raw item is Hermes operational evidence rather than a confirmed `anser` Discord moderation case, this remains a support record, not an `anser` workflow decision. ^[raw/inbox/2026-09-06.md]

## What
- **Pain**: the local model was too slow to compress a large context; a connection timed out after 120s with no response while compressing a 387k-token context. ^[raw/inbox/2026-09-06.md]
- **Fix**: compression was routed to **Nous** instead of the local model, removing the local-model bottleneck for large contexts. ^[raw/inbox/2026-09-06.md]
- **Follow-up tests**: a Maple MLX + deepgrove fork run compressed 5000 tokens in 9s; a later run compressed 130K tokens in 103s with no OOM, and the relevant servers/config were reported as up/correct before final end-to-end Hermes verification. ^[raw/inbox/2026-09-06.md]

## Notes
- This filing is marked `hermes:` / watcher-sourced with low topic similarity (sim 0.06–0.11); treat it as a support case unless Chris re-binds it to `anser`. ^[raw/inbox/2026-09-06.md]
- The 2026-09-07 raw filing repeats the same routing guidance (`Use Nous cloud fallback for contexts >65K`) and adds repeated compression-timeout system messages; these are duplicate Hermes evidence and do not change the case. ^[raw/inbox/2026-09-07-from-senter.md]
- No contested facts; end-to-end Hermes verification was pending at filing time.

## Links
- [[topics/anser/wiki/entities/anser|anser]]
- [[topics/anser/wiki/entities/anser-workflow|anser workflow — Discord moderation patterns]]
- [[topics/anser/wiki/entities/compression-support-case|Compression support case — 2026-09-06]]
