Commande admnistration serveur de production

relancer le serveur web django 
~~~
sudo supervisorctl reload
~~~

# troubleshooting

l'interface d'administration est une page blanche. LEs droits d'écriture sur la base de donnée ne sont pas adaptés.
~~~
sudo chown geodatup:webapps -R .
~~~

Collectstatic provoque une erreur de permission. changer les droits du dossier static
~~~
sudo chown pi:pi -R static/
~~~
