#!/bin/bash
# Запуск Celery workers (в фоне)
cd /opt/gdx2 || exit 1  # ← Замените на реальный путь к проекту

export PATH=$PATH:/usr/local/bin


#nohup
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
exec celery -A src.api.celery.tasks:celery flower --port=5555 > flower.log 2>&1 &
echo "Celery Flower started on http://localhost:5555"  > gdx2.log 2>&1 &
