# Installation 

Create a user for your app, named geodatup and assigned to a system group called webapps.

~~~
sudo groupadd --system webapps
sudo useradd --system --gid webapps --shell /bin/bash --home /var/www/webaps/website geodatup
~~

cd /var/www

mkdir webaps
cd webaps

git clone https://github.com/geodatup/website.git


## Gérer l'application avec l'utilisateur geodatup

~~~
sudo chown geodatup -R /var/www/webaps/website

sudo su - geodatup
~~~




## Créer l'environnement 

~~~
cd /var/www/webaps/website/

virtualenv .

source bin/activate
~~~

Installer les applications requises pour l'environnement

~~~
pip install -r requirements/prod.txt
~~~

Charger le path des paramettres de l'environnement dans les variable du système
~~~
export DJANGO_SETTINGS_MODULE=geodatup.settings.production
~~~

essayer de lancer l'application depuis gunicorn

~~~
gunicorn geodatup.wsgi:application --bind localhost:8001
~~~



Dans le cas ou de multiple applications sont sur le serveur

copier le modèle de fichier gunicorn dans votre dossier

~~~
cp /bin/gunicorn_start /var/www/webaps/website/
~~~

modifier le fichier comme celui ci 

~~~
#!/bin/bash

NAME="geodatup"                                  # Name of the application
DJANGODIR=/var/www/webaps/website             # Django project directory
SOCKFILE=/var/www/webaps/website/run/gunicorn.sock  # we will communicte using this unix socket
USER=geodatup                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=geodatup.settings.production            # which settings file should Django use
DJANGO_WSGI_MODULE=geodatup.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
#  --bind=0.0.0.0:8000 \ 
  --log-level=debug \

~~~

rendre le script executable 

~~~
sudo chmod u+x bin/gunicorn_start
~~~

Troobleshooting

~~~
ImportError: No module named website.wsgi
~~~

L'application nommée website n'exite pas. Il faut verrifier et corriger le nom de l'application dans la commande.


~~~
[2016-09-18 18:29:52 +0000] [5914] [INFO] Starting gunicorn 19.6.0
[2016-09-18 18:29:52 +0000] [5914] [INFO] Listening at: http://127.0.0.1:8001 (5914)
[2016-09-18 18:29:52 +0000] [5914] [INFO] Using worker: sync
[2016-09-18 18:29:52 +0000] [5919] [INFO] Booting worker with pid: 5919
[2016-09-18 18:29:53 +0000] [5919] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/arbiter.py", line 557, in spawn_worker
    worker.init_process()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/workers/base.py", line 126, in init_process
    self.load_wsgi()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/workers/base.py", line 136, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/app/wsgiapp.py", line 65, in load
    return self.load_wsgiapp()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/app/wsgiapp.py", line 52, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/gunicorn/util.py", line 357, in import_app
    __import__(module)
  File "/var/www/webaps/website/geodatup/wsgi.py", line 16, in <module>
    application = get_wsgi_application()
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/django/core/wsgi.py", line 13, in get_wsgi_application
    django.setup(set_prefix=False)
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/django/__init__.py", line 22, in setup
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/django/conf/__init__.py", line 53, in __getattr__
    self._setup(name)
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/django/conf/__init__.py", line 41, in _setup
    self._wrapped = Settings(settings_module)
  File "/var/www/webaps/website/local/lib/python2.7/site-packages/django/conf/__init__.py", line 116, in __init__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
ImproperlyConfigured: The SECRET_KEY setting must not be empty.
[2016-09-18 18:29:53 +0000] [5919] [INFO] Worker exiting (pid: 5919)
[2016-09-18 18:29:53 +0000] [5914] [INFO] Shutting down: Master
[2016-09-18 18:29:53 +0000] [5914] [INFO] Reason: Worker failed to boot.
~~~

soit quelques chose ne va pas dans le fichier de configuration python de l'application django (base.py ou  production.py ...)
soit il faut charger le path du fichier de paramettres dans les variables d'environnement comme ceci :

~~~
export DJANGO_SETTINGS_MODULE=geodatup.settings.production
~~~

Autoriser les autres utilisateurs à accéder à l'application

~~~
sudo chown -R geodatup:users /var/www/webaps/website
sudo chmod -R g+w /var/www/webaps/website
~~~



Pour que le service démarre en même temps que le système on utilise supervisor


installer supervisor :

~~~
sudo aptitude install supervisor
~~~

~~~
nano /etc/supervisor/conf.d/geodatup.conf
~~~

~~~
[program:geodatup]
command = /var/www/webapps/website/geodatup/bin/gunicorn_start                    ; Command to start app
user = geodatup                                                          ; User to run as
stdout_logfile = /webapps/hello_django/logs/gunicorn_supervisor.log   ; Where to write log messages
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                       ; Set UTF-8 as default encoding
~~~



## Créer un vitual env
source myvenv/bin/activate







# Ìnstaller django
Ceci va creer un repertoire pour le projet
```
django-admin startproject geodatup
```
# configurer les fichiers settings.py base, local et de production

```
mkdir geodatup/geodatup/settings
mv geodatup/geodatup/settings.py geodatup/geodatup/settings/base.py
vi geodatup/geodatup/settings/__init__.py
```

Créer un dossier templates
```
mkdir geodatup/geodatup/templates
```

Créer le fichier views.py
```
vi geodatup/geodatup/views.py
```

si vous déplacez les fichiers dans un sous repertoire "settings" il faudra modifier le path DATA_DIR et BAS_DIR du fichier base.py 

```
BASE_DIR =os.path.dirname(os.path.realpath(os.path.dirname(__file__)+ "/.."))

```

Definir la variable d'environnement des settings Django
```
export DJANGO_SETTINGS_MODULE=ann.settings.local
```

# configuration du projet

- Ajouter les apps dans la config

- Ajouter le dossier templates dans la config

```
TEMPLATES = [
    {
        ...
        os.path.join(BASE_DIR, 'geodatup', 'templates'),
        ],
        ...
    }
```

