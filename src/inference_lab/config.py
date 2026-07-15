from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = "InferenceLab"
    environment: str = "development"
    debug: bool = True

def get_settings() -> Settings:
    """Create and return the application settings."""

    return Settings()