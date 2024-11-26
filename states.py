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
    edit_policy = State()


class DoctorStates(StatesGroup):
    policy = State()
    name = State()
    doctor = State()
    time_ = State()


class Communal(StatesGroup):
    hot_water = State()
    cold_water = State()
    electric = State()
    hot_pipe = State()

# тут менял
class DoctorAppointmentStates(StatesGroup):
    doctor = State()
    day = State()
    time = State()
    finish = State()


class CarStates(StatesGroup):
    auto_tipe = State()
    name_auto = State()
    PTS = State()
    number_reg = State()
    number_passport = State()
    number_purchase_and_sale_agreement = State()
    number_OSAGO = State()
    UIN_GOS_the_fee = State()
    number_transport_vehicle = State()