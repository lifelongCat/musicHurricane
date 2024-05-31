# run migrations
python manage.py migrate

# create superuser for admin panel
python manage.py createsuperuser --noinput

# run django project
python manage.py runserver "${DJANGO_HOST}:${DJANGO_PORT}"