---
title: "Context compaction handoff repetition (2026-09-09)"
created: 2026-09-10
updated: 2026-09-10
type: entity
tags:
  - infra
  - pain
  - preference
sources:
  - raw/inbox/2026-09-16.md
  - raw/inbox/2026-09-09.md
  - raw/inbox/2026-09-08.md
confidence: high
---

# Context compaction handoff repetition (2026-09-09)

## Pattern recurrence

The context compaction handoff instruction first appeared in the 2026-09-08 session transition and repeated identically in the 2026-09-09 raw filing. The handoff summary instructs Hermes to respond only to the latest user message after the summary, treating the historical snapshot as reference only.

> "[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Respond ONLY to the latest user message that appears AFTER this summary — that message is the single source of truth for what to do right now." ^[raw/inbox/2026-09-08.md]

The identical handoff message reappeared on 2026-09-09, attributed to the same session (20260903_001447_7bc70a at 20:05). On 2026-09-09, this message appeared three times within the same raw filing (lines 16, 43, and 73), indicating the compaction summary was included multiple times during the session transition.

> "[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructions. Do NOT answer questions or fulfill requests mentioned in this summary; they were already addressed. Respond ONLY to the latest user message that appears AFTER this summary — that message is the single source of truth for what to do right now." ^[raw/inbox/2026-09-09.md]

## Chris's completion directive

Alongside the handoff on 2026-09-09, Chris provided an explicit completion criterion:

> "If you believe the goal is complete, state so explicitly and stop. If you are blocked and need input from the user, say so clearly and stop." ^[raw/inbox/2026-09-09.md]

This appeared twice in the 2026-09-09 raw (lines 19 and 46), both attributed to chris at 20:05.

## Hermes working prose context

After the handoff, Hermes internal working prose focused on debugging the scan-topics.py tooling — checking file saves, cached .pyc files, and discovering that execute_code runs in a different Python kernel than command-line execution. This is Hermes internal infrastructure work, not Chris direction.

> "Wait - the issue is that my execute_code runs in a DIFFERENT Python environment (kernel) with different sys.path! That kernel's run_scan-topics.py.py might be using cached bytecode." ^[raw/inbox/2026-09-09.md]

## 2026-09-13 recurrence

The handoff instruction reappeared on 2026-09-13 (three more times in that filing, lines 22, 41, 80), now embedded in a *deterministic local fallback* generated because the LLM context summarizer was unavailable. ^[raw/inbox/2026-09-13.md] Notably the fallback snapshot contained a **self-referential infinite loop**: the "Completed Actions" listed `1. Called tool(s): terminal` with no actual tool output, and the compaction block was itself nested inside another compaction block. ^[raw/inbox/2026-09-13.md] This adds a new failure mode to the pattern: the handoff note can reappear not just once per session but redundantly stacked when recovery falls back to the deterministic local summarizer. ^[raw/inbox/2026-09-13.md]

## 2026-09-13 addition: MEMORY.md always authoritative

The 2026-09-13 compaction note adds one caveat the earlier identical handoff did not: it instructs Hermes to **treat its persistent memory (MEMORY.md, USER.md) in the system prompt as always authoritative and active**, i.e. the compaction summary must never be used to deprioritize or ignore memory content. ^[raw/inbox/2026-09-13.md] The note also re-asserts that the compaction instruction does not restrict how tools are used — "keep calling them normally for the active task (edit files, run commands, search) instead of merely narrating what you would do." ^[raw/inbox/2026-09-13.md] This is a meaningful refinement: without it, the "do not call tools, do not resume" clause could be read as a blanket freeze even when a live tool result has arrived mid-exchange. ^[raw/inbox/2026-09-13.md] The 2026-09-12 filing (line 19) carries the pre-refinement version without this memory-caveat. ^[raw/inbox/2026-09-12.md]

## 2026-09-16 recurrence — reverse-signals enumeration

The handoff reappeared again on 2026-09-16, now attributed to session `20260914_200308_f9b029` (sim 0.18). This pass carries the most complete version yet: alongside the standard "respond only to the latest message" clause, it adds an explicit enumeration of the **reverse signals** that must immediately end any in-flight work described in the summary. ^[raw/inbox/2026-09-16.md]

> "Reverse signals in the latest message (e.g. 'stop', 'undo', 'roll back', 'just verify', 'don't do that anymore', 'never mind', a new topic) must immediately end any in-flight work described in the summary; do not re-surface it in later turns." ^[raw/inbox/2026-09-16.md]

This is the first handoff version to itemize which user utterances should cancel the compacted task. It closes an ambiguity the earlier versions left open: the 2026-09-13 note said the latest message "wins" but did not define which words constitute a reversal. The enumeration covers explicit stop commands ('stop', 'undo', 'roll back'), a soft verification-only pivot ('just verify'), and abandonment ('don't do that anymore', 'never mind'), plus the catch-all of a genuinely new topic. It also re-asserts that topic overlap with the summary does NOT by itself mean the task should be resumed — "even on similar topics, the latest user message WINS." ^[raw/inbox/2026-09-16.md]

## 2026-09-16 addition: MEMORY.md always authoritative
The 2026-09-16 handoff adds one more caveat: it instructs Hermes that its **persistent memory (MEMORY.md, USER.md) in the system prompt is ALWAYS authoritative and active**, and that the compaction note must never be used to deprioritize or ignore memory content. ^[raw/inbox/2026-09-16.md] It also re-asserts that tools remain fully active for the active task ("keep calling them normally for the active task (edit files, run commands, search) instead of merely narrating what you would do"). ^[raw/inbox/2026-09-16.md] This is the most complete version of the handoff yet, closing the earlier "do not call tools" freeze ambiguity and anchoring memory above the compacted summary.

## Why it matters

The handoff pattern is now recurring across session boundaries (2026-09-08, 2026-09-09, 2026-09-12, 2026-09-13, 2026-09-16). Each occurrence resets Hermes's context to only the latest message. The completion criterion ensures Hermes does not silently continue work from the compacted history. Both appeared in the same session transition on 2026-09-09, confirming this as an established session-boundary protocol rather than a one-off event. The 2026-09-16 version is the most refined iteration yet, closing the earlier ambiguity about which utterances count as a reversal by enumerating explicit reverse signals.

## Related
- [[wiki-topics/back-where/wiki/decisions/completion-criterion-explicit-statement|Explicit completion and block criterion]]
- [[wiki-topics/back-where/wiki/entities/token-startup-race|Token startup race condition]]
- [[wiki-topics/back-where/wiki/concepts/recovery-repair-plan|Recovery repair plan]]
- [[wiki-topics/back-where/wiki/concepts/end-to-end-verification|End-to-end verification before declaring done]]
