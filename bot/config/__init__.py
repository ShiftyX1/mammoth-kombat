from dotenv import load_dotenv
from pathlib import Path

import os

dotenv_path = Path(".") / ".env"
load_dotenv(dotenv_path=dotenv_path)

class ConfigData:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    WEB_APP_URL: str = os.getenv("WEB_APP_URL")

config_data = ConfigData()
