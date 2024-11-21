import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from config import *
from keyboards import *
from databases import DataBase
from users import doctors, communal_services, education, text_from_user
from promts import *
from gpt import gpt_request
from states import *

bot = Bot(token=token)
dp = Dispatcher()
dbase = DataBase('./db.sqlite')


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Привет, найду информацию и расскажу об услуге!",
        reply_markup=start_kb()
    )
    # await state.set_state(StartState.text_of_user)


@dp.callback_query(F.data == 'start')
async def start_cal(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.clear()
    await call.message.answer(
        "Привет, найду информацию и расскажу об услуге!",
        reply_markup=start_kb()
    )
    # await state.set_state(StartState.text_of_user)



# @dp.callback_query(F.data == 'education')
# async def start_education(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=start_education_kb())
#
#


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_routers(doctors.router, education.router, text_from_user.router)

    await dp.start_polling(bot, dbase=dbase)


if __name__ == "__main__":
    asyncio.run(main())