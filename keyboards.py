from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def start_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='Запись к врачу', callback_data='doctors'),
                types.InlineKeyboardButton(text="Образование", callback_data='education'))
    builder.row(types.InlineKeyboardButton(text='ЖКХ', callback_data='communal_services'),
                types.InlineKeyboardButton(text="Авто", callback_data='avto'))
    builder.row(types.InlineKeyboardButton(text='Связаться с ассистентом', callback_data='doctors'))
    return builder.as_markup()


def back_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()


def start_education_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🏫 Записать ребенка в школу', callback_data='school'))
    builder.row(types.InlineKeyboardButton(text='🎓ВУЗ', callback_data='does_not_work'),
                types.InlineKeyboardButton(text="🧒Детский сад", callback_data='kindergarten'))
    builder.row(types.InlineKeyboardButton(text='👨‍💻Колледж', callback_data='does_not_work'))
    builder.row(types.InlineKeyboardButton(text='📝Прошлые записи', callback_data='past_education'))
    # builder.row(types.InlineKeyboardButton(text='📍Ближайшие учебные заведения', callback_data='geo_education'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()


def start_doctors_kb():
    # мой код (тимофей)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='👨‍⚕️ Записаться к врачу', callback_data='make_appointment'))
    builder.row(types.InlineKeyboardButton(text='📄 Полис', callback_data='policy'),
                types.InlineKeyboardButton(text='🏖 Санаторий', callback_data='does_not_work'))  # Sanatorium
    builder.row(types.InlineKeyboardButton(text='🏥 Прикрепиться к поликлинике', callback_data='does_not_work'))
    builder.row(types.InlineKeyboardButton(text='📝Прошлые записи', callback_data='past_doctors'))
    #builder.row(types.InlineKeyboardButton(text='📍Ближайшие учебные заведения', callback_data='geo_doctors'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()


def start_communal_services_kb():
    pass


def start_avto_kb():
    pass


# def doctors_choice_kb():
#     builder = InlineKeyboardBuilder()
#     builder.row(types.InlineKeyboardButton(text='👓 Офтальмолог', callback_data='time_choice'))
#     builder.row(types.InlineKeyboardButton(text='🧠 Невролог', callback_data='time_choice'))
#     builder.row(types.InlineKeyboardButton(text='🦷 Стоматолог', callback_data='time_choice'))
#     return builder.as_markup()
#
#
# def time_choice_kb():
#     builder = InlineKeyboardBuilder()
#     builder.row(types.InlineKeyboardButton(text='🕘 26.11.24 17:30', callback_data='success'))
#     builder.row(types.InlineKeyboardButton(text='🕘 26.11.24 18:00', callback_data='success'))
#     builder.row(types.InlineKeyboardButton(text='🕘 26.11.24 18:30', callback_data='success'))
#     return builder.as_markup()
#
#
def choice_school_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🏫 Лицей', callback_data='lyceum'))
    builder.row(types.InlineKeyboardButton(text='⛪️ Средняя общеобразовательная школа', callback_data='mou'))
    builder.row(types.InlineKeyboardButton(text='🏤Гимназия', callback_data='gim'))
    return builder.as_markup()