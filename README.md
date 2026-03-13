


### 1. Клонируйте репозиторий
```sh
git clone https://github.com/Saifullakh1/inti
cd inti
```

### 2. Создайте и активируйте виртуальное окружение
```sh
python3 -m venv env
source env/bin/activate
```

### 3. Установите зависимости
```sh
pip install -r requirements.txt
```

### 4. Примените миграции
```sh
python manage.py migrate
```

### 5. Запустите сервер
```sh
python manage.py runserver
```

### 6. Создать SuperUser
```sh
python manage.py createsuperuser
```
