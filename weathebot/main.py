import os
import telebot
import requests

from dotenv import load_dotenv
from helpers.generate import image_generate

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Рад тебя видеть. Напиши название города")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    base_url = "http://api.openweathermap.org/data/2.5"
    url = f'{base_url}/weather?q={city}&appid={os.getenv("OPENWEATHER_API_KEY")}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        image_generate(response)

        bot.send_photo(
            message.chat.id,
            caption=f"Погода в городе {city.title()}.",
            photo=open("weather.png", "rb"),
        )
    else:
        bot.reply_to(message, "Вы ввели некорректное название города.")


if __name__ == "__main__":
    bot.polling(none_stop=True)
