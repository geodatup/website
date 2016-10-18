from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from .models import Categorie, Service, Section, Secteur, Software, Formation, CatFormation, Reference
from django.utils import timezone

# Create your views here.
def index(request):
	categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')
	service_list = Service.objects.all().filter(actif=1)
	section_list = Section.objects.all().filter(actif=1)
	secteur_list = Secteur.objects.all().filter(actif=1)

	service_cat1 = service_list.filter(categorie_service__pk=1)
	service_cat2 = service_list.filter(categorie_service__pk=2)	
	service_cat3 = service_list.filter(categorie_service__pk=3)

	secteur_list_tab1 = secteur_list[0:3]
	secteur_list_tab2 = secteur_list[3:6]
	secteur_list_tab3 = secteur_list[6:9]
	secteur_list_tab4 = secteur_list[9:12]


	context = {
	'categorie_list': categorie_list,
	'service_list': service_list,
	'section_list': section_list, 
	'secteur_list':secteur_list,
	'secteur_list_tab1' : secteur_list_tab1,
	'secteur_list_tab2' : secteur_list_tab2,
	'secteur_list_tab3': secteur_list_tab3,
	'secteur_list_tab4': secteur_list_tab4,
	'service_cat1':service_cat1,
	'service_cat2':service_cat2,
	'service_cat3':service_cat3,


	}
	return render(request, 'base.html', context)

def terms(request):
   
    return render(request, 'terms.html')

def privacy(request):
   
    return render(request, 'privacy.html')
