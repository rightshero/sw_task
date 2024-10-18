FROM python:3.12

WORKDIR  /app

COPY ./pyproject.toml  ./poetry.lock /app

RUN pip install poetry==1.8.3

RUN poetry config virtualenvs.create false

RUN poetry install


COPY .  .
