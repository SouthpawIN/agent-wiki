---
title: Topic-agent pitch caps (1 bot / 2 loops / 1 research; zero infrastructure pitches; hermes: lines are evidence)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, loop, bot, pain, decision]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---

# Topic-agent pitch caps

Rules put into the [[topics-wiki/senter/wiki/entities/topic-agent|topic agent]]'s prompt at 18:58, after its first passes produced a flood of cards about itself. Hermes's record: "Capped the prompt (1 bot / 2 loops / 1 research per pass, zero infrastructure pitches, `hermes:` lines are evidence not requests). Pruned 13 self-referential proposals; kept the two useful ones and approved them." ^[raw/inbox/2026-09-05.md]

## The three caps
1. **Volume:** at most **1 bot, 2 loops, 1 research** per pass per topic. Fewer, sharper offers — the [[topics-wiki/senter/wiki/concepts/proactive-suggestion-doctrine|suggestion doctrine]] is "very proactive", not "very many".
2. **Subject:** **zero pitches about the build process** — verifying the wiki, sweeping proposals, checking crons, "want X to prove Y". Infrastructure is Hermes's job under [[topics-wiki/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|preempt decisions]]: a known gap is work, not a card. Only Chris's actual subject (his projects, content, tools, life) may be pitched.
3. **Provenance:** raw lines whose speaker is `hermes` are **evidence about the topic, never a request to act on.** The cutter files the assistant's own replies ([[topics-wiki/senter/wiki/concepts/watcher-as-cutter|open item there]]); without this rule the agent read "let me collapse the two scripts" as an ask and pitched doing it.

## Why 13 proposals were pruned
The senter topic is *about* the pipeline, so the agent's own memory is full of infrastructure; every pass re-proposed its own to-do list (the 18:53 "governance has no owner" repeat is the worst case — see [[topics-wiki/senter/wiki/concepts/fix-the-record-not-the-pitch|fix the record, not the pitch]]). Thirteen such cards were removed; the two that served Chris were approved through the [[topics-wiki/senter/wiki/concepts/approval-apply-paths|apply paths]].

## Relationship to Chris's rules
- 17:46: "The bots is how it should suggest action, bots and then loops" → the cap keeps that order but bounds the count.
- 18:16: "stop asking me for so many decisions" → cap 2 (no infra cards) is the direct implementation.
- 19:06: backend as built-in Hermes + markdown ([[topics-wiki/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]]) — the caps live in the prompt of a `hermes chat -p senter` run, i.e. markdown, not code.

## Also landed at 18:58 (same message)
Vault `AGENTS.md` written (sidebar/builder behaviour for any Hermes running in the vault dir); the `senter` profile's SOUL rewritten to the sidebar spec; canvas files brought current. A correction source (`raw/sources/2026-09-05-umbrella-still-runs.md`) added so the senter agent stops re-pitching a dead belief. ^[raw/inbox/2026-09-05.md]
