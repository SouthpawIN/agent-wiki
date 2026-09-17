---
title: Open items as of 2026-09-10
created: 2026-09-09
updated: 2026-09-10
type: query
tags:
  - question
confidence: medium
sources:
  - raw/inbox/2026-09-08.md
  - raw/inbox/2026-09-09.md
  - raw/inbox/2026-09-09-from-turbofit.md
  - raw/inbox/2026-09-09-from-youtube.md
  - raw/inbox/2026-09-10.md
---

Open items as of 2026-09-09
- ~~Row dots expand from hovered dot~~ — implemented with `--orbShift` transform; hovered dot stays under cursor. ^[raw/inbox/2026-09-06.md]
- ~~Bot naming convention .md suffix~~ — display names now strip the extension; decision and entity pages updated. ^[raw/inbox/2026-09-08.md]
- ~~Missing `topics/senter-wiki/` folder~~ — created with README.md, index.md, .system/, wiki/. ^[raw/inbox/2026-09-08.md]
- ~~FILE_CAP bypass for `.system-live.json`~~ — `/file` route bypass added for the live snapshot. ^[raw/inbox/2026-09-08.md]
- ~~Updates failing due to no git repo~~ — git initialized in the vault, remote set, `.gitignore` created, first commit made. ^[raw/inbox/2026-09-09.md]
- ~~Orb label rename completion~~ — consolidated into `2026-09-09-orb-rename-completion`; both mkTopic array and downstream refs completed together. ^[raw/inbox/2026-09-09.md]
- Open: bot/session discoverability is answerable from current layout, but Chris may still want more explicit signposting for the BOTS section/corner feed.
- Open: Hermes Desktop packaged build does not expose CDP by default; DOM verification path for preview-pane work remains limited to AX/screenshot approaches.
- Open: footer backlink wording is contested because the remote origin remains `agent-wiki` after the 2026-08-29 Senter consolidation; alignment with `SouthpawIN/Senter` is unfinished.
- ~~Open: local model should not be used for general wiki work; routing to a free cloud model needs confirmation and profile wiring~~ — decided in [[topics/senter-wiki/wiki/decisions/2026-09-09-local-lm-reserved-from-general-wiki-work|2026-09-09 — local LM reserved from general wiki work]]; general wiki work no longer uses local LM. ^[raw/inbox/2026-09-09-from-turbofit.md]

## Open as of 2026-09-10
- **Fix the layout** — Chris: "fix the layout" (repeated 7x, escalated: "I've asked you several times all day today and all day yesterday … It's not take two days on this"). ^[raw/inbox/2026-09-10.md]
- **Fix the update** — git repo was initialized 09-09 but "My updates keep failing." The bot schema fix (09-10) and stale watch process cleanup are part of this. See [[topics/senter-wiki/wiki/concepts/proactive-completion-directive|proactive completion directive]].

See also
[[topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-08|open items 2026-09-08]]
[[topics/senter-wiki/wiki/concepts/model-budget-exhaustion-local-lm|model budget exhaustion]]

^[raw/inbox/2026-09-08.md]
^[raw/inbox/2026-09-09.md]
^[raw/inbox/2026-09-09-from-turbofit.md]
^[raw/inbox/2026-09-09-from-youtube.md]
