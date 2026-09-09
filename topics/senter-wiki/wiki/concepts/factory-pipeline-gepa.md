---
title: Factory pipeline — Collect → Generate → Evaluate → Apply (GEPA)
created: 2026-07-07
updated: 2026-09-05
type: concept
tags: [spec, loop]
sources:
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/agent-wiki-repo/sandbox/goop/SENTER.md
confidence: high
---

# Factory pipeline — Collect → Generate → Evaluate → Apply (GEPA)

## The four factories (spec)
All use the same 4-stage pipeline. ^[raw/sources/knowledge/agent-wiki-repo/spec.md]
- **Context** — every 30 min; reads Senter sessions (`session_search(profile='senter')`), writes README/continuity, populates `queue.md` with `[SKILLS]/[AGENTS]/[LOOPS]`; "NEVER overwrite user-edited continuity lines."
- **Skills** — on `[SKILLS]` items; `delegate_task` → 3–5 candidate SKILL.md → rubric (completeness, clarity, reusability, evidence) → `skill_manage(create)`.
- **Agents** — on `[AGENTS]` items + unhosted skills; candidate SOULs → scoring matrix → `hermes profile create`. **No-self-edit rule.**
- **Loops** — on `[LOOPS]` items + unlooped agents; "Does this loop actually execute the project plan?" → cron or kanban (kanban for multi-agent, cron for periodic).
Queue format: `- [ ]` open, `[~]` claimed, `[x]` done; only Context creates entries. Injection format: `## [UNREAD]` → woven into the next response → `## [READ]`. ^[raw/sources/knowledge/agent-wiki-repo/spec.md]

## GEPA for every primitive
"Collect evidence … Generate candidate … Evaluate for redundancy, contradictions, evidence alignment, quality, and safety … Apply only an approved winner." Merge equivalent context, preserve user corrections, flag contradictions, avoid duplicates. ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md] ^[raw/sources/knowledge/agent-wiki-repo/SENTER_AGENT.md] ^[raw/sources/knowledge/agent-wiki-repo/sandbox/goop/SENTER.md]

## How it runs today (2026-09-05)
The spec's cron factories became: [[topics/senter-wiki/wiki/entities/senter-watcher|watcher]] (per message → `raw/inbox`), [[topics/senter-wiki/wiki/entities/topic-worker|topic-worker]] (every 5 min, one `hermes -p senter` run per topic, GEPA collect → generate → evaluate → apply, `.proposed` for bots/loops), [[topics/senter-wiki/wiki/entities/umbrella|umbrella]] (every 30 min, cross-topic), and the [[topics/senter-wiki/wiki/entities/topic-wiki-compile-loop|topic-wiki compile]] (every 15 min, Layer-2 pages). "The flywheel is running end to end." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Design principles behind it
Markdown is the API · the wiki is the system · user-editable everything · dot-prefix for machine internals · topics are self-contained · factories are thin (one `delegate_task`) · injections keep the human in the loop · no self-edit. ^[raw/sources/knowledge/agent-wiki-repo/spec.md] See [[topics/senter-wiki/wiki/concepts/markdown-is-the-api|Markdown is the API]] and [[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]].
