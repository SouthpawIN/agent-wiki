---
name: topic-context-llm-wiki
description: Use when writing or refreshing a topic's context section. Build a thorough interlinked LLM wiki from all collected raw context, never a one-line summary.
version: 0.1.0
distilled: 2026-09-05 17:42
topic: senter
---
# topic-context-llm-wiki
# Topic context as an LLM wiki

## Steps
1. Load the `llm-wiki` skill (Karpathy LLM Wiki pattern) before touching any topic's context section.
2. Gather EVERYTHING in `wiki-topics/<t>/` — `.system/inbox.md`, session exports, continuity, queue, user notes — and treat each as a raw source, not something to compress away.
3. Generate a wiki: one page per individual thing (concept, tool, decision, person, artifact) with `[[wikilinks]]` between them, plus a hub page that indexes every sub-page.
4. Every claim on a page cites the raw source line/file it came from; keep raw sources intact alongside the wiki.
5. On every watcher pass, incrementally extend the wiki (new pages / updated pages) — never regenerate a summary.
6. Render the hub page as the topic's context section in the Senter wiki UI; verify in Chris's real window that it is multi-page, not one line.

## Rules
- Never truncate: if the UI shows a single line for context, that is a failure signal to fix at the root (rendering or generation), not to accept.
- Include all of the user's inputs verbatim — the wiki is the funnel for everything the user cares or worries about, digital and real life.
- User-edited lines are never overwritten.

## Pitfalls
- Writing 'raw understanding' summaries in place of a wiki (this is what Chris rejected as 'still only one line').
- Concentrating wiki-building effort in only 1–2 topics; every topic must get the same treatment.

## Evidence
> the context for center wiki is still only one line From what I see
> you should use the LLM wiki skill for the context section like the context section Should be like entire thorough wikis on each individual thing
> It should be like all of everything that's collected about that topic with that user and all of the inputs that they put into it This is going to be a funnel for all of the contacts for everything that the user cares or worries about across all of their digital and real life
