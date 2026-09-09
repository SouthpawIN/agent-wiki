# Wiki Schema — crow
## Domain
Everything Chris has said, built, decided or worried about regarding **crow** — his inputs verbatim in `raw/`, compiled understanding in `wiki/`.

## Conventions (llm-wiki skill)
- `raw/` is immutable. `raw/inbox/YYYY-MM-DD.md` = the watcher's per-message filings; `raw/sources/` = transcripts, exports, specs, source code.
- `wiki/` pages: lowercase-hyphen filenames, YAML frontmatter (title, created, updated, type, tags, sources, confidence), ≥2 `[[wikilinks]]`, provenance `^[raw/…]` on synthesized paragraphs.
- Every page is listed in `index.md`; every action appended to `log.md`. Pages > 200 lines split. Contradictions noted with dates, `contested: true`.
- Chris's corrections win: lines marked `<!-- chris -->` are never rewritten.

## Tag taxonomy
person, tool, repo, bot, skill, loop, decision, preference, pain, idea, plan, spec, ui, infra, music, money, health, family, timeline, question

## Page thresholds
Create when an entity/concept appears in 2+ raw items or is central to one. Decisions get a page each (what/why/when/evidence). Passing mentions go into an existing page.
