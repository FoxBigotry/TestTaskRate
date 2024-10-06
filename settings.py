from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    TG_KEY: str
    RATE: str


settings = Settings()


__all__ = ["settings"]
