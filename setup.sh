#!/usr/bin/env bash
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

# Yönetici hesabı yalnızca ortam değişkenleri verilirse oluşturulur; koda şifre yazılmaz.
#   DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
if [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
    echo "Creating superuser (if needed)..."
    python manage.py createsuperuser --noinput || echo "Superuser already exists, skipped."
else
    echo "DJANGO_SUPERUSER_PASSWORD not set; skipping superuser creation."
fi

echo "Setup completed!"
