from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

# ------- тут менял -----------------
def start_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='📋 Запись к врачу', callback_data='doctors'),
                types.InlineKeyboardButton(text="🎓 Образование", callback_data='education'))
    builder.row(types.InlineKeyboardButton(text='🏠 ЖКХ', callback_data='communal_services'),
                types.InlineKeyboardButton(text="🚗 Авто", callback_data='avto'))
    builder.row(types.InlineKeyboardButton(text='🤖 Связаться с ассистентом', callback_data='doctors'))
    return builder.as_markup()
# -----------------------------------

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
    # builder.row(types.InlineKeyboardButton(text='📍Ближайшие учебные заведения', callback_data='geo_doctors'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()


def start_communal_services_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='💧Внести показания горячей воды', callback_data='hot_water'))
    builder.row(types.InlineKeyboardButton(text='💧Холодной воды', callback_data='cold_water'),
                (types.InlineKeyboardButton(text='🌫Отопления', callback_data='gas')))
    builder.row(types.InlineKeyboardButton(text='💡Электричества', callback_data='electric'))
    builder.row(types.InlineKeyboardButton(text='📊Вывести данные по счётчикам', callback_data='score'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()

def start_avto_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🚘Поставить технику на учёт', callback_data='technic'))
    builder.row(types.InlineKeyboardButton(text='🗒Моя техника', callback_data='my_technic'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться в меню', callback_data='start'))
    return builder.as_markup()

def accounting_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🚘Машину', callback_data='car'),(types.InlineKeyboardButton(text='🏍Мотоцикл', callback_data='motocicle')))
    builder.row(types.InlineKeyboardButton(text='🚐Прицеп', callback_data='trailer'))
    builder.row(types.InlineKeyboardButton(text='🏗Специальную технику', callback_data='spec'))
    builder.row(types.InlineKeyboardButton(text='🛥️Водный транспорт', callback_data='on_water'))
    builder.row(types.InlineKeyboardButton(text='🚁Воздушный транспорт', callback_data='fly'))
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться назад', callback_data='avto'))
    return builder.as_markup()

def choice_school_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🏫 Лицей', callback_data='lyceum'))
    builder.row(types.InlineKeyboardButton(text='⛪️ Средняя общеобразовательная школа', callback_data='mou'))
    builder.row(types.InlineKeyboardButton(text='🏤Гимназия', callback_data='gim'))
    return builder.as_markup()

# ------- тут менял -----------------
def doctors_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='👁️ Офтальмолог', callback_data='ophthalmologist'))
    builder.row(types.InlineKeyboardButton(text='🧠 Невролог', callback_data='neurologist'))
    builder.row(types.InlineKeyboardButton(text='🦷 Стоматолог', callback_data='dentist'))
    return builder.as_markup()


def day_choice_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='📅 Сегодня', callback_data='today'))
    builder.row(types.InlineKeyboardButton(text='🔜 Завтра', callback_data='tomorrow'))
    builder.row(types.InlineKeyboardButton(text='⏭️ Послезавтра', callback_data='day_after_tomorrow'))
    return builder.as_markup()


def time_choice_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🕟 16:30', callback_data='16:30'))
    builder.row(types.InlineKeyboardButton(text='🕔 17:00', callback_data='17:00'))
    builder.row(types.InlineKeyboardButton(text='🕠 17:30', callback_data='17:30'))
    return builder.as_markup()
# ---------------------------------


def policy_settings_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='📄 Получить полис', callback_data='get_policy'),
                types.InlineKeyboardButton(text='📄 Изменить полис', callback_data='edit_policy'))
    return builder.as_markup()


def back_accounting_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text='🔙Вернуться назад', callback_data='technic'))
    return builder.as_markup()