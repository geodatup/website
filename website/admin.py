from django.contrib import admin

from .models import Categorie, Service, Section, Secteur

# Register your models here.
admin.site.register(Section)
admin.site.register(Categorie)
admin.site.register(Service)