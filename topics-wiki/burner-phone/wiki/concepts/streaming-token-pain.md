---
title: Streaming returns only 1 token / sub-token MTPLX behavior
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - pain
  - question
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Streaming returns only 1 token / sub-token MTPLX behavior

Chris observed that **MTPLX streaming returns only 1 token per chunk** ^[raw/inbox/2026-09-07.md] and then discovered this is structural: *"MTPLX sends sub-token chunks and usage is only in the last chunk."* ^[raw/inbox/2026-09-07.md]

This breaks any counter or estimator that assumes one chunk equals one token, and it was the root cause of an undercount in the streaming test. The targeted fix is to drive completion off usage reported in the final chunk rather than chunk tallying. ^[raw/inbox/2026-09-07.md]

- Root-cause framing, not workaround: prefer counting from final-usage metadata.
- Standing preference applies: reuse built-in tool behavior over a custom counting layer.

## Supersedes
Any assumption that chunk count equals token count in MTPLX streams.

## Open questions
- Does the streaming harness outside this test also treat chunks as tokens?

## Links
- [[topics-wiki/burner-phone/wiki/decisions/mtplx-chunk-count-fix|MTPLX chunk-counting must use final usage, not chunk tally]]
- [[topics-wiki/burner-phone/wiki/decisions/mtplx-streaming-test-rewrite|Rewrite streaming test to use usage-based token counting]]
