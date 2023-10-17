from aiogram import Dispatcher
from aiogram import types
from create_bot import bot




async def all_command(message: types.Message):
        
        await message.answer('Такой команды не существует.')
        await message.delete()
        


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(all_command)