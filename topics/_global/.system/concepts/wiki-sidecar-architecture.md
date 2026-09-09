---
title: Wiki Sidecar — Modular Live Operating View
created: 2026-07-14
updated: 2026-07-14
type: concept
tags: [wiki, sidecar, herm, discord, android, modular, frontend, visualization]
sources: ["queries/discord-wiki-integration.md", "concepts/agent-wiki-authoritative-architecture.md"]
confidence: high
---

# Wiki Sidecar — Modular Live Operating View

## Pivot: from Discord-first to sidecar-first

Earlier design treated Discord (`#wiki-updates`) as the primary live view of
the Idea Wiki. New direction: build the live operating view **first as a
sidecar in Herm**, then extend to other surfaces. Discord (and later Android)
become **modular front-ends** that render the same wiki state — not the
canonical destination.

## Core principle: one state model, many renderers

The canonical source of truth remains Markdown in `/home/sovthpaw/idea-wiki/`.
A **frontend-agnostic state index** (`wiki-state.json`) is generated from that
Markdown. Every surface — Herm sidecar, Discord, Android — renders the index.
No surface owns the data.

```text
Markdown Wiki (source of truth)
        ↓  generator (hook-driven)
wiki-state.json (topic graph + live status)
        ↓
Herm sidecar  |  Discord renderer  |  Android renderer
```

## Live operation (the "operating" part)

Topics carry derived state used for color / visual signal:

| State    | Meaning                                       | Suggested color |
|----------|-----------------------------------------------|-----------------|
| active   | running agent/loop tied to topic              | green           |
| proposed | proposed agent/loop/skill exists              | amber           |
| idea     | captured idea, no proposal yet                | blue            |
| stale    | not updated in N days                          | dim / gray      |
| blocked  | known blocker documented                       | red             |

The index also carries `active_agents`, `active_loops`, `proposed_agents`,
`proposed_loops`, `last_updated`, `health` so renderers can show exactly what
is operating on each topic.

## Herm sidecar (first renderer)

The first renderer is a **standalone HTML sidecar** at
`idea-wiki/tools/wiki-sidecar.html`. It reads `wiki-state.json` over HTTP and
renders the topic graph grouped by kind, colored by `state`, with active
agent/loop/proposed badges. It auto-refreshes every 3s so colors shift live as
topics gain agents, loops, or blockers.

Built as a separate file — it does NOT modify the Hermes desktop/terminal
install. To view it, serve the Idea Wiki over HTTP and open the page:

```bash
python3 -m http.server 8799 --directory /home/sovthpaw/idea-wiki
# then open http://127.0.0.1:8799/tools/wiki-sidecar.html
```

It is intentionally renderer-agnostic: the same `wiki-state.json` can later feed
a native Herm TUI/desktop left sidebar (registered as its own pane so the Eikon
and right rail stay untouched), a Discord renderer, or an Android view.

> Later note: if a native Herm left sidebar is desired, it should be a NEW pane
> in the existing `layout.ts` pane registry (`desktop-controller.tsx`), not a
> modification of the Eikon or the right-rail preview/file-browser panes.

## Modular extension

- **Discord:** render topic embeds/status to `#wiki-updates` (permission-gated;
  currently blocked on Send Messages — see discord-wiki-integration).
- **Android:** native topic view consuming the same state index.
- Future surfaces read the same index; adding one never touches the others.

## Hook integration

The existing Senter `wiki-maintenance` gateway hook (event `agent:end`)
regenerates `wiki-state.json` **immediately** on any Wiki change, then launches
the semantic reconciliation worker. The visual state updates instantly;
deeper synthesis follows.

## Boundaries

- Markdown stays canonical; `wiki-state.json` is derived, never hand-edited.
- Renderers are read-only projections of the index.
- Consequential actions remain approval-gated.
- Keep the state schema stable so all renderers share one contract.

## Related pages

- [[discord-wiki-integration|Discord as a Live View of the Idea Wiki]]
- [[agent-wiki-authoritative-architecture|Agent Wiki — Authoritative Architecture]]
- [[senter-wiki-maintenance-goal|Senter Wiki Maintenance Goal]]
- [[senter-intention|Senter Intention — Optimize the User's Life]]
