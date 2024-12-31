import logging
import os

import requests
from requests import Response
from telebot.types import Message  # type: ignore

loger = logging.getLogger(__name__)


class WeatherRequest:
    def __init__(self) -> None:
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

    def get_city(self, message: Message) -> Response:
        city = message.text.strip().lower()
        url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url)
        loger.info(response.text)

        return response

    def get_location(self, message: Message) -> Response:
        loger.info(message.location)
        latitude = message.location.latitude
        longitude = message.location.longitude
        url = f"{self.base_url}lat={latitude}&lon={longitude}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url)
        loger.info(response.text)

        return response
