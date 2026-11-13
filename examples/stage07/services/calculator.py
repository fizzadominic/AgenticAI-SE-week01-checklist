"""Grade and average calculations; each subject is out of 100."""

from collections.abc import Iterable

from utils.validation import validate_marks


def calculate_grade(marks: float) -> str:
    marks = validate_marks(marks)
    for threshold, grade in ((80, "A"), (70, "B"), (60, "C"), (50, "D")):
        if marks >= threshold:
            return grade
    return "F"


def calculate_marks(subject_marks: Iterable[float]) -> float:
    values = [validate_marks(mark) for mark in subject_marks]
    if not values:
        raise ValueError("At least one subject mark is required.")
    return sum(values) / len(values)
