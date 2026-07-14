#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$root"

printf '%s\n' '== Senter Python ==' 
PYTHONPATH=. pytest -q tests/test_senter_agent.py tests/test_factories.py tests/test_gepa.py tests/test_runtime.py tests/test_sts.py tests/test_surfaces.py tests/test_whole_flow.py tests/test_android_bridge.py tests/test_android_runner.py
PYTHONPATH=. python3 scripts/verify_system.py
python3 sandbox/goop/validate_whole_flow.py sandbox/goop
python3 sandbox/goop/validate_android_surface.py sandbox/hermes-android/ANDROID_SURFACE.json
python3 sandbox/goop/validate_android_bridge.py sandbox/hermes-android/ANDROID_BRIDGE.json

echo '== Herm TUI =='
cd "$root/sandbox/herm-sovth"
bunx tsc --noEmit
bun test test/sidebar.test.tsx
bun run build

echo '== Android live target =='
cd "$root"
if adb devices | awk 'NR > 1 && $2 == "device" { found=1 } END { exit !found }'; then
  serial=$(adb devices | awk 'NR > 1 && $2 == "device" { print $1; exit }')
  python3 sandbox/goop/smoke_android_bridge.py "$serial"
  adb -s "$serial" exec-out screencap -p >/tmp/senter-verify-all.png
  file /tmp/senter-verify-all.png
else
  echo 'No online Android target; contracts above remain the available verification.'
fi

git diff --check
echo '== COMPLETE =='
