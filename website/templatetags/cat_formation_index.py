from django import template

from website.models import Formation, CatFormation
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('formation/liste_catformation.html',takes_context=True)
def show_index(context, catFormation):
    request = context['request']
    catFormationList = CatFormation.objects.all()
    
    #urlMatching = catFormation.objects.filter(slug=slugCatFormation)[0].get_absolute_url()

    
    #return {'catFormationList': catFormationList, 'request':request, 'urlMatching':urlMatching}
    return {'catFormationList': catFormationList, 'request':request}