# Week 01: Student Information System

Validated student records, average marks, letter grades, text reports, environment
configuration, JSON input, logging, automated tests, and a Git workflow exercise.

## Setup (Windows PowerShell)

Run these commands from `week01/student_project`:

```powershell
python --version
python -m pip --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e . --no-build-isolation --no-deps
Copy-Item .env.example .env
$env:DEBUG = "True"
python -m student_app
python -m student_app --name "Sara Khan" --marks 80 90 100
python -m pytest -q
```

The prepared project already has `.venv` and a local `.env`. Do not overwrite local
configuration when reusing it. If activation is restricted, use
`.\.venv\Scripts\python.exe` instead of `python`; activation only changes which
interpreter the shell selects. No machine-wide policy change is necessary.

On Linux/macOS use `source .venv/bin/activate`. After installing, the command
`student-app` also runs the app. The default data and `.env` paths resolve from the
project root even when launched from a different working directory.

## Behavior and assumptions

Default data is the checklist's example: Ali, ID 2024001, BS Computer Science,
semester 4, marks 85. The application prints configuration (excluding API_KEY)
followed by a student report showing grade A.

The checklist supplies example grades but omits exact cutoffs. This implementation
uses A >= 80, B >= 70, C >= 60, D >= 50, F < 50. Student status uses a passing
threshold of 50. Subject marks are equally weighted and must each be finite numbers
between 0 and 100 inclusive. Their arithmetic mean is the student's overall mark.

```powershell
python -m student_app --marks -1
python -m student_app --name ""
python -m student_app --data data/missing.json
```

These return exit code 1 with a concise error and log entry. Invalid CLI syntax
returns argparse's exit code 2. JSON may contain one student object or a nonempty
list of student objects. Each needs `id`, `name`, `program`, `semester`, and `marks`.
IDs must be unique, semester a positive integer, and names must contain letters
with optional spaces, apostrophes, or hyphens. Lists must respect MAX_STUDENTS.
`--name` and `--marks` overrides apply only to a single record.

## Configuration and logging

`.env.example` documents APP_NAME, DEBUG, MAX_STUDENTS, and API_KEY. Existing process
environment variables take priority over `.env`. DEBUG accepts True/False or 1/0;
MAX_STUDENTS must be positive. The setup command sets DEBUG for the current shell
because this workstation has a pre-existing `DEBUG=release`, which is not a boolean
application setting. API_KEY is loaded but never printed or used: this
assignment needs no API service or real credential. The local value is blank.

Startup, successful report events, and errors are written to stderr and
`logs/app.log`. Logs omit student records, configuration values, and raw exception
messages. `.env`, virtual environments, caches, bytecode, and logs are ignored by Git.
`requests` is installed because the assignment requires it; the app runs offline.

## Structure

```text
student_project/
  src/student_app/
    __init__.py, __main__.py, main.py, config.py, logger.py, storage.py
    models/     (__init__.py, student.py)
    services/   (__init__.py, calculator.py)
    utils/      (__init__.py, validation.py)
    reports/    (__init__.py, student_report.py)
  tests/
  data/student.json
  examples/                 # Executable earlier refactoring stages
  docs/concepts.md          # Phase 01 study notes
  docs/verification.md      # Executed checks and remaining submission tasks
  .env.example, .gitignore, pyproject.toml, requirements.txt
```

`main.py` coordinates the flow; storage reads data; the Student class enforces
record invariants; validation checks values; services calculate results; reports
format output; logger and config own their respective setup. Tests cover required
grades, boundaries, invalid input, configuration, JSON errors, limits, and secret
redaction. See `examples/README.md` for the staged refactoring exercises.

Run `python verify_assignment.py` to repeat the lab demonstrations and save their
output to `docs/verification.txt`. This intentionally changes the A cutoff to 800,
observes the required failing grade test, restores the original calculator in a
finally block, and reruns passing tests. Run it while no other process is using or
editing the calculator. The normal test suite never changes application source.

## GitHub handoff

GitHub creation and pushing are being handled by the student. Create an empty
repository named `student-project`, select the required visibility, then run:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/student-project.git
git remote -v
git push -u origin main
```

Open the repository on GitHub and verify the source, tests, README and requirements
are visible, while `.env`, `.venv`, and logs are absent. Authenticate with your own
account if Git prompts. Do not put access tokens into the URL or tracked files.
