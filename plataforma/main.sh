#!/bin/bash

python manage.py migrate
gunicorn --bind :$SERVER_PORT --workers 2 --threads 2 --timeout 10 radiogis_core.wsgi
