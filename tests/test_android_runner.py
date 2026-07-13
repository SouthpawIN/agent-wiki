import importlib.util
from pathlib import Path
import sys

import pytest


path = Path(__file__).parents[1] / "sandbox/goop/android_runner.py"
spec = importlib.util.spec_from_file_location("android_runner", path)
assert spec and spec.loader
runner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = runner
spec.loader.exec_module(runner)


def test_runner_rejects_non_adb():
    with pytest.raises(runner.RunnerError, match="adb argv"):
        runner.run(("sh", "-c", "id"))


def test_runner_rejects_raw_shell_shape():
    with pytest.raises(runner.RunnerError, match="allowlist"):
        runner.run(("adb", "-s", "android:5555", "shell", "id"))


def test_runner_uses_shell_false_and_timeout(monkeypatch):
    seen = {}

    class Result:
        returncode = 0
        stdout = b"PNG"
        stderr = b""

    def fake_run(*args, **kwargs):
        seen["args"] = args
        seen["kwargs"] = kwargs
        return Result()

    monkeypatch.setattr(runner.subprocess, "run", fake_run)
    argv = ("adb", "-s", "android:5555", "exec-out", "screencap", "-p")
    assert runner.run(argv) == b"PNG"
    assert seen["args"] == (argv,)
    assert seen["kwargs"]["shell"] is False
    assert seen["kwargs"]["timeout"] == 15
    assert seen["kwargs"]["capture_output"] is True


def test_runner_converts_timeout(monkeypatch):
    def fake_run(*args, **kwargs):
        raise runner.subprocess.TimeoutExpired(args[0], kwargs["timeout"])

    monkeypatch.setattr(runner.subprocess, "run", fake_run)
    with pytest.raises(runner.RunnerError, match="timed out"):
        runner.run(("adb", "-s", "android:5555", "exec-out", "screencap", "-p"))
