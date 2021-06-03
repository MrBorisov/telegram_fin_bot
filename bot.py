from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from messages import MESSAGES
from states import MyStates

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'])


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])


# добавить клавиатуру с выборов режима

@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])

    if (not argument.isdigit()) or (not int(argument) < len(MyStates.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=argument))

    await state.set_state(MyStates.all()[int(argument)])
    await message.reply(MESSAGES['state_change'], reply=False)


@dp.message_handler(state=MyStates.HAND_STATE, commands=['for'])
async def first_test_state_case_met(message: types.Message):
    await message.reply('for', reply=False)


@dp.message_handler(state=MyStates.HAND_STATE)
async def first_test_state_case_met(message: types.Message):
    await message.reply('Hand!', reply=False)


@dp.message_handler(state=MyStates.STAT_STATE[0])
async def second_test_state_case_met(message: types.Message):
    await message.reply('stat', reply=False)


@dp.message_handler(state=MyStates.CONF_STATE)
async def third_or_fourth_test_state_case_met(message: types.Message):
    await message.reply('conf', reply=False)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
