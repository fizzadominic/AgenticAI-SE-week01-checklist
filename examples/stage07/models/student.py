"""Validated student record."""

from dataclasses import dataclass

from utils.validation import validate_marks, validate_name


@dataclass(frozen=True)
class Student:
    id: str
    name: str
    program: str
    semester: int
    marks: float

    def __post_init__(self):
        for label, value in (("ID", self.id), ("Program", self.program)):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} must be a non-empty string.")
        if type(self.semester) is not int or self.semester < 1:
            raise ValueError("Semester must be a positive integer.")
        object.__setattr__(self, "name", validate_name(self.name))
        object.__setattr__(self, "marks", validate_marks(self.marks))
