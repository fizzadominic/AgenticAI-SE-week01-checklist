from validation import validate_name, validate_marks
from calculator import calculate_grade

def main():
    name = validate_name(input("Student name: "))
    marks = validate_marks(float(input("Marks (0-100): ")))
    print(f"Name: {name}\nMarks: {marks:g}\nGrade: {calculate_grade(marks)}")


if __name__ == "__main__":
    main()
