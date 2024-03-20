from random import randint

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from keyboard import keyboard

import static_text
from config import TOKEN_API
from db.main import my_fruit_count, free_user_id, search_user, add_user
from keyboard import kb, b1, main_keyboard

bot = Bot(TOKEN_API)
ccount=0
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['sstart'])
async def start(message: types.Message):
    if not search_user(message.from_user.id):
        add_user(message.from_user.id, message.from_user.username)
    await message.answer(
        static_text.START, parse_mode='HTML', reply_markup=kb)

    await message.delete()


@dp.message_handler(commands=['fruit'])
async def start(message: types.Message):
    await message.answer(message.from_user.id)
    await message.answer(message.from_user.username)
    fruit_count = my_fruit_count(message.from_user.id)
    await message.answer("\n".join([" ".join([str(el) for el in list(elem)]) for elem in fruit_count]))
    await message.answer(free_user_id())
    await message.delete()


@dp.message_handler(commands=['delete'])
async def start(message: types.Message):
    await message.answer(text="окей", reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text=static_text.HELP)


@dp.message_handler(commands=['home'])
async def help(message: types.Message):
    await message.answer(text="куда направимся?", reply_markup=main_keyboard)


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    global ccount, keyboard
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.message_handler(commands="give_cat")
async def cmd_random(message: types.Message):
    await bot.send_sticker(message.chat.id, static_text.CAT)
    await message.delete()


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    global ccount
    ccount += 1
    b1.clean()
    b1.text = "Нажми меня " + str(ccount)
    # keyboard.set_current(types.InlineKeyboardButton(text="Нажми меня "+str(ccount), callback_data="random_value"))
    i = randint(1, 10)
    if (i == 1):
        await call.message.answer("хахаха  лох")
        await call.answer("loooool")
    await call.message.answer(str(i))
    await call.message.edit_text("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)
    await call.answer("пупупу")
