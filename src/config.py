from pydantic_settings import BaseSettings
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    mongo_username: str
    mongo_password: str
    mongo_database: str
    mongo_host: str
    mongo_port: int


settings = Settings()
