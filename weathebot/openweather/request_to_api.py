import os
import requests
import logging

loger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class WeatherRequest:
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

    def get_city(self, message):
        city = message.text.strip().lower()
        url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url)
        loger.info(response.text)

        return response

    def get_location(self, message):
        loger.info(message.location)
        latitude = message.location.latitude
        longitude = message.location.longitude
        url = f"{self.base_url}lat={latitude}&lon={longitude}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url)
        loger.info(response.text)

        return response
