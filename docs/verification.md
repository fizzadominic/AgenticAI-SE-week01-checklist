# Week 01 completion record

Source: `../../Week 01 Checklist.docx` (original document preserved).
This record distinguishes executed work from student review and GitHub submission.

## Completed and verified locally

- [x] Phase 01 study notes covering application vs LLM vs agent, the agent loop,
  components, and engineering concerns: `concepts.md`.
- [x] Phase 02 stages 01-08 saved as executable snapshots in `examples/`.
  All eight executed using Ali and 85; each produced grade A.
- [x] Phase 02 stage 09 uses the required src layout, model class, services,
  utilities, reports, tests, README, requirements and ignore file.
- [x] Python 3.12.10, pip 25.0.1 and Git 2.55.0 verified.
- [x] Created `.venv`, activated it in PowerShell, and inspected installed packages.
- [x] Installed requests, python-dotenv and pytest; froze installed dependencies
  into requirements.txt. The editable local project is excluded from the freeze.
- [x] Created a second ignored `.venv-recreated`, installed requirements.txt into
  it, and independently ran the full suite: **66 passed**.
- [x] Root `.env` exists with APP_NAME, DEBUG, MAX_STUDENTS and blank API_KEY.
  No actual API credential is required by this offline app.
- [x] Loaded configuration via os and load_dotenv; API_KEY is omitted from output,
  logs and configuration repr. Tests check redaction with a synthetic value.
- [x] Created and loaded `data/student.json`; displayed the student and configuration.
- [x] Demonstrated the fragile stage 02 failing on nonnumeric marks.
- [x] Final app handles invalid name/marks, missing or malformed JSON, invalid
  schemas, duplicate IDs, invalid semesters and configuration, and record limits.
- [x] Verified marks 0 and 100, out-of-range values, booleans and nonfinite numbers.
- [x] Verified startup, report and error logging to stderr and logs/app.log.
- [x] Separated input/storage, validation, calculation, model, reporting and logging.
- [x] Required grade tests: 85=A, 75=B, 65=C, 55=D, 40=F.
- [x] Deliberately introduced a grade bug; observed **1 failed, 4 passed**.
  Restored the calculator; observed **5 passed**, then **66 passed** in the full suite.
  Actual output is saved in `verification.txt`.
- [x] Verified default report, name override, subject averaging, Pass/Fail status,
  invalid input exit code 1, and launching from a different working directory.
- [x] Git initialized on main; inherited existing configured user identity without
  changing global identity settings.
- [x] Initial commit and separate calculation feature commit created.
- [x] Created feature/student-status; implemented and tested display of status;
  committed, switched to main, merged with an explicit merge commit, tested again,
  and deleted the merged feature branch.
- [x] `.env`, `.venv`, bytecode, caches and logs excluded from tracked files.

## Interpretation of missing details

The document supplies no starter code, exact grade boundaries, specific deliberate
bug, or detailed new feature implementation. The README states the grade/averaging
assumptions. Snapshots demonstrate the requested progression. The extra calculator
function is calculate_status; the feature branch connects it to main's output.

The host provides DEBUG=release. Existing process variables correctly override
.env; use `$env:DEBUG = "True"` in PowerShell for this app. Tests isolate their
configuration and use project-local temporary storage because the host's shared
pytest temporary directory is inaccessible.

## Student actions remaining

- [ ] Read the concept notes and confirm personal understanding; prepare the lab
  demonstration. Code execution cannot attest to a student's understanding.
- [ ] Create the GitHub student-project repository, add origin, push main, and
  verify the GitHub contents. The student explicitly elected to handle this.

See README.md for exact setup, execution, testing and GitHub push commands.
