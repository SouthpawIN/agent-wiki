# Remote absorption over SSH (no sshpass, macOS client)

Techniques validated 2026-08-28 absorbing the `senter` Linux workstation (see vault topic
`senter-consolidation`). Use when the user asks you to survey/pull/consolidate data from
another machine they own over SSH.

## Consent gate

Sharing a password in chat puts it in permanent history — tell the user that explicitly and
offer key-based auth as the better option; proceed with whatever they choose. Never type a
password into a GUI auth dialog. After the task, queue "rotate password + install key auth"
as a follow-up item.

## Password SSH without sshpass (pty pattern)

`sshpass` is typically absent on macOS. A pty fork that watches for the password prompt works:

```python
import pty, os, select, time

def ssh_run(cmd, password="...", host="user@host", timeout=60):
    pid, fd = pty.fork()
    if pid == 0:
        os.execvp("ssh", ["ssh", "-o", "StrictHostKeyChecking=no", host, cmd])
    buf = b""; sent = False; start = time.time()
    while time.time() - start < timeout:
        r, _, _ = select.select([fd], [], [], 0.5)
        if r:
            try: data = os.read(fd, 4096)
            except OSError: break
            if not data: break
            buf += data
            if not sent and b"password:" in buf.lower():
                os.write(fd, (password + "\n").encode()); sent = True; buf = b""
    os.close(fd); os.waitpid(pid, 0)
    return buf.decode(errors="replace")
```

Caveat: if the remote shell prints an interactive banner (motd, watchers), it appears in the
returned buffer before command output — strip or ignore it. Host keys: pre-seed with
`ssh-keyscan -T 5 <host> >> ~/.ssh/known_hosts` (create ~/.ssh first, chmod 700) or pass
`-o StrictHostKeyChecking=no`.

## File transfer: scp breaks, base64-over-ssh works

**scp/`ssh cat > file` with `-o BatchMode` fails** when the remote shell prints any banner —
scp dies with `Received message too long <garbage>` because the banner corrupts the protocol
stream. Two fixes, in order of preference:

1. Fix the remote shell (quiet banner) — not always possible.
2. **Stream base64 through the same pty ssh channel** and filter to base64 lines:

```python
# remote: base64 /tmp/payload.tgz  → local: strip non-b64 lines → b64decode
lines = [l.strip() for l in text.splitlines()
         if re.fullmatch(r"[A-Za-z0-9+/=]+", l.strip()) and len(l.strip()) > 8]
blob = "".join(lines)
data = base64.b64decode(blob + "=" * (-len(blob) % 4))
```

This survived a multi-line "Terminal Chat watcher" banner on the remote and moved a 33 MB
tarball intact. For multi-GB payloads, don't base64 through a pty — set up key auth first,
then use rsync/scp normally.

## Remote survey recipe (big-disk machines)

- `du` over a 14 TB home takes many minutes — run it **async on the remote**
  (`nohup bash -c 'du -sm ~/*/ | sort -rn > /tmp/out.txt; echo DONE >> /tmp/out.txt' &`)
  and poll later; don't block the SSH call.
- Survey order: host/OS/disk → `~/.hermes` inventory + subdir sizes → memories + skills list
  → git repos (`find ~ -maxdepth 3 -name .git -type d`) → non-git dirs (scratch/dupes) →
  per-repo sizes → running processes (`ps aux | grep -iE 'hermes|llama'`) → config heads.
- Payload bundling: `tar czf /tmp/core.tgz -C ~/.hermes memories skills cron config.yaml …`
  (exclude caches/logs), then stream-pull.

## Absorption etiquette

- Verify the data before ingesting (one session found `continuity/stream.jsonl` full of
  synthetic fixture rows).
- Note dirty git worktrees (`git status -s`) — they hold uncommitted work that must be
  committed/stashed before any destructive phase on the remote.
- Write findings into the vault topic's README (the survey IS the absorption artifact);
  pull binary payloads into a scratch dir (`~/<host>-absorb/`) with an ABSORPTION-LOG.md.
