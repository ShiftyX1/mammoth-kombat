import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from config import config_data

from routers import start_router


async def main() -> None:
    bot = Bot(
        token=config_data.BOT_TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(router=start_router.router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
