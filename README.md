# Pulsewise (VAP Class 2 project)

AI health and fitness coach for India. This repository holds the rules engine, tests and CI workflow
described in Section 4.3 (Workflow 3) of the project report.

- `app/coach_rules.py`: safety and rules layer that can override the LLM
- `tests/`: unit tests and a small AI-safety evaluation
- `.github/workflows/ci.yml`: GitHub Actions pipeline (test, safety check, staged release)
- `prompts/`: prompt log used for the assignment
- `docs/`: report and app screenshots
