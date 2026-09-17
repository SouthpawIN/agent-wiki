---
title: Live data pipeline verification (2026-09-09) — bridge / git / gh-sync
created: 2026-09-09
updated: 2026-09-09
type: decision
tags: [infra, bridge, git, repo, timeline]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-09-from-senter-wiki.md]
confidence: high
---

# Live data pipeline verification (2026-09-09) — bridge / git / gh-sync

## Summary of verified state (2026-09-09 13:32)
Hermes confirmed the Senter backend infrastructure is live and healthy:

- **Bridge server running**: `com.senter.bridge` launchd service on `127.0.0.1:8643`
- **`/system-live.json` served correctly** via the bridge's `/file` endpoint
- **Vault contents**: 35 topics, 69 bots, 201 skills, 81 loops
- **senter-wiki topic properly populated** ^[raw/inbox/2026-09-09.md]

Hermes: **"The Senter Wiki UI restoration is complete. The backend is functioning, git is initialized for updates, and the live data pipeline works correctly. The UI expects to be loaded in the Hermes Desktop app's webview at `vault-live.html` to display the wiki with live fleet data."** ^[raw/inbox/2026-09-09.md]

## The git fix (why "updates keep failing")
From the re-routed `senter-wiki` raw item, Chris asked (2026-09-09 13:01): **"My updates keep failing. I think that's something to do with the project that we're working on."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

Hermes diagnosed (2026-09-09 13:17): **"The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' - there's no git to track or push changes. The user wants to be able to update AND keep the project."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

Hermes then initialized git and connected it to the remote: **"Let me initialize it as git and connect it to the remote."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

## The gh-sync repo structure
Hermes noted (2026-09-09 13:15): **"I see there are separate repos in `gh-sync`: agent-wiki - the main repo; klerik - another repo; senter - another repo. But the user's working directory is `~/Documents/Projects/Projects`. This might be a symlink, or the Projects folder might be a different location."** ^[raw/inbox/2026-09-09.md]

Hermes (2026-09-09 13:17): **"Looking at the README, the Projects folder should be the agent-wiki Senter codebase."** ^[raw/inbox/2026-09-09.md]

This confirms Chris's vision (see [[topics/senter/wiki/entities/hermes-agent|Hermes Agent]], [[topics/senter/wiki/concepts/native-hermes-vs-custom-backend|native vs custom backend]]): the entire flow — watcher → topics → topic agent → wiki → cards → apply — operates on the markdown vault in `~/Documents/Projects/Projects`, with the gh-sync repos providing the upstream structure.

## Relationship to prior decisions
- The git-init resolves the "updates keep failing" pain noted by Chris. It maps to the [[topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|backend-as-built-in-Hermes decision]] (19:06): the backend should be "just built in Hermes commands and markdown." Git tracking is the literal enabler of that contract — the vault files *are* the backend state. ^[wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown.md]
- The live-data contract ([[topics/senter/wiki/concepts/live-data-contract|live-data contract]]) is now verified end-to-end: bridge serving `.system-live.json` with 35 topics / 69 bots / 201 skills / 81 loops. ^[wiki/decisions/2026-09-05-per-message-watcher.md]
- The "senter-wiki topic now properly populated" corroborates the [[topics/senter/wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing|topic-folder-missing investigation]]: the folder exists with proper structure. ^[wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing.md]

## Open
|- The exact symlink/relationship between `~/Documents/Projects/Projects` and the `gh-sync` `agent-wiki` repo is evidence-level only (marked unresolved in BRIEF "## Learned" 2026-09-09). Whether the vault is a git worktree, symlink, or clone of `agent-wiki` is not confirmed.
|- Following the 13:32 pipeline verification, Hermes reported a bot/sessions layout visibility gap: DOM inspection of the Hermes Desktop was blocked ("browser isn't running"); the plan at 13:33 was to inspect the desktop preview + vault-live view-switching paths. The data contract is verified (79 bots served) but the UI rendering in `vault-live.html` remains under inspection — see [[topics/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|bot/sessions layout inspection]].

## Related
|- [[topics/senter/wiki/entities/senter-bridge|senter-bridge]] — live data pipeline, `/file` endpoint
|- [[topics/senter/wiki/entities/hermes-agent|Hermes Agent]] — runtime, git-init, gh-sync
|- [[topics/senter/wiki/concepts/live-data-contract|Live-data contract]] — "spawn = visible", no timers
|- [[topics/senter/wiki/decisions/2026-09-08-autonomous-completion-standing-approval-extended|Autonomous completion (2026-09-08)]]
|- [[topics/senter/wiki/entities/umbrella|Umbrella]] — WatchPaths sync
|- [[topics/senter/wiki/decisions/2026-09-09-autonomous-senter-wiki-completion-continuation|2026-09-09 autonomous completion continuation]]
|- [[topics/senter/wiki/queries/vault-repo-link-status|Vault-to-repo link status]] — git-init resolution and remaining gh-sync relationship

^[raw/inbox/2026-09-09.md] ^[raw/inbox/2026-09-09-from-senter-wiki.md]
