#!/bin/bash

sleep 2.5m
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('mario', 'devices@casiri.com', 'mario')" | python manage.py shell
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'luismiguel@radiogis.uis.edu.co', 'admin')" | python manage.py shell
gunicorn --bind :$SERVER_PORT --workers 2 --threads 2 --timeout 10 radiogis_core.wsgi
