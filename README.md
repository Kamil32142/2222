# для начала нужно скачать виртуальное окружение

в терминал прописываем:
```
python3 -m venv venv
```

# далее её нужно активировать

source venv/bin/activate (для Linux)

venv\Scripts\activate (для Windows)

# далее скачиваем все необходимые зависимости

## для запуска проекта требуется :

pip install -r requirements/prod.txt

## для теста проекта требуется:

pip install -r requirements/test.txt

## для разработки проекта требуется:

pip install -r requirements/dev.txt

# Чтобы запустить сервер в dev-режиме
cd 2222

cd lyceum

python manage.py runserver
