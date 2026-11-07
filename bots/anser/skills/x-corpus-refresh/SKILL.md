---
name: x-corpus-refresh
description: Refresh the cached @NousResearch and Teknium corpus.
version: 1.0.0
author: Anser
license: MIT
metadata:
  hermes:
    tags: [x, corpus, cache, jsonl]
---

# X corpus refresh

## Procedure

1. Pull the latest posts for `NousResearch` and `Teknium`, newest first, with
   `id`, `created_at`, `text`, `url`, and `is_reply`.
2. Upsert into `data/x-corpus.jsonl` keyed on post id. Append-only; never rewrite
   an existing line (an edited post is a new record with a note).
3. Drop replies to unrelated users unless they contain a technical claim; keep
   reply context one level deep so a quote is not misread.
4. Write `data/corpus-state.json`: `{last_run, newest_id, count, accounts}`.
5. If the API fails, update only `last_run` and set `stale: true`. A stale corpus
   is stated in answers, never hidden.
6. Never store DMs, emails, or anything from a protected account.

## Verify

`wc -l data/x-corpus.jsonl` grows or stays equal; newest id moves forward;
every line parses as JSON with a URL.
