#!/bin/bash
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 5
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --noinput
python manage.py makemigrations categories
python manage.py migrate
# seed the database with Category A and Category B
python manage.py loaddata initial_data.json

# run nginx as a reverse-proxy
nginx 

gunicorn limitless.wsgi --workers 3  --bind 0.0.0.0:8000
