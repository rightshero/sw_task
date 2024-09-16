#!/bin/bash
echo "Create migrations"
python manage.py makemigrations main
echo "=========================================="

echo "Migrate"
python manage.py migrate
echo "==========================================="

echo "Create superuser"
python manage.py shell < createsuperuser.py
echo "==========================================="


echo "Start server"
echo "Website is up and running on http://127.0.0.1:8000/"
python manage.py runserver 0.0.0.0:8000
