#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn band_saas.wsgi --bind=0.0.0.0:80