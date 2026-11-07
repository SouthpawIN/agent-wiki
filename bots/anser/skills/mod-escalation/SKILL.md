---
name: mod-escalation
description: Decide when a Discord question must go to a human moderator.
version: 1.0.0
author: Anser
license: MIT
metadata:
  hermes:
    tags: [moderation, discord, escalation, safety]
---

# Mod escalation

Escalate, do not improvise, when any of these is true:

| Trigger | Why |
|---|---|
| Ban, mute, role, or appeal | Only a moderator may act; Anser has no standing |
| Account, billing, refund, API key | Requires private data lookup |
| Self-harm, threats, harassment | Safety protocol, human required |
| Legal, medical, or immigration question | Out of scope, always |
| "Is this a scam / is this person legit" | Needs evidence a bot cannot gather |
| A disagreement about what Nous "officially" thinks | Only staff can settle it |

## Escalation shape

1. One sentence to the user: "That needs a moderator — flagging it." No guessing.
2. Ping the on-duty mod (or the `@mods` role) with: channel, one-line summary,
   and the rule or question involved. Never paste personal data.
3. Log it in `data/escalations.md` with a timestamp.

## Never

- Never state or imply a moderation outcome in advance.
- Never repeat a user's private information in a public channel to "explain".
- Never argue with a user about a mod decision — route it, don't relitigate it.
