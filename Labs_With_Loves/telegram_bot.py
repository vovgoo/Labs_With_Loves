from aiogram import executor
from aiogram import types
from create_bot import dp 

async def on_startup(_):
    print('Бот успешно запущен.')

from handlers import admin, client, other

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)