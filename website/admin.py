from django.contrib import admin
from django import forms

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Categorie, Service, Section, Secteur, Software, Formation, ChapitreFormation, CatFormation, Reference, ModuleFormation, Personne, Plan, Livrable, Produit, Realisation 


class PlanForm( forms.ModelForm ):
	pitch = forms.CharField(widget=forms.Textarea )
	
	class Meta:
		model = Plan
		exclude = ['']

class PlanAdmin(admin.ModelAdmin):
	form=PlanForm
	list_display = ('nom_plan','tarif')
	prepopulated_fields = {'slug': ('nom_plan',) }
	filter_horizontal = ('servicesAvailable',)


class PersonneAdmin(admin.ModelAdmin):
	list_display = ('nom_personne','fonction')
	prepopulated_fields = {'slug': ('nom_personne',) }

class ChapitreFormationRessource(resources.ModelResource):

    class Meta:
        model = ChapitreFormation
    

class ChapitreFormationAdmin(ImportExportModelAdmin):
	resource_class = ChapitreFormationRessource
	list_display = ('id', 'nom_chapitre', 'module', 'order')
	pass



class ServiceForm( forms.ModelForm ):
	pitch = forms.CharField(widget=forms.Textarea )
	description = forms.CharField( widget=forms.Textarea )
	tooltip = forms.CharField(widget=forms.Textarea)
	html_page = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = Formation
		exclude = ['']

class ServiceAdmin(admin.ModelAdmin):
	form=ServiceForm
	list_display = ('nom_service','categorie_service','css_icon', 'actif', 'landpage')
	prepopulated_fields = {'slug': ('nom_service',) }


class CategorieForm( forms.ModelForm ):
	pitch = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = Formation
		exclude = ['']


class CategorieAdmin(admin.ModelAdmin):
	form=CategorieForm
	list_display = ('id', 'nom_categorie','level','actif')


class SecteurForm( forms.ModelForm ):
	pitch = forms.CharField( widget=forms.Textarea )
	description = forms.CharField( widget=forms.Textarea )
	class Meta:
		model = Formation
		exclude = ['']

class SecteurAdmin(admin.ModelAdmin):
	form=SecteurForm
	list_display = ('id', 'nom_secteur','css_color','css_icon','actif')
	prepopulated_fields = {'slug': ('nom_secteur',) }



class FormationForm( forms.ModelForm ):
	pitch = forms.CharField( widget=forms.Textarea )
	objectif = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = Formation
		exclude = ['']

class FormationRessource(resources.ModelResource):

    class Meta:
        model = Formation
    
class FormationAdmin(ImportExportModelAdmin):
	form=FormationForm
	resource_class = FormationRessource
	list_display = ('id', 'nom_formation','order','atelier','css_color','actif')
	prepopulated_fields = {'slug': ('nom_formation',) }
	filter_horizontal = ('programme',)



class CatFormationForm( forms.ModelForm ):
	pitch = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = CatFormation
		exclude = ['']


class CatFormationRessource(resources.ModelResource):
    class Meta:
        model = CatFormation
    
class CatFormationAdmin(ImportExportModelAdmin):
	form = CatFormationForm
	resource_class = CatFormationRessource
	list_display = ('id', 'nom_catformation','css_color','actif')
	prepopulated_fields = {'slug': ('nom_catformation',) }

class ModuleFormationForm( forms.ModelForm ):
	objectif = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = ModuleFormation
		exclude = ['']


class ModuleFormationRessource(resources.ModelResource):

    class Meta:
        model = ModuleFormation
    
class ModuleFormationAdmin(ImportExportModelAdmin):

	form=ModuleFormationForm
	resource_class = ModuleFormationRessource
	list_display = ('id', 'nom_module', 'order')
	prepopulated_fields = {'slug': ('nom_module',) }
	#filter_horizontal = ('chapitre',)



class SoftwareRessource(resources.ModelResource):

    class Meta:
        model = Software

class SoftwareAdmin(ImportExportModelAdmin):
	resource_class = SoftwareRessource
	list_display = ('id', 'nom_soft','actif')
	prepopulated_fields = {'slug': ('nom_soft',) }


class SectionAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'nom_section','actif')
	prepopulated_fields = {'slug': ('nom_section',) }

class ProduitForm( forms.ModelForm ):
	pitch = forms.CharField( widget=forms.Textarea )
	description = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = ModuleFormation
		exclude = ['']

class ProduitAdmin(admin.ModelAdmin):
	form=ProduitForm
	list_display = ('id', 'nom_produit', 'service','secteur','actif')


# Register your models here.
admin.site.register(Section, SectionAdmin)
admin.site.register(Secteur, SecteurAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(CatFormation, CatFormationAdmin)
admin.site.register(Reference)
admin.site.register(ModuleFormation, ModuleFormationAdmin)
admin.site.register(ChapitreFormation, ChapitreFormationAdmin)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Produit, ProduitAdmin)


admin.site.register(Livrable)

admin.site.register(Realisation)