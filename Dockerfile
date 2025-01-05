FROM python:3.12.8-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


WORKDIR /WeatherBot

RUN pip install --upgrade pip wheel "poetry==1.8.4"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY weatherbot ./weatherbot

CMD ["poetry","run", "start"]
