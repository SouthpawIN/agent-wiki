---
title: 2026-09-05 — Backend should be built-in Hermes commands + markdown; the UI stays
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, infra, plan, spec]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-05 — Backend as built-in Hermes + markdown; the UI stays

**What.** At 19:06 [[wiki-topics/senter/wiki/entities/chris|Chris]] set the direction for the *backend* of the whole Senter flow: ^[raw/inbox/2026-09-05.md]

> "If there's a way that we can get this entire flow down to just built in Hermes commands and markdown, that would be great. But with the UI, with everything like that we built, I'm not saying go back on you anything like that. I'm just saying the backend stuff could probably work to be a lot more efficient now that we know what the idea is for the intended flow."

Three parts, in his own framing:
1. **Target:** the flow — watcher → topics → topic agent → wiki → cards → apply — expressed as native Hermes commands operating on markdown files, nothing bespoke where a built-in exists.
2. **Exemption:** the [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] and "everything like that we built" are **not** to be rolled back. "I'm not saying go back on anything."
3. **Reason:** efficiency, *now that the intended flow is known*. The custom pieces were scaffolding built while the shape was still being discovered ([[wiki-topics/senter/wiki/comparisons/topic-pipeline-16-37-vs-17-46|two pipeline shapes in one afternoon]]); with the shape fixed, they can be re-expressed.

**Why (lineage).** This is the second time Chris has said it. Earlier on 2026-09-05 he asked Hermes to "see what of Hermes we can squeeze into each one of these lanes into topics, [skills, bots, loops]" and to talk to [[wiki-topics/senter/wiki/entities/anser|anser]] to find what already exists ([[wiki-topics/senter/wiki/entities/hermes-agent|Hermes Agent page]]). It also follows from [[wiki-topics/senter/wiki/concepts/markdown-is-the-api|markdown is the API]] and from the [[wiki-topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|memory-layer decision]]: if the wiki is Hermes's memory, the machinery around it should be Hermes's machinery. ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Hermes's reply (19:12), not contradicted.** "Agreed, and the backend is already mostly that — the topic agent is `hermes chat -p senter` over markdown, loops are `hermes cron`, bots are `hermes profile`, the wiki is the `llm-wiki` skill layout. What's still custom: the watcher (Hermes has no per-message hook), the bridge (SSE + file proxy for the UI), and the TF-IDF cutter." The full ledger is in [[wiki-topics/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]]. ^[raw/inbox/2026-09-05.md]

**How it is applied.** Under [[wiki-topics/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|preempt decisions]], "that would be great" is a directive, not a question to card back. Each remaining custom piece has a standing burden: either name the Hermes built-in that replaces it, or name the missing Hermes capability that keeps it custom — and a missing capability is a candidate for the PR ledger under the [[wiki-topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|upstream PR policy]], since Chris works with the Hermes team and wants core gaps upstreamed.

**Evidence.** Chris 19:06 (quoted above); Hermes 19:12 inventory; earlier "squeeze Hermes into the lanes" instruction. Status: direction locked; no rollback of UI; the three custom pieces documented with reasons as of 19:12.
