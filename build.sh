#!/usr/bin/env bash
# Exit on error
set -o errexit

set DJANGO_SETTINGS_MODULE=educa.settings.prod

pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate