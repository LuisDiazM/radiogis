#!/bin/bash

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind :$SERVER_PORT --workers 2 --threads 2 --timeout 10 radiogis_core.wsgi
