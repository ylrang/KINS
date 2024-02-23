#!/bin/bash
set -e

echo "Deployment started ..."               

# Pull the latest version of the app
echo "Copying New changes...."
git pull https://${{ secrets.ACCESS_TOKEN }}@github.com/ylrang/KINS.git main
echo "New changes copied to server !"

# Activate Virtual Env
source source /home/devncnc/project/venv/bin/activate             # activate your virtual environment. change zvenv with your venv name
echo "Virtual env 'venv' Activated !"

echo "Clearing Cache..."
python manage.py clean_pyc
python manage.py clear_cache

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