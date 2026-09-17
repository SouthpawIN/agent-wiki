---
title: Benchmark reasoning token count — 2026-09-15
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, tool, pain]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Benchmark reasoning token count — 2026-09-15

At 12:31 on 2026-09-15, in response to Hermes reporting that downloads are progressing, Chris corrects the benchmark approach: "No, I want reasoning. I told you to do it the context length that they'll be running at in Hermes So I mean, you're not testing with enough tokens. It's not getting out of its reasoning We know that these models think a while." ^[raw/inbox/2026-09-15.md]

His point: benchmarking a reasoning model with too few tokens doesn't measure what matters, because these models "think a while" before producing the useful part of their output. A fair benchmark must run at the context length the model will actually be used at, so reasoning has room to complete. ^[raw/inbox/2026-09-15.md]

This sharpens the earlier tokens-per-second concern (2026-09-06/07): Chris is not just chasing a throughput number — he wants the benchmark to reflect real reasoning workloads, not a truncated short-generation figure. ^[raw/inbox/2026-09-06.md]

## Related

- [[topics/what-mean/wiki/concepts/tokens-per-second|Tokens per second]]
- [[topics/what-mean/wiki/entities/ornith-model|Ornith model]]
