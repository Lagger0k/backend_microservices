# Backend microservices.
Задача: Создать backend часть, состоящую из нескольких сервисов:
1. Сервер очередей rabbitmq
2. API с методом /queue_reverse_text.
В качестве параметра должен быть произвольный текст.
Обработка заключается в том, что запрос попадает в очередь rabbitmq. (реализовано на FastAPI).
3. Background worker.
Читает очередь заданий в rabbitmq, выполняет их обработку переворачивая текст.
4. WEBSOCKET API Пассивно получает результаты обработки задач по мере их получения.
# Запуск:
1. Скачать репозиторий себе в проект.
2. Выполнить команду `docker-compose up -d --build`
3. Для тестирования запустить скрипт `queue_reverse_text.py` и ввести в терминале произвольный текст.

Посмотреть результат работы можно подключившись к контейнеру с именем **websocket_container**
