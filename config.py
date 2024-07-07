from aiogram import Dispatcher, Bot
from decouple import config

Admin = ['6703150919',]

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
