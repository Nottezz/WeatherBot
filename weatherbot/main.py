import logging
import os

import telebot  # type: ignore
from dotenv import load_dotenv
from telebot import types

from weatherbot.helpers.generate import image_generate  # type: ignore
from weatherbot.openweather.request_to_api import WeatherRequest  # type: ignore

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

loger = logging.getLogger(__name__)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(
        text="Отправить местоположение", request_location=True
    )
    keyboard.add(button_geo)
    bot.send_message(
        message.chat.id,
        "Привет! "
        "Рад тебя видеть. \n\n"
        "Напиши название города или нажми на кнопку для отправки своего местоположения.",
        reply_markup=keyboard,
    )
    loger.info(message.chat)


@bot.message_handler(content_types=["text"])
def get_weather(message):
    openweather = WeatherRequest()
    response = openweather.get_city(message)

    if response.status_code == 200:
        image_generate(response)

        bot.send_photo(
            message.chat.id,
            caption="Данные предоставлены openweathermap.org.",
            photo=open("weather.png", "rb"),
        )
        loger.info("Success")
    else:
        bot.reply_to(message, "Вы ввели некорректное название города.")
        loger.error(response.text)


@bot.message_handler(content_types=["location"])
def location(message):
    openweather = WeatherRequest()
    response = openweather.get_location(message)
    if response.status_code == 200:
        image_generate(response)
        bot.send_photo(
            message.chat.id,
            caption="Данные предоставлены openweathermap.org.",
            photo=open("weather.png", "rb"),
        )
        loger.info("Success")
    else:
        bot.send_message(message.chat.id, "Ошибка! Повторите ещё раз")
        loger.error(response.text)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(module)s - %(levelname)s - %(message)s",
    )
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
