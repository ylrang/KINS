#!/bin/bash
set -e

# Activate Virtual Env
source /home/devncnc/project/venv/bin/activate
echo "Virtual environment 'venv' activated"

echo "Installing dependencies..."
pip install -r requirements.txt --no-input

echo "Serving static files..."
python manage.py collectstatic --noinput

echo "Running migration..."
python manage.py makemigrations
python manage.py migrate

# Deactivate Virtual Env
deactivate                          
echo "Virtual environment 'venv' deactivated" 

echo "Restarting the server..."
sudo systemctl restart uwsgi

echo "Deployment complete"