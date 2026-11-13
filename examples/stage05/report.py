from calculator import calculate_grade


def generate_report(student):
    return f"Name: {student['name']}\nMarks: {student['marks']:g}\nGrade: {calculate_grade(student['marks'])}"
