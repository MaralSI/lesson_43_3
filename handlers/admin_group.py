import logging 
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Admin, bot

spam_words = ['спам', 'подписывайтесь', "скидки", 'дурак', 'дебил']

user_warnings = {}


async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f'Добро пожаловать, {member.full_name}!\n\n'
                             f'Правила группы!\n'
                             f'* Не спамить\n'
                             f'* Не материться\n'
                             f'* Не рекламировать\n')


async def warn_user(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in Admin:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должны быть ответом на сообщение')
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1 

            for admin in Admin:
                await bot.send_message(chat_id=admin, text=f'{user_name} получил предупреждение ({user_warnings[user_id]}/3)')

                if user_warnings[user_id] >= 3:
                    await bot.kick_chat_member(message.chat.id, user_id)
                    await bot.send_message(chat_id=admin, text=f'{user_name} был удален за превышение количества предупреждений!')


async def delete_user_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in Admin:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должны быть ответом на сообщение')
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name

            await message.answer(f'Вы действительно хотите удалить {user_name}?',
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f'Удалить', callback_data=f'delete_user {user_id}')))
            
    else:
        await message.answer('Эта команда должна быть использована в группе')


async def complete_delete_user(call: types.CallbackQuery):
    user_id = int(call.data.replace("delete_user ", ""))
    try:
        await bot.kick_chat_member(call.message.chat.id, user_id)
        await call.answer(text='Пользователь удален', show_alert=True)
        await bot.delete_message(call.message.chat.id, call.message_id)

    except Exception as e:
        logging.error(f'Error in complete_delete_user: {e}')
        await call.answer(text='Не удалось удалить пользователя', show_alert=True)

async def filter_spam(message: types.Message):
    for word in spam_words:
        if word in message.text:
            await message.delete()
            await message.answer('Не выражаться и не спамить!')
            break



def register_admin_group(dp: Dispatcher):
    dp.register_message_handler(welcome_user, content_types=[types.ContentType.NEW_CHAT_MEMBERS])
    dp.register_message_handler(warn_user, commands=['warn'], commands_prefix='!/')
    dp.register_message_handler(delete_user_handler, commands=['d'], commands_prefix='!/')
    dp.register_callback_query_handler(complete_delete_user, lambda call: call.data and call.data.startswith('delete_user '))

    dp.register_message_handler(filter_spam)