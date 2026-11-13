import pytest


@pytest.fixture(autouse=True)
def isolated_configuration(monkeypatch):
    """Keep developer or CI shell variables from affecting test expectations."""
    monkeypatch.setenv("APP_NAME", "Student Information System")
    monkeypatch.setenv("DEBUG", "True")
    monkeypatch.setenv("MAX_STUDENTS", "100")
    monkeypatch.setenv("API_KEY", "")
