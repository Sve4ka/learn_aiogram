from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from command import dp
from db.main import add_fruits
from keyboard import addshop, finishshop
from keyboard import fruit

NEW_FUIT = """
СОЗДАЕМ НОВЫЙ ПРОДУКТ
Название   {}
Цена       {}
Количество {}
Описание {}"""


class ProductStates(StatesGroup):
    name = State()
    price = State()
    count = State()
    decr = State()
    wait = State()
    end = State()


async def update_keyboard(state: FSMContext):
    async with state.proxy() as data:
        nn = data['f_name']
        pp = data['f_price']
        cc = data['f_count']
        dd = data['f_decr']
        call = data['callback']
        if nn != "None" and pp != "None" and cc != "None" and dd != "None":
            await call.message.edit_text(text="проверьте введенные данные и если все "
                                              "верно нажмите на клавишу finish" + NEW_FUIT.format(nn, pp, cc, dd),
                                         reply_markup=finishshop)
        else:
            await call.message.edit_text(NEW_FUIT.format(nn, pp, cc, dd), reply_markup=addshop)


@dp.callback_query_handler(text='new_cancel', state='*')
async def new_cancel(call: types.CallbackQuery, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await call.message.edit_text("создание продукта принудительно завершено, продукт не был сохранен")


@dp.callback_query_handler(text='new_fr', state="*")
async def new_fr(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(f_name="None")
    await state.update_data(f_price="None")
    await state.update_data(f_count="None")
    await state.update_data(f_decr="None")
    await state.update_data(callback=call)
    await update_keyboard(state)


@dp.callback_query_handler(text='new_fr_name', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите имя", reply_markup=addshop)
    await ProductStates.name.set()


@dp.callback_query_handler(text='new_fr_price', state="*")
async def inl_new_fr_price(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите цену", reply_markup=addshop)
    await ProductStates.price.set()


@dp.callback_query_handler(text='new_fr_count', state="*")
async def inl_new_fr_count(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите количество", reply_markup=addshop)
    await ProductStates.count.set()


@dp.callback_query_handler(text='new_fr_descr', state="*")
async def inl_new_fr_decr(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите описание", reply_markup=addshop)
    await ProductStates.decr.set()


@dp.callback_query_handler(text='new_fr_okeys', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        nn = data['f_name']
        pp = data['f_price']
        cc = data['f_count']
        add_fruits(call.from_user.id, float(pp), str(nn), int(cc))
    await state.finish()
    await call.message.edit_text("Данные сохранены", reply_markup=fruit)


@dp.message_handler(state=ProductStates.name)
async def price_state(message: types.Message, state: FSMContext):
    # if "'" in message.text.lower():
    #     await message.delete()
    #     return
    name = message.text.lower()
    await state.update_data(f_name=name)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(ProductStates.wait.state)


@dp.message_handler(state=ProductStates.decr)
async def price_state(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(f_decr=price)
    await message.delete()
    await state.set_state(ProductStates.wait.state)
    await update_keyboard(state)


@dp.message_handler(state=ProductStates.count)
async def price_state(message: types.Message, state: FSMContext):
    try:
        price = int(message.text)
        await state.update_data(f_count=price)
        await message.delete()
        await state.set_state(ProductStates.wait.state)
        await update_keyboard(state)
    except Exception:
        await message.delete()


@dp.message_handler(state=ProductStates.price)
async def price_state(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
        await state.update_data(f_price=price)
        await message.delete()
        await state.set_state(ProductStates.wait.state)
        await update_keyboard(state)
    except Exception:
        await message.delete()


@dp.message_handler(state=ProductStates.wait)
async def wait_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        nn = data['f_name']
        pp = data['f_price']
        cc = data['f_count']
        dd = data['f_decr']
        call = data['callback']

        print(nn, pp, cc, dd)
        if nn is not None and pp is not None and cc is not None and dd is not None:
            await call.edit_text(text="проверьте введенные данные и если все "
                                      "верно нажмите на клавишу finish" + NEW_FUIT.format(nn, pp, cc, dd),
                                 reply_markup=finishshop)
        else:
            print(nn, pp, cc, dd)
            return
