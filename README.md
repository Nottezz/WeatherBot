# WeatherBOT

Телеграмм-бот [@PeperWeatherBot](https://t.me/PeperWeatherBot) предназначен для ознакомления с текущей погодой в указанном городе или в вашей локации.

## .env переменные

- `TOKEN` - Telegram bot токен
- `OPENWEATHER_API_KEY` - токен для работы с API сервиса [openweathermap.org](https://openweathermap.org/)

## Dev scripts

- `poetry run lint` - run isort, black and mypy check 
- `poetry run format` - start formatting