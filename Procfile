web: gunicorn database_site.wsgi 
heroku pg:psql postgresql-octagonal-21927 --app financedatabase
release: python manage.py makemigrations database_app
release: python manage.py sqlmigrate darabase_app 0001
release: python manage.py migrate
heroku run : python manage.py createsuperuser
 


