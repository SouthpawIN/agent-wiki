---
name: agent-oversight
description: Use when supervising teammate agents doing machine work.
---

# Agent Oversight (Teammate Supervision)

How to supervise another Hermes profile (e.g. `@hermes`) doing hands-on work on machines — installs, provisioning, anything destructive or long-running.

## Workflow

1. **Handoff via message_agent.** Compose the request yourself (never forward the user's words verbatim). Include: target machine + access method, the task, explicit safety rails, and the reporting contract (see below). It's fire-and-forget — the reply arrives as a background-process notification; relay it attributed to the agent.
2. **Set a reporting contract up front.** Demand milestone notes at every step (connected → verified → mutated → done) and instant escalation on blockers. Batched updates leave the user blind for long stretches. If the teammate goes quiet, send a priority bump referencing the user's deadline rather than waiting.
3. **Verify claims independently.** A teammate's self-report is a self-report. When the user asks 'where is it at' or before relaying status that matters, check ground truth yourself (ping the host, check the connection, read the actual state). This caught a 'no install started, machine offline' truth that relayed optimism would have hidden.
4. **Safety gates on destructive ops.** Encode rails in every handoff: (a) explicit user GO before disk formatting/wipes — a relayed 'do it now' is NOT automatically format authorization unless the user said so for the full sequence; (b) verification steps the teammate must pass before mutation (e.g. driver-in-initramfs check before kexec, checksum-verified data absorb before wipe); (c) a short heads-up message immediately before the destructive step.
5. **Take ownership of blockers.** When a blocker is environmental (machine offline, missing creds), don't just relay — run your own reachability probe so you can tell the user exactly what's physically needed and can confirm recovery yourself.

## Reachability triage (remote host unreachable)

Run all three; each tells you something different:
- `ping <host>` — host OS stack up? (0% loss = alive; 100% = powered off or network dead)
- Tailscale status — is the mesh peer seen recently? `tx N rx 0` with growing tx means the peer is powered off (packets dying on the floor); 'direct' connection beats 'relay' for throughput.
- `nc -z -G 5 <ip> 22` — SSH daemon listening?

macOS quirk: the Tailscale app binary is at `/Applications/Tailscale.app/Contents/MacOS/Tailscale` (the bare `tailscale` CLI may crash with a bundleIdentifier fatal error on some installs). Commands: `tailscale status`, `tailscale ping <host>`.

If everything is dark: the fix is physical (power button, PSU, cable, router port) — give the user a concrete at-the-box checklist (power LED? fan? NIC link lights?) instead of retrying software probes.

## Watching for recovery

Poll reachability on a loop rather than asking the user to keep reporting: a background `for` loop pinging every ~25s with a break-on-success, `background=true` + notify. Expect boot + Tailscale reconnect to take several minutes after a power cycle. When it flips online, kill the watcher, verify once more, and re-send the GO to the teammate in the same turn.

## DM delivery reliability (message_agent)

- Delivery is queue-behind-turn: if the teammate is mid-turn, messages can sit ~120s and fail with `target_busy` (exit 1, message NOT delivered). Retry — but don't spam; check the running process and re-send the LATEST consolidated instruction only (stale retries just queue duplicates).
- A teammate being unreachable via DM usually means it's heads-down working, not stalled. Verify with ground-truth probes: network activity (Tailscale `tx N rx M` with BOTH growing = active work; `tx high rx 0` = dead peer), SSH port answering, session duration. Report this distinction to the user instead of speculating.
- Format-GO nuance: a generic relayed 'GO' is NOT format authorization by default — but a user reply that explicitly and verbatim authorizes formatting (e.g. 'FORMAT GO', 'a. wipe it all') relayed verbatim IS sufficient when the user has already been told exactly what would be wiped (14T used, 8.3T Models unrecoverable) and answered anyway. Relay the user's words verbatim for destructive authorization, with the decision context attached.
- Long teammate turn (10-20 min) after a decision request usually means it already received an earlier queued GO and is executing. Confirm via activity probes before concluding it stalled.

## User-communication style (learned the hard way)

- Lead with the concrete status and what's needed from the user, in bold/clear callouts — users under deadline pressure skim.
- Distinguish honestly between 'agent says' and 'I verified'.
- When the user says 'this is the second time and made no progress', stop relaying and investigate directly.

## Deep-probe patterns (direct senter inspection)

When DM to the worker stalls, verify ground truth yourself instead of re-queueing:
- **Read the worker's own logs on this Mac:** every senter step is mirrored to `/tmp/senter_*.log` (prep, nic, data, iso, sha, mount, extract, kern, initrd, overlay). Tail them before asking the worker for status — they show real milestones and exact errors (e.g. `extract_fail`, `gzip: stdin: not in gzip format`).
- **SSH to senter is slow over Tailscale:** expect 60–250s handshake. Always run SSH probes as `background=true` with `notify=true`, `ConnectTimeout=20–30`, `ControlMaster=no`, `ControlPath=none`, long `wait` windows, and `tail` the log rather than polling foreground `timeout=30` calls (they false-timeout). `ping` + `nc -z -G 5 <ip> 22` + `Tailscale status` are fast liveness checks; SSH commands are slow.
- **Bootstrap tarball:** Arch now ships `bootstrap.tar.zst` (zstd), not `.tar.gz`. `tar -xzf` on a `.zst` gives `gzip: stdin: not in gzip format` — use `tar --zstd -xf` under `sudo -n`. `bsdtar` is not installed on stock Ubuntu. `sudo -n tar --zstd` was proven to extract cleanly (creates `/tmp/omarchy-boot/root.x86_64`).
- **Overlay SSH key bug:** two generations of the worker's `ssh-setup.service` wrote truncated/empty `authorized_keys` (observed: `AAAAC3NzaC1lZDI1NTE5AAAAIB` and `echo  >`). Post-kexec SSH would fail and the box would go dark mid-wipe. Fix before kexec: inject the full ed25519 pubkey (`ssh-ed25519 AAAAC3... hermes-mac`) via `sudo -n sh -c 'cat > /tmp/omarchy-boot/overlay/airootfs-ssh/ssh-setup.service'` with a single `ExecStart` that does `systemctl enable --now sshd; mkdir -p /root/.ssh; echo 'FULLKEY' > /root/.ssh/authorized_keys; chmod 600`. Verify with `grep ExecStart` and `cat /tmp/omarchy-boot/overlay/mykey.pub`.
- **Sudo on senter:** `sovthpaw` already has `NOPASSWD:ALL` (present in `/etc/sudoers.d`). Verify with `sudo -n true; echo SUDO_RC=$?` (RC 0 = no password). Do not ask the user to run a `tee /etc/sudoers.d/...` one-liner when probe proves NOPASSWD — just run `sudo -n`.
- **kexec on Ubuntu:** bare `kexec -l` without sudo gives `kexec_file_load failed: Operation not permitted` — expected; run under `sudo -n`. For Plan B (chroot install) the kexec/overlay path is irrelevant — install the key into the chroot's `/root/.ssh` after pacstrap instead.
- **Activity vs stall:** `Tailscale status` `tx N rx M` with both counters climbing (~190k→273k over minutes) + SSH port open = heavy bidirectional activity = active install. `tx high rx 0` = dead peer.

## Plan choice (kexec vs chroot)

The official omarchy-4.0.1 ISO ships ONLY `vmlinuz-linux-t2` / `initramfs-linux-t2.img` — the same T2 fork that hung this HP before. The NIC gate (grep initramfs for `e1000e.ko.zst` + `igb.ko.zst`) can pass on a newer fixed build (observed: kernel 7.1.8-arch1-Watanare-T2-3), but even a passing gate leaves kexec hang risk. For this hardware, the chroot/Arch-bootstrap path (extract `root.x86_64`, repartition sda, `pacstrap` base + linux + omarchy repo, systemd-boot, tailscale + sshd) is deterministic with zero kexec risk; prefer it unless the user explicitly opts into kexec for speed.

## References

- `references/senter-omarchy.md` — session detail: the senter Omarchy install case (machine, rails, watchdog notes, kexec-hang endgame + recovery plan).
- `references/ssh-probe-patterns.md` — copy-paste SSH/tar/sudo probe recipes for senter (slow-Tailscale-safe).

## Hard-won rules for destructive remote installs (apply to ANY machine, not just senter)

1. **Never wipe/repartition the disk the running OS boots from.** An in-place `mkfs` on the mounted root hangs forever; a `sgdisk --zap` on an in-use disk corrupts the running system. Wipe only from a live environment or against an unmounted target.
2. **kexec hang = permanent disqualification.** If a kexec hangs a box once, do not retry after 'fixes' (e.g. verified NIC modules) — the failure mode is in the handoff, not the initramfs. Switch to chroot or physical-media install.
3. **Kill stuck destructive chains immediately and verify** (`kill` → `ps` count 0 → `df`/`lsblk` unchanged), and tell the user plainly what state the disk is in afterward.
4. **Take over directly when the worker's channel is broken** (scp/stdin corruption, jammed DM queue). Run scripts via `ssh host 'bash -s' < local.sh`; avoid scp and stdin heredocs; prove root with `ls -ld /root` (mode/owner only, never secrets).
5. **During an outage, lead with the single physical action the user must take** and keep a continuous break-on-success watchdog running; say plainly that software cannot reach a powered-off machine.
