# Микросервисная архитектура для платформы онлайн-торговли

## Описание проекта

Этот проект реализует микросервисную архитектуру для платформы онлайн-торговли. В состав системы входят пять микросервисов, которые взаимодействуют между собой через gRPC:

- **Сервис управления пользователями (User Service):** управление данными пользователей и аутентификация.
- **Сервис обработки заказов (Order Service):** создание и управление заказами.
- **Сервис управления платежами (Payment Service):** обработка и управление транзакциями.
- **Сервис отслеживания заказов (Tracking Service):** отслеживание состояния заказов.
- **Сервис отзывов (Review Service):** оставление и чтение отзывов.

## Структура проекта

```
project_root/
├── user_service/         # Сервис управления пользователями
│   ├── user_service.py   # Основной код сервиса
│   ├── user_service.proto # gRPC спецификация
│   ├── Dockerfile        # Docker-конфигурация
│   └── requirements.txt  # Зависимости для Python
├── order_service/        # Сервис обработки заказов
│   ├── order_service.py
│   ├── order_service.proto
│   ├── Dockerfile
│   └── requirements.txt
├── payment_service/      # Сервис управления платежами
│   ├── payment_service.py
│   ├── payment_service.proto
│   ├── Dockerfile
│   └── requirements.txt
├── tracking_service/     # Сервис отслеживания заказов
│   ├── tracking_service.py
│   ├── tracking_service.proto
│   ├── Dockerfile
│   └── requirements.txt
├── review_service/       # Сервис отзывов
│   ├── review_service.py
│   ├── review_service.proto
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml    # Конфигурация для сборки и запуска всех сервисов
├── README.md             # Документация
└── .gitignore            # Исключения для Git
```

## Установка и запуск

1. **Установите Docker и Docker Compose**
   Убедитесь, что Docker установлен и работает на вашей системе.

2. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/igralkin/ProtoProject.git
   cd microservices-platform
   ```

3. **Соберите и запустите контейнеры**
   Используйте команду:
   ```bash
   docker-compose up --build
   ```

4. **Тестирование взаимодействия**
   Вы можете использовать gRPC-клиент, например [BloomRPC](https://github.com/bloomrpc/bloomrpc), для тестирования методов каждого сервиса.

## Зависимости

- Python >= 3.8
- grpcio
- grpcio-tools
- Docker >= 20.10
- Docker Compose >= 1.29

## Взаимодействие микросервисов

Диаграмма компонентов системы демонстрирует взаимодействие между микросервисами (добавьте сюда ссылку или изображение диаграммы).

## Лицензия

Проект распространяется под MIT License. Подробнее см. [LICENSE](LICENSE).
