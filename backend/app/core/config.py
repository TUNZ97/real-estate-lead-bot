from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Prefer repo-root .env, then backend/.env
_ROOT = Path(__file__).resolve().parents[3]  # .../backend/app/core → repo root
_BACKEND = Path(__file__).resolve().parents[2]  # .../backend
_ENV_FILES = [
    str(_ROOT / ".env"),
    str(_BACKEND / ".env"),
]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_ENV_FILES,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "primehomes-lead-bot"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_BASE_URL: str = "http://localhost:8000"
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    # Local MySQL (no Docker required for development)
    DATABASE_URL: str = (
        "mysql+pymysql://root:password@localhost:3306/primehomes_lead_bot"
    )

    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440

    N8N_BASE_URL: str = "http://localhost:5678"
    N8N_WEBHOOK_URL: str = "http://localhost:5678/webhook/customer-message"
    N8N_WEBHOOK_SECRET: str = ""

    AI_PROVIDER: str = "openai"
    AI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4o-mini"
    AI_BASE_URL: str = ""
    AI_TIMEOUT_SECONDS: int = 30

    LOG_LEVEL: str = "INFO"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
