from inference_lab.config import get_settings


def main() -> None:
    """Start the InferenceLab application."""

    settings = get_settings()

    print(f"{settings.app_name} started")
    print(f"Environment: {settings.environment}")
    print(f"Debug mode: {settings.debug}")
    print(f"AWS region: {settings.aws_region}")
    print(f"Request timeout: {settings.request_timeout_seconds} seconds")
    print(f"Log level: {settings.log_level}")
    print(f"AWS profile: {settings.aws_profile}")
    print(f"AWS region: {settings.aws_region}")


if __name__ == "__main__":
    main()