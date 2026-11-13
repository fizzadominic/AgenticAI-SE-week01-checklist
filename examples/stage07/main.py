from models.student import Student

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

def main():
    student = Student("2024001", input("Student name: "), "BS Computer Science", 4,
                      float(input("Marks (0-100): ")))
    print(generate_report(student))


if __name__ == "__main__":
    main()
