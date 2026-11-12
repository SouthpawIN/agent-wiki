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

## Git contract

Commit and push only `bots/**` prose, only after both gates pass; never touch
`senter_agent/`, `tests/`, `scripts/`, `catalogs/`, or a loop's schedule. A
maintainer that can edit its own validator has no validator.

## Commands

```bash
cd ~/work/agent-wiki
python -m senter_agent . --json | jq '.documents, (.proposals|length)'
python -m senter_agent . --status
python scripts/verify_bots.py .          # bots=9 skills=N loops=N problems=0
PYTHONPATH=.:/opt/data/pylibs /opt/data/.local/bin/pytest -q
# `python -m pytest` fails here: the hermes venv has no pytest. Use the binary.
# this container's venv has no pypdf either; tests need it on the path.
# ~25 min: youtube's assemble tests render 1080p60 x264. Run in the background.
```

## Where the state lives

`.system/` is **gitignored**. Queues, `continuity.md` and `injections.md` exist
only inside the clone that holds them, so a fresh clone (including
`~/.hermes/wiki`) starts with no queue at all and every run there claims nothing
and writes nothing. Work in `~/work/agent-wiki`, then copy `bots/*/.system`
into the other clone after pushing. An empty queue is a missing clone, not an
idle fleet — say so instead of exiting quietly.

## Pitfall — a corrupt clone from an interrupted run

A cron run killed mid-`fetch` leaves loose objects truncated to **0 bytes**. The
symptoms look like data loss: `git status` prints `error: object file ... is
empty`, `git rev-parse HEAD` says `fatal: bad object HEAD`, and the working tree
holds 0-byte copies of whatever was open (FLEET.md, BOT.md, a SKILL.md).

Repair, in this order — nothing is lost if the commit reached origin:

```bash
# 1. delete only zero-byte loose objects (never a blanket `git gc`/reset --hard)
python3 -c "import os;[os.unlink(os.path.join(r,f)) for r,d,fs in os.walk('.git/objects')
            for f in fs if os.path.getsize(os.path.join(r,f))==0]"
rm -f .git/AUTO_MERGE .git/index.lock    # a broken AUTO_MERGE ref breaks checkout
# 2. refetch from origin, then rebuild the tree from HEAD
git fetch --prune origin && git reset --mixed origin/main && git checkout -- .
git status --short   # must be clean before reconciling anything
```

Do this before reading the fleet: reconciling against a 0-byte FLEET.md "fixes"
the index into nonsense. Both clones (`~/work/agent-wiki` and
`~/.hermes/wiki`) share one origin and corrupt together — repair both.

