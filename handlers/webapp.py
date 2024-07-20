from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import dp


async def webapp_reply(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton('Geeks online', web_app=types.WebAppInfo(url='https://online.geeks.kg')),
                 KeyboardButton('Kaktus Media', web_app=types.WebAppInfo(url='https://kaktus.media')),
                 KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg-ru/')))

    await message.answer('Нажми на кнопку ниже для перехода на сайты:', reply_markup=keyboard)


async def webapp_inline(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton('Geeks online', web_app=types.WebAppInfo(url='https://online.geeks.kg')),
                 InlineKeyboardButton('Kaktus Media', web_app=types.WebAppInfo(url='https://kaktus.media')),
                 InlineKeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg-ru/')))
    
    await message.answer('Нажми на кнопку ниже для перехода на сайты:', reply_markup=keyboard)


def register_webapp(db: Dispatcher):
    dp.register_message_handler(webapp_reply, commands=['webreply'])
    dp.register_message_handler(webapp_inline, commands=['webinline'])