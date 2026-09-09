---
name: remote-os-install
description: Use when installing an OS on a remote machine over SSH.
---

# Remote-driven OS Install

Class-level playbook for installing an OS on a machine you control only via SSH (plus a human at the physical box for power/boot-menu actions).

## Golden rules (earned the hard way)

1. **Never format the disk the running OS boots from.** `mkfs`/`sgdisk --zap-all` on the mounted root either hangs forever or corrupts the OS mid-write. The wipe can only happen from a live environment (ISO/PXE/USB) where the target disk is unmounted, OR from a chroot install whose target is a *different* disk.
2. **kexec is a gamble, not a plan.** It hangs certain hardware (real case: HP box hung twice despite NIC drivers verified present in the initramfs). If a kexec boot fails once, do NOT retry — switch to a physical boot path (live USB / PXE / Target Disk Mode). A hung kexec box requires a physical power-cycle.
3. **Pre-flight gates before any destructive step**, in this order: (a) machine reachable + SSH works, (b) NIC drivers of the *installer* kernel/initramfs verified present (extract the initramfs cpio and grep for the NIC driver .ko), (c) data absorb/backup verified (md5 spot-checks, absorption log), (d) explicit wipe authorization captured verbatim.
4. **Relayed GO ≠ format authorization.** A GO relayed through another agent or chat is intent, not consent. Get the wipe authorization from the user directly, verbatim, before formatting. Users under time pressure may yell 'GO' — a generic GO is still not a format GO.

## Boot-path decision ladder (prefer top)

1. **Chroot install (no kexec, no reboot needed to start):** download the distro's bootstrap tarball, extract as root, repartition a NON-running disk, pacstrap/debootstrap into it, install bootloader, reboot once. Deterministic, fully scriptable over SSH. This is the default path. If the only target disk is the running root, this path is unavailable — go to 2/3.
2. **Live USB prepared remotely:** flash a standard installer ISO to a USB stick from the controlling machine; human plugs into target, boots it (F9/F12 boot menu), enables sshd (2 commands), then everything else is remote. Use the DISTRO's standard kernel, not vendor forks.
3. **PXE network boot:** boot server on the controller, target boots over ethernet. Works when no stick is available and target firmware exposes Network/PXE boot.
4. **Target Disk Mode (Mac as boot drive):** Mac boots into Recovery → Share Disk over a USB-C *data* cable; target sees it as a drive. Niche fallback.

Non-options to never waste time on: USB-A-to-USB-A cable between two PCs (carries no data), plain USB cable 'into the MacBook' (host-to-host is impossible).

## Staging & gotchas

- **Stage everything on the target's disk before cutting anything**: bootstrap tarball, installer kernel+initramfs, ssh key, config overlay. A tmpfs stage dies at kexec/reboot; a stage on the (later-wiped) disk dies at format — know which.
- **Arch bootstrap tarball is `.tar.zst`** — plain `tar -x` fails with 'gzip: stdin: not in gzip format'. Use `tar --zstd -xf ...` (or bsdtar if present).
- **macOS shell-watcher corrupts non-interactive SSH stdin/stdout** (scp fails 'message too long', base64 pipes mangled). Workarounds that DO work: `ssh host 'bash -s' < localscript.sh`, heredoc'd scripts written via `cat > /tmp/x.sh << 'EOF'`, simple one-line commands. Avoid scp and stdin-piped payloads.
- **kexec must run under sudo** (`Operation not permitted` as plain user even with kexec binary present).
- **Custom initramfs/airootfs edits:** verify the injected ssh key is FULL and correct inside the rebuilt artifact — a truncated authorized_keys key = unreachable machine right when the disk is wiped. Re-read the built file, grep the full key.
- **Inject into live env:** sshd + systemd-networkd enabled via multi-user.target.wants symlinks + a .network file with DHCP, plus `PermitRootLogin prohibit-password`.
- **Disk-size reality:** mkfs.btrfs/ext4 on a 16T+ disk takes minutes; a partition command that shows no progress for 5-10 min may still be working — check `lsblk` for committed changes before declaring it hung, but an in-place-on-root mkfs will *never* finish.
- **Verification over self-report:** an assistant agent's 'blocked on permissions' claims may actually be tool misuse (wrong tar flag ≠ permission problem). Independently run the failing command yourself before accepting a blocker.
- **Keep a kill-and-verify reflex:** if a destructive chain runs against a live root, kill it (`sudo kill`) and verify with `lsblk`/`df` that the disk is unchanged before anything else.

## Orchestration

- When a teammate agent owns the install, the overseer must be able to act: keep an independent SSH channel with sudo, watch `/proc`/`lsblk` directly, and take over when the teammate is queue-jammed or wrong. Don't just relay messages for hours.
- Progress = process evidence (packet counters climbing on direct Tailscale links, new processes, changed lsblk), not prose claims.

See `references/senter-2026-08-session.md` for the concrete incident (kexec hangs, grub recovery via `ls` probing, current state tracking).