# Отправка не ревью № 1

## Подготовка и запуск проекта

### Склонировать репозиторий на локальную машину

*git clone <https://https://github.com/Nikita-Kechaev/foodgram-project-react>

*Cоздайте .env файл в директории backend/foodgram/fodgram/ и впишите:

    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    POSTGRES_USER=<пользователь бд>
    POSTGRES_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    DJANGO_SECRET_KEY=<секретный ключ проекта django>
    DJANGO_DEBUG=1
    ```
*перейдите в директорию infra/
*выполните команду sudo docker-compose up
*выполните миграции

    ```
    sudo docker-compose exec backend python manage.py makemigrations
    sudo docker-compose exec backend python manage.py migrate
    ```
*создайте суперпользователя

    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
Админ-панель проекта доступна по адресу

    ```
    http://127.0.0.1:8000/admin
    ```
Проект доступен по адресу

    ```
    http://127.0.0.1:8000
    ```
