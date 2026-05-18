# GDX2 — Сервис геологических отчетов

FastAPI-приложение для управления и публикации геологических отчетов с поддержкой пространственных данных.

## 📋 Оглавление

- [О проекте](#о-проекте)
- [Структура проекта](#структура-проекта)
- [Технологический стек](#технологический-стек)
- [Установка](#установка)
- [Переменные окружения](#переменные-окружения)
- [Запуск приложения](#запуск-приложения)
- [API Endpoints](#api-endpoints)
- [Примеры запросов](#примеры-запросов)
- [Тестирование](#тестирование)
- [Миграции БД](#миграции-бд)
- [Celery задачи](#celery-задачи)
- [Логирование](#логирование)
- [Production развертывание](#production-развертывание)

---

## 📖 О проекте

GDX2 — это веб-сервис для:
- Загрузки и каталогизации геологических отчетов ТГФ (Территориальные геологические фонды)
- Полнотекстового поиска по отчетам
- Работы с пространственными данными (полигоны, линии, точки)
- Генерации GeoJSON файлов
- Отслеживания истории запросов и задач

---

## 📁 Структура проекта

```
gdx2/
├── src/                          # Исходный код приложения
│   ├── main.py                   # Точка входа FastAPI приложения
│   ├── cfg.py                    # Конфигурация и переменные окружения
│   ├── models.py                 # SQLAlchemy модели базы данных
│   ├── schemas.py                # Pydantic схемы для API
│   ├── routers.py                # Основной маршрутизатор API
│   ├── log.py                    # Настройка логирования
│   ├── db/
│   │   └── db.py                 # Подключение к PostgreSQL
│   ├── api/                      # API модули
│   │   ├── health/               # Health check эндпоинты
│   │   ├── report/               # Отчеты (основной функционал)
│   │   ├── sta/                  # Полигоны
│   │   ├── stl/                  # Линии
│   │   ├── stp/                  # Точки
│   │   ├── stall/                # Сводные данные
│   │   ├── author/               # Авторы (справочник)
│   │   └── celery/               # Celery задачи
│   ├── alembic/                  # Миграции базы данных
│   ├── data/                     # GeoJSON данные
│   ├── geojson/                  # Выходные GeoJSON файлы
│   ├── upload/                   # Загружаемые файлы
│   └── log/                      # Логи приложения
├── tests/                        # Тесты
│   ├── conftest.py
│   ├── test_endpoints.py
│   ├── test_models.py
│   ├── test_schemas.py
│   ├── test_services.py
│   ├── test_utils.py
│   └── test_database.py
├── services/                     # systemd сервисы для Linux
├── .env                          # Переменные окружения (dev)
├── .env_prod                     # Переменные окружения (prod)
├── requirements.txt              # Зависимости
├── requirements-test.txt         # Тестовые зависимости
├── alembic.ini                   # Конфигурация Alembic
├── pytest.ini                    # Конфигурация pytest
├── run_windows.bat               # Скрипт запуска (Windows)
├── start_celery.bat              # Запуск Celery (Windows)
├── gdx2_start.sh                 # Скрипт запуска (Linux)
└── README.md                     # Документация
```

---

## 🛠 Технологический стек

| Компонент | Технология |
|-----------|------------|
| **Фреймворк** | FastAPI 0.109+ |
| **База данных** | PostgreSQL + PostGIS |
| **ORM** | SQLAlchemy (async) |
| **Драйвер БД** | asyncpg, psycopg2-binary |
| **Миграции** | Alembic |
| **Очереди задач** | Celery + Redis |
| **Сервер** | Uvicorn + Gunicorn |
| **Валидация** | Pydantic |
| **Excel** | openpyxl |
| **Тесты** | pytest, pytest-asyncio, httpx |

---

## 📦 Установка

### Требования
- Python 3.10+
- PostgreSQL 13+ с расширением PostGIS
- Redis 6+

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd gdx2
```

### 2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

```sql
-- Создание пользователя и базы данных
CREATE USER gdx2 WITH PASSWORD 'gdx2password';
CREATE DATABASE gdx2 OWNER gdx2;
\c gdx2
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

### 5. Применение миграций

```bash
alembic upgrade head
```

---

## 🔧 Переменные окружения

### Основные переменные (.env)

| Переменная | Описание | По умолчанию | Пример |
|------------|----------|--------------|--------|
| `DEVENV` | Окружение (dev/prod) | `dev` | `dev` |
| `GDX2_SERVER_HOST` | Хост сервера | `0.0.0.0` | `0.0.0.0` |
| `GDX2_SERVER_PORT` | Порт сервера | `8001` | `8001` |
| `GDX2_SCHEMA` | Схема БД | `gdx2` | `gdx2` |
| `GDX2_DB_DSN` | DSN подключения к БД | - | `postgresql://user:pass@host:5432/dbname` |
| `REDIS_HOST` | Хост Redis | `localhost` | `localhost` |
| `REDIS_PORT` | Порт Redis | `6379` | `6379` |
| `NUMBER_PROCESS` | Количество процессов | `1` | `4` |

### Пример .env для разработки

```env
DEVENV=dev
GDX2_SERVER_HOST=0.0.0.0
GDX2_SERVER_PORT=8001
GDX2_SCHEMA=gdx2
GDX2_DB_DSN=postgresql://gdx2:secure_password@localhost:5432/gdx2
REDIS_HOST=localhost
REDIS_PORT=6379
NUMBER_PROCESS=1
```

### Пример .env для production

```env
DEVENV=prod
GDX2_SERVER_HOST=0.0.0.0
GDX2_SERVER_PORT=8001
GDX2_SCHEMA=gdx2
GDX2_DB_DSN=postgresql://gdx2:secure_password@server:5432/gdx2
REDIS_HOST=localhost
REDIS_PORT=6379
NUMBER_PROCESS=4
```

---

## 🚀 Запуск приложения

### Разработка (Windows)

```bash
# Запуск основного сервиса
run_windows.bat

# Или вручную
uvicorn src.main:app --reload --host 0.0.0.0 --port 8001
```

### Разработка (Linux)

```bash
./gdx2_start.sh
```

### Production

```bash
# Windows
start_gdx2_deploy.bat

# Linux (с использованием systemd)
sudo systemctl start gdx2
sudo systemctl enable gdx2
```

### Запуск Celery workers

```bash
# Windows
start_celery.bat

# Linux
 celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h
 celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker2@%h
 celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker3@%h
```

### Запуск Flower (мониторинг Celery)

```bash
celery -A src.api.celery.celery_app flower --port=5555
```

---

## 🌐 API Endpoints

### Главная

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/` | Информация о сервисе |
| GET | `/docs` | Swagger документация |
| GET | `/redoc` | ReDoc документация |

### Health Check

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/health` | Проверка работоспособности |

### Отчеты (Report)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/api/v1/report/upload/` | Загрузка Excel файла |
| GET | `/api/v1/report/update` | Обновление из файла |
| GET | `/api/v1/report/updatefromfiletask` | Обновление через Celery задачу |
| GET | `/api/v1/report/all` | Все отчеты |
| GET | `/api/v1/report/count` | Количество отчетов |
| GET | `/api/v1/report/rgf/all` | Отчеты РГФ |
| GET | `/api/v1/report/tgf/all` | Отчеты ТГФ |
| GET | `/api/v1/report/year/{year}` | Отчеты по году |
| GET | `/api/v1/report/author` | Авторы отчетов |
| GET | `/api/v1/report/search/{str}` | Полнотекстовый поиск |
| POST | `/api/v1/report/message` | Создать сообщение |
| GET | `/api/v1/report/message` | Получить сообщения |

### Полигоны (STA)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/sta/all` | Все полигоны |
| GET | `/api/v1/sta/count` | Количество полигонов |
| GET | `/api/v1/sta/{id}` | Полигон по ID |
| GET | `/api/v1/sta/rosg/{rosg}` | Полигоны по ROSG |

### Линии (STL)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/stl/all` | Все линии |
| GET | `/api/v1/stl/count` | Количество линий |
| GET | `/api/v1/stl/{id}` | Линия по ID |

### Точки (STP)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/stp/all` | Все точки |
| GET | `/api/v1/stp/count` | Количество точек |
| GET | `/api/v1/stp/{id}` | Точка по ID |

### Сводные данные (STALL)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/stall/all/method/unique` | Уникальные методы |
| GET | `/api/v1/stall/all/vid_iz/unique` | Уникальные виды изученности |
| GET | `/api/v1/stall/all/god_nach/unique` | Уникальные годы начала |

### Авторы (Author)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/v1/author/all` | Все авторы |
| GET | `/api/v1/author/count` | Количество авторов |
| GET | `/api/v1/author/{guid}` | Автор по GUID |
| POST | `/api/v1/author/` | Создать автора |
| PUT | `/api/v1/author/{guid}` | Обновить автора |
| DELETE | `/api/v1/author/{guid}` | Удалить автора |

---

## 📝 Примеры запросов

### 1. Получить информацию о сервисе

```bash
curl http://localhost:8001/
```

**Ответ:**
```json
{
  "msg": "Success",
  "Info": "Hello it is FastAPI-NSI project",
  "Swagger Documentation": "http://0.0.0.0:8001/docs"
}
```

### 2. Health check

```bash
curl http://localhost:8001/api/v1/health
```

**Ответ:**
```json
{
  "msg": "pong!"
}
```

### 3. Получить все отчеты

```bash
curl http://localhost:8001/api/v1/report/all
```

### 4. Получить количество отчетов

```bash
curl http://localhost:8001/api/v1/report/count
```

**Ответ:**
```json
{
  "count": 1234
}
```

### 5. Полнотекстовый поиск

```bash
curl http://localhost:8001/api/v1/report/search/нефтегазоносность
```

### 6. Загрузка Excel файла

```bash
curl -X POST \
  -F "file=@/path/to/report.xlsx" \
  http://localhost:8001/api/v1/report/upload/
```

### 7. Фильтрация по году

```bash
curl http://localhost:8001/api/v1/report/year/2023
```

### 8. Получение всех авторов (справочник)

```bash
curl http://localhost:8001/api/v1/author/all
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 42,
  "data": [
    {
      "guid": "550e8400-e29b-41d4-a716-446655440000",
      "name_ru": "Иванов И.И.",
      "created_at": "2024-01-15T10:30:00",
      "updated_at": "2024-01-15T10:30:00"
    }
  ]
}
```

### 9. Получение количества авторов

```bash
curl http://localhost:8001/api/v1/author/count
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 42
}
```

### 10. Получение автора по GUID

```bash
curl http://localhost:8001/api/v1/author/550e8400-e29b-41d4-a716-446655440000
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 1,
  "data": {
    "guid": "550e8400-e29b-41d4-a716-446655440000",
    "name_ru": "Иванов И.И.",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T10:30:00"
  }
}
```

### 11. Создание автора

```bash
curl -X POST "http://localhost:8001/api/v1/author/?name_ru=Петров%20П.П."
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 1,
  "data": {
    "guid": "660e8400-e29b-41d4-a716-446655440001",
    "name_ru": "Петров П.П.",
    "created_at": "2024-06-01T12:00:00",
    "updated_at": "2024-06-01T12:00:00"
  }
}
```

### 12. Обновление автора

```bash
curl -X PUT "http://localhost:8001/api/v1/author/550e8400-e29b-41d4-a716-446655440000?name_ru=Иванов%20Иван%20Иванович"
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 1,
  "data": {
    "guid": "550e8400-e29b-41d4-a716-446655440000",
    "name_ru": "Иванов Иван Иванович",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-06-01T12:05:00"
  }
}
```

### 13. Удаление автора

```bash
curl -X DELETE http://localhost:8001/api/v1/author/550e8400-e29b-41d4-a716-446655440000
```

**Ответ:**
```json
{
  "msg": "OK",
  "count": 1,
  "data": "Author with guid 550e8400-e29b-41d4-a716-446655440000 deleted"
}
```

### 14. Использование с авторизацией (если добавится)

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8001/api/v1/report/all
```

### 15. Python пример (httpx)

```python
import httpx
import asyncio

async def get_reports():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/api/v1/report/all")
        return response.json()

# Запуск
reports = asyncio.run(get_reports())
print(reports)
```

---

## 🧪 Тестирование

### Установка тестовых зависимостей

```bash
pip install -r requirements-test.txt
```

### Запуск всех тестов

```bash
pytest
```

### Запуск с подробным выводом

```bash
pytest -v
```

### Запуск с покрытием (требуется pytest-cov)

```bash
pytest --cov=src --cov-report=html
```

### Запуск конкретных тестов

```bash
# Конкретный файл
pytest tests/test_endpoints.py -v

# Конкретная функция
pytest tests/test_endpoints.py::test_root -v

# По маркеру
pytest -m smoke
```

### Структура тестов

| Файл | Описание | Статус |
|------|----------|--------|
| `test_endpoints.py` | Тесты API эндпоинтов | ✅ 10 тестов |
| `test_models.py` | Тесты моделей | ⚠️ Базовые |
| `test_schemas.py` | Тесты схем | ⚠️ Частичные |
| `test_services.py` | Тесты сервисов | ❌ Требует реализации |
| `test_utils.py` | Тесты утилит | ⚠️ Минимальные |
| `test_database.py` | Тесты БД | ⚠️ Требует БД |

### Конфигурация pytest (pytest.ini)

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v
```

---

## 🗄 Миграции БД

### Инициализация Alembic

```bash
# Первая инициализация (если нет migrations)
alembic init alembic
```

### Создание новой миграции

```bash
# Автогенерация на основе моделей
alembic revision --autogenerate -m "Description of changes"

# Пустая миграция
alembic revision -m "Add new column"
```

### Применение миграций

```bash
# Применить все миграции
alembic upgrade head

# Применить одну миграцию
alembic upgrade +1

# Откатить одну миграцию
alembic downgrade -1

# Откатить к конкретной
alembic downgrade <revision_id>
```

### Проверка статуса

```bash
# Показать текущую версию
alembic current

# Показать все миграции
alembic history
```

---

## ⚙️ Celery задачи

### Конфигурация

Celery использует Redis как брокер и бэкенд результатов.

```python
# Конфигурация по умолчанию
CELERY_BROKER_URL = redis://localhost:6379/0
CELERY_RESULT_BACKEND = redis://localhost:6379/0
```

### Запуск worker

```bash
# Базовый запуск
celery -A src.api.celery.celery_app worker --loglevel=info

# С несколькими процессами
celery -A src.api.celery.celery_app worker --loglevel=info --concurrency=4

# Для Windows (solo pool)
celery -A src.api.celery.celery_app worker --loglevel=info --pool=solo
```

### Запуск beat (периодические задачи)

```bash
celery -A src.api.celery.celery_app beat --loglevel=info
```

### Мониторинг с Flower

```bash
celery -A src.api.celery.celery_app flower --port=5555
```

Доступ к Flower: http://localhost:5555

---

## 📊 Логирование

### Формат логов

```
%(asctime)s %(levelname)s %(message)s
```

### Расположение логов

```
src/log/
├── YYYY-MM-DD-HH-MM-SS_gdx2.log
```

### Уровень логирования

- **Dev**: INFO, DEBUG
- **Prod**: WARNING, ERROR

### Пример логирования в коде

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Starting process")
logger.debug("Debug info")
logger.error("Error occurred")
```

---

## 🚀 Production развертывание

### Systemd сервисы (Linux)

Файлы сервисов расположены в `services/`:

- `gdx2.service` — основной сервис
- `gdx2-celery-worker[1-5].service` — воркеры Celery
- `gdx2-celery-flower.service` — мониторинг Flower

### Установка сервисов

```bash
# Копирование сервисов
sudo cp services/gdx2.service /etc/systemd/system/
sudo cp services/gdx2-celery-worker*.service /etc/systemd/system/

# Перезагрузка systemd
sudo systemctl daemon-reload

# Включение сервисов
sudo systemctl enable gdx2
sudo systemctl enable gdx2-celery-worker1
# ... остальные воркеры

# Запуск
sudo systemctl start gdx2
```

### Мониторинг

```bash
# Статус сервисов
sudo systemctl status gdx2

# Просмотр логов
sudo journalctl -u gdx2 -f

# Перезапуск
sudo systemctl restart gdx2
```

### Nginx конфигурация (пример)

```nginx
server {
    listen 80;
    server_name gdx2.example.com;

    location / {
        proxy_pass http://localhost:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /docs {
        proxy_pass http://localhost:8001/docs;
    }
}
```

---

## 🔒 Безопасность

### CORS

По умолчанию CORS разрешает все origins (**только для разработки!**).

Для production настройте в `src/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-domain.com",
        "https://www.your-domain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Рекомендации

1. Используйте HTTPS в production
2. Храните секреты в vault/secrets manager
3. Ограничьте доступ к базе данных
4. Настройте rate limiting
5. Включите аутентификацию для чувствительных endpoints

---

## 🤝 Вклад в проект

### Code Style

Проект использует:
- Black для форматирования
- Flake8 для линтинга
- Type hints для типизации

### Pre-commit хуки (рекомендуется)

```bash
pip install pre-commit
pre-commit install
```

### Запуск линтеров

```bash
# Форматирование
black src/ tests/

# Линтинг
flake8 src/ tests/

# Проверка типов
mypy src/
```

---

## 📄 Лицензия

[Укажите лицензию проекта]

---

## 📞 Контакты

- **Разработчик**: Замараев В.В.
- **Документация API**: http://localhost:8001/docs
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

---

## 🙏 Благодарности

- FastAPI команда
- SQLAlchemy команда
- Все контрибьюторы проекта
