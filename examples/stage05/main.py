from student import create_student
from report import generate_report

def main():
    student = create_student(input("Student name: "), float(input("Marks (0-100): ")))
    print(generate_report(student))


if __name__ == "__main__":
    main()
