from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.utils import get_dollar_rate
from logs.logger import get_logger
from state import Generate


logger = get_logger()
router_message = Router()


@router_message.message(F.text, Generate.start_talk)
async def get_name_and_send_rate(message: Message, state: FSMContext):
    try:
        name = message.text
        dollar_rate = get_dollar_rate()

        if dollar_rate:
            await message.answer(f"Рад знакомству, {name}! Курс доллара сегодня {dollar_rate}р.")
            logger.info("Успешная отправка сообщения с курсом")
        else:
            await message.answer(f"Рад знакомству, {name}! Не удалось получить курс доллара.")
            logger.info("Успешная отправка сообщения, курс не получен")
    except Exception as e:
        logger.error(f"Ошибка получения курса: {e}")
    await state.clear()


@router_message.message()
async def any_message(message: Message):
    await message.answer("Простите я вас не понимаю 😔.\n"
                         "Сейчас я умею только спрашивать имя и сообщать курс доллара\n"
                         "Для начала введите или нажмите команду /start")
