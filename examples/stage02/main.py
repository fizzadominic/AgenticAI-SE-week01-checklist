name = input("Student name: ").strip()
if not name or not all(c.isalpha() or c == " " for c in name):
    raise ValueError("Name must contain letters and spaces.")
marks = float(input("Marks (0-100): "))
if not 0 <= marks <= 100:
    raise ValueError("Marks must be between 0 and 100.")
grade = "A" if marks >= 80 else "B" if marks >= 70 else "C" if marks >= 60 else "D" if marks >= 50 else "F"
print(f"Name: {name}\nMarks: {marks:g}\nGrade: {grade}")
