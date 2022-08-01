FROM python:3.9.13-alpine

ENV POETRY_VERSION=1.1.14

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

COPY ping.py ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

ENTRYPOINT ["python", "./ping.py"]