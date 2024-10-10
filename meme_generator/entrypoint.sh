#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Retry mechanism for database connection
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"  # Log message if Postgres is unavailable
  sleep 1  # Wait for 1 second before retrying
done

>&2 echo "Postgres is up - executing command"  # Log message when Postgres is available

# Run database migrations
python3 manage.py migrate

# Start the Django development server
exec python3 manage.py runserver 0.0.0.0:8000