---
title: kashik
created: 2026-09-17
updated: 2026-09-17
type: wiki
sources:
  - index.md
  - wiki/
  - raw/inbox/
  - .system/
---

# kashik

Last updated: 2026-09-17 | Total pages: 9

---

## INTEGRATIONS

This wiki is fed by:

- **Raw inbox:** `raw/inbox/` — daily cuts from Hermes sessions
- **Sessions:** `.system/sessions/` — full conversation transcripts
- **Wiki pages:** `wiki/` — structured knowledge base

---

## README

### Entities

- [kashik](wiki/kashik.md) — kashik is Chris's silent historian and librarian for the Senter wiki. It watches agent activity and maintains per-agent `llm-wiki` documentation for Chris's sec

### Concepts

- [Librarian concept](wiki/librarian-concept.md) — A governing discovery layer across all topics in the Senter wiki, owned conceptually by kashik.
- [llm-wiki](wiki/llm-wiki.md) — The per-agent wiki documentation convention Chris has adopted for the Senter vault.
- [Progressive disclosure frontmatter](wiki/progressive-disclosure-frontmatter.md) — A filesystem-simplification strategy: put key discovery information into page frontmatter so deeper nested folders can be reduced or removed.
- [Wiki orientation procedure (resuming an existing wiki)](wiki/wiki-orientation-procedure.md) — A standing rule for the kashik compile loop: always orient before ingesting, querying, or linting. The procedure is repeated verbatim in the watcher's filings,

### Decisions

- [Simplify filesystem structure](wiki/simplify-filesystem-structure.md) — Chris decided to simplify the topic filesystem using frontmatter-based progressive disclosure rather than maintaining deep nested topic folders.
- [String split slug generation](wiki/string-split-slug-generation.md) — A decision about how wiki page slugs are derived from filenames.
- [Topic discovery governance](wiki/topic-discovery-governance.md) — Chris decided to introduce a librarian concept that governs discovery across topics in the Senter wiki.

### Queries

- [Clone official repos to read documentation](wiki/clone-official-repos-to-read-docs.md) — On 2026-09-14, Chris located the official repositories for kashik and moved to clone the key ones so he could read their documentation properly instead of worki

---

## SKILLS

Topic skills stored in this wiki:

- **[wiki-orientation-procedure](skills/wiki-orientation-procedure/SKILL.md) — Always orient before ingesting, querying, or linting an existing topic wiki. Standing rule — stated "CRITICAL — do this every session" and repeated ve

---

## BOTS

Proposed bots:

- **[wiki-librarian](agents/wiki-librarian.md.proposed) — **I see you're introducing a librarian concept for cross-topic discovery — want a bot that audits aliases, anti-scope boundaries, and routing rules ac


---

## LOOPS

Proposed loops:

- **[frontmatter-progressive-disclosure-check](loops/frontmatter-progressive-disclosure-check.md.proposed) — owner: senter-wiki-bot · cadence: every build · status: SUGGESTED
