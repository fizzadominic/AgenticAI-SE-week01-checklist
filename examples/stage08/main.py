from models.student import Student
from student_report import generate_report

def main():
    student = Student("2024001", input("Student name: "), "BS Computer Science", 4,
                      float(input("Marks (0-100): ")))
    print(generate_report(student))


if __name__ == "__main__":
    main()
