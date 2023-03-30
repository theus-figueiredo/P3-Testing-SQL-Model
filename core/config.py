from pydantic import BaseConfig
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host = getenv('HOST')
db_name = getenv('DB_NAME')
db_port = getenv('DB_PORT')
db_user = getenv('DB_USER')
db_password = getenv('DB_PASSWORD')


class Settings(BaseConfig):
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{db_user}:{db_password}@{host}:{db_port}/{db_name}'
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()
    
