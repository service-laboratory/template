from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = Field(...)
    sentry_dsn: str = Field(...)
    services: list[str] = Field(...)


settings = Settings()
