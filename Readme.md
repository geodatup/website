
Readme.md


# vitual env
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

