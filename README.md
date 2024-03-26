# для начала нужно скачать виртуальное окружение

в терминал прописываем:
```
python3 -m venv venv
```

# далее её нужно активировать
для Linux):
```
source venv/bin/activate
```
 (для Windows):
```
venv\Scripts\activate
```

# далее скачиваем все необходимые зависимости

## для запуска проекта требуется :
```
pip install -r requirements/prod.txt
```
## для теста проекта требуется:
```
pip install -r requirements/test.txt
```
## для разработки проекта требуется:
```
pip install -r requirements/dev.txt
```
# Чтобы запустить сервер в dev-режиме
```
cd 2222
```
```
cd lyceum
```
```
python manage.py runserver
```
# для того чтобы сделать Fixture /data.json пишем в терминал:
```
cd 2222
```
```
cd lyceum
```
```
python manage.py dumpdata catalog > fixtures/data.json
```

