import datetime

from PIL import Image, ImageDraw, ImageFont


def image_generate(response):
    width, height = 800, 600
    background_color = (255, 255, 255)  # Белый цвет
    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)

    city = response.json()["name"]
    weather_description = response.json()["weather"][0]["description"]
    current_temperature = response.json()["main"]["temp"]
    feel_temperature = response.json()["main"]["feels_like"]
    wind_speed = response.json()["wind"]["speed"]
    sunrise = response.json()["sys"]["sunrise"]
    sunset = response.json()["sys"]["sunset"]

    readable_sunrise = datetime.datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")
    readable_sunset = datetime.datetime.fromtimestamp(sunset).strftime("%H:%M:%S")

    text = (
        f"Город: {city}\n"
        f"Погода: {weather_description}\n"
        f"Текущая температура: {current_temperature} {chr(0x00B0)}С\n"
        f"Ощущается как: {feel_temperature} {chr(0x00B0)}С\n\n"
        f"Скорость ветра: {wind_speed} м/c\n"
        f"Рассвет: {readable_sunrise}\n"
        f"Закат: {readable_sunset}"
    )
    font = ImageFont.truetype("arial.ttf", 35)
    text_bbox = draw.textbbox((0, 0), text, font=font)

    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((width - text_width) / 2, (height - text_height) / 2)
    text_color = (0, 0, 0)

    draw.text(position, text, font=font, fill=text_color)

    image.save("weather.png")
