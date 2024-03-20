from aiogram import types

from command import dp
from db.main import eat_apple, count_apple, add_apple
from keyboard import addshop
from keyboard import shop, buy, my_shop, my_profile, main_keyboard, fruit, apple


@dp.callback_query_handler(text="main")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text="ДОБРО ПОЖАЛОВАТЬ В НАЧАЛЬНОЕ ОКНО МАГАЗИНА", reply_markup=shop)
    # await call.message.edit_reply_markup(shop)


@dp.callback_query_handler(text="shop")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text("ДОБРО ПОЖАЛОВАТЬ В ОКНО ВАШЕГО МАГАЗИНА")
    await call.message.edit_reply_markup(my_shop)


@dp.callback_query_handler(text="profile")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text("{}, ДОБРО ПОЖАЛОВАТЬ В ОКНО ПОЛЬЗОВАТЕЛЯ".format(call.from_user.username))
    await call.message.edit_reply_markup(my_profile)


@dp.callback_query_handler(text="buy")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text("ДОБРО ПОЖАЛОВАТЬ В ОКНО ПОКУПКИ")
    await call.message.edit_reply_markup(buy)


@dp.callback_query_handler(text="fruit")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text("ДОБРО ПОЖАЛОВАТЬ В ОКНО ВЫБОРА ФРУКТОВ")
    await call.message.edit_reply_markup(fruit)


@dp.callback_query_handler(text="add_product")
async def add_product(call: types.CallbackQuery):
    await call.message.edit_text("давайте добавим новый фрукт", reply_markup=addshop)


@dp.callback_query_handler(text="apple")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text="Сейчас есть {} яблок\nНельзя есть если яблок больше нет".format(count_apple()),
                                 reply_markup=apple)


@dp.callback_query_handler(text="eat_apples")
async def main_callback(call: types.CallbackQuery):
    if count_apple() > 0:
        eat_apple()
    await call.message.edit_text(text="Сейчас есть {} яблок\nНельзя есть если яблок больше нет".format(count_apple()),
                                 reply_markup=apple)


@dp.callback_query_handler(text="add_apple")
async def main_callback(call: types.CallbackQuery):
    add_apple()
    await call.message.edit_text(text="Сейчас есть {} яблок\nНельзя есть если яблок больше нет".format(count_apple()),
                                 reply_markup=apple)


@dp.callback_query_handler(text="home")
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text("куда направимся?")
    await call.message.edit_reply_markup(main_keyboard)
