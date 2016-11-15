from django import template

from website.models import Section
from django.template.loader import get_template

register = template.Library()



@register.inclusion_tag('sections/section.html',takes_context=True)
def show_section_list(context):
    request = context['request']
    section_list = Section.objects.all().filter(actif=1)
    


    return {'section_list': section_list, 'request':request}

@register.inclusion_tag('sections/nav_section.html',takes_context=True)
def show_section_navlist(context):
    request = context['request']
    section_list = Section.objects.all().filter(actif=1)
    


    return {'section_list': section_list, 'request':request}