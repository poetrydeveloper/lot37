from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    HTTP_PORT: str

    @property
    def database_url(self):
        DATABASE_URL = (f"postgresql+asyncpg://"
                        f"{self.DB_USER}:{self.DB_PASS}@"
                        f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        return DATABASE_URL

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
