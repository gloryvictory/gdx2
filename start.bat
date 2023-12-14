start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker2@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker3@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker4@%h
start celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker5@%h
start celery -A src.api.celery.tasks:celery flower
start python src\main.py


