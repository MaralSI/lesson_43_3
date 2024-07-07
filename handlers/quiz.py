from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, PollType
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
            options=answer,
            is_anonymous=True,
            type=PollType.QUIZ,
            correct_option_id=1,
            explanation='Под индексом 1',
            open_period=60,
            reply_markup=button_quiz
       )


async def quiz_2(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup()
    button_quiz_1 = InlineKeyboardButton("Дальше", callback_data='button_2')
    button_quiz.add(button_quiz_1)


    question = 'Messi or Ronaldu'
    photo_quiz = open('media/mem3.png', 'rb')
    answer = ['Messi', 'Ronaldu', 'Я']

    await bot.send_photo(chat_id=call.from_user.id, photo=photo_quiz)
    await bot.send_poll(
            chat_id=call.from_user.id,
            question=question,
            options=answer,
            is_anonymous=True,
            type=PollType.QUIZ,
            correct_option_id=2,
            explanation='Слушай свое эго',
            open_period=60,
            reply_markup=button_quiz
       )
async def button_handler(callback_query: types.CallbackQuery):
    if callback_query.data == 'button_1':
        await bot.answer_callback_query(callback_query.id, text="Вы нажали кнопку 'Дальше'")
        await bot.send_message(callback_query.from_user.id, "Теперь вы можете продолжить викторину или завершить её.")

def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')