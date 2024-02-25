# для начала нужно скачать виртуальное окружение

в терминал прописываем:
python3 -m venv venv

# далее её нужно активировать

source venv/bin/activate (для Linux)

venv\Scripts\activate (для Windows)

# далее скачиваем все необходимые зависимости

pip install -r requirements.txt

# запускаем сервер в dev-режиме
cd 2222

cd lyceum

python manage.py runserver
