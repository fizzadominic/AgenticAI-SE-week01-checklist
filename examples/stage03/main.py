"""Validate external values before calculations or reporting."""

import math
from numbers import Real


def validate_name(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name must be a non-empty string.")
    normalized = " ".join(name.split())
    if not any(char.isalpha() for char in normalized):
        raise ValueError("Student name must contain a letter.")
    if not all(char.isalpha() or char in " '-’" for char in normalized):
        raise ValueError("Student name may contain letters, spaces, apostrophes and hyphens.")
    return normalized


def validate_marks(marks: Real) -> float:
    if isinstance(marks, bool) or not isinstance(marks, Real):
        raise ValueError("Marks must be a number between 0 and 100.")
    if not math.isfinite(marks) or not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return float(marks)

"""Grade and average calculations; each subject is out of 100."""

from collections.abc import Iterable




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

def main():
    name = validate_name(input("Student name: "))
    marks = validate_marks(float(input("Marks (0-100): ")))
    print(f"Name: {name}\nMarks: {marks:g}\nGrade: {calculate_grade(marks)}")


if __name__ == "__main__":
    main()
