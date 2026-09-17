# BRIEF — back-where

## Scope
Chris's Hermes runtime/model/UI/TTS issues on local M1 hardware, plus the verification and recovery behavior he expects from fixes.

## Anti-scope
Generic wiki UI work belongs to weaver/vault-live topics; upstream Hermes code changes belong to teknium PR ledger, not this topic's raw items.

## Lens
Record what Chris actually experienced and decided, not the build process around it.

## Standing preferences
- Model picker choice must persist until real fallback is required.
- UI must return to exact prior state after a regression; small changes must not push layout.
- Every fix must be tested end-to-end in Hermes before declaring done.
- Do not touch files again until the target is rebuilt from the vault's own specs.

## Learned
- Recovery pattern: rebuild from vault specs before touching files during Hermes repair.
- TTS entitlement failures may stem from stale cached JWT after credit top-up; retry with force_fresh=True.
- Interrupted background processes may complete work on disk; verify state before redoing.
- Chris's M1 MacBook 32GB should run the chosen model at Q3 with 262k contacts and D flash 2 given sufficient batch/prefill tuning.
- Interrupted turns may leave a short follow-up request; inspect on-disk state before re-executing Calibri/Bonsai or any next step.
- Token startup race condition: during UI restoration, token reads may occur before the server is ready; treat server readiness as the prerequisite before retrying auth.
- Context compaction handoff pattern recurs across session boundaries (2026-09-08, 2026-09-09); treat latest message after handoff as the only active task.
- Python execute_code runs in an isolated kernel; changes may not propagate to command-line execution.
