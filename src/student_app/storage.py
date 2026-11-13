"""Read JSON student records; keep disk access outside application flow."""

import json
from pathlib import Path

from student_app.models.student import Student


def load_students(path: Path, max_students: int) -> list[Student]:
    with path.open(encoding="utf-8") as stream:
        data = json.load(stream)
    records = data if isinstance(data, list) else [data]
    if not records:
        raise ValueError("Student data must contain at least one record.")
    if len(records) > max_students:
        raise ValueError("Student count exceeds MAX_STUDENTS.")
    required = {"id", "name", "program", "semester", "marks"}
    students = []
    for record in records:
        if not isinstance(record, dict) or set(record) != required:
            raise ValueError("Each student must have id, name, program, semester and marks.")
        students.append(Student(**record))
    if len({student.id for student in students}) != len(students):
        raise ValueError("Student IDs must be unique.")
    return students
