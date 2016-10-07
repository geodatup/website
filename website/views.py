from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from .models import Categorie, Service, Section, Secteur
from django.utils import timezone

# Create your views here.
def index(request):
	categorie_list = Categorie.objects.all()
	service_list = Service.objects.all()
	service_cat_1 = Service.objects.filter()


	section_list = Section.objects.all()
	secteur_list = Secteur.objects.all()
	context = {'categorie_list': categorie_list,'service_list': service_list,'section_list': section_list, 'secteur_list':secteur_list}
	return render(request, 'base.html', context)

def terms(request):
   
    return render(request, 'terms.html')

def privacy(request):
   
    return render(request, 'privacy.html')
