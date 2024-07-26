from config import dp, Admin, bot
from aiogram.utils import executor
import logging
from handlers import commands, echo, quiz, FSM_reg, FSM_store, notification, send_products, webapp, admin_group
import buttons
from db import main_db
from Google_Sheets import sheets


async def on_startup(_):
    for i in Admin:
        await notification.set_scheduler()
        await bot.send_message(chat_id=i, text='Bot started',
                                reply_markup=buttons.start_buttons)
        await main_db.sql_create()


async def on_shutdown(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Бот выключен!')


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_reg.register_fsm_for_user(dp)
FSM_store.register_fsm_store(dp)
notification.register_notification(dp)
send_products.register_send_products(dp)
webapp.register_webapp(dp)
sheets.register_google_sheets(dp)


admin_group.register_admin_group(dp)

# Эхо функция - вызывать самым последним
# echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)