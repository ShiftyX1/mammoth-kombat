from telegram_webapp_auth import parse_user_data, parse_init_data, validate
from fastapi import HTTPException, Depends, APIRouter
from fastapi.security.http import HTTPBase, HTTPAuthorizationCredentials
from pydantic import BaseModel

from ..config import telegramcfg  # Telegram Bot configuration

auth_router = APIRouter()

telegram_authentication_schema = HTTPBase()


class TelegramUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    language_code: str


def verify_token(auth_cred: HTTPAuthorizationCredentials) -> TelegramUser:
    settings = telegramcfg
    init_data = auth_cred.credentials
    try:
        if validate(init_data, settings.secret_key):  # generated using generate_secret_key function
            raise ValueError("Invalid hash")
    except ValueError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

    init_data = parse_init_data(init_data)
    user_data = parse_user_data(init_data["user"])
    return TelegramUser.parse_obj(user_data)


def get_current_user(
    auth_cred: HTTPAuthorizationCredentials = Depends(telegram_authentication_schema)
) -> TelegramUser:
    return verify_token(auth_cred)
