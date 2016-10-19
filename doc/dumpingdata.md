# dump data

~~~
python manage.py dumpdata --natural-foreign --indent=2 website filer auth.User --exclude=filer.image.1 > dump.json
~~~