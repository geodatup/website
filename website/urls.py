from django.conf.urls import patterns, url
from . import views
#from .views import RubriqueListView, RubriqueDetailView, OeuvreListView, OeuvreDetailView


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)