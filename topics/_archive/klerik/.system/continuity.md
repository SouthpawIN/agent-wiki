# Continuity — klerik

Raw understanding, 2026-08-27 (from GitHub metadata + README):
- Hermes Agent meta-profile for reviewing and correcting other agent profiles
- Language: Python; 9 stars; last push 2026-07-08; original work.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)

## learned 2026-09-05 17:12 (worker, from 2 inbox blocks)
- 2026-09-05 (assistant-side, not Chris): a proposal-only planner already exists in the vault — verify it runs against the vault before writing any new planning code for klerik
- 2026-09-05 (assistant-side, not Chris): topic build-out per spec = continuity + queue with real items + injections + skills/agents/loops + catalogs, all populated with real content, no placeholders

## learned 2026-09-05 17:47 (worker, from 3 inbox blocks)
- 2026-09-05 (assistant-side, not Chris): the vault's md() renderer already converts [[x|y]] wiki-links into <a data-wiki> — do not write new link-rendering code; every topic gets init'd and only the two big topics get fully compiled
