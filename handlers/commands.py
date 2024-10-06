from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from state import Generate

router_command = Router()


@router_command.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    await state.set_state(Generate.start_talk)
    await message.answer("Добрый день. Как вас зовут?")
