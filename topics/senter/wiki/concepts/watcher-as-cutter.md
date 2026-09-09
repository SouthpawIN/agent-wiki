---
title: Watcher as cutter (split messages by subject, file the pieces)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, tool, infra, decision]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Watcher as cutter

Second form of the [[topics/senter/wiki/entities/watcher|watcher]], live 2026-09-05 17:53. The first form (16:37) routed **whole messages** to the single best-fitting topic. [[topics/senter/wiki/entities/chris|Chris]]'s 17:46 correction made it a **cutter**: ^[raw/inbox/2026-09-05.md]

> "the watcher is watching my conversation with the sidebar, watching the session's live, and is just cutting out pieces that are by topic and sorting those into their topic."

## Mechanism (as built)
- Watches the session live (Hermes `state.db` message table — the inbox frontmatter reads `source: hermes state.db messages (watcher)`).
- Splits each message at subject changes: **sentence groups are classified individually, then re-joined when consecutive pieces agree.**
- Files each cut into `topics/<t>/raw/inbox/<day>.md` under a header `## <time> · <speaker> · <session id> · sim <score>`; `raw/` is immutable.
- **Proof case:** Chris's own 17:46 message — the wiki-architecture half stayed in `senter`, the video-creation half ("I see you're talking about video creation, how well I create something that can edit for you, or something that can create shorts") went to `youtube`.
- New subject → two immediate cards: "Want me to research it?" and "Want a bot for this?" — **no thresholds.** The 16:37 rule "every 12 filings on a topic proposes a skill candidate" is superseded.

## Why cutting, not routing
Chris jumps between subjects mid-sentence over voice dictation ([[topics/senter/wiki/concepts/voice-dictation-name-map|dictation]]); a whole-message router would either drop the minority subject or mis-file the whole thing. Cutting keeps every topic's raw complete — which the [[topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|memory-layer decision]] ("all of it, not summaries") requires. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Downstream
Each topic's cuts are consumed by that topic's [[topics/senter/wiki/entities/topic-agent|topic agent]]. The sidebar itself never files anything — the whole point is "so the sidebar does not have to be interrupted" ([[topics/senter/wiki/concepts/five-part-architecture|five-part architecture]]).

## Pre-prompting (19:23)
Sorting stopped being TF-IDF-only at 19:23: "each topic declares what belongs to it and how to think about it, and the cutter/agent read it." Every topic's `BRIEF.md` carries an **Aliases** list the cutter "binds hard on" (for `senter`: senter, sidebar, watcher, topic agent, umbrella, fleet, klerik, looker, paladin, approval(s), cron, profile, gateway, bridge, workflow, pipeline) plus a scope/anti-scope the receiving [[topics/senter/wiki/entities/topic-agent|topic agent]] uses to bounce a wrong cut as `misrouted`. Full account: [[topics/senter/wiki/concepts/topic-brief-pre-prompting|topic BRIEF pre-prompting]]. ^[raw/inbox/2026-09-05.md]

## Open
- Cut quality was a TF-IDF classification per sentence group (today's `sim` scores ran 0.06–0.39); since 19:23 aliases sit in front of similarity, but nothing in the raw yet *measures* mis-cuts before/after. A wrong cut silently starves one topic agent and pollutes another.
- Speaker = `hermes` cuts (the assistant's own replies) are filed too — the wiki must treat them as *what was built/claimed*, not as Chris's decisions.
