from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, ReplyKeyboardRemove
from aiohttp.web_routedef import route

from keyboards import *
from databases import DataBase
from states import *

from datetime import datetime, timedelta


router = Router()


@router.callback_query(F.data == 'doctors')
async def start_doctors(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите, что вы хотите сделать?", reply_markup=start_doctors_kb())


@router.callback_query(F.data == 'policy')
async def get_policy(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    policy = dbase.get_policy(call.from_user.id)
    if policy:
        await call.message.answer('Выберите, что вы хотите сделать:', reply_markup=policy_settings_kb())
    else:
        await call.message.answer("<b>У вас еще не установлен медицинский полис</b>\n"
                                  "Чтобы прикрепить полис, <b>введите его код</b>", parse_mode='html')
        await state.set_state(PolicyStates.code)
    #await call.message.answer('Выберите, что вы хотите сделать:', reply_markup=policy_settings_kb())


@router.callback_query(F.data == 'get_policy')
async def start_policy(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    policy = dbase.get_policy(call.from_user.id)
    await call.message.answer(f"Ваш код медицинского полиса - <b>{policy[1]}</b>", reply_markup=back_kb(),
                              parse_mode='html')


@router.callback_query(F.data == 'edit_policy')
async def edit_policy(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Введите свой новый полис:')
    await state.set_state(PolicyStates.edit_policy)


@router.message(StateFilter(PolicyStates.edit_policy))
async def edit_name_policy(message: types.Message, state: FSMContext, dbase: DataBase):
    policy = message.text
    dbase.edit_policy(int(message.from_user.id), policy)
    await message.answer('Вы успешно изменили полис!', reply_markup=back_kb())
    await state.clear()


@router.message(StateFilter(PolicyStates.code))
async def policy_code(message: types.Message, state: FSMContext):
    await state.update_data(code=message.text)
    await message.answer("Введите ваше имя")
    await state.set_state(PolicyStates.name)
    #dbase.new_policy(message.from_user.id, message.text)
    #await state.clear()
    #await message.answer("<b>Ваша заявка принята</b>", reply_markup=start_doctors_kb(), parse_mode='html')


@router.message(StateFilter(PolicyStates.name))
async def policy_name(message: types.Message, state: FSMContext, dbase: DataBase):
    data = await state.get_data()
    dbase.new_policy(message.from_user.id, data['code'], message.text)
    if 'go_doctor' not in list(data):
        await message.answer("<b>Ваша заявка принята</b>", reply_markup=start_doctors_kb(), parse_mode='html')
    else:
        await message.answer('Выберите врача', reply_markup=doctors_kb())
        await state.set_state(DoctorAppointmentStates.time)


@router.callback_query(F.data == 'make_appointment')
async def make_appointment(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    policy = dbase.get_policy(call.from_user.id)
    if policy:
        await call.message.answer('Выберите врача', reply_markup=doctors_kb())
        await state.update_data(go_doctor='1')
        await state.set_state(DoctorAppointmentStates.doctor)
    else:
        await call.message.answer("<b>У вас еще не установлен медицинский полис</b>\n"
                                  "Чтобы прикрепить полис, <b>введите его код</b>", parse_mode='html')
        await state.set_state(PolicyStates.code)


@router.callback_query(StateFilter(DoctorAppointmentStates.doctor))
async def doctor_choice(call: types.CallbackQuery, state: FSMContext):
    dict_data = {'ophthalmologist': 'Офтальмолог', 'neurologist': 'Невролог', 'dentist': 'Стоматолог'}
    await state.update_data(doctor=dict_data[call.data])
    await call.message.answer("<b>Выберите день, в которой вы сможете пойти</b>", reply_markup=day_choice_kb(), parse_mode='html')
    await state.set_state(DoctorAppointmentStates.time)


@router.callback_query(StateFilter(DoctorAppointmentStates.time))
async def day_choice(call: types.CallbackQuery, state: FSMContext):
    dict_data = {'today': 'Сегодня', 'tomorrow': 'Завтра', 'day_after_tomorrow': 'Послезавтра'}
    if dict_data[call.data] == 'Сегодня':
        day = datetime.today().strftime("%d.%m.%Y")
        await state.update_data(day=day)
    elif dict_data[call.data] == 'Завтра':
        day = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        await state.update_data(day=day)
    else:
        day = (datetime.today() + timedelta(days=2)).strftime("%d.%m.%Y")
        await state.update_data(day=day)
    await call.message.answer("<b>Выберите время, в которое вы сможете пойти</b>", reply_markup=time_choice_kb(), parse_mode='html')
    await state.set_state(DoctorAppointmentStates.finish)


@router.callback_query(StateFilter(DoctorAppointmentStates.finish))
async def finish_appointment(call: types.CallbackQuery, state: FSMContext, dbase: DataBase):
    await state.update_data(time=call.data)
    data = await state.get_data()

    appointment = False
    appointments = dbase.get_day_time(call.from_user.id)
    for day, time in appointments:
        if day == data['day'] and time == data['time']:
            appointment = True
    if not appointment:
        await call.message.answer('<b>Вы успешно записались к врачу!</b>', reply_markup=back_kb(), parse_mode='html')
        dbase.doctor_appointment(call.from_user.id, data['doctor'], data['time'], data['day'])
        await state.clear()
    if appointment:
        await call.message.answer('<b>Вы уже записаны в этот день и в это время, попробуйте записаться на другое время.</b>', reply_markup=back_kb(), parse_mode='html')
        await state.clear()


@router.callback_query(F.data == 'past_doctors')
async def past_appointments(call: types.CallbackQuery, state: FSMContext, dbase: DataBase):
    appointments = dbase.get_appointments(call.from_user.id)
    message = ''
    for _, doctor, time, day in list(appointments):
        message += f'Вы {day} записаны к {doctor}у на {time}\n'
    await call.message.delete()
    await call.message.answer(f'<b>{message}</b>', reply_markup=back_kb(), parse_mode='html')
