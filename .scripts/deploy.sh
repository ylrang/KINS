#!/bin/bash
set -e

# Activate Virtual Env
source /home/devncnc/project/venv/bin/activate
echo "Virtual env 'venv' Activated !"

#echo "Clearing Cache..."
#python manage.py clean_pyc
#python manage.py clear_cache

echo "Installing Dependencies..."
pip install -r requirements.txt --no-input

echo "Serving Static Files..."
python manage.py collectstatic --noinput

echo "Running Database migration..."
python manage.py makemigrations
python manage.py migrate

# Deactivate Virtual Env
deactivate                          
echo "Virtual env 'venv' Deactivated !" 

echo "Restarting App..."
sudo systemctl restart uwsgi

echo "Deployment Finished !"