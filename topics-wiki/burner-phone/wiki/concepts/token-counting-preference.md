---
title: Token counting preference — count from final usage, not chunks
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - preference
  - tool
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Token counting preference — count from final usage, not chunks

Chris's preference is to **debug and rewrite the test** so completion is determined by the usage value in the last streaming chunk, not by counting chunks or chunks × estimated token length. ^[raw/inbox/2026-09-07.md]

This is a repeatable procedure for MTPLX-based streaming tests. ^[raw/inbox/2026-09-07.md]

## Links
- [[topics-wiki/burner-phone/wiki/decisions/mtplx-chunk-count-fix|MTPLX chunk-counting must use final usage, not chunk tally]]
- [[topics-wiki/burner-phone/wiki/concepts/streaming-token-pain|Streaming returns only 1 token / sub-token MTPLX behavior]]
