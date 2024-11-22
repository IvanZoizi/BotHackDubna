from random import shuffle

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import *
from states import SchoolStates, KindStates
from databases import DataBase

router = Router()
