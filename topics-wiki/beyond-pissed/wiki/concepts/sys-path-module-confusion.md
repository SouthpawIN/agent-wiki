---
title: sys.path Module Confusion
created: 2026-09-10
updated: 2026-09-10
type: concept
tags: [infra, pain, tool]
sources: [raw/inbox/2026-09-09.md]
confidence: high
---

# sys.path Module Confusion

The Python environment used by Hermes's `execute_code` tool has `/Users/sovthpaw/Documents/Projects/Projects/assets` prepended to `sys.path`. This causes `scan-topics.py` to be **imported as a module** rather than **executed as a script**, which in turn causes Python to load the compiled `pyc` cache instead of the freshly-edited source file.

> Wait - the sys.path includes `/Users/sovthpaw/Documents/Projects/Projects/assets` at the top! This means when I import `scan_topics`, it's looking for a module there, not running it as a script! Let me check if there's a `scan_topics.py` module somewhere else, or if the assets directory has become part of the module path: ^[raw/inbox/2026-09-09.md]
> The issue is that my Python environment in execute_code has sys.path that includes `/Users/sovthpaw/Documents/Projects/Projects/assets` at the top, which means when I import or execute code, the `scan-topics.py` file is being treated as a module rather than executed as a script. ^[raw/inbox/2026-09-09.md]

## Impact

When attempting to verify fixes to `scan-topics.py`, Hermes edited the source file but the `execute_code` tool continued loading the **stale `.pyc` cache**. This produced the illusion that fixes were not being applied — the JSON output continued showing `skills: []` even after the source was changed to `skills: 0`.

> My pycache is being used (but I deleted it) ^[raw/inbox/2026-09-09.md]
> There's something modifying the data between scan and write ^[raw/inbox/2026-09-09.md]
> The file was written but then overwritten ^[raw/inbox/2026-09-09.md]

## Root Cause

The `assets/scan-topics.py --watch 20` process was running in a **separate shell** with the old code in memory. Meanwhile, `execute_code`'s `sys.path` included the `assets/` directory, causing `import scan_topics` to resolve to a cached module rather than re-reading the edited file. The two mechanisms — the watch loop and the module cache — both served stale code.

> Let me run the scan from a different directory to avoid path issues: ^[raw/inbox/2026-09-09.md]

## Mitigation

The fix required two simultaneous actions:
1. **Kill and restart** the `--watch 20` process so it loads the new source
2. **Clear `__pycache__`** and ensure `execute_code` runs the script (not imports it as a module)

See also: [[topics-wiki/beyond-pissed/wiki/concepts/scan-loop-schema-fix|Scan Loop Schema Fix]], [[topics-wiki/beyond-pissed/wiki/decisions/git-state-drift-recovery|Git State Drift Recovery]], [[topics-wiki/beyond-pissed/wiki/entities/center-vault|Center Vault]]
