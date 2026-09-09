---
title: Rewrite streaming test to use usage-based token counting
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - plan
  - tool
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Rewrite streaming test to use usage-based token counting

## What
Rewrite the streaming test so completion is driven by usage from the final chunk instead of chunk tallying.

## Why
*"My chunk-counting was wrong. Let me rewrite the test to properly use streaming with usage-based token counting."* ^[raw/inbox/2026-09-07.md]

## When
2026-09-07

## Evidence
- *"The streaming only returns 1 token. Let me debug the response format."* ^[raw/inbox/2026-09-07.md]
- *"MTPLX sends sub-token chunks and usage is only in the last chunk."* ^[raw/inbox/2026-09-07.md]

## Supersedes
The previous streaming test that tallied chunks as tokens.

## Open questions
- Does this rewrite require changes to shared test fixtures or other streaming tests?

## Links
- [[topics/burner-phone/wiki/decisions/mtplx-chunk-count-fix|MTPLX chunk-counting must use final usage, not chunk tally]]
- [[topics/burner-phone/wiki/concepts/streaming-token-pain|Streaming returns only 1 token / sub-token MTPLX behavior]]
