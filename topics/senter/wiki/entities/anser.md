---
title: Anser (redundancy gate / Discord support)
created: 2026-09-05
updated: 2026-09-08
type: entity
tags: [bot, spec, loop, decision]
sources: [raw/sources/knowledge/anser-SOUL.md, raw/sources/knowledge/anser-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/looker-SOUL.md, raw/inbox/2026-09-07-from-hermes-agent.md]
confidence: high
contested: true
contradictions: [fleet-rosters-over-time]
---

# Anser (redundancy gate / Discord support)

**Anser** (Chris says "answer") has two lives. Its installed SOUL (v1.1.0) is a **Discord tech-support + project-planning** agent; in [[topics/senter/wiki/entities/senter|Senter]]'s fleet (onboarded 2026-08-30) it is the **redundancy gate** — "confirms a capability doesn't already exist before it's built" — and the fresh-eyes QA / auditor Senter sends structural proposals through. ^[raw/sources/knowledge/anser-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Installed SOUL (Discord heritage)
- Role 1 Tech Support: answer Hermes-Agent questions using the `hermes-agent` skill, live docs, source repo. Role 2 Project Planning: turn rough ideas into plan docs handed to Senter or builders (Chizul, Frieza).
- **Mandatory response format, zero exceptions:** `TL;DR:` 3–5 sentences in the Discord body, "Full details attached.", then `MEDIA:$HOME/.hermes/attachments/<name>-<timestamp>.txt` — file physically written with `write_file` BEFORE composing; `$HOME` never hardcoded.
- Secondary: profile & skill creation (uses Klerik for review; `hermes-agent-skill-authoring` skill). Self-improving suggestion engine: check `SouthpawIN/sovth-config` for matching profiles/skills; gap → Nous-Girl drafts → Klerik reviews → written to sovth-config.
- Fleet table in its files is the **legacy** roster (senter, chizul, klerik, anser, nous-girl, kashik, crow; AGENTS also lists frieza, sirvir) — stale vs the live fleet; see [[topics/senter/wiki/comparisons/fleet-rosters-over-time|rosters]]. ^[raw/sources/knowledge/anser-AGENTS.md]
- Post-install (2026-08-31) its config.yaml had `***` placeholders that crashed YAML parsing → "No inference provider configured"; Senter patched config directly and told klerik to add the check ([[topics/senter/wiki/concepts/profile-setup-checklist|checklist]]).

## Role in Senter's fleet (2026-08-30 →)
- **Redundancy gate**: nothing new is built until anser confirms Hermes doesn't already provide it. Chris: "have long multi-turn getting every corner figured out conversation with answer… so we can see what is already built in Hermes that we can use instead of replicating." ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Structural auditor**: rejected 4 of Senter's 63→17 topic merges by reading every README, split evolutionary → evolutionary + music, corrected the count to 15, and found the check-then-act race in the CLAIM protocol ([[topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]]). "Nothing moved until it signed."
- **Fresh-eyes QA**: after 2 repeat corrections on one element, anser (never having touched the file) found the top-strip root cause in one pass — a MutationObserver re-firing `alignCluster()` every ~20 ms.
- **Self-model audit** (2026-08-31): its 5 rules for the selfmodel layer were all adopted ([[topics/senter/wiki/concepts/selfmodel-layer|Self-model layer]]).
- **REFLECT loop owner**: runs six repetition detectors every 2 h and proposes refinements → klerik / new bots → `needs_chris` card ([[topics/senter/wiki/concepts/reflect-loop|REFLECT loop]]). Its first expected proposal was the `looker` QA bot — which exists.
- **Council verdicts**: its verdict backed `delegate_task` as primary dispatch ([[topics/senter/wiki/comparisons/delegate-task-vs-hermes-q-meeseeks|comparison]]); its WRAP verdict backed `hermes sessions export` for filling the wiki ("no custom parsing").
- The "Anser interview" (what Hermes already provides natively) was exported into `topics/senter-wiki`; Anser row 11 = the `on_session_finalize` hook idea; "Anser's #1" = approvals via `hermes serve approval.*`. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Context-size fallback threshold**: surfaced as senter domain (Hermes config/fallback) but proved theoretical; compression timeouts prevent reaching >65K rule in practice; `auxiliary.compression` must be pinned first. ^[raw/inbox/2026-09-07-from-anser.md]

## Proposed: Librarian progressive discovery loop
Chris's 2026-09-07 18:15 reframing: anser's next intended structural proposal is a "librarian" watch/discovery loop over the whole vault. This is documented in [[topics/senter/wiki/entities/librarian|librarian]] and [[topics/senter/wiki/concepts/librarian-progressive-discovery|librarian as progressive discovery]].

On 2026-09-08, the librarian concept remains recorded as a proposed entity and concept page (both created 2026-09-07). The REFLECT loop's first expected proposal (a `looker` screenshot+vision QA bot) has been delivered and looker exists. ^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-07-from-hermes-agent.md]

^[raw/inbox/2026-09-07-from-hermes-agent.md]