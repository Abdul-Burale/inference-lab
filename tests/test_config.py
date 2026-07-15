import pytest
from pydantic import ValidationError

from inference_lab.config import Settings, get_settings


def test_get_settings_returns_settings_instance() -> None:
    get_settings.cache_clear()

    settings = get_settings()

    assert isinstance(settings, Settings)


def test_default_settings_values() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_name == "InferenceLab"
    assert settings.environment == "development"
    assert settings.debug is True
    assert settings.aws_region == "eu-west-2"
    assert settings.request_timeout_seconds == 30
    assert settings.log_level == "INFO"


def test_settings_read_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_NAME", "TestLab")
    monkeypatch.setenv("ENVIRONMENT", "testing")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("REQUEST_TIMEOUT_SECONDS", "60")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_name == "TestLab"
    assert settings.environment == "testing"
    assert settings.debug is False
    assert settings.aws_region == "us-east-1"
    assert settings.request_timeout_seconds == 60
    assert settings.log_level == "DEBUG"


def test_invalid_environment_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            environment="staging",
        )


def test_invalid_timeout_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            request_timeout_seconds=0,
        )