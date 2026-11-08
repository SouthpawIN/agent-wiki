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

## The tool

```bash
python bots/anser/scripts/corpus.py refresh --accounts NousResearch Teknium --limit 50
python bots/anser/scripts/corpus.py import --from-json posts.json   # no credentials needed
python bots/anser/scripts/corpus.py search "web app" --days 90 --top 5
python bots/anser/scripts/corpus.py pack "is hermes free"           # citation-ready answer stub
python bots/anser/scripts/corpus.py status
```

`refresh` shells out to `xurl`; on auth failure it records `stale: true` and the
error in `data/corpus-state.json` instead of leaving a silent gap. `pack` returns
`grounded: false` and the "not publicly stated" stub when nothing matches — that
string is the answer.

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
