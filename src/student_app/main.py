"""Coordinate configuration, input, validation, calculations and output."""

import argparse
import logging
import sys
from pathlib import Path

from student_app.config import PROJECT_ROOT, load_settings
from student_app.logger import configure_logging
from student_app.models.student import Student
from student_app.reports.student_report import generate_report
from student_app.services.calculator import calculate_marks
from student_app.storage import load_students
from student_app.utils.validation import validate_name


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Display validated student reports.")
    parser.add_argument("--data", type=Path, default=PROJECT_ROOT / "data" / "student.json")
    parser.add_argument("--name", help="Override the name of a single student.")
    parser.add_argument("--marks", nargs="+", type=float, help="Subject scores to average (0-100).")
    args = parser.parse_args(argv)
    logger = logging.getLogger("student_app")
    try:
        settings = load_settings()
        logger = configure_logging(PROJECT_ROOT / "logs", settings.debug)
        logger.info("Application started")
        students = load_students(args.data, settings.max_students)
        if args.name is not None or args.marks is not None:
            if len(students) != 1:
                raise ValueError("Name/marks overrides require a single student record.")
            student = students[0]
            students = [Student(
                student.id,
                validate_name(args.name) if args.name is not None else student.name,
                student.program, student.semester,
                calculate_marks(args.marks) if args.marks is not None else student.marks,
            )]
        print(f"{settings.app_name}\nDebug: {settings.debug}\nMaximum students: {settings.max_students}\n")
        for student in students:
            print(generate_report(student))
        logger.info("Generated %d student report(s)", len(students))
        return 0
    except (ValueError, OSError) as error:
        # Do not log raw external values or exception details that may contain secrets.
        logger.error("Application could not complete (%s)", type(error).__name__)
        print("Error: check configuration, student data and input values. See README.md.", file=sys.stderr)
        return 1
