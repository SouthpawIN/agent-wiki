---
title: "/hotkeys Slash Command"
created: 2026-09-15
updated: 2026-09-15
type: idea
tags: [idea, tool, plan, ui]
sources: ["raw/inbox/2026-09-15.md"]
confidence: medium
---

# /hotkeys Slash Command

On `2026-09-15 02:17`, Chris requested a new Hermes-Agent feature: a `/hotkeys` slash command that displays — and, going forward, edits — the combined set of Hermes-Agent and system hotkeys.^[raw/inbox/2026-09-15.md]

## The request
Chris's words:

> "I want you to create a simple slash command for Hermes-Agent like /hotkeys that will show both the Hermes Agent and system hotkeys. ( want this to be platform agnostic, as I plan for you to share this to my github for my other system that has a different operating system to test, so they can't be hardcoded, they have to scan the system on each /hotkeys call. Keep the door open to be able to adjust the hotkeys from here as well, so it should show the hotkeys in chat with editable fields and toggles if necessary"
> — 2026-09-15 02:17 ^[raw/inbox/2026-09-15.md]

## Requirements as stated
- **Display** both the Hermes-Agent hotkeys and the host-system hotkeys in one view.
- **Platform-agnostic / no hardcoding** — the command must scan the host OS at each call, because Chris plans to share the code to his GitHub and test it on a different operating system.^[raw/inbox/2026-09-15.md]
- **Editable in-chat** — leave the door open to adjust hotkeys from within the conversation: show the hotkeys with editable fields and toggles.^[raw/inbox/2026-09-15.md]

## Status
- Requested on `2026-09-15`; not yet built. It is a Hermes-Agent product feature (not a wiki/vault concern), so it should be routed to the Hermes builder to implement. See also the `/hotkeys` bot pitch in the action feed.
- Related to the broader pattern of live-editable settings in chat (cf. the "adjust the hotkeys from here" intent).

## Related
- [[topics/hermes-agent/wiki/entities/session-20260915-262k-81tok|262K / 81.2 tok/s Milestone — 2026-09-15]]
- [[topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]]
- [[topics/hermes-agent/wiki/decisions/131k-on-32gb-feasibility-decision-2026-09-07|131K on 32GB Feasibility Decision — 2026-09-07]]
