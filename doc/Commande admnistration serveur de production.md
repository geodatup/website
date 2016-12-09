#Commande admnistration serveur de production


- créer un nouvel utilisateur et un dossier home qui pointe sur son application
- définir les droits de proprieté sur l'ensemble des sources
- créer environnement python3
- PIP3 install requirements
- configurer gunicorn 

voir le blog nginx + gunicon + django + supervisor


relancer le serveur web django 

~~~
cd /var/webapps/website
bin/activate
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
