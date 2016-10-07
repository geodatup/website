source ~/myvenv/bin/activate
cd ~/Projects/geodatup/
export DJANGO_SETTINGS_MODULE=geodatup.settings.local
python manage.py runserver 0.0.0.0:8000
