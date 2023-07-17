from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseSettings):
    POSTGRESQL_HOSTNAME: str = os.environ["POSTGRESQL_HOST"]
    POSTGRESQL_USERNAME: str = os.environ["POSTGRESQL_USER"]
    POSTGRESQL_PASSWORD: str = os.environ["POSTGRESQL_PASSWORD"]
    POSTGRESQL_DATABASE: str = os.environ["POSTGRESQL_DB"]
    JSON_FILE_PATH: str = os.environ["JSON_FILE_PATH"]


settings = Settings()
