#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Retry mechanism for database connection
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

# Run database migrations
python3 manage.py migrate

# Check if a superuser already exists
if ! python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists()"; then
  echo "Creating superuser..."
  python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@test.com', 'admin123')"
  echo "Superuser created with username 'admin' and email 'admin@test.com'."
else
  echo "Superuser already exists. Skipping creation."
fi

# Start the Django development server
exec python3 manage.py runserver 0.0.0.0:8000
