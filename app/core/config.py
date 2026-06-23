import os

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "fastapi-service")
    ENV: str = os.getenv("ENV", "dev")

settings = Settings()