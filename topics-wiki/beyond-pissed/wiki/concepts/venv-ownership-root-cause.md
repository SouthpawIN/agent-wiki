---
title: Venv Ownership Root Cause (root-owned venv)
created: 2026-09-15
updated: 2026-09-16
type: concept
tags: [infra, pain]
sources: [raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: medium
---

# Venv Ownership Root Cause (root-owned venv)

A Python virtualenv created by `root` on a remote host breaks for the normal user: its interpreter symlink points back into `/root/.local/share/uv/...`, a path `sovthpaw` cannot traverse, so the venv's Python is unusable and the CLI that depends on it fails.

> I see the problem clearly now. The venv was created by `root` — its Python symlink points into `/root/.local/share/uv/...` which `sovthpaw` can't traverse. The whole venv needs to be rebuilt as the user. ^[raw/inbox/2026-09-15.md]

## Root Cause and Fix

The fix is to rebuild the **entire** venv as the user rather than patching the offending symlink or `chown`-ing across `/root`. Two practical obstacles had to be cleared first:

1. **Ownership, not permissions alone** — the diagnosis started as "wrong ownership" and was confirmed by the symlink target landing inside `/root` (unreadable by `sovthpaw`)^[raw/inbox/2026-09-15.md].
2. **`su -c` quoting** — running the rebuild via `su -c` tripped over shell quoting, so Hermes instead wrote the rebuild to a script file and ran it on the remote machine^[raw/inbox/2026-09-15.md].

After the venv was rebuilt as `sovthpaw`, the CLI reported working:

> The CLI is working now. Let me update my memory with the fix and address the rest of your setup: ^[raw/inbox/2026-09-15.md]

## Completion (2026-09-16)

On 2026-09-16 Chris confirmed the fix was actually carried out on the machine: the O'Marki Hermes venv was rebuilt as `sovthpaw` with Python **3.13**, and `hermes --version` works afterward. ^[raw/inbox/2026-09-16.md]

> FIXED Hermes install on Omarchy: venv was root-owned with Python pointing to `/root/.local/share/uv/...`; rebuilt as sovthpaw with Python 3.13; `hermes --version` works [tool: terminal] ^[raw/inbox/2026-09-16.md]

## Why This Class of Failure Matters

It mimics other Python-environment symptoms in this topic — e.g. `sys.path` prepend confusion and the `execute_code`/`terminal` timeout-wrapper artifact — but the **mechanism is different** (filesystem ownership of a symlink, not a stale `.pyc` or a wrapper message), so it is easy to misdiagnose as a code/cache problem. The tell is a symlink target landing under `/root` (or another user's home). ^[raw/inbox/2026-09-15.md]

See [[topics-wiki/beyond-pissed/wiki/concepts/sys-path-module-confusion|sys.path Module Confusion]] and [[topics-wiki/beyond-pissed/wiki/concepts/execute-code-timeout-behavior|Execute Code Timeout Behavior]] for the sibling, misdiagnosable environment issues, and [[topics-wiki/beyond-pissed/wiki/entities/oh-my-archi|Oh My Archi]] for the home-lab build it belonged to.

See also: [[topics-wiki/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]], [[topics-wiki/beyond-pissed/wiki/decisions/multi-project-order-of-operations|Multi-Project Order of Operations]]
