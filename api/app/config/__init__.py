from dotenv import load_dotenv
from pathlib import Path

import os


dotenv_path = Path(".") / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    API_HOST: str = os.getenv("API_HOST")
    API_PORT: int = os.getenv("API_PORT")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")
    
    db_config: dict = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "database": DB_NAME,
                    "host": DB_HOST,
                    "password": DB_PASS,
                    "port": DB_PORT,
                    "user": DB_USER,
                }
            }
        },
        "apps": {
            "models": {
                "models": ["models.user"],
                "default_connection": "default",
            }
        },
    }

from telegram_webapp_auth import generate_secret_key

class TelegramBotConfig:
    def __init__(self) -> None:
        self.BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    
    def secret_key(self) -> str:
        return generate_secret_key(telegram_bot_token=self.BOT_TOKEN)

telegramcfg = TelegramBotConfig()
config = Config()

AERICH_CONFIG = config.db_config
