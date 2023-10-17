from http import client
from unicodedata import name
from aiogram import Dispatcher, types
from create_bot import bot
from keyboards import client_autorization, client_menu, language
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

KEY = None

class Labs(StatesGroup):
    NAME = State()
    LANGUAGE = State()
    NOMER = State()
    OPLATA = State()

async def start(message: types.Message):
        await bot.send_message(message.from_user.id, f'Добро пожаловать в моего бота. Для того что бы приступить к работе, вам нужно пройти авторизацию. Что бы это сделать вам нужно нажать нажать на кнопку Авторизация✅.', reply_markup = client_autorization)


async def autorizate(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id='@SwitchAndWas', user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        await bot.send_message(message.from_user.id,'Вход успешно выполнен. Вы были направлены в главное меню.', reply_markup=client_menu)
    else:
        await bot.send_message(message.from_user.id, 'Вам отказано в доступе. Для того что бы получить права доступа, обратитесь к администратору!')

async def price(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id='@SwitchAndWas', user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        await message.answer('Цена за лабарторную работу в данный момент состовляет: 7 BYN')
    else: 
        await message.answer('У вас отстутствуют права доступа.')


async def lb_start(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id='@SwitchAndWas', user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        await Labs.NAME.set()
        await bot.send_message(message.from_user.id, 'Для начала введи свое Имя и Фамилию.', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('У вас отсутствуют права доступа.')
    

async def load_NAME(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['NAME'] = message.text
    await Labs.next()
    await bot.send_message(message.from_user.id, "Теперь выбери язык программирования который тебе нужен.", reply_markup= language)


async def load_LANGUAGE(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['LANGUAGE'] = message.text
    await Labs.next()
    await bot.send_message(message.from_user.id, "Теперь введи номер лабараторной работы которая тебе нужна.", reply_markup=ReplyKeyboardRemove())

async def load_NOMER(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['NOMER'] = message.text
    await Labs.next()
    await message.answer("Теперь оплати работу. Для этого нужно скинуть 7 BYN на данную карту. Сюда же вам надо вписать точное время, когда была совершенна операция.")

async def load_OPLATA(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['OPLATA'] = float(message.text)
        
    nam = data.get('NAME')
    lang = data.get('LANGUAGE')
    nom = data.get('NOMER')
    op = data.get('OPLATA')
    await bot.send_message(message.from_user.id, 'Работа успешна добавлена в очередь.', reply_markup = client_menu)
    await bot.send_message(601819112,f'У вас заказана лабараторная работа\nИмя и фамилия: {nam}\nЯзык программирования: {lang}\nНомер лабарторной работы: {nom}\nВремя оплаты: {op}\n\nCurrent ID {message.from_user.id}')
    await state.finish()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(autorizate, text = 'Авторизироваться✅')
    dp.register_message_handler(price, text = 'Цена за лабараторную работу💲')
    dp.register_message_handler(lb_start, text = 'Заказать лабараторную работу❓', state = None)
    dp.register_message_handler(load_NAME, state = Labs.NAME)
    dp.register_message_handler(load_LANGUAGE, state = Labs.LANGUAGE)
    dp.register_message_handler(load_NOMER, state =Labs.NOMER)
    dp.register_message_handler(load_OPLATA, state =Labs.OPLATA)

    