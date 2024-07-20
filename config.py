from aiogram import Dispatcher, Bot # type: ignore
from decouple import config # type: ignore
from aiogram.contrib.fsm_storage.memory import MemoryStorage # type: ignore

Admin = [995712956, ]

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
storege = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storege)