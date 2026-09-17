---
title: Git State Drift Recovery
created: 2026-09-10
updated: 2026-09-10
type: decision
tags: [decision, infra, pain, plan]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Git State Drift Recovery

On 2026-09-10 the git repository at `~/Documents/Projects/Projects` **disappeared** — the `.git` directory vanished — and was subsequently restored by Hermes. This state drift is distinct from the original 2026-09-09 discovery that the directory had no git repo at all; here the repo existed, then was lost, then was recovered.

> The git repo is gone somehow. ^[raw/inbox/2026-09-10.md]
> The git repo IS there now — looks like something restored it. ^[raw/inbox/2026-09-10.md]

## Upstream Not Set

The `main` branch has **no upstream set**, which means `git pull` / `git push` cannot track a remote by default.

> There's the update problem! The `main` branch has no upstream set. Let me fix this: ^[raw/inbox/2026-09-10.md]

## Scan-Loop Staleness

A continuous `scan-topics.py --watch 20` loop was running with **old code** (the version that wrote `skills: []` as a list). After the scan-topics.py fix was committed (changing `skills` to integer `0`, adding the `model` field, and fixing `.md` stripping), the watch process must be **restarted** to use the corrected code.

> Process 91303 is running `/Users/sovthpaw/Documents/Projects/Projects/assets/scan-topics.py --watch 20` - this is a WATCH loop that's running continuously and repacking the data every 20 seconds! This watch loop is using the OLD version of the code (with `skills: []`). ^[raw/inbox/2026-09-09.md]
> Restart the watch process with the fixed code. ^[raw/inbox/2026-09-10.md]

## Bot Schema Fix

The scan-topics.py fix changed bot entries so that:
- `skills` is now an integer (`0`) instead of a list (`[]`)
- `model` is included as an empty string (`""`)
- `.md` file extensions are properly stripped from agent/loop names

> The print output shows `BOT ... skills=0` for vault-level bots, but the file was written by `write()` function. ^[raw/inbox/2026-09-09.md]
> Now I can see `"skills": 0` and `"model": ""` in the JSON. The scan fix is working - the file was rewritten with the correct values. ^[raw/inbox/2026-09-10.md]

## sys.path Module Resolution

The Python environment's `sys.path` includes `/Users/sovthpaw/Documents/Projects/Projects/assets` at the top, causing `scan-topics.py` to be treated as a **module** rather than a **script** when imported via `execute_code`. This led to confusion about whether fixes were being applied — the module-cached version was running, not the edited file.

> Wait - the sys.path includes `/Users/sovthpaw/Documents/Projects/Projects/assets` at the top! This means when I import `scan_topics`, it's looking for a module there, not running it as a script! ^[raw/inbox/2026-09-09.md]
> The issue is that my Python environment in execute_code has sys.path that includes `/Users/sovthpaw/Documents/Projects/Projects/assets` at the top, which means when I import or execute code, the `scan-topics.py` file is being treated as a module rather than executed as a script. ^[raw/inbox/2026-09-09.md]

## Remaining Blockers

1. Restart the `--watch 20` process with the fixed scan-topics.py code
2. Set `main` branch upstream to `origin` so `git pull`/`git push` work
3. Commit and push the scan-topics.py schema fix

> Git repo is initialized ✓ · JSON file has correct bot schema ✓ · The code handles the data correctly ✓ ^[raw/inbox/2026-09-10.md]
> Git repo is initialized ✓ — JSON file has correct bot schema ✓ — The code handles the data correctly ✓ ^[raw/inbox/2026-09-10.md]

See also: [[topics-wiki/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics-wiki/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]], [[topics-wiki/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]], [[topics-wiki/beyond-pissed/wiki/entities/agent-wiki|Agent Wiki]]
