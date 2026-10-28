# Wiki Log — turbofit
## 2026-09-16 reorganize | Models portal pattern
- Removed blurbs from index table — now just clickable links
- Each model page becomes a portal for focused sub-agent research
- This structure is the template for all other topics in the wiki

## 2026-09-16 create | Model pages created
- Created 17 model pages in models/
- Each page is a portal awaiting focused research

## 2026-09-19 dedupe | Archived turbofit-mtp-performance redirect
- Identified duplicate: `turbofit-mtp-performance.md` was a redirect to `turbofit-mpl-performance.md`
- No unique evidence in redirect (only wikilink preservation needed)
- Archived to `topics/_archive/turbofit-mtp-performance-redirect/`
- Verified 0 title duplicates remaining in turbofit wiki

## 2026-10-18 scope | Universal product, two fit lists, SALT engine
- Chris re-scoped TurboFit: universal public product, not personal fleet
- New roadmap created (ROADMAP.md): two fit lists (GPU-dense/unified-MoE), benchmark publication, dynamic model+engine registry, SALT-core engine, Tailscale solidification
- Captured verbatim intent in raw/sources/2026-10-18-universal-scope.md; updated continuity + critical-gaps

## 2026-10-28 consolidate | Everything into one spot (GitHub → vault)
- Absorbed the whole `SouthpawIN/turbofit` prose tree (33 pages) into `references/` — docs/, references/*.md, ROADMAP, CHANGELOG, WORKFLOWS, SKILL, after-install — each with a provenance header pinned to commit `0ff572b`.
- Absorbed the seven sibling repos as entity pages + `references/ecosystem.md`: sirvir (TurboSouth), SALT-core, model-momento, benchmark-infographics, turbohaul-manager, southpaw-turbohaul, turbohaul-llmfit.
- Rebuilt `index.md` as a generated catalog: two-ladder tables come straight from `fit-lists.json`, lane lists point at real files (they all pointed at one skill file before).
- Fixed the dense body `wiki/index.md`: replaced the stale "5 candidates / Agentic lineup" section with the canonical two ladders; added a banner tying body → catalog → hub.
- Link integrity: 0 broken relative links in the topic (cross-repo `../../../../../turbofit/...` links resolved to `~/Documents/turbofit`, i.e. nowhere); 118 wikilinks normalised to real page stems.
- Moved 8 stranded TurboFit table pages out of the miscut `add-one` topic into `wiki/{decisions,concepts,entities}/`.
- Provenance + open questions: `raw/sources/2026-10-28-github-consolidation.md`.
