import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from config import *
from keyboards import *
from databases import DataBase
from users import doctors, communal_services, education, text_from_user, avto

bot = Bot(token=token)
dp = Dispatcher()
dbase = DataBase('./db.sqlite')


@dp.message(Command("start"), StateFilter('*'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Привет, найду информацию и расскажу об услуге!",
        reply_markup=start_kb()
    )


@dp.callback_query(F.data == 'start', StateFilter('*'))
async def start_cal(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.clear()
    await call.message.answer(
        "Привет, найду информацию и расскажу об услуге!",
        reply_markup=start_kb()
    )


@dp.callback_query(F.data == 'does_not_work', StateFilter('*'))
async def does_not_work(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Функционал не реализован</b>", reply_markup=back_kb(), parse_mode='html')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_routers(doctors.router, education.router, text_from_user.router, avto.router, communal_services.router)

    await dp.start_polling(bot, dbase=dbase)


if __name__ == "__main__":
    asyncio.run(main())