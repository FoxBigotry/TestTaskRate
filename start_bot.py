import asyncio
from aiogram import Bot, Dispatcher
from settings import settings
from handlers.messages import router_message
from handlers.commands import router_command
from logs.logger import get_logger


logger = get_logger()
dp = Dispatcher()


async def main():
    try:
        bot = Bot(token=settings.TG_KEY)
        router_command.include_router(router_message)
        dp.include_router(router_command)
        logger.info("Бот начал работу")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка старта бота: {e}")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error("Бот завершил работу")
