from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from .models import Personne, Categorie, Service,  Secteur, Software, Formation, CatFormation, Reference, ChapitreFormation, Realisation
from django.utils import timezone

# Create your views here.
def index(request):
	categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')
	service_list = Service.objects.all().filter(actif=1)	

	catFormation_List_actif = CatFormation.objects.all().filter(actif=1)
	catFormation_List = CatFormation.objects.all()

	context = {
	'categorie_list': categorie_list,
	'service_list': service_list,
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


class CategorieDetailView(generic.DetailView):
    model = Categorie
    context_object_name = 'categorie'
    template_name = 'categories/categorieDetail.html'


class CategorieListView(generic.ListView):
    model = Categorie
    template_name = 'categories/categorieIndexList.html'

class SecteurDetailView(generic.DetailView):
    model = Secteur
    context_object_name = 'secteur'
    template_name = 'secteurs/secteurDetail.html'

class SecteurListView(generic.ListView):
    model = Secteur
    template_name = 'secteurs/secteurIndexList.html'

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


def privacy(request):
   
    return render(request, 'privacy.html')

def about(request):
   
    return render(request, 'about.html')

###########BLOG views connections

def blog(request): #general
    tag_or_cat = request.GET.get('q', '')
    search = request.GET.get('s', '')
    return redirect("http://blog.geodatup.fr/"+tag_or_cat+"/"+search)

    #return redirect("http://blog.geodatup.fr")

