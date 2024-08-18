import os
import telebot
import requests
import logging

from dotenv import load_dotenv
from helpers.generate import image_generate

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

loger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Рад тебя видеть. Напиши название города")
    loger.info(message.chat)


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    base_url = "https://api.openweathermap.org/data/2.5"
    url = f'{base_url}/weather?q={city}&appid={os.getenv("OPENWEATHER_API_KEY")}&units=metric'
    response = requests.get(url)
    loger.info(response.text)

    if response.status_code == 200:
        image_generate(response)

        bot.send_photo(
            message.chat.id,
            caption=f"Погода в городе {city.title()}.",
            photo=open("weather.png", "rb"),
        )
        loger.info('Success')
    else:
        bot.reply_to(message, "Вы ввели некорректное название города.")
        loger.error(response.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)
