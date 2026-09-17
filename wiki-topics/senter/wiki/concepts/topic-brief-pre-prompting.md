---
title: Topic BRIEF pre-prompting (each topic declares what belongs to it and how to think about it)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, infra, tool, decision, preference]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---

# Topic BRIEF pre-prompting

The **pre-prompting layer** is the last piece Hermes added on 2026-09-05 (19:23), directly after the [[wiki-topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|19:06 backend decision]] and the 19:12 inventory that named the TF-IDF cutter as one of three still-custom parts. Hermes's framing: ^[raw/inbox/2026-09-05.md]

> "Now the pre-prompting layer — the thing that makes sorting smarter than TF-IDF: each topic declares what belongs to it and how to think about it, and the cutter/agent read it."

It is a `hermes:` line — what was built, not a Chris order — but it answers two things Chris did say: the 17:46 picture ("cutting out pieces that are by topic and sorting those into their topic… each individual topic will have its own agent") and the 19:06 wish that the backend be "just built in Hermes commands and markdown." A per-topic markdown file that both the [[wiki-topics/senter/wiki/concepts/watcher-as-cutter|cutter]] and the [[wiki-topics/senter/wiki/entities/topic-agent|topic agent]] read is exactly that: sorting intelligence expressed as markdown, no new code path. ^[raw/inbox/2026-09-05.md]

## The artifact — `wiki-topics/<t>/BRIEF.md`
Present in all 19 live topics as of 19:25 (this topic's copy written 19:25). Sections, in order:

| Section | Who reads it | What it does |
|---|---|---|
| **What this topic is** | agent | one-paragraph definition ("The BACKEND and the ORGANISATION — not the wiki's look") |
| **Belongs here (scope)** | cutter + agent | positive claims — what to pull into this topic |
| **Does NOT belong here (anti-scope → route elsewhere)** | cutter + agent | explicit hand-offs: wiki look → `senter-wiki`, music/YouTube audio → `music`/`youtube`, model ladder → `turbofit`, Hermes internals/PRs → `hermes-agent`. The agent lists anything it receives from these under `misrouted` instead of wikifying it |
| **Aliases (the cutter binds hard on these words)** | cutter | deterministic hooks that beat TF-IDF similarity — for `senter`: senter, sidebar, watcher, topic agent, umbrella, fleet, klerik, looker, paladin, approval(s), cron, profile, gateway, bridge, workflow, pipeline |
| **Lens — how to read new context** | agent | classification rules: system-workflow talk → dated DECISION page quoting Chris and naming what it supersedes; a correction ("I don't like the separation", "you still don't get it") → record correction + the wrong model, flag the old page `contested`; a standing preference ("stop asking me", "root cause only") → `entities/chris.md` + BRIEF standing preferences; name the implicated fleet bot and link its entity page |
| **Standing preferences** | agent | applied to every suggestion: root causes, everything live, markdown + built-in Hermes over custom code, bots first then loops, reuse a fleet bot, no pitches about the build process |
| **What a good suggestion looks like** | agent | "One line, phrased as a question Chris can say yes to, tied to a quote from him, naming the bot that would do it" |
| **Learned (agent-appended, newest first)** | agent writes | one-line learnings returned by each pass under `brief`; appended, never rewriting Chris's lines |

Chris edits the file freely; lines ending `<!-- chris -->` are never rewritten — the same rule the wiki already had in `SCHEMA.md` ([[wiki-topics/senter/wiki/concepts/fix-the-record-not-the-pitch|fix the record]]). ^[raw/inbox/2026-09-05.md]

## What it changes in the pipeline
- **Cutter.** Before 19:23 a cut was a TF-IDF sentence-group similarity (`sim 0.07`–`0.39` on today's filings — low across the board). The aliases give it hard bindings per topic, so "klerik" or "approval" lands in `senter` even when the surrounding sentence scores low. This is the concrete answer to the open item recorded on [[wiki-topics/senter/wiki/concepts/watcher-as-cutter|watcher as cutter]] ("nothing in the raw yet measures mis-cuts").
- **Topic agent.** The BRIEF is prepended to the agent's prompt as "operating orders"; anti-scope gives it a `misrouted` output so a wrong cut gets bounced rather than wikified; the lens gives it Chris's own reading rules; the `brief` output makes each pass teach the next one. The agent's memory is now two layers: the wiki (facts) and the BRIEF (how to read new facts).
- **Native-vs-custom ledger.** The cutter row in [[wiki-topics/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]] gains a markdown half: the *rules* are native (a `.md` file), only the similarity fallback remains code.

## Relation to earlier ideas
- It is the per-topic form of `SCHEMA.md`'s "Domain" line, expanded from one sentence to a full operating brief — the same move Chris demanded for CONTEXT at 17:40 ("still only one line") in [[wiki-topics/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|CONTEXT = full LLM wiki]].
- It supersedes the thresholds-only sorting story for the cutter (propose ≥ .35 / auto ≥ .50 remain for topic *governance* merges, per [[wiki-topics/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|the calibration decision]]; aliases sit in front of similarity for *filing*).

## Open
- Chris has not yet spoken about BRIEF.md (last Chris line in raw is 19:06). Whether he edits a BRIEF himself — the `<!-- chris -->` path — is unrecorded.
- No raw line yet shows a before/after mis-cut count; the 19:23 line asserts "smarter than TF-IDF" as design intent, not measurement.
