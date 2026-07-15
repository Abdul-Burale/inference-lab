from inference_lab.config import get_settings

def main() -> None:
    settings = get_settings()
    
    print(f"{settings.app_name} started")
    print(f"Environment: {settings.environment}")
    print(f"Debug mode: {settings.debug}")

if __name__ == "__main__":
    main()