# dumping data



~~~
python manage.py dumpdata --natural-foreign --indent=2 auth.User > dump/auth.json
python manage.py dumpdata --natural-foreign --indent=2 filer >  dump/filer.json
python manage.py dumpdata --natural-foreign --indent=2 website.catformation >  dump/dump-catformation.json
python manage.py dumpdata --natural-foreign --indent=2 website.categorie >  dump/dump-categorie.json
python manage.py dumpdata --natural-foreign --indent=2 website.chapitreformation > dump/dump-chapitreformation.json
python manage.py dumpdata --natural-foreign --indent=2 website.formation  > dump/dump-formation.json
python manage.py dumpdata --natural-foreign --indent=2 website.moduleformation > dump/dump-moduleformation.json
python manage.py dumpdata --natural-foreign --indent=2 website.personne > dump/dump-personne.json
python manage.py dumpdata --natural-foreign --indent=2 website.reference > dump/dump-reference.json
python manage.py dumpdata --natural-foreign --indent=2 website.secteur > dump/dump-secteur.json
python manage.py dumpdata --natural-foreign --indent=2 website.section > dump/dump-section.json
python manage.py dumpdata --natural-foreign --indent=2 website.service > dump/dump-service.json
python manage.py dumpdata --natural-foreign --indent=2 website.software > dump/dump-software.json
python manage.py dumpdata --natural-foreign --indent=2 website.plan > dump/dump-plan.json
python manage.py dumpdata --natural-foreign --indent=2 website.produit > dump/dump-produit.json
python manage.py dumpdata --natural-foreign --indent=2 website.reference > dump/dump-realisation.json
~~~


# migrate and reload
~~~
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
~~~

# load data

One line command
~~~
python manage.py loaddata dump/auth.json && python manage.py loaddata dump/filer.json && python manage.py loaddata  dump/dump-catformation.json && python manage.py loaddata dump/dump-categorie.json && python manage.py loaddata dump/dump-chapitreformation.json && python manage.py loaddata dump/dump-formation.json && python manage.py loaddata dump/dump-moduleformation.json && python manage.py loaddata dump/dump-personne.json && python manage.py loaddata dump/dump-secteur.json && python manage.py loaddata dump/dump-section.json && python manage.py loaddata dump/dump-service.json && python manage.py loaddata dump/dump-software.json && python manage.py loaddata dump/dump-plan.json 
~~~

multi-line command
~~~
sudo python manage.py loaddata dump/auth.json
sudo python manage.py loaddata dump/filer.json 
sudo python manage.py loaddata dump/dump-catformation.json
sudo python manage.py loaddata dump/dump-categorie.json
sudo python manage.py loaddata dump/dump-moduleformation.json
sudo python manage.py loaddata dump/dump-chapitreformation.json
sudo python manage.py loaddata dump/dump-formation.json
sudo python manage.py loaddata dump/dump-personne.json
sudo python manage.py loaddata dump/dump-secteur.json
sudo python manage.py loaddata dump/dump-section.json
sudo python manage.py loaddata dump/dump-service.json 
sudo python manage.py loaddata dump/dump-software.json 
sudo python manage.py loaddata dump/dump-plan.json 
sudo python manage.py loaddata dump/dump-reference.json 
~~~
