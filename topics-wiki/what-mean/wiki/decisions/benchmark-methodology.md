---
title: Benchmark methodology — reasoning-first
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [preference, pain, tool]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Benchmark methodology — reasoning-first

Chris's standing preference for how to benchmark the local 27B / Ornith models: test at the context length the model will actually run at in Hermes, so the benchmark captures full reasoning rather than a truncated short generation. ^[raw/inbox/2026-09-15.md]

Stated at 12:31 on 2026-09-15: "I told you to do it the context length that they'll be running at in Hermes... you're not testing with enough tokens. It's not getting out of its reasoning We know that these models think a while." ^[raw/inbox/2026-09-15.md]

Why: short token counts measure throughput but miss the part that matters for reasoning models, because "these models think a while" before producing the useful output. ^[raw/inbox/2026-09-15.md]

Contested / open: Hermes had run a 500-token generation on 2026-09-06 (9 tok/s). Chris's 09-15 correction implies that generation was too short to be a fair benchmark. ^[raw/inbox/2026-09-06.md]

## Related

- [[topics-wiki/what-mean/wiki/queries/benchmark-reasoning-tokens|Benchmark reasoning token count — 2026-09-15]]
- [[topics-wiki/what-mean/wiki/concepts/tokens-per-second|Tokens per second]]
