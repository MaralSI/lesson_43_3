from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons


class RegisterUser(StatesGroup):
    name_product = State()
    size = State()
    amount_product = State()
    phone = State()

async def fsm_start(message: types.Message):
    await RegisterUser.name_product.set()
    await message.answer(text="Введите название продукта:", reply_markup=buttons.cancel)


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите размер:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите количество продуктов:')


async def load_amount_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount_product'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите контактные данные (телефон):')


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    keyboard = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton(text='Yes', callback_data='confirm_yes')
    no_button = InlineKeyboardButton(text='No', callback_data='confirm_no')
    keyboard.add(yes_button, no_button)

    await RegisterUser.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f"Наименование продукта - {data['name_product']}\n"
                                       f"Размер- {data['size']}\n"
                                       f"Количество продукта - {data['amount_product']}\n"
                                       f"Контактные данные/телефон - {data['size']}\n"
                                       f"<b>Верные ли данные ?</b>",
                               reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            await main_db.sql_insert_list(
                name_product=data['name_product'],
                size=data['size'],
                amount_product=data['amount_product'],
                phone=data['phone']
            )

            await main_db.sql_insert_order(
                name_product==data['name_product'],
                numbers_product =data['numbers_product'],
                price = data['price'],
                info_product = data['info_product']
            )

            await message.answer('Отлично! Регистрация пройдена.', reply_markup=buttons.start_buttons)
            await state.finish()
    elif message.text == 'Нет':
        await message.answer('Отменено!', reply_markup=buttons.start_buttons)
        await state.finish()

    else:
        await message.answer(text='Нажмите на кнопку!')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено')


# Finite State Machine
def register_fsm_for_user(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['registration'])
    dp.register_message_handler(load_name_product, state=RegisterUser.name_product)
    dp.register_message_handler(load_amount_product, state=RegisterUser.amount_product)
    dp.register_message_handler(load_size, state=RegisterUser.size)
    dp.register_message_handler(load_phone, state=RegisterUser.phone)
    dp.register_callback_query_handler(submit, state=RegisterUser.submit)