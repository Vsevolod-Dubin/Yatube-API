# api_final
api final

## Описание
Yatube API — backend сервис блог-платформы с постами, группами, комментариями и подписками.

## Установка
```bash
git clone <repo-url>
cd yatube_api
python -m venv env
source env/bin/activate  # или env\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Получить все посты
GET /api/v1/posts/

# Создать пост
POST /api/v1/posts/ 
Content-Type: application/json
{
  "text": "Новый пост",
  "group": 1
}

# Получить комментарии к посту
GET /api/v1/posts/1/comments/

# Подписаться на пользователя
POST /api/v1/follow/ 
Content-Type: application/json
{
  "following": "username"
}

# Получить токены JWT
POST /api/v1/jwt/create/
{
  "username": "TestUser",
  "password": "1234567"
}