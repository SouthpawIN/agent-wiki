# Wiki Log — only-device

## [2026-09-12] create | wiki initialized (topic-wiki.py init)
## [2026-09-13] compile | compiled raw/2026-09-12.md + raw/2026-09-13.md → entities/duo.md, concepts/adb-wireless-debugging.md, concepts/boot-from-file.md, decisions/hermes-duo-access-path.md
## [2026-09-14] compile | compiled raw/2026-09-14.md + raw/2026-09-14-from-dispatched-m2s.md → concepts/omarchy-os-control-plane.md; folded recovery-mode resetpassword/dd sub-thread into boot-from-file.md
## [2026-09-15] compile | compiled raw/2026-09-14.md + raw/2026-09-15.md → decisions/omarchy-no-shell-access-path.md; updated concepts/omarchy-os-control-plane.md with 09-15 probe result (open but unresponsive); folded SSH-refused + Chris "sent those two commands" + root-tailscale-ssh attempts
## [2026-09-15] compile | re-compiled raw/2026-09-14.md + raw/2026-09-15.md → enriched decisions/omarchy-no-shell-access-path.md status (still waiting, no shell re-established); authored skill omarchy-no-shell-diagnosis (port-probe → control-plane → access-path procedure)

## [2026-09-15] compile | compiled raw/2026-09-14.md + raw/2026-09-15.md → concepts/mac-no-timeout-command.md (Mac lacks `timeout`, cascaded SSH/TLS probe failures); added cross-references to decisions/omarchy-no-shell-access-path.md and concepts/omarchy-os-control-plane.md
## [2026-09-16] compile | confirmed raw/2026-09-14.md + raw/2026-09-15.md already captured in decisions/omarchy-no-shell-access-path.md + concepts/mac-no-timeout-command.md + concepts/omarchy-os-control-plane.md (all cite both sources); added comparisons/duo-android-vs-omarchy-x86-access.md (Duo ADB/SSH onboarding vs Omarchy SSH-down/control-plane-unreachable access contrast); enriched decisions/omarchy-no-shell-access-path.md with 09-16 heartbeat (still waiting, no shell re-established), bumped updated to 2026-09-16
