rem set DEVENV=prod
rem set DB_HOST=r48-vldb02.zsniigg.local
rem set DB_NAME=gdx2
rem set DB_SCHEMA=gdx2
rem set DB_USER=gdx2
rem set DB_PASS=gdx2pwd

set DEVENV=prod

set GDX2_SERVER_HOST=0.0.0.0
set GDX2_SERVER_PORT=8001
set GDX2_SCHEMA=gdx2
set GDX2_DB_DSN=postgresql://gdx2:gdx2pwd@r48-vldb02.zsniigg.local:5432/gdx2

set REDIS_HOST=localhost
set REDIS_PORT=6379

set NUMBER_PROCESS=1


start C:\Apps\pg_tileserv\start_tileserv.bat

start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker2@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker3@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker4@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker5@%h
start celery -A src.api.celery.tasks:celery flower
start python src\main.py


