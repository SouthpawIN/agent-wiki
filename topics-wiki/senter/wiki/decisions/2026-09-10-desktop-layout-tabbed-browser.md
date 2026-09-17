---
title: 2026-09-10 — Desktop layout: tabbed browser main zone + bot options above sidebar
created: 2026-09-10
updated: 2026-09-12
type: decision
tags: [decision, ui, layout, desktop, plugin, investigation]
sources: [raw/inbox/2026-09-10.md, raw/inbox/2026-09-11.md, raw/inbox/2026-09-12.md]
confidence: high
---

# 2026-09-10 — Desktop layout: tabbed browser main zone + bot options above sidebar

## The vision (Chris)

Chris, 2026-09-10 15:22: **"I want you to bring back the options that were here, such as the sidebar. I really wish that that had the tabs on top of it to open a new session and a bot and everything that's in the default permies, I want all those options here in the sidebar as well. And in the main window, right now we see the center of wiki."** ^[raw/inbox/2026-09-10.md]

Chris, 2026-09-11 18:10 (precise current-layout description + want): **"Capture what I'm currently running and then add those features to it because I generally like the layout that I have now... there is a skinny sidebar where I'm talking to you and in the main content area Right now is the browser. Right now that browser is open on my wiki that we've been working on, but this is going to be a plugin. So this central area, I want to have tabs where I can open up a new instance of this plugin or a new browser so that I can switch tabs and have one tab on like maybe Discord or X and then another tab on the wiki. And then also above the sidebar is where I want to see the options for bots and all that stuff too."** ^[raw/inbox/2026-09-11.md]

Two concrete wants:
1. **Main zone = tabbed browser** — open the wiki (plugin) or Discord/X/etc. as switchable tabs, each its own tab.
2. **Bot options above the sidebar** — the "new session / open bot / default permies" tab strip restored at the top of the left sidebar.

## What Hermes tried (and reversed)

- **2026-09-11 18:15** built a **tabbed Browser plugin** — tab bar (add/close/switch), URL bar, home-screen quick-launch; each tab its own iframe. ^[raw/inbox/2026-09-11.md]
- **2026-09-12 14:13** **deleted the plugin** — Chris was right; Hermes Desktop already ships a real Chromium browser in the preview pane. A fake iframe tab bar is redundant. ^[raw/inbox/2026-09-12.md]
- Correct path: open a real `<webview>` tab in the preview pane with **⌘K → type the URL / search** (e.g. opens Discord as a genuine Chromium tab, not an iframe). ^[raw/inbox/2026-09-12.md]

## The tab strip (bot options above sidebar)

- The **SESSIONS | BOTS tab strip** is a **default Hermes layout element** at the top of the left sidebar. If it's missing, the layout was customized and the Bots pane dropped out. ^[raw/inbox/2026-09-12.md]
- **Recover it:** **⌘K → "Reset layout"** (or "Reset desktop layout") re-runs default-tree adoption and the tab strip reappears. If the command doesn't exist in the build, the layout tree is persisted in **localStorage as `hermes.desktop.layoutTree.v2`**. ^[raw/inbox/2026-09-12.md]
- Hermes already added `hermes-bots` to the enabled plugins; the layout just needs to be reset to re-adopt it. ^[raw/inbox/2026-09-12.md]

## Scope note

Per BRIEF anti-scope, *how the wiki looks/behaves on screen* (tabs, layout, the browser pane) belongs to `senter-wiki`; the **backend** (that the wiki is served, that bots are live fleet data) is `senter`. This decision is a `senter-wiki` UI-layout outcome, but it was discovered through the `senter` watcher and is recorded here because it names the bot options, the sidebar, and the fleet-visible layout that `senter` owns as live-data contract. See also [[topics-wiki/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|bot/sessions layout inspection]].

## Open status

- The real `<webview>` tab path (⌘K) is the working mechanism; the custom plugin is gone.
- Whether Chris has re-applied the default layout (and thus sees SESSIONS|BOTS) is unconfirmed from here.
- Related: [[topics-wiki/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|2026-09-09 bot/sessions layout inspection]]; [[topics-wiki/senter/wiki/concepts/preview-pane-viewport|preview pane viewport]].
