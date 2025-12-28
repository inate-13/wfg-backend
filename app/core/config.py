from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "transaction-service")
    environment: str = os.getenv("ENV", "local")

    mongo_uri: str = os.getenv("MONGO_URI")
    db_name: str = os.getenv("DB_NAME")


settings = Settings()
