# Phase 02 learning snapshots

No Stage 01 source was supplied in the checklist. These examples use Ali / 85
and the documented grade cutoffs. The final application is in ../src/student_app.

| Stage | Change |
| --- | --- |
| 01 | One file, fixed student sample |
| 02 | Input, validation, grading, output in one file |
| 03 | Extract validate_name, validate_marks, calculate_grade and main |
| 04 | Separate main.py, validation.py and calculator.py |
| 05 | Add student.py data handling and report.py |
| 06 | Introduce utils/, services/, models/ packages |
| 07 | Introduce the Student class and create an object |
| 08 | Extract student_report.py |
| 09 | Final professional structure in ../src/student_app |

Run `python examples/stage01/main.py`. For stages 02-08, run the corresponding
main.py and enter a name, then marks, when prompted; Ali and 85 should produce A.
Stage 02 is the fragile application: nonnumeric marks raise an unhandled
ValueError. The final application validates inputs, catches errors and logs them.

`python examples/build_stages.py` regenerates the historical examples. They
deliberately retain early design limitations; use the final app for normal work.
