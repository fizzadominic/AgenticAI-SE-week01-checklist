from utils.validation import validate_name, validate_marks


def create_student(name, marks):
    return {"name": validate_name(name), "marks": validate_marks(marks)}
