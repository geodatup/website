from geodatup.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd*i=4eppnc7((&7ym*i)(!ecxz433-$b07@%!8xp(8lw5)iw=d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

