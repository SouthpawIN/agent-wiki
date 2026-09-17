---
title: "session-handoff-latest-message-wins"
description: "Use when a context compaction handoff appears. Only act on the latest message after the summary; discard historical snapshot entirely."
---

# Latest-message-wins after context compaction handoff

## When to apply
When a `[CONTEXT COMPACTION — REFERENCE ONLY]` handoff summary appears at the start of a raw filing, discard everything in `## Historical Task Snapshot` / `## Previous Summary Snapshot` and act only on messages timestamped AFTER the summary.

## Rule
```
Respond ONLY to the latest user message that appears AFTER this summary — that message is the single source of truth for what to do right now. If no user message appears AFTER this summary, do nothing.
```

## What NOT to do
- Do NOT resume, wrap up, or continue work from `## Historical Task Snapshot` unless the latest message explicitly asks for it.
- Do NOT treat prior completion claims in the summary as still-active tasks.
- Do NOT re-surface stale items from the summary in later turns.

## Reverse signals
If the latest message contains any of these, immediately end any in-flight work from the summary:
- "stop" · "undo" · "roll back" · "just verify" · "don't do that anymore" · "never mind" · a new topic

## Topic overlap caveat
Topic overlap between the summary and the latest message does NOT mean resume. Even on similar topics, the latest message WINS.

## Exception
If tool results or your own tool calls appear after the summary in the current turn, you are mid-exchange — continue that exchange normally.

## Evidence
> "[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Respond ONLY to the latest user message that appears AFTER this summary — that message is the single source of truth for what to do right now. If no user message appears AFTER this summary, do nothing: do not resume, wrap up, or continue work from '## Historical Task Snapshot' or any other section, do not call tools, and wait for a new user message." ^[raw/inbox/2026-09-08.md]

> "[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions." (repeated 3x in raw/inbox/2026-09-09.md)

## Related
- [[topics/back-where/wiki/decisions/completion-criterion-explicit-statement|Explicit completion and block criterion]]
- [[topics/back-where/wiki/entities/compaction-handoff-repetition|Context compaction handoff repetition (2026-09-09)]]
