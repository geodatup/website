from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from .models import Personne, Categorie, Service, Section, Secteur, Software, Formation, CatFormation, Reference, ChapitreFormation, Realisation
from django.utils import timezone

# Create your views here.
def index(request):
	categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')
	service_list = Service.objects.all().filter(actif=1)
	section_list = Section.objects.all().filter(actif=1)
	secteur_list = Secteur.objects.all()

	service_cat1 = service_list.filter(categorie_service__level=1)
	service_cat2 = service_list.filter(categorie_service__level=2)	 
	service_cat3 = service_list.filter(categorie_service__level=3)

	secteur_list_tab1 = secteur_list[0:3]
	secteur_list_tab2 = secteur_list[3:6]
	secteur_list_tab3 = secteur_list[6:9]
	secteur_list_tab4 = secteur_list[9:12]

	catFormation_List_actif = CatFormation.objects.all().filter(actif=1)
	catFormation_List = CatFormation.objects.all()


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
	'catFormation_List':catFormation_List,
	}
	return render(request, 'base.html', context)


class ServiceDetailView(generic.DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'services/serviceDetail.html'


class ServiceListView(generic.ListView):
    model = Service
    template_name = 'services/serviceIndexList.html'

class SecteurDetailView(generic.DetailView):
    model = Secteur
    context_object_name = 'secteur'
    template_name = 'secteurs/secteurDetail.html'

class SecteurListView(generic.ListView):
    model = Secteur
    template_name = 'secteurs/secteurIndexList.html'

class SectionDetailView(generic.DetailView):
    model = Section
    context_object_name = 'section'
    template_name = 'sections/sectionDetail.html'

class SectionListView(generic.ListView):
    model = Section
    template_name = 'sections/sectionIndexList.html'

class CatFormationDetailView(generic.DetailView):
    model = CatFormation
    context_object_name = 'catFormation'
    template_name = 'formation/catFormationDetail.html'


class CatFormationListView(generic.ListView):
    model = CatFormation
    template_name = 'formation/catFormationIndexList.html'


class PersonneDetailView(generic.DetailView):
    model = Personne
    context_object_name = 'Personne'
    template_name = 'about/PersonneDetail.html'


class PersonneListView(generic.ListView):
    model = Personne
    template_name = 'about/PersonneIndexList.html'


def support(request):
   
    return render(request, 'support/support.html')

def terms(request):
   
    return render(request, 'terms.html')


def galerie(request):
   
    return render(request, 'galerie.html')

def showcase(request):
    showcase_list = Realisation.objects.all().filter(actif=1)
    context = {
    'showcase_list': showcase_list,
    }
   
    return render(request, 'showcase.html', context)


def blog(request):
   
    return redirect("http://blog.geodatup.fr")

def privacy(request):
   
    return render(request, 'privacy.html')

def about(request):
   
    return render(request, 'about.html')
