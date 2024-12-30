# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Генерация файлов из .proto
COPY order_service.proto order_service.proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order_service.proto

# Копируем код сервиса
COPY order_service.py order_service.py

# Запуск сервиса
CMD ["python", "order_service.py"]
