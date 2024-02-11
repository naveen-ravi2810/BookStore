from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    DB_URI: str = os.getenv("postgresql_uri")
    JWT_KEY: str = os.getenv("jwt_secret_key")
    JWT_ALGORITHM: str = os.getenv("jwt_algorithm", "HS256")
    REDIS_HOST: str = os.getenv("redis_host")
    REDIS_PORT: int = os.getenv("redis_port")
    REDIS_DB: int = os.getenv("redis_db")


setting = Settings()
