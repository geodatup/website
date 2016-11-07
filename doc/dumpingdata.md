# dumping data

~~~
python manage.py dumpdata --natural-foreign --indent=2 filer auth.User --exclude=filer > dump.json
~~~


~~~

python manage.py dumpdata --natural-foreign --indent=2 website.formation  > dump/dump-formation.json
python manage.py dumpdata --natural-foreign --indent=2 website.catformation >  dump/dump-catformation.json
python manage.py dumpdata --natural-foreign --indent=2 website.software > dump/dump-software.json
python manage.py dumpdata --natural-foreign --indent=2 website.moduleformation > dump/dump-moduleformation.json
python manage.py dumpdata --natural-foreign --indent=2 website.chapitreformation > dump/dump-chapitreformation.json

~~~


python manage.py makemigrations && python manage.py migrate && python manage.py loaddata dump/dump.json &&
 python manage.py loaddata  dump/dump-catformation.json && python manage.py loaddata dump/dump-software.json && python manage.py loaddata dump/dump-moduleformation.json && python manage.py loaddata dump/dump-chapitreformation.json && python manage.py loaddata dump/dump-formation.json && python manage.py runserver 


python manage.py makemigrations && python manage.py migrate && python manage.py runserver