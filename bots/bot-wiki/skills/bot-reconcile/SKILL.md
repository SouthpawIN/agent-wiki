---
name: bot-reconcile
description: Reconcile the bot fleet against its own index; claim one queue item.
version: 1.0.0
author: Klerik
license: MIT
metadata:
  hermes:
    tags: [bots, wiki, maintenance, loops]
---

# Bot reconcile

The nightly procedure. Read-only until step 5.

## Procedure

1. **Enumerate** `bots/*/BOT.md`. Parse frontmatter. Build a table of
   slug → status → declared loops → declared skills.
2. **Compare** against `bots/_fleet/FLEET.md`. Any mismatch is an index bug:
   rewrite the index row, never the bot. The bot is ground truth about itself.
3. **Check disk against declarations.** Every `skills/` entry named in BOT.md
   exists; every `loops/*.md` file is named in BOT.md. Orphans get an `## Log`
   line and a queue item, not a silent delete.
4. **Check `status: blocked`** rows have a non-empty `Needs from Chris`. If not,
   demote to `paused` and log once.
5. **Claim one item.** Oldest `[ ]` in any `.system/queue.md`, cross-bot queue
   last. Mark `[~]`. Produce the artifact it names. Mark `[x]` only after
   `python -m senter_agent . --json` and `pytest -q` both pass.
6. **Inject.** Append to `bots/<slug>/.system/injections.md` under `[UNREAD]`:
   one sentence, outcome-first. The human reads this next time they talk to him.

## Stop conditions

- Two consecutive runs claim nothing → write nothing, exit quietly.
- A queue item asks for money, publishing, or a government filing → leave it
  `[ ]`, add `HOLD:` to the reason, mention once in the injection.
- Any test failure → revert your edits, `[!]` the item, report the failing test
  name. A factory that ships a red tree is worse than an idle one.

## Commands

```bash
cd ~/work/agent-wiki
python -m senter_agent . --json | jq '.documents, (.proposals|length)'
python -m senter_agent . --status
pytest -q
```
