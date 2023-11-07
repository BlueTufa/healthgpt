FROM python:3.11-slim-bookworm

WORKDIR /app/server

COPY src/ .

RUN pip install --upgrade pip poetry
RUN poetry build

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "5", "--log-level", "debug"]
