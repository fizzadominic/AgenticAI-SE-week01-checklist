"""Format a student record for display."""

from models.student import Student
from services.calculator import calculate_grade


def generate_report(student: Student) -> str:
    return "\n".join([
        "Student Report",
        "--------------",
        f"ID: {student.id}",
        f"Name: {student.name}",
        f"Program: {student.program}",
        f"Semester: {student.semester}",
        f"Marks: {student.marks:g}/100",
        f"Grade: {calculate_grade(student.marks)}",
    ])
