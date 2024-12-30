# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Генерация файлов из .proto
COPY ../protos /protos
RUN python -m grpc_tools.protoc -I/protos --python_out=. --grpc_python_out=. /protos/order_service.proto /protos/user_service.proto

# Копируем код сервиса
COPY order_service.py order_service.py

# Запуск сервиса
CMD ["python", "order_service.py"]
