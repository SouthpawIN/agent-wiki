# Senter — the concept (Chris, 2026-09-03, verbatim-adjacent)

**Hermes makes Skills out of repeated asks. Context → Skills.**

Vocabulary: **Agent** = an agentic harness (Hermes Agent). **Bot** = a specialized sub-worker of that Agent. Sub-agents are more like drones.

**Bots** make sense when a collection of Skills requires its own continuity/learning — skills become the toolbox for a craft, and a craft benefits from having a memory/intelligence as a dedicated Bot.

**When a Bot has a purpose, naturally a Loop springs out.**

```
Context → Skills → Bots → Loops
```

The four dots denote, and sort by, these four objects. All four are Markdown:

| object  | markdown                                   |
|---------|--------------------------------------------|
| Context | the knowledge base (topics-wiki/*/README.md, .system/*, feed) |
| Skills  | SKILL.md                                    |
| Bots    | AGENTS.md / SOUL.md / {whatever}.md          |
| Loops   | cron / hook scheduling                       |

This is a **Cursor × Obsidian** setup: everything you talk about gets captured as **Topics** in a wiki, and each topic works through Context → Skills → Bots → Loops independently, while you maintain one chat about the whole wiki — anything you care or worry about, in any order. Jump between topics; it sorts and automates them all, looking for efficiencies and reusable artifacts between topics.

## Navigation (the rule)

- **Search a term + Enter** → the **WIKI** page, sorted by relevance to the term.
- **CONTEXT orb** → the **CONTEXT** page (the old Feed, renamed). Not just the bot feed: **every new chunk of context that enters Hermes-Agent**, each tagged with the topic title it is most similar to (plus an **UNSORTED** area for chunks that match nothing). Sorted by relevance to the search term / title.
- **SKILLS orb** → the **SKILLS** page: all skills, sorted by relevance to the term.
- **BOTS orb** → the **BOTS** page: all bots, sorted by relevance to the term.
- **LOOPS orb** → the **LOOPS** page: all crons / webhooks / other automations, and which bots they automate — sorted by relevance to the term.
- With no search term active, the "term" is the current hero title (the topic in the header).
