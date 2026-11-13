"""Reproduce learning snapshots; no starter source was supplied in the checklist."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "src/student_app"


def write(stage, filename, content):
    path = ROOT / f"stage{stage:02d}" / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build():
    write(1, "main.py", 'name = "Ali"\nmarks = 85\nprint(f"Name: {name}\\nMarks: {marks}\\nGrade: A")\n')
    write(2, "main.py", '''name = input("Student name: ").strip()
if not name or not all(c.isalpha() or c == " " for c in name):
    raise ValueError("Name must contain letters and spaces.")
marks = float(input("Marks (0-100): "))
if not 0 <= marks <= 100:
    raise ValueError("Marks must be between 0 and 100.")
grade = "A" if marks >= 80 else "B" if marks >= 70 else "C" if marks >= 60 else "D" if marks >= 50 else "F"
print(f"Name: {name}\\nMarks: {marks:g}\\nGrade: {grade}")
''')
    validation = (SOURCE / "utils/validation.py").read_text(encoding="utf-8")
    calculator = (SOURCE / "services/calculator.py").read_text(encoding="utf-8").replace("student_app.utils.validation", "validation")
    function_main = '''def main():
    name = validate_name(input("Student name: "))
    marks = validate_marks(float(input("Marks (0-100): ")))
    print(f"Name: {name}\\nMarks: {marks:g}\\nGrade: {calculate_grade(marks)}")


if __name__ == "__main__":
    main()
'''
    write(3, "main.py", validation + "\n" + calculator.replace("from validation import validate_marks", "") + "\n" + function_main)
    write(4, "validation.py", validation)
    write(4, "calculator.py", calculator)
    write(4, "main.py", "from validation import validate_name, validate_marks\nfrom calculator import calculate_grade\n\n" + function_main)
    student_functions = '''from validation import validate_name, validate_marks


def create_student(name, marks):
    return {"name": validate_name(name), "marks": validate_marks(marks)}
'''
    report_function = '''from calculator import calculate_grade


def generate_report(student):
    return f"Name: {student['name']}\\nMarks: {student['marks']:g}\\nGrade: {calculate_grade(student['marks'])}"
'''
    data_main = '''def main():
    student = create_student(input("Student name: "), float(input("Marks (0-100): ")))
    print(generate_report(student))


if __name__ == "__main__":
    main()
'''
    for filename, content in {"validation.py": validation, "calculator.py": calculator, "student.py": student_functions, "report.py": report_function, "main.py": "from student import create_student\nfrom report import generate_report\n\n" + data_main}.items():
        write(5, filename, content)
    for stage in (6, 7, 8):
        for package in ("utils", "services", "models"):
            write(stage, f"{package}/__init__.py", '"""Learning snapshot package."""\n')
        write(stage, "utils/validation.py", validation)
        write(stage, "services/calculator.py", calculator.replace("from validation", "from utils.validation"))
        if stage == 6:
            write(stage, "models/student.py", student_functions.replace("from validation", "from utils.validation"))
            write(stage, "report.py", report_function.replace("from calculator", "from services.calculator"))
            write(stage, "main.py", "from models.student import create_student\nfrom report import generate_report\n\n" + data_main)
        else:
            write(stage, "models/student.py", (SOURCE / "models/student.py").read_text(encoding="utf-8").replace("student_app.utils.validation", "utils.validation"))
            class_main = '''def main():
    student = Student("2024001", input("Student name: "), "BS Computer Science", 4,
                      float(input("Marks (0-100): ")))
    print(generate_report(student))


if __name__ == "__main__":
    main()
'''
            report = (SOURCE / "reports/student_report.py").read_text(encoding="utf-8").replace("student_app.models", "models").replace("student_app.services", "services")
            if stage == 7:
                write(stage, "main.py", "from models.student import Student\n\n" + report + "\n" + class_main)
            else:
                write(stage, "student_report.py", report)
                write(stage, "main.py", "from models.student import Student\nfrom student_report import generate_report\n\n" + class_main)


if __name__ == "__main__":
    build()
