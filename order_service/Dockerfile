# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код сервиса
COPY order_service.py order_service.py
COPY order_service.proto order_service.proto

# Запуск сервиса
CMD ["python", "order_service.py"]
