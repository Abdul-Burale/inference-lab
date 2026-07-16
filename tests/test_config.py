import pytest
from pydantic import ValidationError

from inference_lab.config import Settings, get_settings


def test_get_settings_returns_settings_instance() -> None:
    """get_settings should return a Settings object."""

    get_settings.cache_clear()

    settings = get_settings()

    assert isinstance(settings, Settings)


def test_default_settings_values() -> None:
    """Settings should provide the expected defaults."""

    settings = Settings(_env_file=None)

    assert settings.app_name == "InferenceLab"
    assert settings.environment == "development"
    assert settings.debug is True
    assert settings.aws_profile == "inference-lab"
    assert settings.aws_region == "eu-west-2"
    assert settings.request_timeout_seconds == 30
    assert settings.log_level == "INFO"


def test_settings_read_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Environment variables should override default values."""

    monkeypatch.setenv("APP_NAME", "TestLab")
    monkeypatch.setenv("ENVIRONMENT", "testing")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("AWS_PROFILE", "test-profile")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("REQUEST_TIMEOUT_SECONDS", "60")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_name == "TestLab"
    assert settings.environment == "testing"
    assert settings.debug is False
    assert settings.aws_profile == "test-profile"
    assert settings.aws_region == "us-east-1"
    assert settings.request_timeout_seconds == 60
    assert settings.log_level == "DEBUG"


def test_invalid_environment_is_rejected() -> None:
    """An unsupported environment name should fail validation."""

    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            environment="staging",
        )


@pytest.mark.parametrize(
    "invalid_timeout",
    [
        0,
        -1,
        301,
    ],
)
def test_invalid_timeout_is_rejected(invalid_timeout: int) -> None:
    """Timeouts outside the permitted range should fail validation."""

    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            request_timeout_seconds=invalid_timeout,
        )


@pytest.mark.parametrize(
    "valid_timeout",
    [
        1,
        30,
        300,
    ],
)
def test_valid_timeout_is_accepted(valid_timeout: int) -> None:
    """Timeouts within the permitted range should be accepted."""

    settings = Settings(
        _env_file=None,
        request_timeout_seconds=valid_timeout,
    )

    assert settings.request_timeout_seconds == valid_timeout


def test_invalid_log_level_is_rejected() -> None:
    """An unsupported logging level should fail validation."""

    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            log_level="TRACE",
        )