import json
import logging

import pytest

from student_app.config import Settings, load_settings
from student_app.main import main
from student_app.models.student import Student
from student_app.storage import load_students


@pytest.fixture
def student_file(tmp_path):
    path = tmp_path / "student.json"
    path.write_text(json.dumps({"id": "1", "name": "Ali", "program": "CS", "semester": 1, "marks": 85}), encoding="utf-8")
    return path


def test_successful_report(student_file, capsys):
    assert main(["--data", str(student_file), "--name", "Sara", "--marks", "80", "90"]) == 0
    output = capsys.readouterr().out
    assert "Name: Sara" in output
    assert "Marks: 85/100" in output
    assert "Grade: A" in output
    assert "Maximum students:" in output


@pytest.mark.parametrize("kind", ["missing", "malformed", "invalid_marks", "wrong_schema", "empty", "duplicate"])
def test_bad_data_is_handled(student_file, kind, capsys):
    if kind == "missing":
        student_file.unlink()
    elif kind == "malformed":
        student_file.write_text("{broken", encoding="utf-8")
    else:
        record = json.loads(student_file.read_text())
        if kind == "invalid_marks":
            record["marks"] = -1
        elif kind == "wrong_schema":
            del record["name"]
        elif kind == "empty":
            record = []
        else:
            record = [record, record]
        student_file.write_text(json.dumps(record), encoding="utf-8")
    assert main(["--data", str(student_file)]) == 1
    assert "Error:" in capsys.readouterr().err


def test_student_limit(student_file):
    record = json.loads(student_file.read_text())
    student_file.write_text(json.dumps([record, dict(record, id="2")]))
    with pytest.raises(ValueError, match="MAX_STUDENTS"):
        load_students(student_file, 1)


@pytest.mark.parametrize("semester", [0, -1, True, 1.5])
def test_invalid_semester(semester):
    with pytest.raises(ValueError):
        Student("1", "Ali", "CS", semester, 85)


@pytest.mark.parametrize("key,value", [("DEBUG", "maybe"), ("MAX_STUDENTS", "0"), ("MAX_STUDENTS", "many"), ("APP_NAME", " ")])
def test_invalid_configuration(monkeypatch, key, value):
    monkeypatch.setenv(key, value)
    with pytest.raises(ValueError):
        load_settings()


def test_secret_is_never_displayed(monkeypatch, student_file, capsys):
    secret = "test-only-secret-do-not-display"
    monkeypatch.setenv("API_KEY", secret)
    assert main(["--data", str(student_file)]) == 0
    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert secret not in repr(Settings("App", False, 100, secret))
    logger = logging.getLogger("student_app")
    for handler in logger.handlers:
        handler.flush()
        if isinstance(handler, logging.FileHandler):
            from pathlib import Path
            assert secret not in Path(handler.baseFilename).read_text(encoding="utf-8")
