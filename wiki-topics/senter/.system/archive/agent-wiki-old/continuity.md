# Continuity — agent-wiki / Senter

Raw understanding, updated 2026-08-29:

- Senter IS the wiki product (three-eyed owl). agent-wiki repo = the Senter codebase; klerik = QA agent profile; senter repo = fleet orchestrator profile. User directive 2026-08-29: merge all three into ONE repo named **Senter**, cleaning up the GitHub org.
- The GOOP vault on this Mac (~/Documents/Projects/Projects) is the working instance; 54 topics, all structured per agent-wiki-spec.
- 2026-08-29 events: turbofit provider fix (commit 4cc6b06, feat/live-refit); senter HP box wiped for Omarchy (absorb verified first), recovery pending user live-USB boot.
- Senter recovery lesson learned: pivot_root to tmpfs mid-install is fragile on a 90%-full disk with a mounted 6.2G ISO — treat live-USB + sshd as the only validated remote-install path on this hardware.
- (Edit this file to correct my understanding; I never overwrite user-edited lines.)
