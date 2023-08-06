from aiogram import types

from loader import dp
from keyboards.default import lights_all, red_kb, yellow_kb, green_kb
from states import Lights

@dp.message_handler(commands='trafficlighton')
async def bot_traffic_light_on(message: types.Message):
    await Lights.StateOn.set()
    await message.answer("Ви увімкнули світлофор 🚦.\n"
                         "Тепер можете увімкнути будь-яке світло:",
                         reply_markup=lights_all)