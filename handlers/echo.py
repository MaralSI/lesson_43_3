
from aiogram import types, Dispatcher

async def echo(message: types.Message):
    await message.answer(text='Нет такой команды!')

def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)