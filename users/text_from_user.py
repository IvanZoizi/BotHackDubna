import asyncio
from random import shuffle

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *
from states import SchoolStates, KindStates, PolicyStates
from databases import DataBase
from gpt import gpt_request
from promts import *


router = Router()


@router.message(F.text, StateFilter(None))
async def start_answer_user(message: types.Message, state: FSMContext, dbase: DataBase):
    await state.clear()
    text = gpt_request(message.text, promt_start)
    print(text)
    if 'school' in text:
        data = text.split(',')
        if len(data) == 1:
            await state.set_state(SchoolStates.name)
            await message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")
        else:
            if 'None' not in data[1] and 'None' not in data[2]:
                name, surname, fatherhood = data[1].split()
                await state.update_data(name=name, surname=surname, fatherhood=fatherhood, year=data[2].strip())
                await message.answer("Теперь выберете школу, в которую пойдет ваш ребенок",
                                     reply_markup=choice_school_kb())
                await state.set_state(SchoolStates.choose_school)
            elif 'None' in data[1] and 'None' not in data[2]:
                await state.update_data(year=data[2].strip())
                await state.set_state(SchoolStates.name)
                await message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")
            elif 'None' not in data[1] and 'None' in data[2]:
                name, surname, fatherhood = data[1].split()
                await state.update_data(name=name, surname=surname, fatherhood=fatherhood)
                await message.answer("📅 Введите дату рождения ребенка")
                await state.set_state(SchoolStates.year)
    elif 'kindergarten' in text:
        data = text.split(',')
        if len(data) == 1:
            await state.set_state(KindStates.name)
            await message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")
        else:
            if 'None' not in data[1] and 'None' not in data[2]:
                name, surname, fatherhood = data[1].split()
                check = dbase.get_educational_user(name, surname)
                if not check:
                    await message.answer("<b>Вы уже пытались записать ребенка, попробуйте еще раз</b>",
                                         reply_markup=back_kb(), parse_mode='html')
                dbase.new_educational_user(message.from_user.id, name, surname, fatherhood,
                                           data[2],
                                           'Детский сад')
                await message.answer("<b>Скоро мы подберем вам детский сад и свяжемся с вами!</b>", parse_mode='html',
                                     reply_markup=back_kb())
            elif 'None' in data[1] and 'None' not in data[2]:
                await state.update_data(year=data[2].strip())
                await state.set_state(KindStates.name)
                await message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")
            elif 'None' not in data[1] and 'None' in data[2]:
                name, surname, fatherhood = data[1].split()
                await state.update_data(name=name, surname=surname, fatherhood=fatherhood)
                await message.answer("📅 Введите дату рождения ребенка")
                await state.set_state(KindStates.year)
    elif text == 'past_education':
        users = dbase.get_educational_user_data(message.from_user.id)
        if not users:
            await message.answer("<b>У вас пока нету никаких записей</b>", parse_mode='html',
                                      reply_markup=back_kb())
        else:
            emodsi = ['👧🏻', '🧒', '👧', '🧒🏻']
            shuffle(emodsi)
            text = '<b>Ваши заявки</b>\n\n'
            for i in range(len(users)):
                child = users[i]
                text += f"{emodsi[i % len(emodsi)]} <b>{child[2]} {child[1]} {child[3]}</b>, {child[4]}, {child[5]}\n\n"

            await message.answer(text, parse_mode='html', reply_markup=back_kb())
    elif text == 'education':
        await message.answer("Выберете, что вы хотите сделать?", reply_markup=start_education_kb())
    elif text == 'doctors':
        await message.answer('...', reply_markup=start_doctors_kb())
    elif text == 'policy':
        policy = dbase.get_policy(message.from_user.id)
        if policy:
            await message.answer(f"<b>Ваш код медицинского полиса - {policy[2]}</b>", reply_markup=back_kb(),
                                      parse_mode='html')
        else:
            await message.answer("У вас еще не установлен медицинский полис, в виде его код")
            await state.set_state(PolicyStates.code)
    elif text == 'communal_services':
        await message.answer('...', reply_markup=start_communal_services_kb())
    elif text == 'avto':
        await message.answer('...', reply_markup=start_avto_kb())
    elif text == 'does_not_work':
        await message.answer("<b>Функционал не реализован</b>", reply_markup=back_kb(), parse_mode='html')
    else:
        await message.answer("Возможно я не смогу вам помочь с данным вопросов, скоро к вам подключиться ассистент и поможет вам",
                             reply_markup=back_kb())

