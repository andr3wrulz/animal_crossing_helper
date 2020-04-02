#!/bin/bash

# Execute the migrations
echo [STARTUP] Migrating database.
python manage.py migrate --noinput

# Start the web server
echo [STARTUP] Starting Django Server.
exec python manage.py runserver 0.0.0.0:8000