from random import choice
from time import time

from aiogram import executor, types
from aiogram.types import ReplyKeyboardRemove

from command import dp


async def on_startup(_):
    print("HI, i work")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    if message.sticker.file_unique_id == "AgADCx8AAjvGIEg":
        await message.reply("нет, ты хороший")
    # await message.answer(message.sticker.file_unique_id)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if (
            message.from_user.id == 976008787 or message.from_user.id == 926795930 or message.from_user.id == 2145086501) and int(
            time()) % 101 == 0:
        await message.reply(choice(["""Что сказал слепой когда зашёл в бар:
-Привет,всем, кого не видел!""",
                                    """Заходит негр с попугаем в бар, а бармен спрашивает:
 — Где ты такого купил.
 А попугай отвечает:
 — Да так, за углом.""", """Шутки про утопленников обычно несмешные, потому что лежат на поверхности.""",
                                    """Акробат умер на батуте, но еще какое-то время продолжал радовать публику.""",
                                    """Однорукий человек заплакал, увидев магазин «секонд-хенд».""",
                                    """Одна девочка так сильно боялась прыгать с парашютом, что прыгнула без него.""",
                                    """Из студенческого общежития куда-то исчезли все кошки… Вот такие пироги."""]))
    # elif "привет" in message.text.lower():
    #     await message.answer("приветики💚")
    elif "если думаешь" in message.text.lower():
        await message.reply("ой иди нахуй")
    # elif "люблю" in message.text.lower() and "не" in message.text.lower():
    #     # await bot.send_message(chat_id=message.from_user.id, text="ты делаешь мне грустно")
    #     await message.reply("а я все равно тебя люблю")
    # elif ("люблю" in message.text.lower()):
    #     await message.reply("и я тебя люблю")
    # elif ("кря" in message.text.lower()):
    #     await message.answer("кря")
    # elif ("ква" in message.text.lower()):
    #     await message.answer("ква")
    elif ("даун" in message.text.lower()):
        await message.reply("нет, ты хороший")
    elif ("умер" in message.text.lower() or "смерт" in message.text.lower()):
        await message.reply("не надо! 😢")
    elif ("курва" in message.text.lower()):
        try:
            await message.answer(text="окей", reply_markup=ReplyKeyboardRemove())
        except Exception:
            return


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
