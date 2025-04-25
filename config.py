from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    ALGORITHM: str
    CODE_TOKEN_EXPIRE_MINUTES: int
    BOT_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()