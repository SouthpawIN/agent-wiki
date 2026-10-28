# Wiki Schema — turbofit

## Domain
Everything Chris has said, built, decided or worried about regarding **turbofit** — his inputs verbatim in `raw/`, compiled understanding in `wiki/`.

## Conventions (llm-wiki skill)
- `raw/` is immutable. `raw/inbox/YYYY-MM-DD.md` = the watcher's per-message filings; `raw/sources/` = transcripts, exports, specs, source code.
- `wiki/` pages: lowercase-hyphen filenames, YAML frontmatter (title, created, updated, type, tags, sources, confidence), ≥2 `wikilinks`, provenance `^[raw/…]` on synthesized paragraphs.
- Every page is listed in `index.md`; every action appended to `log.md`. Pages > 200 lines split. Contradictions noted with dates, `contested: true`.
- Chris's corrections win: lines marked `<!-- chris -->` are never rewritten.

## Tag taxonomy
person, tool, repo, bot, skill, loop, decision, preference, pain, idea, plan, spec, ui, infra, music, money, health, family, timeline, question

## Content Type Hierarchy
The `type` field determines how a page appears in the index:

| Type | Section in Index | Notes |
|------|-----------------|-------|
| `model` | **Models** (top-level, first) | Individual model pages — the stars of the wiki |
| `concept` | Concepts | Technical concepts, runtime patterns |
| `comparison` | Comparisons | Side-by-side model/runtime analysis |
| `decision` | Decisions | Actionable decisions with evidence |
| `query` | Queries | Filed query results |
| `entity` | Everything else | Anything that doesn't fit above |

## Models Directory
The `models/` folder is **first-class** — not nested under entities. Each model page gets its own file with:
- Unique blurb (what makes it special)
- Research findings
- Best runtimes (NVIDIA, AMD, Apple Silicon, CPU)
- Systems where it's active

```
wiki/
├── models/           # ⭐ MODELS (top-level, each model gets its own page)
├── comparisons/      # Side-by-side runtime/model comparisons
├── concepts/         # Technical concepts
├── decisions/       # Actionable decisions
├── queries/         # Filed query results
└── raw/             # Immutable sources
```

## Page thresholds
Create when an entity/concept appears in 2+ raw items or is central to one. Decisions get a page each (what/why/when/evidence). Passing mentions go into an existing page.

## Index Structure
The index is generated with this section order (models first):

1. **Models** — `type: model` pages (each model gets its own line)
2. **Comparisons** — `type: comparison`
3. **Concepts** — `type: concept`
4. **Decisions** — `type: decision`
5. **Queries** — `type: query`
6. **Other** — everything else
