#!/bin/bash

# Настройки окружения
#export DEVENV=prod
#export GDX2_SERVER_HOST=0.0.0.0
#export GDX2_SERVER_PORT=8001
#export GDX2_SCHEMA=gdx2
#export GDX2_DB_DSN="postgresql://gdx2:gdx2pwd@r48-vpg01.zsniigg.local:5432/gdx2"
#export REDIS_HOST=localhost
#export REDIS_PORT=6379
#export NUMBER_PROCESS=1

# Запуск pg_tileserv (если установлен как исполняемый, или через скрипт)
# Убедитесь, что путь корректен и start_tileserv.bat адаптирован под Linux
# Допустим, вы сделали аналогичный .sh скрипт или запускаете напрямую pg_tileserv
#
# Пример (если pg_tileserv в PATH):
#
#nohup pg_tileserv --host $GDX2_SERVER_HOST --port $GDX2_SERVER_PORT > pg_tileserv.log 2>&1 &

# Если у вас есть отдельный скрипт start_tileserv.sh — раскомментируйте:
# nohup /path/to/start_tileserv.sh > tileserv.log 2>&1 &

#echo "pg_tileserv started"

# Запуск Celery workers (в фоне)
cd /opt/gdx2 || exit 1  # ← Замените на реальный путь к проекту

nohup celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h > worker1.log 2>&1 &
sleep 1
nohup celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker2@%h > worker2.log 2>&1 &
sleep 1
nohup celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker3@%h > worker3.log 2>&1 &
sleep 1
nohup celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker4@%h > worker4.log 2>&1 &
sleep 1
nohup celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker5@%h > worker5.log 2>&1 &

echo "Celery workers started" > gdx2.log 2>&1 &

# Запуск Flower
nohup celery -A src.api.celery.tasks:celery flower --port=5555 > flower.log 2>&1 &
echo "Celery Flower started on http://localhost:5555"  > gdx2.log 2>&1 &

# Запуск основного Python-приложения
nohup python3 src/main.py > gdx2.log 2>&1 &
echo "Main application started" > gdx2.log 2>&1 &

echo "All services launched in background." > gdx2.log 2>&1 &
