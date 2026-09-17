---
title: "Skills & Bots Progressive Disclosure in the Wiki"
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [ui, preference, spec]
sources: ["raw/inbox/2026-09-17.md"]
confidence: high
---

# Skills & Bots Progressive Disclosure in the Wiki

On `2026-09-17 10:45` Chris set out how the wiki should present its skills and bots — as browsable lists where each entry uses progressive disclosure, and where the wiki itself becomes the home for every skill and bot in Hermes Agent.^[raw/inbox/2026-09-17.md]

## What Chris said
- "the skills and bots should be lists and the title of each list should be clickable to go to that skill or bot in this wiki because this wiki is also going to house all of the skills and bots within Hermes agent."^[raw/inbox/2026-09-17.md]
- The list item should show "the clickable name of the skill or bot and then the description underneath it to be the description from the front matter."^[raw/inbox/2026-09-17.md]
- The browsing model is "as if the human is sorting through them the same way that an agent would with progressive disclosure where we can see the title and the description and then we can click on it to go see the whole thing and edit and see it or whatever we need to do."^[raw/inbox/2026-09-17.md]

## The design in practice
- **Lists, not walls.** Skills and bots render as lists, one entry per skill/bot.
- **Title is a link.** Each entry's title links to that skill's or bot's page in the wiki (e.g. `[[wiki-topics/hermes-agent/wiki/entities/...]]`), so a click lands on the full page.
- **Description from front matter.** The text under each title is the `description` field from the skill/bot's front matter — the same short line an agent would read when sorting.
- **Progressive disclosure.** The human sees only title + description first, then clicks through to the full page to read, edit, or inspect — mirroring how an agent narrows candidates.
- **The wiki houses everything.** This is not topic-local; the wiki is the intended home for *all* Hermes skills and bots, so the same pattern applies across topics.

## Why it matters
- It turns the wiki into a navigable catalog rather than a set of disconnected pages — the same navigable structure already being applied to the topic index restructure (Hermes consolidating each topic root `index.md` into a clean entry point).^[wiki-topics/hermes-agent/wiki/concepts/topic-index-restructure-2026-09-16]
- It matches how the fleet is actually consumed: a human and an agent both sort by title + one-line description before opening anything. It pairs naturally with the `/hotkeys` slash-command idea, which likewise aims to expose and edit Hermes's combined command/skill set from one surface.^[wiki-topics/hermes-agent/wiki/concepts/hotkeys-slash-command]

## Scope note
- The presentation rule is wiki-wide (all skills and bots in Hermes), so it belongs under `senter-wiki` as the UI owner, but it is captured here because it is this topic's raw item and it directly governs how this topic's skills and bots should appear. The build/UI execution is weaver's.

## Related
- [[wiki-topics/hermes-agent/wiki/concepts/topic-index-restructure-2026-09-16|Topic Index Restructure — 2026-09-16]]
- [[wiki-topics/hermes-agent/wiki/concepts/hotkeys-slash-command|/hotkeys Slash Command]]
- [[wiki-topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]]
