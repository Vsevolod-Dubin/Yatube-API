# Yatube API

**Yatube API** is a RESTful backend service for a social blogging platform.  
It provides endpoints for user registration, creating posts and comments, following authors, and browsing personalized feeds.

## Technologies

- Python 3.9+
- Django
- Django REST Framework
- Simple JWT

## Installation

```bash
git clone <repo-url>
cd yatube_api
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Example Requests

### Get all posts
```http
GET /api/v1/posts/
```

### Create a post
```http
POST /api/v1/posts/
Content-Type: application/json

{
  "text": "New post",
  "group": 1
}
```

### Get comments for a post
```http
GET /api/v1/posts/1/comments/
```

### Follow a user
```http
POST /api/v1/follow/
Content-Type: application/json

{
  "following": "username"
}
```

### Get JWT tokens
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "TestUser",
  "password": "1234567"
}
```

## Documentation

After starting the project, API documentation is available at:
```
http://localhost:8000/redoc/
```

## Author

[Vsevolod](https://github.com/Vsevolod-Dubin)

<details>
<summary>🇷🇺 Нажмите, чтобы раскрыть описание на русском</summary>

# api_final

**Yatube API** — backend сервис блог-платформы с постами, группами, комментариями и подписками.

## Технологии

- Python 3.9+
- Django
- Django REST Framework
- Simple JWT

## Установка

```bash
git clone <repo-url>
cd yatube_api
python -m venv env
source env/bin/activate  # или env\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Примеры запросов

### Получить все посты
```http
GET /api/v1/posts/
```

### Создать пост
```http
POST /api/v1/posts/
Content-Type: application/json

{
  "text": "Новый пост",
  "group": 1
}
```

### Получить комментарии к посту
```http
GET /api/v1/posts/1/comments/
```

### Подписаться на пользователя
```http
POST /api/v1/follow/
Content-Type: application/json

{
  "following": "username"
}
```

### Получить токены JWT
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "TestUser",
  "password": "1234567"
}
```

## Документация

После запуска проекта документация доступна по адресу:
```
http://localhost:8000/redoc/
```

## Автор

[Vsevolod](https://github.com/Vsevolod-Dubin)

</details>
