from random import shuffle

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *
from states import NewStates
from databases import DataBase
from gpt import gpt_request
from promts import *

router = Router()


@router.message(F.text, StateFilter(None))
async def start_answer_user(message: types.Message, state: FSMContext):
    await state.clear()
    text = gpt_request(message.text, promt_start)
    print(text)
    if text == 'school':
        await state.set_state(NewStates.name)
        await message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")
    elif text == 'past_education':
        pass
    elif text == 'education':
        await message.answer("Выберете, что вы хотите сделать?", reply_markup=start_education_kb())
    elif text == 'doctors':
        await message.answer('...', reply_markup=start_doctors_kb())
    elif text == 'communal_services':
        await message.answer('...', reply_markup=start_communal_services_kb())
    elif text == 'avto':
        await message.answer('...', reply_markup=start_avto_kb())
    else:
        await message.answer("Возможно я не смогу вам помочь с данным вопросов, скоро к вам подключиться ассистент и поможет вам",
                             reply_markup=back_kb())

