from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_TIME: int = 3600
settings = Settings()
