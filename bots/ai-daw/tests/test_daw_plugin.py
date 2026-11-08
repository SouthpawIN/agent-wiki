"""The AI DAW plugin, exercised end to end with the dry-run engine."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

PLUGIN = Path(__file__).parents[1] / "plugin"
sys.path.insert(0, str(PLUGIN))

from daw.core import LAYER_ORDER, Project, measure_loudness  # noqa: E402
from daw.adapters import get_engine  # noqa: E402
from daw.adapters.dryrun import DryRunEngine  # noqa: E402

pytestmark = pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg required")


@pytest.fixture()
def project(tmp_path: Path) -> Project:
    return Project.create(tmp_path / "projects", "demo", bpm=120, key="A minor",
                          sections=[{"name": "intro", "bars": 2}, {"name": "main", "bars": 2}])


def test_create_writes_a_plain_manifest(project: Project) -> None:
    manifest = json.loads((project.root / "project.json").read_text())
    assert manifest["id"] == "demo" and manifest["bpm"] == 120
    assert manifest["tracks"] == []
    assert project.duration_seconds() == pytest.approx(8.0), "4 bars at 120 bpm"


def test_create_refuses_to_clobber(tmp_path: Path) -> None:
    Project.create(tmp_path / "p", "demo")
    with pytest.raises(ValueError, match="already exists"):
        Project.create(tmp_path / "p", "demo")


def test_unknown_engine_fails_with_a_hint(project: Project) -> None:
    with pytest.raises(KeyError, match="known:"):
        get_engine("suno-magic")


def test_generate_layer_writes_a_real_stem(project: Project) -> None:
    result = project.generate_layer(instrument="drums", prompt="tight four-on-the-floor")
    assert result["ok"] and not result["reused"]
    stem = project.root / result["path"]
    assert stem.exists() and stem.stat().st_size > 1000

    manifest = json.loads((project.root / "project.json").read_text())
    track = manifest["tracks"][0]
    assert track["instrument"] == "drums" and track["version"] == 1
    assert track["engine"] == "dryrun" and track["files"] == [result["path"]]


def test_generation_is_idempotent_on_the_same_signature(project: Project) -> None:
    first = project.generate_layer(instrument="bass", prompt="warm sub", seed=7)
    second = project.generate_layer(instrument="bass", prompt="warm sub", seed=7)
    assert second["reused"] is True
    assert second["path"] == first["path"]
    assert len(json.loads((project.root / "project.json").read_text())["tracks"]) == 1


def test_a_changed_prompt_makes_a_new_version_and_keeps_the_keeper(project: Project) -> None:
    first = project.generate_layer(instrument="lead", prompt="first idea", seed=3)
    second = project.generate_layer(instrument="lead", prompt="second idea", seed=3)
    assert second["reused"] is False and second["version"] == 2
    assert (project.root / first["path"]).exists(), "alternates are never overwritten"
    assert (project.root / second["path"]).exists()


def test_engine_failure_surfaces_as_ok_false(project: Project) -> None:
    class Dead:
        name = "dead"
        model = "dead-1"
        install_hint = "start the server"

        def capabilities(self):  # pragma: no cover - unused here
            return None

        def health(self) -> bool:
            return False

        def generate(self, request):  # pragma: no cover - health gate fires first
            raise AssertionError("must not be called")

    result = project.generate_layer(instrument="drums", prompt="x", engine="dead",
                                    engines={"dead": Dead()})
    assert result["ok"] is False
    assert result["hint"] == "start the server"


def test_set_track_updates_gain_and_mute(project: Project) -> None:
    project.generate_layer(instrument="drums", prompt="beat")
    assert project.set_track("drums", gain_db=-3.0, muted=True)["ok"]
    assert project.set_track("nope", gain_db=0)["ok"] is False
    status = project.status()
    drums = next(t for t in status["tracks"] if t["id"] == "drums")
    assert drums["gain_db"] == -3.0 and drums["muted"] is True


def test_reference_mix_is_built_from_existing_layers(project: Project) -> None:
    assert project.reference_mix() is None, "nothing generated yet"
    project.generate_layer(instrument="drums", prompt="beat")
    project.generate_layer(instrument="bass", prompt="sub")
    ref = project.reference_mix()
    assert ref and Path(ref).exists()
    assert Path(ref).stat().st_size > 0


def test_stems_are_aligned_to_the_project_duration(project: Project, tmp_path: Path) -> None:
    for instrument in ("drums", "bass"):
        project.generate_layer(instrument=instrument, prompt=f"{instrument} take")
    out = tmp_path / "stems"
    result = project.render_stems(out)
    assert result["ok"] and len(result["stems"]) == 2
    for stem in result["stems"]:
        info = measure_duration(stem)
        assert info == pytest.approx(project.duration_seconds(), abs=0.25)


def test_mix_reports_loudness_and_flags_a_hot_peak(project: Project, tmp_path: Path) -> None:
    for instrument in ("drums", "bass", "harmony"):
        project.generate_layer(instrument=instrument, prompt=f"{instrument} take")
    result = project.render_mix(tmp_path / "mix.wav")
    assert result["ok"], result
    assert Path(result["mix"]).exists()
    assert result["tracks"] == ["drums", "bass", "harmony"]
    loudness = measure_loudness(Path(result["mix"]))
    assert loudness["integrated_lufs"] is not None
    assert loudness["true_peak_db"] is None or loudness["true_peak_db"] <= -1.0


def test_mix_of_nothing_is_a_reported_failure(project: Project, tmp_path: Path) -> None:
    result = project.render_mix(tmp_path / "mix.wav")
    assert result["ok"] is False and result["error"] == "nothing to mix"


def test_status_names_the_missing_layers(project: Project) -> None:
    project.generate_layer(instrument="drums", prompt="beat")
    status = project.status()
    assert status["missing_layers"] == [name for name in LAYER_ORDER if name != "drums"]


def test_dryrun_engine_declares_local_and_free() -> None:
    caps = DryRunEngine().capabilities()
    assert caps.local is True and caps.stems is True and caps.license == "MIT"


def measure_duration(path: str | Path) -> float:
    import subprocess
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return float(out.stdout.strip())
