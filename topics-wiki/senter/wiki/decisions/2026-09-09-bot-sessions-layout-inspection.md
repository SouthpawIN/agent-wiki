---
title: 2026-09-09 — Bot/sessions layout visibility inspection (ongoing after pipeline verification)
created: 2026-09-09
updated: 2026-09-09
type: decision
tags: [decision, ui, infra, gap, investigation, timeline]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-09-from-senter-wiki.md]
confidence: medium
---

# 2026-09-09 — Bot/sessions layout visibility inspection (ongoing after pipeline verification)

## The trigger

From the re-routed `senter-wiki` raw item, Chris, 2026-09-09 13:01: **"ok so how do I see my bots and sessions in this layout? Look at the Hermes Desktop and fix the layout, also My updates keep failing. I think that's something to do with the project that we're working on."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

This is a **bot/sessions layout visibility** question — Chris asking how his running bots and sessions appear in the Hermes Desktop UI, and asking them to be fixed. Per BRIEF anti-scope, the *how the wiki looks on screen* belongs to `senter-wiki`; but the question of whether bots-profiles/sessions are *visible as live fleet data* is a pipeline/infra concern — it depends on `.system-live.json` being served correctly through the [[topics-wiki/senter/wiki/entities/senter-bridge|bridge]] and the [[topics-wiki/senter/wiki/concepts/live-data-contract|live-data contract]] ("spawn = visible").

## What Hermes did (13:15–13:33)

### 13:15 — gh-sync repo structure investigation
Hermes noted the three separate repos in `gh-sync` (`agent-wiki`, `klerik`, `senter`) and the working-directory tension with `~/Documents/Projects/Projects`. ^[raw/inbox/2026-09-09.md]

### 13:17 — Root cause of "updates keep failing"
Hermes diagnosed: **"The Projects folder is NOT a git repository, but it contains files that should be. This is why 'updates keep failing' — there's no git to track or push changes. The user wants to be able to update AND keep the project."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

Hermes then initialized git and connected it to the remote: **"Let me initialize it as git and connect it to the remote."** ^[raw/inbox/2026-09-09.md]

