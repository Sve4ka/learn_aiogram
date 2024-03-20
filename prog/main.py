from random import choice
from time import time

from aiogram import executor, types

from command import dp


async def on_startup(_):
    print("HI, i work")


# @dp.message_handler(content_types=['sticker'])
# async def send_sticker_id(message: types.Message):
# await message.answer(message.sticker.file_id)
# await bot.send_sticker(message.from_user.id, sticker="CAACAgQAAxkBAAO3YsmWkTZGlI3-C20hAR0Ni7VX1OwAAlgAA845CA0YTGAbMvUI0ykE")


@dp.message_handler()
async def echo_upper(message: types.Message):
    if "привет" in message.text.lower():
        await message.answer("приветики💚")
    elif "если думаешь" in message.text.lower():
        await message.reply("ой иди нахуй")
    elif "люблю" in message.text.lower() and "не" in message.text.lower():
        # await bot.send_message(chat_id=message.from_user.id, text="ты делаешь мне грустно")
        await message.reply("а я все равно тебя люблю")
    elif ("люблю" in message.text.lower()):
        await message.reply("и я тебя люблю")
    elif ("кря" in message.text.lower()):
        await message.answer("кря")
    elif ("ква" in message.text.lower()):
        await message.answer("ква")
    elif ("даун" in message.text.lower()):
        await message.reply("нет, ты хороший")
    elif ("умер" in message.text.lower() or "смерт" in message.text.lower()):
        await message.reply("не надо! 😢")
    elif (message.from_user.id == 926795930 or message.from_user.id == 2145086501) and int(time()) % 101 == 0:
        await message.reply(choice("""Что сказал слепой когда зашёл в бар:
-Привет,всем, кого не видел!""", """
Заходит негр с попугаем в бар, а бармен спрашивает:
— Где ты такого купил.
А попугай отвечает:
— Да так, за углом."""))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
