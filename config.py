from aiogram import Dispatcher, Bot # type: ignore
from decouple import config # type: ignore
from aiogram.contrib.fsm_storage.memory import MemoryStorage # type: ignore

Admin = [7495645497, ]

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)