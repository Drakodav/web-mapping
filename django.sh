#django
docker stop django_project
docker rm django_project
docker image rm geodjangoapp

# run default config precautions
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"
python manage.py makemigrations
python manage.py migrate


docker build -t geodjangoapp .
docker create --name django_project --network geonet --network-alias na_django -t \
geodjangoapp
# -p 8001:8001 \

docker start django_project
