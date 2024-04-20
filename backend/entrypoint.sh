# run migrations
python manage.py migrate

# create superuser for admin panel
python manage.py createsuperuser --noinput

# run django project
python manage.py runserver 0.0.0.0:"${DJANGO_PORT}"