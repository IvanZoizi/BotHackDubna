from aiogram.fsm.state import StatesGroup, State


class NewStates(StatesGroup):
    name = State()
    year = State()
    choose_school = State()
