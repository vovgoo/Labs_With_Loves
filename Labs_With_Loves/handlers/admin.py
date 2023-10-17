from aiogram import Dispatcher
from aiogram import types
from create_bot import bot, dp

ID = None

async def admin_autoriz(message: types. Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Вы успешно авторизировались в качестве администратора.')
    await message.delete()

async def send(message: types.Message):
    if ID == message.from_user.id:
        await bot.send_message(message.text[6:15],message.text[16:])

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_autoriz, commands=['admins'], is_chat_admin = True)
    dp.register_message_handler(send, commands=['send'])