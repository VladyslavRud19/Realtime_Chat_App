# Real-Time Chat Application

## Опис
Інтерактивний чат із підтримкою WebSocket, кімнат, авторизації, обміну файлами та моніторингу з'єднань.

## Встановлення
1. Встановіть Docker та Docker Compose.
2. Клонуйте репозиторій: `git clone <repo-url>`
3. Запустіть: `docker-compose up --build`

## Використання
- Відкрийте `http://localhost:3000` у браузері.
- Введіть ID кімнати та надсилайте повідомлення/файли.

## Приклади повідомлень
- Текст: `{"type": "text", "message": "Hello!"}`
- Файл: `{"type": "file", "filename": "doc.pdf", "content": "base64data"}`