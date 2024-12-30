# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Генерация файлов из .proto
COPY user_service.proto user_service.proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user_service.proto

# Копируем код сервиса
COPY user_service.py user_service.py

# Запуск сервиса
CMD ["python", "user_service.py"]
