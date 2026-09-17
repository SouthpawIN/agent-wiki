---
title: Scan Loop Schema Fix
created: 2026-09-10
updated: 2026-09-10
type: concept
tags: [infra, pain, tool, plan]
sources: [raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Scan Loop Schema Fix

The `scan-topics.py` script had a bug in its bot schema: it wrote `skills` as an empty list `[]` instead of an integer `0`, omitted the `model` field entirely, and improperly handled `.md` file extensions on agent/loop names. This caused the `/file` route and `vault-live.html` BOTS view to render incorrectly because the consuming code expected `skills` to be an integer and `model` to be present.

> The scan has a bug - it expects `'model'` in bot entries but some bots don't have that field. I need to check the scan_topics function to fix this: ^[raw/inbox/2026-09-09.md]
> Now I also need to fix the `scan_vault_agents` function which uses `md.name.split(".md")[0]` - this should work but let me also check the loops scan for the same issue: ^[raw/inbox/2026-09-09.md]
> But the `scan_loops()` function uses `md.stem` directly. Let me also check the `scan_vault_agents` function: ^[raw/inbox/2026-09-09.md]

## Fix Applied

The fix changed bot entries from:
```json
{"name": "bot-name", "skills": [], "model": null}
```
to:
```json
{"name": "bot-name", "skills": 0, "model": ""}
```

And corrected the `.md` stripping in both `scan_vault_agents` (was using `split('.md')[0]`, which fails on double extensions like `.md.proposed`) and `scan_loops` (was using `md.stem` directly, which also fails on `.md.proposed` files).

## Verification

After the fix, the JSON was verified directly:
> Now I can see `"skills": 0` and `"model": ""` in the JSON. The scan fix is working - the file was rewritten with the correct values. ^[raw/inbox/2026-09-10.md]
> The print output shows `BOT ... skills=0` for vault-level bots. ^[raw/inbox/2026-09-09.md]

## Watch Loop Must Restart

Because `scan-topics.py --watch 20` (process 91303) was running the **old** code with `skills: []`, it continued overwriting the correctly-fixed JSON every 20 seconds until the watch process is restarted with the updated code.

> There it is! Process 91303 is running `/Users/sovthpaw/Documents/Projects/Projects/assets/scan-topics.py --watch 20` - this is a WATCH loop that's running continuously and repacking the data every 20 seconds! This watch loop is using the OLD version of the code (with `skills: []`). ^[raw/inbox/2026-09-09.md]
> Restart the watch process with the fixed code. ^[raw/inbox/2026-09-10.md]

## Commit Status

The fix was committed to git on 2026-09-10:
> Good - there's a commit from me about fixing the bot schema. ^[raw/inbox/2026-09-10.md]

See also: [[topics/beyond-pissed/wiki/decisions/git-state-drift-recovery|Git State Drift Recovery]], [[topics/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]], [[topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]]
