#!/bin/bash

echo "Starting Gdx2 Services" 
sudo systemctl start gdx2-celery-flower.service
sudo systemctl start gdx2-celery-worker1.service
sudo systemctl start gdx2-celery-worker2.service
sudo systemctl start gdx2-celery-worker3.service
sudo systemctl start gdx2-celery-worker4.service
sudo systemctl start gdx2-celery-worker5.service
sudo systemctl start gdx2.service

sudo systemctl status gdx2-celery-flower.service
sudo systemctl status gdx2-celery-worker1.service
sudo systemctl status gdx2-celery-worker2.service
sudo systemctl status gdx2-celery-worker3.service
sudo systemctl status gdx2-celery-worker4.service
sudo systemctl status gdx2.service
echo "All services launched in background." 
