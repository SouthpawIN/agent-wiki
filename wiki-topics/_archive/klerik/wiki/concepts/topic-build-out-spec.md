---
title: Topic build-out spec (what a "real" topic contains)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, plan, infra]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: medium
---
# Topic build-out spec

**Definition.** A topic in the Senter vault is a work unit a bot "absorbs". On 2026-09-05 the klerik topic was built out to the full shape: "Now I'll build out the topic properly per the spec: continuity, queue with real items, injections, skills-capabilities/agents/loops, catalogs — all real." ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Components named in that message** (all present on disk in `wiki-topics/klerik/` as of this compile):
- `.system/continuity.md` — the topic agent's running understanding; user-edited lines never overwritten.
- `.system/queue.md` — "with real items", i.e. actual actionable entries, not placeholders. For klerik that is the REFLECT-pass backlog from anser.
- `.system/injections.md` — context to be injected into the owning bot.
- `skills-capabilities/`, `agents/`, `triggers-loops/` — the three product layers (Context → Skills → Bots → Loops per Chris's concept.md).
- catalogs — the roster / cross-topic indexes.

**The rule inside the rule: "all real".** No dummy data, no placeholder rows — matching klerik's authoring rule 8 ("No dummy data … 'on disk' ≠ 'connected'") and Chris's standing preference against workarounds and temp fixes. A topic with an empty queue is not built out; a topic with a queue nobody drains is built out but not owned — which is the current klerik state described in [[wiki-topics/klerik/wiki/entities/klerik|klerik]].

**Relationship to the wiki layer.** The build-out spec covers the `.system/` machine side; this `wiki/` tree (entities/concepts/decisions/comparisons/queries) is the compiled-understanding side added by the llm-wiki convention (SCHEMA.md). Both are fed from the same per-message inbox — see [[wiki-topics/klerik/wiki/decisions/2026-09-05-per-message-inbox-filing|Per-message inbox filing]].
