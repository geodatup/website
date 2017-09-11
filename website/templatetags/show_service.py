from django import template

from website.models import Categorie, Service
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('services/service.html',takes_context=True)
def show_service_by_categorie(context):
    request = context['request']
    service_list = Service.objects.all().filter(actif=1) 
    categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')


    return {'service_list': service_list, 'categorie_list':categorie_list, 'request':request}

@register.inclusion_tag('services/service-by-cat.html',takes_context=True)
def show_service_by_categorie_simple(context):
    request = context['request']
    service_list = Service.objects.filter(actif=1)
    categorie_list = Categorie.objects.filter(actif=1).order_by('level')


    return {'service_list': service_list, 'categorie_list':categorie_list, 'request':request}

@register.inclusion_tag('services/service-by-cat-menu.html',takes_context=True)
def show_service_by_categorie_menu(context):
    request = context['request']
    service_list = Service.objects.all().filter(actif=1)
    categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')


    return {'service_list': service_list, 'categorie_list':categorie_list, 'request':request}

@register.inclusion_tag('services/service-by-cat-dropdown-menu.html',takes_context=True)
def show_service_by_categorie_dropdown_menu(context):
    request = context['request']
    service_list = Service.objects.all().filter(actif=1)
    categorie_list = Categorie.objects.all().filter(actif=1).order_by('level')


    return {'service_list': service_list, 'categorie_list':categorie_list, 'request':request}

@register.inclusion_tag('services/service-mainpage.html',takes_context=True)
def show_service_by_categorie_mainpage(context):
    request = context['request']
    service_list = Service.objects.all().filter(actif=1)
    categorie_list = Categorie.objects.all().filter(nom_categorie="Accompagnement").order_by('level')


    return {'service_list': service_list, 'categorie_list':categorie_list, 'request':request}
