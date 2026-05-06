#!/usr/bin/env bash
set -e

# Django setup
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser (if needed)..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@karabaglar.com', 'admin123')
    print("Admin user created!")
else:
    print("Admin user already exists!")
END

echo "Setup completed!"
