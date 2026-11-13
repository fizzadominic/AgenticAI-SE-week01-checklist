import pytest

from student_app.services.calculator import calculate_grade, calculate_marks, calculate_status


@pytest.mark.parametrize("marks, grade", [(85, "A"), (75, "B"), (65, "C"), (55, "D"), (40, "F")])
def test_required_grades(marks, grade):
    assert calculate_grade(marks) == grade


@pytest.mark.parametrize("marks, grade", [(0, "F"), (49.99, "F"), (50, "D"), (59.99, "D"), (60, "C"), (69.99, "C"), (70, "B"), (79.99, "B"), (80, "A"), (100, "A")])
def test_grade_boundaries(marks, grade):
    assert calculate_grade(marks) == grade


def test_average_marks():
    assert calculate_marks([80, 90, 100]) == 90


@pytest.mark.parametrize("values", [[], [101], [-1], [True]])
def test_invalid_subject_marks(values):
    with pytest.raises(ValueError):
        calculate_marks(values)


@pytest.mark.parametrize("marks,status", [(0, "Fail"), (49.99, "Fail"), (50, "Pass"), (100, "Pass")])
def test_student_status(marks, status):
    assert calculate_status(marks) == status


def test_status_rejects_invalid_marks():
    with pytest.raises(ValueError):
        calculate_status(101)
