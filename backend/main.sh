#!/bin/bash

sleep 2.5m
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('mario', 'luismiguel@radiogis.uis.edu.co', 'mario')" | python manage.py shell
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn --bind :$SERVER_PORT --workers 2 --threads 2 --timeout 10 radiogis_core.wsgi
