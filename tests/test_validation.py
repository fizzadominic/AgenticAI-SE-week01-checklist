import pytest

from student_app.utils.validation import validate_marks, validate_name


@pytest.mark.parametrize("marks", [0, 50, 85.5, 100])
def test_valid_marks(marks):
    assert validate_marks(marks) == marks


@pytest.mark.parametrize("marks", [-1, 101, "85", None, True, float("nan"), float("inf"), -float("inf")])
def test_invalid_marks(marks):
    with pytest.raises(ValueError):
        validate_marks(marks)


@pytest.mark.parametrize("name", ["Ali", "Anne-Marie", "O'Neil", "علی"])
def test_valid_names(name):
    assert validate_name(name) == name


def test_normalizes_name():
    assert validate_name("  Ali   Khan ") == "Ali Khan"


@pytest.mark.parametrize("name", ["", "   ", "123", "Ali123", None, "--"])
def test_invalid_names(name):
    with pytest.raises(ValueError):
        validate_name(name)
