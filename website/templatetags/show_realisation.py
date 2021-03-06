from django import template

from website.models import Realisation, Service
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('showcase/showcase-gallery.html',takes_context=True)
def show_realisation_by_service_gallery(context, service, slug):
    request = context['request']
    showcase_list = Realisation.objects.filter(actif=1, service__slug=slug)
 
    return {'showcase_list': showcase_list, 'request':request}

@register.inclusion_tag('showcase/showcase-gallery.html',takes_context=True)
def show_realisation_by_categorie_gallery(context, categorie, slug):
    request = context['request']
    showcase_list = Realisation.objects.filter(actif=1, service__categorie_service__slug=slug)
 
    return {'showcase_list': showcase_list, 'request':request}
