from inference_lab.config import Settings, get_settings

def test_get_settings_returns_settings_instance() -> None:
    settings = get_settings()

    assert isinstance(settings, Settings)

def test_default_settings_value() -> None:
    settings = get_settings()

    assert settings.app_name == "InferenceLab"
    assert settings.environment == "development"
    assert settings.debug is True
