from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = Field(...)
    services: list[str] = Field(...)


settings = Settings()