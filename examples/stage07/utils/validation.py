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
