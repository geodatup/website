Commande admnistration serveur de production


- créer un nouvel utilisateur et un dossier home qui pointe sur son application
- définir les droits de proprieté sur l'ensemble des sources
- créer environnement python3
- PIP3 install requirements
- configurer gunicorn 

voir le blog nginx + gunicon + django + supervisor


relancer le serveur web django 

~~~
sudo supervisorctl reload
~~~

collectstatic

~~~
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
