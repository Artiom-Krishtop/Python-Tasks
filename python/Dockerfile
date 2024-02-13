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
# COPY ./№1_2 /app/№1_2
# COPY ./№2_2 /app/№2_2

# Команда, которая будет выполнена при запуске контейнера
CMD ["python3", "№2_2/main.py"]