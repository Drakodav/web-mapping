#!/bin/bash

#django
docker image rm geodjangoapp
docker build -t geodjangoapp .

docker stop django_project
docker rm django_project
docker create --name django_project --network geonet --network-alias na_django -t \
geodjangoapp

docker start django_project

# run default config precautions
docker exec django_project python manage.py makemigrations
docker exec django_project python manage.py migrate
docker exec django_project \
    python manage.py shell \
    -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"
docker exec django_project \
    python manage.py shell \
    -c "from world import load; load.run()"
