from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    SERVICE_NAME: str = "fjc_rs_core_service"
    DEBUG: bool = True

    SECRET_KEY: str

    POSTGRES_SYNC_URL: str
    POSTGRES_ASYNC_URL: str

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / '.env', BASE_DIR / '.env.prod'),
        env_file_encoding='utf-8'
    )


settings = Settings()


