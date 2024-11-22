from random import shuffle

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *
from states import SchoolStates, KindStates
from databases import DataBase

router = Router()


@router.callback_query(F.data == 'education')
async def start_education(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=start_education_kb())


@router.callback_query(F.data == 'school')
async def school(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(SchoolStates.name)
    await call.message.delete()
    await call.message.answer("🧒 Чтобы записать ребенка в школу для начала напишите ФИО ребенка")


@router.message(StateFilter(SchoolStates.name))
async def school_name(message: types.Message, state: FSMContext):
    surname, name, fatherhood = message.text.split()
    await state.update_data(name=name, surname=surname, fatherhood=fatherhood)
    data = await state.get_data()
    if 'year' not in list(data):
        await message.answer("📅 Введите дату рождения ребенка")
        await state.set_state(SchoolStates.year)
    else:
        await message.answer("Теперь выберете школу, в которую пойдет ваш ребенок", reply_markup=choice_school_kb())
        await state.set_state(SchoolStates.choose_school)


@router.message(StateFilter(SchoolStates.year))
async def school_year(message: types.Message, state: FSMContext):
    await state.update_data(year=message.text)
    await message.answer("Теперь выберете школу, в которую пойдет ваш ребенок", reply_markup=choice_school_kb())
    await state.set_state(SchoolStates.choose_school)


@router.callback_query(StateFilter(SchoolStates.choose_school))
async def school_choose(call: types.CallbackQuery, state: FSMContext, dbase: DataBase):
    await call.message.delete()
    dict_edu = {'lyceum': 'Лицей', 'mou': 'Муниципальное образовательное учреждение', 'gim': 'Гимназия'}
    data = await state.get_data()
    await state.clear()
    check = dbase.get_educational_user(data['name'], data['surname'])
    if not check:
        await call.message.answer("<b>Вы уже пытались записать ребенка, попробуйте еще раз</b>",
                             reply_markup=back_kb(), parse_mode='html')
    dbase.new_educational_user(call.from_user.id, data['name'], data['surname'], data['fatherhood'], data['year'],
                               dict_edu[call.data])
    await call.message.answer("<b>Скоро мы подберем вам школу и свяжемся с вами!</b>", parse_mode='html', reply_markup=back_kb())


@router.callback_query(F.data == 'past_education')
async def past_education(call: types.CallbackQuery, dbase: DataBase):
    users = dbase.get_educational_user_data(call.from_user.id)
    if not users:
        await call.message.answer("<b>У вас пока нету никаких записей</b>", parse_mode='html',
                                  reply_markup=back_kb())
    else:
        emodsi = ['👧🏻', '🧒', '👧', '🧒🏻']
        shuffle(emodsi)
        text = '<b>Ваши заявки</b>\n\n'
        for i in range(len(users)):
            child = users[i]
            text += f"{emodsi[i % len(emodsi)]} <b>{child[2]} {child[1]} {child[3]}</b>, {child[4]}, {child[5]}\n\n"

        await call.message.answer(text, parse_mode='html', reply_markup=back_kb())


@router.callback_query(F.data == 'kindergarten')
async def kindergarten(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(KindStates.name)
    await call.message.delete()
    await call.message.answer("🧒 Чтобы записать ребенка в детский сад для начала напишите ФИО ребенка")


@router.message(StateFilter(KindStates.name))
async def kindergarten_name(message: types.Message, state: FSMContext, dbase: DataBase):
    surname, name, fatherhood = message.text.split()
    await state.update_data(name=name, surname=surname, fatherhood=fatherhood)
    data = await state.get_data()
    if 'year' not in list(data):
        await message.answer("📅 Введите дату рождения ребенка")
        await state.set_state(KindStates.year)
    else:
        data = await state.get_data()
        await state.clear()
        check = dbase.get_educational_user(data['name'], data['surname'])
        if not check:
            await message.answer("<b>Вы уже пытались записать ребенка, попробуйте еще раз</b>",
                                 reply_markup=back_kb(), parse_mode='html')
        dbase.new_educational_user(message.from_user.id, data['name'], data['surname'], data['fatherhood'],
                                   data['year'],
                                   'Детский сад')
        await message.answer("<b>Скоро мы подберем вам детский сад и свяжемся с вами!</b>", parse_mode='html',
                             reply_markup=back_kb())


@router.message(StateFilter(KindStates.year))
async def kindergarten_year(message: types.Message, state: FSMContext, dbase: DataBase):
    await state.update_data(year=message.text)
    data = await state.get_data()
    await state.clear()
    check = dbase.get_educational_user(data['name'], data['surname'])
    if not check:
        await message.answer("<b>Вы уже пытались записать ребенка, попробуйте еще раз</b>",
                             reply_markup=back_kb(), parse_mode='html')
    dbase.new_educational_user(message.from_user.id, data['name'], data['surname'], data['fatherhood'], data['year'],
                               'Детский сад')
    await message.answer("<b>Скоро мы подберем вам детский сад и свяжемся с вами!</b>", parse_mode='html', reply_markup=back_kb())



