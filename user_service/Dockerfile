# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код сервиса
COPY user_service.py user_service.py
COPY user_service.proto user_service.proto

# Запуск сервиса
CMD ["python", "user_service.py"]
