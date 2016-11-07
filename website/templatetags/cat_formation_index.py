from django import template

from website.models import Formation, CatFormation
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('section-formation.html',takes_context=True)
def show_index(context, catFormation,slug):
    request = context['request']
    catFormation_List = CatFormation.objects.exclude(slug=slug)
    titre = 'Les autres formations'
    
    return {'catFormation_List': catFormation_List, 'titre' : titre, 'request':request}