---
title: Progressive disclosure (how the wiki is read)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, tool, idea]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Progressive disclosure (how the wiki is read)

Chris's answer to "how does the sidebar stay aware of 7 MB of context?": read it the way Hermes discovers skills — index first, then the file, then one section. "this whole wiki could be one giant agent that self-managing it that's doing progressive disclosure like how skills are discovered." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## As built (2026-09-05 16:26)
- `assets/build-index.py` writes `topics-wiki/<t>/.system/INDEX.md`: one line per file (size, gist) plus each markdown file's heading outline **with line numbers**.
- Read path: row → INDEX → file → `read_file offset/limit` for one section — "never loads 5 MB." The scanner regenerates INDEX on every pass, so it is live.
- The `agent-wiki-vault` skill (loaded whenever anyone touches the vault) carries the read protocol and the rule: **"if it isn't in the wiki it isn't remembered; export the session there when it ends."**
- Raw memory, not summaries: `topics-wiki/senter-wiki` got 9 full session transcripts since Aug 27 (5.2 MB, incl. a 1,083-message session) via `hermes sessions export --format md`, the agent-wiki-vault skill + 10 reference docs, bridge and scanner source, the Anser interview; `topics-wiki/senter` got SOUL + AGENTS for senter/klerik/looker/weaver/paladin/anser and the fleet-coordination skill (these are this wiki's raw/).

## Open: who reads INDEX first, automatically
Hermes proposed (Chris undecided, said "before I make that decision…"): (1) a standing instruction in the default profile's AGENTS.md to consult `topics-wiki/*/.system/INDEX.md` before answering anything about Senter; (2) the `on_session_finalize` hook to auto-export each session; (3) later, the wiki as one self-managing `senter` profile owning INDEX for the others. See [[topics-wiki/senter/wiki/entities/senter|Senter]].

## Precedent: the selfmodel rule
Anser's 2026-08-31 rule for the [[topics-wiki/senter/wiki/concepts/selfmodel-layer|self-model layer]] said the same thing: "query-on-demand, NEVER injected verbatim into context — flush distilled one-liners into `memory` instead." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Chris's correction on depth (17:40)
Disclosure must lead to *whole* wikis, not one-liners: "the context section should be like entire thorough wikis on each individual thing… all of everything that's collected about that topic with that user." → [[topics-wiki/senter/wiki/decisions/2026-09-05-context-section-is-a-full-llm-wiki|decision]]; related [[topics-wiki/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|memory layer]].
