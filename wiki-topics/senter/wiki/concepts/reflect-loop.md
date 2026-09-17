---
title: REFLECT loop (repetition → bot edits)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [loop, spec, bot]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: medium
---

# REFLECT loop (repetition → bot edits)

Chris's ask: "be proactive — turn repeated issues into bot edits or new bots; add a self-reflective loop." REFLECT "replaces hand-written lessons." Spec: `wiki-topics/senter/triggers-loops/reflect.md`; summary in skill `references/self-healing-pipeline.md`. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Mechanics
- Owner: [[wiki-topics/senter/wiki/entities/anser|anser]]. Every **2 h** it runs **six repetition detectors** over `Ideas.md`, topic queues and `events.jsonl`.
- Output = PROPOSALS, never silent changes: refinements → [[wiki-topics/senter/wiki/entities/klerik|klerik]]; new bots / SOUL changes → a `needs_chris` card ([[wiki-topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]).
- First expected proposal: a `looker` screenshot+vision QA bot, "since three bots re-implemented that capability in one day" — [[wiki-topics/senter/wiki/entities/looker|looker]] now exists.
- Pass 2 caught rule 14 ("no `python3 -c`") being tripped 15× in 7 min via spelling variants (`python -c`, `<venv>/bin/python -c`, `execute_code <<PY`, `cmd | python3`) — and the enforcer installed the rule with `printf >>`. Lesson: rules name the gate's pattern FAMILY, not a command spelling.
- Planned detector: any new unlabeled timer (`setInterval`, `time.sleep`/`POLL`) after the "live live live — no timed loaders" rule.
- Tooling breaches by delegate children (a shell heredoc to session.md under pressure) are flagged to REFLECT/klerik rather than hidden.

## Relation to the flywheel
REFLECT is the first automated instance of [[wiki-topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|context → skills → bots → loops]] stage 2→3, and the ancestor of the 2026-09-05 [[wiki-topics/senter/wiki/entities/watcher|watcher]]'s "every 12 filings propose a skill" rule. Its per-topic generalization is what Chris asked for on 2026-09-05: proposals "all the time," per message.
