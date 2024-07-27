from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons
class RegisterUser(StatesGroup):
    name_product = State()
    numbers_product = State()
    price = State()
    info_product = State()


async def fsm_start(message: types.Message):
    await RegisterUser.name_product.set()
    await message.answer(text="Введите название продукта:", reply_markup=buttons.cancel)

async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите количество продуктов:')


async def load_numbers_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['numbers_product'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите цену продукта:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите информацию о продукте:')


async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text


    keyboard = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton(text='Yes', callback_data='confirm_yes')
    no_button = InlineKeyboardButton(text='No', callback_data='confirm_no')
    keyboard.add(yes_button, no_button)

    await RegisterUser.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f"Наименование продукта - {data['name_product']}\n"
                                       f"количество продукта - {data['Numbers_product']}\n"
                                       f"Цена продукта- {data['price']}\n"
                                       f"Информация о продукте - {data['info_product']}\n"
                                       f"<b>Верные ли данные ?</b>",
                               reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


async def submit(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'confirm_yes':
        await callback_query.message.answer('Отлично! Регистрация пройдена.', reply_markup=buttons.start_buttons)
        await state.finish()
    elif callback_query.data == 'confirm_no':
        await callback_query.message.answer('Отменено!', reply_markup=buttons.start_buttons)
        await state.finish()

    else:
        await callback_query.message.answer(text='Нажмите на кнопку!')


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
    dp.register_message_handler(load_numbers_product, state=RegisterUser.numbers_product)
    dp.register_message_handler(load_price, state=RegisterUser.price)
    dp.register_message_handler(load_info_product, state=RegisterUser.info_product)
    dp.register_callback_query_handler(submit, state=RegisterUser.submit)