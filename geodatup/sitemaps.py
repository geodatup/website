from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers  import reverse
from website.models import Service, Secteur,  Formation, CatFormation

class StaticViewSitemap(sitemaps.Sitemap):
	priority= 0.5
	changefreq ='daily'

	def items(self):
		return ['terms','privacy', 'about', 'cdg']

	def location(self, item):
		return reverse(item)



class CatFormationSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return CatFormation.objects.all()

    def location(self, item):
	    return item.get_absolute_url()



class ServiceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Service.objects.all()

    def location(self, item):
	    return item.get_absolute_url()


class SecteurSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Secteur.objects.all()

    def location(self, item):
	    return item.get_absolute_url()


class FormationSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Formation.objects.all()

    def location(self, item):
	    return item.get_absolute_url()


