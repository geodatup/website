#Commande admnistration serveur de production



##Preparation de l'environnement de production

déposer les sources de l'application (clone) dans le dossier webapps

~~~
cd /var/www/webapps
sudo git clone  https://github.com/geodatup/[appname].git
~~~
Puis 
- créer un nouvel utilisateur et un dossier home qui pointe sur son application
- définir les droits de proprieté sur l'ensemble des sources
- créer environnement python3
- PIP3 install requirements
- configurer gunicorn 

[voir le blog nginx + gunicon + django + supervisor](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/)

~~~
sudo useradd --system --gid webapps --shell /bin/bash --home /var/www/webapps/[appname] [appname]
sudo chown [appname] /var/www/webapps/[appname]
sudo su - [appname]
~~~

dans le dossier créer l'environnement virtuel et l'activer

~~~
virtualenv --python=python3.4 .
source bin/activate
~~~

Installer les dep

~~~
pip install -r requirements.txt 
~~~


relancer le serveur web django 

~~~
sudo supervisorctl reload
~~~

collectstatic

~~~
sudo su - geodatup
python manage.py collectstatic
~~~

Installer tous les package python de base 

~~~
sudo su - geodatup
pip3 install -r requierements/base.txt
~~~
puis relancer supervisorctl en dehors de la session geodatup

# déploiement en production 


~~~
cd /var/www/webapps/website
source bin/activate
sudo git pull
sudo python manage.py migrate
sudo python manage.py loaddata dump/auth.json
sudo python manage.py loaddata dump/filer.json 
sudo python manage.py loaddata dump/dump-catformation.json
sudo python manage.py loaddata dump/dump-categorie.json
sudo python manage.py loaddata dump/dump-moduleformation.json
sudo python manage.py loaddata dump/dump-chapitreformation.json
sudo python manage.py loaddata dump/dump-formation.json
sudo python manage.py loaddata dump/dump-personne.json
sudo python manage.py loaddata dump/dump-reference.json
sudo python manage.py loaddata dump/dump-secteur.json
sudo python manage.py loaddata dump/dump-section.json
sudo python manage.py loaddata dump/dump-service.json 
sudo python manage.py loaddata dump/dump-software.json
sudo python manage.py loaddata dump/dump-plan.json
sudo python manage.py loaddata dump/dump-produit.json
sudo supervisorctl reload
sudo su - geodatup
python manage.py collectstatic

~~~



# troubleshooting

l'interface d'administration est une page blanche. LEs droits d'écriture sur la base de donnée ne sont pas adaptés.

~~~
sudo chown geodatup:webapps -R .
~~~

Collectstatic provoque une erreur de permission. changer les droits du dossier static
s'assurer d'etre connecter avec l'utilisateur geodatup


Gunicorn ne se lance pas. 

~~~
EACESS
supervisor: child process was not spawned
~~~

le fichier gunicorn_start n'est pas executable. Appliquer les droits de l'utilisateur

~~~
cd webapps/website/bin/
sudo chown geodatup:webapps -R .
~~~



# Maintenir le site de production sur le serveur

```sudo su  geodatup && source bin/activate```

backup des données

