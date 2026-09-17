---
name: mtplx-streaming-count
description: Use when counting MTPLX tokens. Use final chunk usage.
version: 0.1.0
distilled: 2026-09-07 06:47
topic: burner-phone
---
# mtplx-streaming-count
## Rule
Count streamed tokens from `usage` in the final chunk, not from chunk count or chunk size.

## Steps
1. Consume the full stream without tokenizing chunk strings.
2. Capture the last chunk only.
3. Read its `usage`/token count.
4. Use that value as completion truth.

## Pitfall
Sub-token chunks make chunk-counting systematically wrong. If the final chunk lacks usage, retry with full response metadata or fall back to non-streaming completion.

## Evidence
> MTPLX sends sub-token chunks and usage is only in the last chunk.
> Let me rewrite the test to properly use streaming with usage-based token counting.
