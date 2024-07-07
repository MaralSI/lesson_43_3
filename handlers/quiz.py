from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

async def quiz(message: types.Message):
   button_quiz = InlineKeyboardMarkup()
   button_quiz_1 = InlineKeyboardButton("Дальше", callback_data='button_1')
   button_quiz.add(button_quiz_1)

   question = 'BMW or Mercedes'

   answer = ['BMW', 'Mercedes']

   await bot.send_poll(
       chat_id=message.from_user.id,
       question=question,
       answer=answer,
       is_anonymous=True,
       type='quiz',
       correct_option_id=1,
       explanation='IZI',
       open_period=60,
       reply_markup=button_quiz
   )

   def register_quiz(dp: Dispatcher):
       dp.register_message_handler(quiz, commands=['quiz'])





