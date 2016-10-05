from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django_tables2   import RequestConfig
from django.utils import timezone

# Create your views here.
def index(request):
	categories_list = Categories.objects.all()
	services_list = Services.objects.all()
    context = {'categories_list': categories_list; 'services_list': services_list;}
	return render(request, 'base.html', context)

def terms(request):
   
    return render(request, 'terms.html')

def privacy(request):
   
    return render(request, 'privacy.html')
