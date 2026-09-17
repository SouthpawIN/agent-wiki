---
name: session-handoff-latest-message-wins
description: Use when a context compaction handoff appears. Only act on the latest message after the summary; discard historical snapshot entirely.
version: 0.1.0
distilled: 2026-09-10 12:20
topic: back-where
---
# session-handoff-latest-message-wins
Apply when `[CONTEXT COMPACTION — REFERENCE ONLY]` appears. Act only on messages after the handoff summary. Reverse signals: stop, undo, roll back, just verify, don't do that anymore, never mind, new topic — end in-flight summary work immediately. Topic overlap does not mean resume. Exception: if tool results appear after summary in current turn, continue normally.

## Evidence
> Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Respond ONLY to the latest user message that appears AFTER this summary
> If no user message appears AFTER this summary, do nothing: do not resume, wrap up, or continue work from '## Historical Task Snapshot'
