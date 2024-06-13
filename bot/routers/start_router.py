from aiogram import Router
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config_data


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🐘 Готов тратить время!", web_app=WebAppInfo(
            url=config_data.WEB_APP_URL
        )
    )
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Привет, мамонтенок!", reply_markup=webapp_builder())
