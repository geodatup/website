from django.contrib import admin

from .models import Categorie, Service, Section, Secteur, Software, Formation, CatFormation, Reference

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('nom_service','categorie_service', 'css_icon', 'actif')


class CategorieAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_categorie','level','actif')



class SecteurAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_secteur','actif')

# Register your models here.
admin.site.register(Section)
admin.site.register(Secteur, SecteurAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Software)
admin.site.register(Formation)
admin.site.register(CatFormation)
admin.site.register(Reference)