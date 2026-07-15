from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Validated application configuration."""

    app_name: str = "InferenceLab"

    environment: Literal[
        "development",
        "testing",
        "production",
    ] = "development"
    
    debug: bool = True

    aws_region: str = "eu-west-2"

    request_timeout_seconds: int = Field(
        default=30,
        gt = 0,
        lt=300,
    )
    
    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    """Load and cache the application settings."""

    return Settings()