# api_final

Yatube API — backend сервис блог-платформы с постами, группами, комментариями и подписками.

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
