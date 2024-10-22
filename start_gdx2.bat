set DEVENV=prod
set DB_HOST=r48-vldb02.zsniigg.local
set DB_NAME=gdx2
set DB_SCHEMA=gdx2
set DB_USER=gdx2
set DB_PASS=gdx2pwd

set GDX2_SERVER_PORT=8001
set GDX2_DB_DSN=postgresql://gdx2map:gdx2mappwd@r48-vldb02.zsniigg.local:5432/gdx2map
start gdx2map_backend.exe

start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker2@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker3@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker4@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker5@%h
start celery -A src.api.celery.tasks:celery flower
start python src\main.py


