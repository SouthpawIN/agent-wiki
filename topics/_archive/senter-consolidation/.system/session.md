
# Session — senter-consolidation — 2026-08-29 (WIPE EXECUTED — box down)

## What happened
- Stopped all senter services (llama-server, turbofit-controller, gateway)
- Built custom ssh-enabled initramfs (root:omarchy-live + Mac key) from Omarchy ISO initramfs
- Pulled airootfs.sfs (7.2G) to Mac, md5 verified (68cd39cb...)
- HTTP server on Mac :8080 serving /arch/ (omarchy-netboot dir)
- kexec'd Omarchy live kernel with archiso_http_srv=http://192.168.1.210:8080/ ip=dhcp copytoram

## CURRENT BLOCKER
- senter did NOT come back on LAN/tailscale after kexec (~40 min down)
- Hypothesis: the "linux-t2" kernel is T2-Mac-specific; this HP workstation's NIC driver is
  missing in that initramfs → no DHCP → no HTTP fetch → live env hung at archiso fetch stage
  (or kernel panic on wrong-hardware kernel)

## RECOVERY OPTIONS
1. Physical power-cycle by Chris → box boots back into INTACT Ubuntu (we never wiped the disk!)
   Then use netboot approach with the CORRECT kernel: Ubuntu's own vmlinuz (kexec new kernel
   = Ubuntu generic) + custom initramfs that does the install, OR omarchy ISO built for x86_64
   generic (the t2 variant was wrong choice — need omarchy-3.8.4 non-t2 ISO or archiso).
2. Check HTTP server log for any fetch from 192.168.1.172 — none so far (only my curl test).

## KEY FACT
- The DISK WAS NOT WIPED YET — old Ubuntu is intact on sda2. kexec failure is recoverable
  with a simple reboot. No data at risk (all absorbed to Mac anyway).
