source ~/myvenv/bin/activate
cd ~/Projects/geodatup/
export DJANGO_SETTINGS_MODULE=geodatup.settings.local_no_debug
python manage.py runserver 0.0.0.0:8080