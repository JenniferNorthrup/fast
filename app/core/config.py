import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "fast")
    ENV: str = os.getenv("ENV", "dev")

    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int = 5432

    REDIS_HOST: str
    REDIS_PORT: int = 6379

    class Config:
        env_file = ".env"  # local only

settings = Settings()

class Settings(BaseSettings):
    ENV: str = "local"

    POSTGRES_HOST: str | None = None

    def resolve(self):
        if self.ENV == "local":
            self.POSTGRES_HOST = self.POSTGRES_HOST or "postgres"

        if self.ENV == "prod" and not self.POSTGRES_HOST:
            raise ValueError("POSTGRES_HOST must be set in prod")

        return self