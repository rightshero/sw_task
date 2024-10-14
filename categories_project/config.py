from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """
    to config any settings in applications
    """
    debug: bool
    secret_key: str
    database_url: str
    NAME: str
    DB_USER: str
    PASSWORD: str
    HOST: str
    PORT: str

    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore')


# Decorator to wrap a function in a memoizing callable (cache).
# See documentation: https://docs.python.org/3/library/functools.html#functools.lru_cache
@lru_cache
def get_settings() -> Settings:
    return Settings(env_file='.env')


SETTINGS: Settings = get_settings()
