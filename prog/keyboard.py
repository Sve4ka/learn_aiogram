from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

ccount = 0

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help@Sve4ka_Learn_aiogram_bot'))
kb.add(KeyboardButton('/delete@Sve4ka_Learn_aiogram_bot'))

keyboard = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text="Нажми меня " + str(ccount), callback_data="random_value")
keyboard.add(b1)

main_keyboard = InlineKeyboardMarkup()
m1 = InlineKeyboardButton("РАНДОМ", callback_data="random_value")
m2 = InlineKeyboardButton("SHOP", callback_data="main")
main_keyboard.add(m1, m2)

shop = InlineKeyboardMarkup()
s0 = InlineKeyboardButton(text="menu", callback_data="home")
s1 = InlineKeyboardButton("return", callback_data="main")
s2 = InlineKeyboardButton("my shop", callback_data="shop")
s3 = InlineKeyboardButton("my profile", callback_data="profile")
s4 = InlineKeyboardButton("fruit", callback_data="fruit")
s5 = InlineKeyboardButton("vegetable", callback_data="vegetable")
s6 = InlineKeyboardButton("buy", callback_data="buy")
s7 = InlineKeyboardButton("add product", callback_data="add_product")
s8 = InlineKeyboardButton("apple", callback_data="apple")
s9 = InlineKeyboardButton("eat apple", callback_data="eat_apples")
s10 = InlineKeyboardButton("add apple", callback_data="add_apple")

shop.add(s0).add(s2).add(s3).add(s6)
keyboard.add(s0)

my_shop = InlineKeyboardMarkup()
my_shop.add(s1).add(s4)

my_profile = InlineKeyboardMarkup()
my_profile.add(s1)

buy = InlineKeyboardMarkup()
buy.add(s1)

ik0 = InlineKeyboardButton("my product", callback_data="fruit")
ik00 = InlineKeyboardButton("new", callback_data="new_fr")
ik1 = InlineKeyboardButton("price", callback_data="new_fr_price")
ik2 = InlineKeyboardButton("name", callback_data="new_fr_name")
ik3 = InlineKeyboardButton("count", callback_data="new_fr_count")
ik4 = InlineKeyboardButton("description", callback_data="new_fr_descr")
ik5 = InlineKeyboardButton("all_okeys", callback_data="new_fr_okeys")
ik6 = InlineKeyboardButton("cancel", callback_data="new_cancel")
addshop = InlineKeyboardMarkup()

fruit = InlineKeyboardMarkup()
fruit.add(s2).add(s8).add(s7).add(ik00)
apple = InlineKeyboardMarkup()
apple.add(s4).add(s9).add(s10)

finishshop = InlineKeyboardMarkup()

addshop.add(ik2).add(ik1).add(ik3).add(ik4).add(ik6)
finishshop.add(ik5)
