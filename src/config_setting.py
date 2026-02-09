from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str | None = None
    CORS_ORIGINS: list[str] = ["*"]
    
    SUB_NAME: str
    JWT_SECRET_KEY: str
    JWT_SIGNUP_KEY: str
    JWT_REFRESH_SECRET_KEY: str
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

setting = get_settings()
