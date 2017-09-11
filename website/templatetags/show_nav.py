from django import template

from website.models import Categorie, Secteur, Service, CatFormation
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('nav-service.html',takes_context=True)
def show_nav_everywhere(context):
	request = context['request']
	categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')
	service_list = Service.objects.all().filter(actif=1)
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
	return { 'categorie_list': categorie_list, 'service_list': service_list,  'secteur_list':secteur_list, 'secteur_list_tab1' : secteur_list_tab1, 'secteur_list_tab2' : secteur_list_tab2, 'secteur_list_tab3': secteur_list_tab3, 'secteur_list_tab4': secteur_list_tab4, 'service_cat1':service_cat1, 'service_cat2':service_cat2, 'service_cat3':service_cat3, 'catFormation_List':catFormation_List, 'request':request}