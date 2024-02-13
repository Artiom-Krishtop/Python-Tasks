FROM python:latest

# Установка зависимостей проекта
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        && \
    rm -rf /var/lib/apt/lists/*

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование зависимостей проекта и установка их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта в контейнер
# COPY . /app

# Команда, которая будет выполнена при запуске контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]