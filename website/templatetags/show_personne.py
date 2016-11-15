from django import template

from website.models import Personne
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('about/team.html',takes_context=True)
def show_team(context):
    request = context['request']
    team_list = Personne.objects.all().filter(type_personne='Equipe', actif=1)

    return {'team_list': team_list, 'request':request}