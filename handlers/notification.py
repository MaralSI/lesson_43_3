from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
from config import bot
from apscheduler.triggers.cron import CronTrigger
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import random

users = [6703150919, ]
notification = []
class Notification(StatesGroup):
    waiting_for_message = State()

async def send_notification():
    for user in users:
        if notification:
            message = random.choice(notification)
        else:
            message = 'У вас нет запланированных задач!'
        await bot.send_message(chat_id=user,
                               text=f"🔔 Напоминание 🔔 \n"
                                    f"Добрый день! "
                                    f"Не забудьте про - {message}")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(send_notification,
                      CronTrigger(hour='20',
                                  minute='41',
                                  start_date=datetime.datetime.now()
                                  ),
                      )
    scheduler.start()


async def handler_notification_command(message: types.Message):
    await message.reply('Введите сообщение для уведомления: ')
    await Notification.waiting_for_message.set()


async def handle_notification_text(message: types.Message, state: FSMContext):
    notification_message = message.text
    notification.append(notification_message)

    await message.reply(f'Сообщение "{notification_message}" добавлено в список уведолений')
    await state.finish()


def register_notification(dp: Dispatcher):
    dp.register_message_handler(handler_notification_command, commands=['notification'])
    dp.register_message_handler(handle_notification_text, state=Notification.waiting_for_message)
