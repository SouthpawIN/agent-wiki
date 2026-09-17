---
name: venv-rebuild-as-user
description: Fix a root-owned Python venv that the normal user can't traverse (symlink points into /root).
---

# Venv Rebuild as User (root-owned venv)

## When to use
A Python venv fails with "cannot traverse" / import errors for a normal user, and the interpreter symlink points into `/root/.local/share/uv/...` (or another user's home). The venv was created by `root` on a remote host.

## Root cause
A venv created by `root` is unusable by `sovthpaw`: its `python` symlink points back into `/root/.local/share/uv/...`, a path the normal user cannot traverse. Fixing the symlink or `chown`-ing across `/root` is wrong — the **whole venv must be rebuilt as the user**.

## Steps
1. Confirm the tell: run `readlink -f <venv>/bin/python` (or `ls -l`) and check the target lands under `/root`. Also confirm with a simple `python -c "import sys"` failing for the normal user.
2. Recreate the venv as the user: `python3 -m venv <path>` (do NOT use `sudo` / `su` for this).
3. Reinstall dependencies inside the new venv.

## Pitfalls
- **`su -c` quoting breaks the rebuild.** When the venv lives on a remote host you reach via `su`, quoting the `python3 -m venv` one-liner inside `su -c '...'` trips over the shell. Instead: write the rebuild to a script file on the remote machine, then run the script. ^[raw/inbox/2026-09-15.md]
- Don't chase this as a code/cache problem — it mimics `sys.path` prepend confusion and the `execute_code`/`terminal` timeout-wrapper artifact, but the mechanism is filesystem ownership of a symlink, not a stale `.pyc`.
- The diagnosis starts as "wrong ownership" and is confirmed only when the symlink target is observed under `/root`.

## Evidence
- "The venv was created by `root` — its Python symlink points into `/root/.local/share/uv/...` which `sovthpaw` can't traverse. The whole venv needs to be rebuilt as the user." ^[raw/inbox/2026-09-15.md]
- "Quoting issues with `su -c`. Let me do this via a script file on the remote machine instead." ^[raw/inbox/2026-09-15.md]
- "The CLI is working now." ^[raw/inbox/2026-09-15.md]
