#!/bin/bash

echo "Stopping Gdx2 Services" 
sudo systemctl stop gdx2-celery-flower.service
sudo systemctl stop gdx2-celery-worker1.service
sudo systemctl stop gdx2-celery-worker2.service
sudo systemctl stop gdx2-celery-worker3.service
sudo systemctl stop gdx2-celery-worker4.service
sudo systemctl stop gdx2.service

echo "All services stopped." 