### 13:17 — Layout issues identified
**"Layout issues in Hermes Desktop (need to see bots-profiles/sessions)."** — Hermes flagged the bot/sessions visibility as item 1 of 2 outstanding items (update issue #2 was already addressed by the git fix). ^[raw/inbox/2026-09-09.md]

### 13:02 — DOM inspection attempts (interleaved with the repo investigation)
From the `senter-wiki` raw item: **"I'll check the live Hermes Desktop DOM and fix the layout so bots and sessions are visible, then address the update issue."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

Then: **"Now let me inspect the Hermes Desktop DOM to understand the actual layout:"** followed by **"The browser isn't running. Let me check for other ways to see the layout."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

### 13:27 — Status check
Hermes listed two items: **"Layout issues in Hermes Desktop (need to see bots-profiles/sessions)"** and **"Updates failing (now git is initialized)."** ^[raw/inbox/2026-09-09.md]

### 13:32 — Live data pipeline verified; UI restoration declared complete
Hermes confirmed: bridge running/healthy, `/system-live.json` served correctly (35 topics / 69 bots / 201 skills / 81 loops), senter-wiki topic properly populated. **"'The Senter Wiki UI restoration is complete. The backend is functioning, git is initialized for updates, and the live data pipeline works correctly.'"** ^[raw/inbox/2026-09-09.md]

### 13:33 — Layout inspection plan remains open
Hermes: **"I'll inspect the desktop preview and the vault-live view-switching/data-loading paths to make bots and sessions actually visible, then patch whatever is broken."** ^[raw/inbox/2026-09-09-from-senter-wiki.md]

## The tension

At 13:32, Hermes declared the UI restoration complete and the live data pipeline healthy (35 topics / 69 bots / 201 skills / 81 loops). At 13:33, Hermes stated an intent to "inspect the desktop preview and the vault-live view-switching/data-loading paths to make bots and sessions actually visible." ^[raw/inbox/2026-09-09-from-senter-wiki.md] ^[raw/inbox/2026-09-09.md]

This means: the **backend contract** (`system-live.json` serving live bot/session counts) is verified, but the **UI view-switching path** that renders those live bots-profiles/sessions in the Hermes Desktop layout is still under inspection. The 69 bots figure in the live data snapshot means bot data is available; the question is whether the [[topics-wiki/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]]'s vault-live.html is wired to display them in the right layout pane.

## Relationship to existing pages

- The git-init fix (13:17) resolves "updates keep failing" — already captured in [[topics-wiki/senter/wiki/concepts/vault-repo-mapping|vault-repo-mapping]] and [[topics-wiki/senter/wiki/queries/vault-repo-link-status|vault-repo link status]]. ^[raw/inbox/2026-09-09-from-senter-wiki.md]
- The live-data pipeline verification (13:32) is captured in [[topics-wiki/senter/wiki/decisions/2026-09-09-live-data-pipeline-verification|live data pipeline verification]]. ^[raw/inbox/2026-09-09.md]
- Chris's continuation directive is captured in [[topics-wiki/senter/wiki/decisions/2026-09-09-autonomous-senter-wiki-completion-continuation|autonomous completion continuation]]. ^[raw/inbox/2026-09-09.md]
- The bot/sessions layout visibility inspection is the open thread — it lives in `senter-wiki`'s domain for the visual fix, but the data contract is a `senter` concern.

## Status

**Open.** The DOM inspection at 13:02 was attempted and blocked ("browser isn't running"). The plan at 13:33 ("inspect the desktop preview and the vault-live view-switching/data-loading paths") was stated but not recorded as completed in the raw items. The live data (69 bots) is being served; whether the wiki UI's layout path renders them visibly in the Hermes Desktop preview pane is the next verification step.

## Related

- [[topics-wiki/senter/wiki/entities/senter|senter]] — continuation directive, standing approval
- [[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge]] — serves `.system-live.json` (verified 2026-09-09: 35 topics / 69 bots / 201 skills / 81 loops)
- [[topics-wiki/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] — the `vault-live.html` that must render the live bots-profiles/sessions
- [[topics-wiki/senter/wiki/concepts/live-data-contract|Live-data contract]] — "spawn = visible", no timers
- [[topics-wiki/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|Event-driven trigger gaps]] — related open question about whether the topic agent fires on new inbox writes
- [[topics-wiki/senter/wiki/decisions/2026-09-09-live-data-pipeline-verification|Live data pipeline verification]] — the 13:32 verification this followed

|^[raw/inbox/2026-09-09.md] ^[raw/inbox/2026-09-09-from-senter-wiki.md]

## 2026-09-10 continuation — data path + UI rendering investigation

`raw/inbox/2026-09-10.md` is Hermes working output from the same debugging session that produced the 20:05–20:33 scan-topics.py investigation. It adds no new Chris decision but continues evidence on the bot/sessions visibility path:

- 10:23: **\"The update mechanism is the git repository. The git repo is there. Let me verify the current JSON file has the correct structure by checking if the bridge can serve it:\"** ^[raw/inbox/2026-09-10.md]
- 10:29: **\"Let me check the bots section of the JSON file for the senter-wiki-readme-live bot:\"** ^[raw/inbox/2026-09-10.md]
- 10:30: **\"The issue might be that the Hermes Desktop is showing old data because the bridge might be serving a cached version, or there's something wrong with how the BOTS view renders in vault-live.html. Let me check the vault-live.html to see if there are any issues with the renderBots function:\"** ^[raw/inbox/2026-09-10.md]

This re-confirms the open question from 20:33: whether the Hermes Desktop UI is serving a cached `.system-live.json` (a data-path issue), or whether `vault-live.html`'s `renderBots` function has a separate rendering path issue (a UI issue belonging to senter-wiki). The data contract is verified (69 bots served); the UI rendering path remains under inspection.

^[raw/inbox/2026-09-10.md]

## 2026-09-09 20:05–20:33 follow-up — `scan-topics.py` snapshot schema inconsistencies

The same bridge scan output revealed a deeper issue than the earlier naming display question: the live snapshot schema is inconsistent across scan paths, which breaks consumers expecting uniform bot objects.

Evidence:
- Hermes, 2026-09-09 20:10: **"`scan_bots()` returns profile bots with `model`, but `scan_topics()` creates topic bots without `model`, and `snapshot()` prints assuming all bots have it."** ^[raw/inbox/2026-09-09-from-wiki-want.md]
- Hermes, 2026-09-09 20:11–20:16: the `skills` field is typed differently depending on source — `scan_bots()` uses an integer count, while `scan_topics()` and `scan_vault_agents()` use `[]` lists. ^[raw/inbox/2026-09-09-from-wiki-want.md]
- Hermes, 2026-09-09 20:25: in `scan_vault_agents()` there are duplicate `skills` assignments at lines 227 and 230, leaving the stored value stale. ^[raw/inbox/2026-09-09-from-wiki-want.md]

Implications:
- UI formatters and downstream loops that assume `bot['model']` exists will break for topic-level bots.
- A format string expecting `<3` for `skills` will fail when `skills` is `[]`.
- Even after attempted fixes, a vault bot still rendered as `skills=[]` in `.system-live.json`, indicating the patch had not fully landed.

Contested point: the 2026-09-08 page closed the original `.md` suffix concern as "not a bug, by design." The 2026-09-09 evidence keeps that naming claim, but adds a real schema/merge bug in `snapshot()` that the earlier page did not address.

Open question: Hermes did not confirm whether the `.system-live.json` the UI actually reads is the bridge-served file or a stale local copy.

## Related

- [[topics-wiki/senter/wiki/decisions/2026-09-08-bridge-scan-topics-bot-name-parsing|bridge scan-topics bot name parsing]]
- [[topics-wiki/senter/wiki/concepts/vault-agents-vs-profile-bots|vault agents vs profile bots]]
- [[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge]]
- [[topics-wiki/senter/wiki/queries/verify-apply-paths-and-watchpaths-landed|verify apply paths and WatchPaths landed]]
