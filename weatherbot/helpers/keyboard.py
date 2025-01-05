from telebot import types  # type: ignore


def keyboard_start() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(
        text="Отправить местоположение",
        request_location=True,
    )
    keyboard.add(button_geo)

    return keyboard


def keyboard_help() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    button_feedback = types.InlineKeyboardButton(
        text="Отправить обратную связь", url="https://t.me/Nottezz"
    )
    button_github = types.InlineKeyboardButton(
        text="Изучить проект на GitHub",
        url="https://github.com/R00kie-dot/WeatherBot",
    )
    keyboard.add(button_feedback)
    keyboard.add(button_github)

    return keyboard
