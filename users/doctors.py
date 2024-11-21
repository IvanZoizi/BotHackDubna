from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *

router = Router()


@router.message(F.data == 'doctors')
async def start_doctors(call: types.CallbackQuery):
    await call.message.delete()
    #await call.message.answer("Выберете, что вы хотите сделать?", reply_markup=)