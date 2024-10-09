#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Check if CREATE_SUPERUSER is set to true in the environment
if [[ $CREATE_SUPERUSER == "true" ]]; then
    # Create the superuser using environment variables for email and username
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL" --username "$DJANGO_SUPERUSER_USERNAME"
fi
