from django import template

from website.models import Categorie
from django.template.loader import get_template
from django.db.models import Q

register = template.Library()



@register.inclusion_tag('categorie-mainpage.html',takes_context=True)
def show_categorie_mainpage(context):
    request = context['request']
    categorie_list = Categorie.objects.filter(mainpage=1, actif=1).order_by('level')

    return {'categorie_list_mainpage':categorie_list, 'request':request}
