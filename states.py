from aiogram.fsm.state import StatesGroup, State


class SchoolStates(StatesGroup):
    name = State()
    year = State()
    choose_school = State()


class KindStates(StatesGroup):
    name = State()
    year = State()