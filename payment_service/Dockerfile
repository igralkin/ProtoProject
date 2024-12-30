# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Генерация файлов из .proto
COPY ../protos /protos
RUN python -m grpc_tools.protoc -I/protos --python_out=. --grpc_python_out=. /protos/payment_service.proto

# Копируем код сервиса
COPY payment_service.py payment_service.py

# Запуск сервиса
CMD ["python", "payment_service.py"]
