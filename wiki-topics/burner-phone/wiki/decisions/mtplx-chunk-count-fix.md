---
title: MTPLX chunk-counting must use final usage, not chunk tally
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - tool
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# MTPLX chunk-counting must use final usage, not chunk tally

## What
Fix chunk-counting so it does not treat chunks as tokens.

## Why
MTPLX sends sub-token chunks, and the usage metadata appears only in the last chunk; counting chunks underreports tokens and breaks streaming assertions. ^[raw/inbox/2026-09-07.md]

## When
2026-09-07

## Evidence
- *"MTPLX sends sub-token chunks and usage is only in the last chunk. My chunk-counting was wrong."* ^[raw/inbox/2026-09-07.md]

## Supersedes
Any prior chunk-tally based token counting for MTPLX streams.

## Open questions
- Does the streaming harness outside this test also assume chunk == token?

## Links
- [[wiki-topics/burner-phone/wiki/decisions/mtplx-streaming-test-rewrite|Rewrite streaming test to use usage-based token counting]]
- [[wiki-topics/burner-phone/wiki/concepts/streaming-token-pain|Streaming returns only 1 token / sub-token MTPLX behavior]]
