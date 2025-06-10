import logging
import os

import telebot  # type: ignore
from dotenv import load_dotenv
from telebot import types

from weatherbot.helpers.generate import image_generate
from weatherbot.helpers.keyboard import keyboard_help, keyboard_start
from weatherbot.openweather.request_to_api import WeatherRequest

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

loger = logging.getLogger(__name__)


@bot.message_handler(commands=["start"])
def send_welcome(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        "Привет! "
        "Рад тебя видеть. \n\n"
        "Напиши название города или нажми на кнопку для отправки своего местоположения.",
        reply_markup=keyboard_start(),
    )
    loger.info(message.chat)


@bot.message_handler(commands=["help"])
def send_help_message(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        "Напиши название города или нажми на кнопку для отправки своего местоположения. Или можете посмотреть на меня изнутри 😉",
        reply_markup=keyboard_help(),
    )
    loger.info(message.chat)


@bot.message_handler(content_types=["text"])
def get_weather(message: types.Message) -> None:
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
def location(message: types.Message) -> None:
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


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(module)s - %(levelname)s - %(message)s",
    )
    loger.info("Run bot")
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
