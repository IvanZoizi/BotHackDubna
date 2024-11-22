from aiogram.fsm.state import StatesGroup, State


class SchoolStates(StatesGroup):
    name = State()
    year = State()
    choose_school = State()


class KindStates(StatesGroup):
    name = State()
    year = State()


class PolicyStates(StatesGroup):
    code = State()
    name = State()


class DoctorStates(StatesGroup):
    policy = State()
    name = State()
    doctor = State()
    time_ = State()