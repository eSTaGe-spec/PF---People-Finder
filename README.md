PF - People Finder
People Finder (PF) - аналог фриланс сайтов. Это максимально упрощенная версия, но с рабочим JavaScript и Django Rest Framework (DRF).
Особенности
PF поддерживает следующие функции:

1) Регистрация и вход в систему пользователей.
2) Создание заданий.
3) Просмотр всех заданий.
4) Просмотр всех пользователей и их профилей.
5) Редактирование профиля.
6) Возможность взять на выполнение задание
7) Просмотр в профиле созданных и взятых заданий.

Используемые технологии
  <ul>
    <li>Python</li>
    <li>Django & DRF</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
  </ul>
    

База данных SQLite используется для хранения данных.
Установка
Для установки PF выполните следующие действия:

Клонируйте репозиторий:

    git clone https://github.com/eSTaGe-spec/PF---People-Finder.git

Создайте и активируйте виртуальное окружение:



    python -m venv venv
    .\venv\Scripts\activate

Установите необходимые зависимости:



    pip install -r requirements.txt

Перейдите в директорию проекта и выполните миграции:


    cd app
    python manage.py makemigrations
    python manage.py migrate

Создайте суперпользователя:

    python manage.py createsuperuser

Запустите сервер:


    python manage.py runserver

Теперь вы можете войти в систему под учетной записью суперпользователя и начать использовать PF!

Добавьте данных в бд для лучшего использования сайта
http://127.0.0.1:8000/admin/

P.S
Возможны поправки проекта в будущем
