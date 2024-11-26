from aiogram import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import *
from databases import DataBase
from states import Communal

router = Router()


@router.callback_query(F.data == 'communal_services')
async def start_education(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=start_communal_services_kb())


@router.callback_query(F.data == 'hot_water')
async def hot(call: CallbackQuery, state: FSMContext):
    await state.set_state(Communal.hot_water)
    await call.message.edit_text('Введите показания горячей воды:')


@router.message(Communal.hot_water)
async def hot_water(message: Message, state: FSMContext, dbase: DataBase):
    data_user = dbase.get_communal_services(message.from_user.id)
    print(data_user)
    try:
        if int(message.text) < 0:
            return await message.answer("Некорректные данные, попробуйте еще раз")
        if int(message.text) < int(data_user[1]):
            return await message.answer("Новые показания не могут быть меньше прошлых")
    except ValueError:
        return await message.answer("Некорректные данные, попробуйте еще раз")
    dbase.edit_communal_services(message.from_user.id, 'hot_water', int(message.text))
    await state.clear()
    await message.answer('Ваши показания по горячей воде обновлены.\nЧто будем делать дальще?',
                         reply_markup=start_communal_services_kb())


@router.callback_query(F.data == 'cold_water')
async def cold(call: CallbackQuery, state: FSMContext):
    await state.set_state(Communal.cold_water)
    await call.message.edit_text('Введите показания холодной воды:')


@router.message(Communal.cold_water)
async def cold_water(message: Message, state: FSMContext, dbase: DataBase):
    data_user = dbase.get_communal_services(message.from_user.id)
    try:
        if int(message.text) < 0:
            return await message.answer("Некорректные данные, попробуйте еще раз")
        if int(message.text) < int(data_user[2]):
            return await message.answer("Новые показания не могут быть меньше прошлых")
    except ValueError:
        return await message.answer("Некорректные данные, попробуйте еще раз")
    dbase.edit_communal_services(message.from_user.id, 'cold_water', int(message.text))
    await state.clear()
    await message.answer('Ваши показания по холодной воде обновлены. \n Что будем делать дальще?',
                         reply_markup=start_communal_services_kb())


@router.callback_query(F.data == 'gas')
async def hot_trub(call: CallbackQuery, state: FSMContext):
    await state.set_state(Communal.hot_pipe)
    await call.message.edit_text('Введите показания отопления:')


@router.message(Communal.hot_pipe)
async def hot_trub1(message: Message, state: FSMContext, dbase: DataBase):
    data_user = dbase.get_communal_services(message.from_user.id)
    try:
        if int(message.text) < 0:
            return await message.answer("Некорректные данные, попробуйте еще раз")
        if int(message.text) < int(data_user[3]):
            return await message.answer("Новые показания не могут быть меньше прошлых")
    except ValueError:
        return await message.answer("Некорректные данные, попробуйте еще раз")
    dbase.edit_communal_services(message.from_user.id, 'gas', int(message.text))
    await state.clear()
    await message.answer('Ваши показания по отоплению обновлены. \n Что будем делать дальще?',
                         reply_markup=start_communal_services_kb())


@router.callback_query(F.data == 'electric')
async def electric(call: CallbackQuery, state: FSMContext):
    await state.set_state(Communal.electric)
    await call.message.edit_text('Введите показания электричества:')


@router.message(Communal.electric)
async def electric1(message: Message, state: FSMContext, dbase: DataBase):
    data_user = dbase.get_communal_services(message.from_user.id)
    try:
        if int(message.text) < 0:
            return await message.answer("Некорректные данные, попробуйте еще раз")
        if int(message.text) < int(data_user[4]):
            return await message.answer("Новые показания не могут быть меньше прошлых")
    except ValueError:
        return await message.answer("Некорректные данные, попробуйте еще раз")
    dbase.edit_communal_services(message.from_user.id, 'electric', int(message.text))
    await state.clear()
    await message.answer('Ваши показания по электричеству обновлены. \n Что будем делать дальще?',
                         reply_markup=start_communal_services_kb())


@router.callback_query(F.data == 'score')
async def score(call: CallbackQuery, dbase: DataBase):
    data = dbase.get_communal_services(call.from_user.id)
    await call.message.edit_text(f'Ваши данные по счётчикам:\n\n'
                                 f'Горячая вода: {data[1] if data[1] != -1 else "Показаний нету"}\n'
                                 f'Холодная вода: {data[2] if data[2] != -1 else "Показаний нету"}\n'
                                 f'Отопление: {data[3] if data[3] != -1 else "Показаний нету"}\n'
                                 f'Электричество: {data[4] if data[4] != -1 else "Показаний нету"}',
                                     reply_markup=start_communal_services_kb())