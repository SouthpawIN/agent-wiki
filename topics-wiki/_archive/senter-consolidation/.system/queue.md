# Queue — senter-consolidation

## [SKILLS]
- Merge senter's turbofit skill cluster (8 skills) with Mac's thinner turbofit skill.
- Absorb southpaw-models, local-llm-fleet-management, herm*, agent-hub, omni-va-local-server,
  youtube-playlist-to-acestep-lora, song-catalog skills into vault skill-registry catalog.

## [AGENTS]
- Identify + decide fate of senter's live cron job (executions.db, ticker heartbeats) before wipe.
- Brief A/B/C in session.md ready to launch.

## [LOOPS]
- Verify continuity/stream.jsonl on senter (looks like synthetic fixture data) before ingesting.

## [OPS]
- Install SSH key auth to senter; rotate password (in chat history 2026-08-28).
- Turbofit dirty worktree on senter: commit or stash (plugin.js, plugin_tools.py, sparse-moe ref).
- Free space plan for senter disk (90% full) before Omarchy rebuild — most space is
  evolutionary-training (874G) + Models (8.3T); decide what survives the wipe via backup list.
- Wire Mac→senter gateway auth (Mac Hermes could route aux inference to senter's /main/v1/).

## [EXECUTED 2026-08-28 evening]
- [x] Model switch: Mac Hermes → senter gateway (main/v1, Qwen3.8-27B Q3KXL)
- [x] Dedupe executed: 6 merges, 17 archived (_archive_20260828, 41G), 1 delete, MANIFEST written
- [x] turbofit/hermes-browser-extension/llama.cpp-latest dirty worktrees checkpoint-committed
- [x] idea-wiki absorbed: 51 merged, 7 topics created, 13 concepts + 5 root docs to _global
- [ ] personal.tgz (1.4G Documents+lyrics+Sync) transferring in background → extract to ~/senter-absorb
- [ ] Lyrics journal found at ~/Music/lyrics/journal.md + ~/Music/library/lyrics/journal.md (in transit)
- [ ] Before wipe: verify Downloads/ Pictures/ Desktop/ etc. have nothing unique; then P3

## [P3 WIPE — authorized by Chris "wipe it" + "remote drive it" 2026-08-29]
- [x] Media tarball (15.9G: Desktop/Apollo+brand, Downloads small, Videos yt+screencasts) transferred
      in 15 chunks, md5-verified (df15b051...), extracted to ~/senter-absorb/{Desktop,Downloads,Videos}
- [x] Omarchy 3.8.4 ISO (7.96G) staged on senter at /tmp/omarchy/omarchy.iso
- [x] kexec-tools installed on senter
- NEXT: final pre-wipe checklist → wipe home + data partitions → kexec into Omarchy installer →
  install → fresh Hermes + tailnet
- EXCLUDED deliberately (re-downloadable): DeepSeek-158B gguf (114G), UE5.7.4 (66G), WizardLM-2
  shards (79G), Qwen3.6-27B gguf (16G) — public downloads, not personal data

## [WIPE SCOPE CONFIRMED — Chris 2026-08-29]
- NO dual boot, NO recovery partition, NO preserved OS data. Fresh machine.
- ONLY exception: save Steam login (session/ticket) so Chris can log straight back into
  Armored Core 6 after reinstall. Grab ~/.steam or ~/.local/share/Steam config (login.vdf,
  config.vdf, ssfn files) BEFORE wiping — store in ~/senter-absorb/steam-login/.
- Everything else on the disk gets wiped: Models 8.3T, projects, OS, home.
