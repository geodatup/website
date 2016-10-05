
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
#from filer.fields.image import FilerImageField


# Create your models here.
class Categories(models.Model):
    nom_categorie = models.CharField(max_length=15)
#    icon = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
#    slug = models.SlugField(
#        u'slug',
#        blank=False,
#        default='',
#        help_text=u'mettre un slug unique pour cette rubrique',
#        max_length=64,
#    )
#    
#    def get_absolute_url(self):
#        return reverse('geodatup:categorieDetail', kwargs={'slug': self.slug, })
#        
     def __str__(self):
         return self.nom_categorie


class Services(models.Model):
    nom_service = models.CharField(max_length=15)
    categorie_service = models.ForeignKey(Categories)
   
     def __str__(self):
         return self.nom_service


#class Rubrique(models.Model):
#    nom_rubrique = models.CharField(max_length=30)
#    annee = models.PositiveIntegerField(blank=True, null=True)
#    commentaire = models.TextField(blank=True, null=True)
#    article = HTMLField(blank=True, null=True)
#    slug = models.SlugField(
#        u'slug',
#        blank=False,
#        default='',
#        help_text=u'mettre un slug unique pour cette rubrique',
#        max_length=64,
#    )
#    icon = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
#
#    def get_absolute_url(self):
#        return reverse('galerie:rubriqueDetail', kwargs={'slug': self.slug, })
#        
#    def __str__(self):
#    	return self.nom_rubrique
#
#
#
#class Oeuvre(models.Model):
#    titre = models.CharField(max_length=50)
#    dimension = models.CharField(max_length=50, null=True, blank=True)
#    technique = models.CharField(max_length=50, null=True, blank=True)
#    article = HTMLField(blank=True, null=True)
#    rubrique = models.ForeignKey(Rubrique)
#    photo = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
#    slug = models.SlugField(
#        u'slug',
#        blank=False,
#        default='',
#        help_text=u'mettre un slug unique pour cette oeuvre',
#        max_length=64,
#    )
#    def get_absolute_url(self):
#        return reverse('galerie:oeuvreDetail', kwargs={'slug': self.slug, })
#
#    def __str__(self):
#        return self.titre#