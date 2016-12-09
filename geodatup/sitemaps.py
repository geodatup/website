from django.contrib import sitemaps
from django.core.urlresolvers  import reverse

class StaticViewSitemap(sitemaps.Sitemap):
	priority= 0.5
	changefreq ='daily'

	def items(self):
		return ['terms','privacy', 'about']

	def location(self, item):
		return reverse(item)