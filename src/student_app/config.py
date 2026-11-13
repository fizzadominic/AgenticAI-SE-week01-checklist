"""Load configuration without exposing secrets in output."""

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    app_name: str
    debug: bool
    max_students: int
    api_key: str = field(repr=False, default="")


def load_settings() -> Settings:
    load_dotenv(PROJECT_ROOT / ".env")
    debug = os.getenv("DEBUG", "False").strip().lower()
    if debug not in {"true", "false", "1", "0"}:
        raise ValueError("DEBUG must be True, False, 1 or 0.")
    try:
        max_students = int(os.getenv("MAX_STUDENTS", "100"))
    except ValueError:
        raise ValueError("MAX_STUDENTS must be a positive integer.") from None
    if max_students < 1:
        raise ValueError("MAX_STUDENTS must be a positive integer.")
    app_name = os.getenv("APP_NAME", "Student Information System").strip()
    if not app_name:
        raise ValueError("APP_NAME must not be empty.")
    return Settings(app_name, debug in {"true", "1"}, max_students, os.getenv("API_KEY", ""))
