from django.contrib import admin

from .models import Categorie, Service, Section, Secteur, Software, Formation, CatFormation, Reference, ContenuFormation

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('nom_service','categorie_service', 'css_icon', 'actif')
	prepopulated_fields = {'slug': ('nom_service',) }


class CategorieAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_categorie','level','actif')


class SecteurAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_secteur','actif')


class FormationAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_formation','actif')
	prepopulated_fields = {'slug': ('nom_formation',) }


class CatFormationAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_catformation','actif')
	prepopulated_fields = {'slug': ('nom_catformation',) }


class ContenuFormationAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_contenu','actif')
	prepopulated_fields = {'slug': ('nom_contenu',) }


class SoftwareAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom_soft','actif')
	prepopulated_fields = {'slug': ('nom_soft',) }





# Register your models here.
admin.site.register(Section)
admin.site.register(Secteur, SecteurAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(CatFormation, CatFormationAdmin)
admin.site.register(Reference)
admin.site.register(ContenuFormation, ContenuFormationAdmin)