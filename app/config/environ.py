from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    flask_env : str
    jwt_secret_key: str
    jwt_access_token_expires_hours: int
    jwt_access_token_expires_days: int
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()