from aiogram import Bot, Dispatcher
from config import settings
from .handlers import router
import asyncio
import logging
import sys


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())