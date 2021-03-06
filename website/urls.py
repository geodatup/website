from django.conf.urls import patterns, url
from . import views

app_name = 'website'
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),	
	url(r'^service/(?P<slug>[^/]+)', views.ServiceDetailView.as_view(), name='serviceDetail'),
	url(r'^service/$', views.ServiceListView.as_view(), name='serviceIndex'),
	url(r'^categorie/(?P<slug>[^/]+)', views.CategorieDetailView.as_view(), name='categorieDetail'),
	url(r'^categorie/$', views.CategorieListView.as_view(), name='categorieIndex'),
	url(r'^secteur/(?P<slug>[^/]+)', views.SecteurDetailView.as_view(), name='secteurDetail'),
	url(r'^secteur/$', views.SecteurListView.as_view(), name='secteurIndex'),	
	url(r'^catformation/(?P<slug>[^/]+)', views.CatFormationDetailView.as_view(), name='catformationDetail'),
	url(r'^catformation/$', views.CatFormationListView.as_view(), name='catformationIndex'),
	url(r'^personne/$', views.PersonneListView.as_view(), name='personneIndex'),
	url(r'^personne/(?P<slug>[^/]+)', views.PersonneDetailView.as_view(), name='personneDetail'),
	
	url(r'^support/$', views.support, name='support'),
	url(r'^galerie/$', views.galerie, name='galerie'),	
	url(r'^showcase/$', views.showcase, name='showcase'),
	url(r'^blog/$', views.blog, name='blog'),
	)

