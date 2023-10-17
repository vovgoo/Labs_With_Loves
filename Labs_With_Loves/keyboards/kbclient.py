from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
b1 = KeyboardButton('Авторизироваться✅')
b2 = KeyboardButton('Цена за лабараторную работу💲')
b3 = KeyboardButton('Заказать лабараторную работу❓')
b4 = KeyboardButton('Python🐍') 
b5 = KeyboardButton('C++👾')

client_autorization = ReplyKeyboardMarkup(resize_keyboard=True)
client_autorization.add(b1)

client_menu = ReplyKeyboardMarkup(resize_keyboard=True)
client_menu.add(b2,b3)

language = ReplyKeyboardMarkup(resize_keyboard=True)
language.add(b4, b5) 