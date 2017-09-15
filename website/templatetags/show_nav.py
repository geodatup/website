from django import template

from website.models import Categorie, Secteur, Service, CatFormation
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('nav-service.html',takes_context=True)
def show_nav_everywhere(context):
	request = context['request']
	categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')
	service_list = Service.objects.all().filter(actif=1)
	

	catFormation_List_actif = CatFormation.objects.all().filter(actif=1)
	catFormation_List = CatFormation.objects.all()


	context = {
	'categorie_list': categorie_list,
	'service_list': service_list,
	'catFormation_List':catFormation_List,
	}
	return { 'categorie_list': categorie_list, 'service_list': service_list, 'catFormation_List':catFormation_List, 'request':request}