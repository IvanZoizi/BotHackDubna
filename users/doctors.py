from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *
from databases import DataBase
from states import *

router = Router()


@router.callback_query(F.data == 'doctors')
async def start_doctors(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=start_doctors_kb())


@router.callback_query(F.data == 'policy')
async def start_policy(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    policy = dbase.get_policy(call.from_user.id)
    if policy:
        await call.message.answer(f"Ваш код медицинского полиса - <b>{policy[1]}</b>", reply_markup=back_kb(),
                                  parse_mode='html')
    else:
        await call.message.answer("<b>У вас еще не установлен медицинский полис</b>\n"
                                  "Чтобы прикрепить полис, <b>введите его код</b>", parse_mode='html')
        await state.set_state(PolicyStates.code)


@router.message(StateFilter(PolicyStates.code))
async def policy_code(message: types.Message, state: FSMContext):
    await state.update_data(code=message.text)
    await message.answer("Введите ваше имя")
    await state.set_state(PolicyStates.name)


@router.message(StateFilter(PolicyStates.name))
async def policy_name(message: types.Message, state: FSMContext, dbase: DataBase):
    data = await state.get_data()
    await state.clear()
    dbase.new_policy(message.from_user.id, data['code'], message.text)
    await message.answer("<b>Ваша заявка принята</b>", reply_markup=start_doctors_kb(), parse_mode='html')


@router.callback_query(F.data == 'make_appointment')
async def make_appointment(call: types.CallbackQuery, dbase: DataBase, state: FSMContext):
    await call.message.delete()
    policy = dbase.get_policy(call.from_user.id)
    if policy:  # Тут сделать, что если нету полиса он его заполняет и он заполняется в бд, если есть, то спрашиваем врача и время, время он пишет сам

        await call.message.answer(f"Введите ваше имя", reply_markup=back_kb(),
                                  parse_mode='html')
    else:
        await call.message.answer("<b>У вас еще не установлен медицинский полис</b>\n"
                                  "Чтобы прикрепить полис, <b>введите его код</b>", parse_mode='html')
        await state.set_state(PolicyStates.code)

