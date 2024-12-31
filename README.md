Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:mainer93/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Заполните файл .env:

```
APP_TITLE=Фонд поддержки котиков
APP_DESCRIPTION=Приложение для Благотворительного фонда поддержки котиков
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=SECRET_KEY
FIRST_SUPERUSER_EMAIL=superuser@example.com
FIRST_SUPERUSER_PASSWORD=yourpassword
```

Выполните все неприменённые миграции через команду:

```
alembic upgrade head
```

Запустите проект:

```
uvicorn app.main:app --reload
```

Создание отчета в Google Sheets:
1. Создайте проект в Google Cloud Platform — связующее звено между нужными Google API и Python-приложением
2. Подключите к проекту два API: Google Sheets API и Google Drive API
3. Создайте сервисный аккаунт
4. Получите ключ и JSON-файл с данными сервисного аккаунта, чтобы управлять подключёнными API из Python-приложения
5. Дозаполните файл .env по шаблону:

```
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
EMAIL=
```