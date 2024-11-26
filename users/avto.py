from aiogram import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import *
from databases import DataBase
from states import *

router=Router()



@router.callback_query(F.data == 'avto')
async def start_education(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=start_avto_kb())


@router.callback_query(F.data == 'technic')
async def start_education(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Что вы хотите поставить на учёт?", reply_markup=accounting_kb())


@router.callback_query(F.data == 'car')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Легковой автомобиль")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")


@router.callback_query(F.data == 'motocicle')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Мотоцикл")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")

@router.callback_query(F.data == 'trailer')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Прицеп")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")

@router.callback_query(F.data == 'spec')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Специальный транспорт")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")


@router.callback_query(F.data == 'on_water')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Водный транспорт")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")


@router.callback_query(F.data == 'fly')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(auto_tipe="Воздушный транспорт")
    await state.set_state(CarStates.name_auto)
    await call.message.delete()
    await call.message.answer("Введите название машины")


@router.message(StateFilter(CarStates.name_auto))
async def school_name(message: types.Message, state: FSMContext):
    await state.update_data(name_auto=message.text)
    await message.answer("Введите номер ПТС")
    await state.set_state(CarStates.PTS)


@router.message(StateFilter(CarStates.PTS))
async def school_name(message: types.Message, state: FSMContext):
    await state.update_data(PTS=message.text)
    await message.answer("Введите номер и серию регистрации")
    await state.set_state(CarStates.number_reg)


@router.message(StateFilter(CarStates.number_reg))
async def school_name(message: types.Message, state: FSMContext):
    number_reg, series_reg = message.text.split()
    await state.update_data(number_reg=number_reg, series_reg=series_reg)
    await message.answer("Введите номер и серию паспорта\n(того на кого зарегистрирован автомобиль)")
    await state.set_state(CarStates.number_purchase_and_sale_agreement)


@router.message(StateFilter(CarStates.number_passport))
async def school_name(message: types.Message, state: FSMContext):
    number_passport, series_passport = message.text.split()
    await state.update_data(number_passport=number_passport, series_passport=series_passport)
    await message.answer("Введите специальный номер купли продажи")
    await state.set_state(CarStates.number_purchase_and_sale_agreement)


@router.message(StateFilter(CarStates.number_purchase_and_sale_agreement))
async def school_name(message: types.Message, state: FSMContext):
    await state.update_data(number_purchase_and_sale_agreement=message.text)
    await message.answer("Введите номер и серию ОСАГО")
    await state.set_state(CarStates.number_OSAGO)


@router.message(StateFilter(CarStates.number_OSAGO))
async def school_name(message: types.Message, state: FSMContext):
    number_OSAGO, series_OSAGO = message.text.split()
    await state.update_data(number_OSAGO=number_OSAGO,series_OSAGO=series_OSAGO)
    await message.answer("Введите номер оплаты госпошлины(УИН)")
    await state.set_state(CarStates.UIN_GOS_the_fee)


@router.message(StateFilter(CarStates.UIN_GOS_the_fee))
async def school_name(message: types.Message, state: FSMContext):
    await state.update_data(UIN_GOS_the_fee=message.text)
    await message.answer("Введите номер и серию технического паспорта")
    await state.set_state(CarStates.number_transport_vehicle)


@router.message(StateFilter(CarStates.number_transport_vehicle))
async def school_name(message: types.Message, state: FSMContext):
    number_transport_vehicle, series_transport_vehicle = message.text.split()
    await state.update_data(number_transport_vehicle=number_transport_vehicle,series_transport_vehicle=series_transport_vehicle)
    data = await state.get_data()
    await message.answer(f"Ваши данные зарегистрированы"
                         f"Ваши данны е по технике\n"
                         f"Тип машины:{data['auto_tipe']}\n"
                         f"Имя машины:{data['name_auto']}\n "
                         f"Введите номер ПТС:{data['number_reg']},{data['series_reg']}\n", reply_markup=back_accounting_kb())


@router.callback_query(F.data == 'my_technic')
async def start_education(call: types.CallbackQuery,state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    await call.message.answer(f"Ваши данные по технике\n"
                              f"Тип машины:{data['auto_tipe']}\n"
                              f"Имя машины:{data['name_auto']}\n "
                              f"Введите номер ПТС:{data['number_reg']},{data['series_reg']}\n")
