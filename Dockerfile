FROM python:3.12

WORKDIR /app

RUN pip install poetry

# Configuring poetry
RUN poetry config virtualenvs.create false
RUN poetry config cache-dir /tmp/poetry_cache

COPY . .
# Copying requirements of a project
COPY poetry.lock pyproject.toml /app

RUN poetry install

EXPOSE 8000

CMD ["gunicorn", "sw_task.wsgi:application", "--bind", "0.0.0.0:8000"]