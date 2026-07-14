#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
HOME_DIR=${HERMES_HOME:-"$ROOT/sandbox/hermes-home"}
mkdir -p "$HOME_DIR"
export HERMES_HOME="$HOME_DIR"
export SENTER_GOOP_ROOT="${SENTER_GOOP_ROOT:-$ROOT/sandbox/goop}"
export SENTER_GOOP_PROFILE="${SENTER_GOOP_PROFILE:-$SENTER_GOOP_ROOT/profiles/base}"

if ! command -v bun >/dev/null 2>&1; then
  echo "bun is required to run the Home TUI" >&2
  exit 127
fi

cd "$ROOT/sandbox/herm-sovth"
exec bun run src/index.tsx "$@"
