"""Run the lab demonstrations and preserve real output in docs/verification.txt."""

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
TRANSCRIPT = []


def run(arguments, expected=0, stdin=None, cwd=ROOT):
    env = dict(os.environ, DEBUG="True", APP_NAME="Student Information System", MAX_STUDENTS="100", API_KEY="")
    result = subprocess.run(
        [sys.executable, *arguments], cwd=cwd, env=env, input=stdin,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    entry = f"$ python {' '.join(arguments)}\n{result.stdout}{result.stderr}Exit code: {result.returncode}\n"
    TRANSCRIPT.append(entry)
    print(entry)
    if result.returncode != expected:
        raise RuntimeError(f"Expected exit code {expected}, got {result.returncode}")
    return result


def main():
    os.chdir(ROOT)
    for stage in range(1, 9):
        result = run([f"examples/stage{stage:02d}/main.py"], stdin="Ali\n85\n")
        assert "Grade: A" in result.stdout
    run(["examples/stage02/main.py"], expected=1, stdin="Ali\nnot-a-number\n")
    run(["-m", "student_app"])
    run(["-m", "student_app", "--name", "Sara Khan", "--marks", "80", "90", "100"])
    run(["-m", "student_app", "--marks", "40"])
    run(["-m", "student_app", "--marks", "-1"], expected=1)
    run(["-m", "student_app", "--name", ""], expected=1)
    run(["-m", "student_app", "--data", "data/missing.json"], expected=1)
    run(["-m", "student_app"], cwd=ROOT.parent)
    target = ROOT / "src/student_app/services/calculator.py"
    original = target.read_bytes()
    try:
        # No specific bug is supplied: make 85 incorrectly produce B instead of A.
        text = original.decode("utf-8")
        assert '(80, "A")' in text
        target.write_text(text.replace('(80, "A")', '(800, "A")'), encoding="utf-8")
        result = run(["-m", "pytest", "-q", "tests/test_calculator.py::test_required_grades"], expected=1)
        assert "1 failed, 4 passed" in result.stdout
    finally:
        target.write_bytes(original)
    run(["-m", "pytest", "-q", "tests/test_calculator.py::test_required_grades"])
    run(["-m", "pytest", "-q"])
    (ROOT / "docs/verification.txt").write_text("\n".join(TRANSCRIPT), encoding="utf-8")


if __name__ == "__main__":
    main()
