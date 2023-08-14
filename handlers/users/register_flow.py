from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.flow import Flow

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def bot_get_contact(message: types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer("Wrong data, You are not that user")
    else:
        await Flow.RegisterState.set()
        await message.answer(f"Hello {message.from_user.full_name}!")

@dp.message_handler(CommandStart(), state=Flow.RegisterState)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("You have already shared your phone number")
