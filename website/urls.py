from django.conf.urls import patterns, url
from . import views
#from .views import RubriqueListView, RubriqueDetailView, OeuvreListView, OeuvreDetailView

app_name = 'website'
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),	
	url(r'^service/(?P<slug>[^/]+)', views.ServiceDetailView.as_view(), name='serviceDetail'),
	url(r'^service/$', views.ServiceListView.as_view(), name='serviceIndex'),
	url(r'^secteur/(?P<slug>[^/]+)', views.SecteurDetailView.as_view(), name='secteurDetail'),
	url(r'^secteur/$', views.SecteurListView.as_view(), name='secteurIndex'),	
	url(r'^section/(?P<slug>[^/]+)', views.SectionDetailView.as_view(), name='sectionDetail'),
	url(r'^section/$', views.SectionListView.as_view(), name='sectionIndex'),
	url(r'^catformation/(?P<slug>[^/]+)', views.CatFormationDetailView.as_view(), name='catformationDetail'),
	url(r'^catformation/$', views.CatFormationListView.as_view(), name='catformationIndex'),
	
	url(r'^support/$', views.support, name='support'),
	url(r'^galerie/$', views.galerie, name='galerie'),	
	url(r'^showcase/$', views.showcase, name='showcase'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog, name='blog'),
	)

