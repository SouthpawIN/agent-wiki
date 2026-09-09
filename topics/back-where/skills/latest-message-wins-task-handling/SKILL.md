---
name: latest-message-wins-task-handling
description: Use when a turn resumes from compaction or a Historical Task Snapshot. Treat only the latest user message as active unless it explicitly reopens an earlier task.
version: 0.1.0
distilled: 2026-09-07 19:51
topic: back-where
---
# latest-message-wins-task-handling
1. Read the latest user message after any snapshot/summary block.
2. If it contains a reversal/new topic, immediately stop any in-flight work implied by the snapshot.
3. Do not finish stale snapshot items unless the latest message explicitly asks.
4. Treat MEMORY.md/USER.md/system prompt memory as authoritative.
5. Summarize active intent in one line and proceed.

## Evidence
> Treat ONLY the latest message as the active task and discard stale items from '## Historical Task Snapshot' entirely — do not 'wrap up' or 'finish' work described there unless the latest message explicitly asks for it.
> Reverse signals in the latest message (e.g. 'stop', 'undo', 'roll back', 'just verify', 'don't do that anymore', 'never mind', a new topic) must immediately end any in-flight work described in the summary; do not re-surface it in later turns.
