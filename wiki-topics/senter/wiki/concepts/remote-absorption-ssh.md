---
title: Remote absorption over SSH (senter Linux workstation)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [tool, infra, skill]
sources: [raw/sources/knowledge/ref-remote-absorption-ssh.md]
confidence: medium
---

# Remote absorption over SSH (senter Linux workstation)

Techniques validated **2026-08-28** while absorbing the **`senter` Linux workstation** — a machine of Chris's named senter, with a ~14 TB home, its own `~/.hermes` (memories, skills, cron, config), git repos and running hermes/llama processes — into the vault topic `senter-consolidation`. The reference doc is a skill reference for "survey/pull/consolidate data from another machine the user owns over SSH." ^[raw/sources/knowledge/ref-remote-absorption-ssh.md]

## Consent gate
A password shared in chat lands in permanent history — say so, offer key-based auth, proceed with whatever Chris chooses. Never type a password into a GUI auth dialog. Afterwards queue "rotate password + install key auth."

## Password SSH without sshpass (macOS client)
`pty.fork()` + `os.execvp("ssh", ["ssh","-o","StrictHostKeyChecking=no", host, cmd])`, watch the fd for `password:` and write it once. Interactive banners (motd, watchers) precede command output — strip them. Pre-seed host keys with `ssh-keyscan -T 5 <host> >> ~/.ssh/known_hosts`.

## File transfer: scp breaks, base64-over-ssh works
`scp`/`ssh cat > file` with `-o BatchMode` die with `Received message too long <garbage>` when the remote shell prints a banner. Fix 1: quiet the remote shell. Fix 2: stream `base64 /tmp/payload.tgz` through the same pty channel, keep only lines matching `[A-Za-z0-9+/=]+` longer than 8 chars, pad and decode. This survived a multi-line "Terminal Chat watcher" banner and moved a 33 MB tarball intact. Multi-GB → set up key auth then rsync/scp.

## Remote survey recipe
- `du` over 14 TB takes minutes → run async on the remote with `nohup … > /tmp/out.txt; echo DONE` and poll.
- Order: host/OS/disk → `~/.hermes` inventory + sizes → memories + skills → git repos (`find ~ -maxdepth 3 -name .git`) → non-git dirs → per-repo sizes → processes (`ps aux | grep -iE 'hermes|llama'`) → config heads.
- Bundle: `tar czf /tmp/core.tgz -C ~/.hermes memories skills cron config.yaml …` (exclude caches/logs), stream-pull.

## Absorption etiquette
Verify data before ingesting (one `continuity/stream.jsonl` was full of synthetic fixture rows — the "no dummy data" instinct, see [[wiki-topics/senter/wiki/concepts/live-data-contract|live-data contract]]). Note dirty worktrees (`git status -s`) before any destructive phase. Write findings into the topic README ("the survey IS the absorption artifact"); binary payloads to `~/<host>-absorb/` with an `ABSORPTION-LOG.md`. Same archive-never-delete spirit as [[wiki-topics/senter/wiki/entities/paladin|paladin]]'s structural rules; timeline placement in [[wiki-topics/senter/wiki/queries/senter-timeline|Senter timeline]].
