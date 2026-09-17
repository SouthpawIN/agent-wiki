---
name: knowledge-vault
description: Build an Obsidian vault of project topics from user sources.
version: 1.1.0
author: Hermes background curator
license: MIT
metadata:
  hermes:
    tags: [obsidian, vault, knowledge-base, goop]
    related_skills: [obsidian]
---

# Knowledge Vault Building

## When to Use

Use when the user asks to build or organize an Obsidian/markdown vault of their ideas, projects, or repositories pulled from external sources (GitHub, notes, chat history).

Organize a user's ideas/projects from external sources into a markdown vault (Obsidian) as reusable topic dashboards. This user runs vaults to their own [agent-wiki (GOOP)](https://github.com/SouthpawIN/agent-wiki) standard.

## Vault location

The `obsidian` bundled skill's env-var/fallback conventions apply, but the authoritative source on macOS is Obsidian's registry: `~/Library/Application Support/obsidian/obsidian.json` maps vault ids to paths, `"open": true` marks the active vault. Real vaults may be nested (e.g. `~/Documents/Projects/Projects`) — do not guess `~/Documents/Obsidian Vault`.

## Topic anatomy (GOOP standard)

```
topics-wiki/<slug>/
├── README.md          ← human dashboard (facts + source README/description extract)
├── .system/           ← machine internals (dot-prefix hides in Obsidian)
│   ├── continuity.md  ← raw understanding; user corrects here; never overwrite user edits
│   ├── queue.md       ← [SKILLS]/[AGENTS]/[LOOPS] checklist work items
│   └── injections.md  ← status feed with [UNREAD]/[READ] sections
├── skills-capabilities/  agents/  triggers-loops/
```

Root: `index.md` (entry), `catalogs/` (fleet-dashboard, topic-index, agent-roster, skill-registry, loop-registry), `topics-wiki/_global/.system/` (registry mirrors), `agent-wiki-spec.md`, `Sources.md`, `Ideas.md`, `log.md`. User editing any markdown file IS the steering mechanism.

## Workflow

1. Collect source data in ONE scripted pass (see `references/github-deep-pull.md` for the GitHub case), save JSON to /tmp.
2. Write ONE Python builder script that emits the whole vault from the data; run it once. Never hand-write hundreds of write_file calls.
3. Clean embedded READMEs: strip frontmatter, HTML comments, badges, images, tags; truncate ~2.6KB with a truncation note + link to the original.
4. YAML frontmatter on every note (title, updated ISO date, type, tags); wikilinks `[[path|label]]`; status vocabulary ACTIVE / DORMANT (since date) / ARCHIVED.
5. Log the build in `log.md` and record pulled vs queued sources in `Sources.md`.

The vault is a live canvas: re-pull sources on request, act on `[SKILLS]`/`[AGENTS]`/`[LOOPS]` queue items, and watch for user edits.

## References

- `references/github-deep-pull.md` — GitHub repo/README collection specifics and pitfalls.