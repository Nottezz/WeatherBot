from telebot import types  # type: ignore


def keyboard_start() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(
        text="Отправить местоположение",
        request_location=True,
    )
    keyboard.add(button_geo)

    return keyboard


def keyboard_help() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(
        text="Отправить местоположение",
        request_location=True,
    )
    button_github = types.KeyboardButton(
        text="Изучить проект на GitHub",
        web_app=types.WebAppInfo(url="https://github.com/R00kie-dot/WeatherBot"),
    )
    keyboard.add(button_geo)
    keyboard.add(button_github)

    return keyboard
