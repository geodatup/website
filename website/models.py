
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from filer.fields.image import FilerImageField
#from filer.fields.image import FilerImageField

# Create your models here.

class Secteur(models.Model):
    nom_secteur = models.CharField(max_length=15)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)
    
    def __str__(self):
    	return self.nom_secteur

class Section(models.Model):
    nom_section = models.CharField(max_length=30)
    level_choix =  (
    ('navbar-top','navbar-top'),
    ('navbar-top-sub1','navbar-top-sub1'),    
    ('navbar-top-sub2','navbar-top-sub2'),
    ('navbar-verticale','navbar-verticale')
    )
    level = models.CharField(max_length=50,
        choices=level_choix,
        default='indéfini'
        )
    css_icon = models.CharField(max_length=100, null=True, blank=True)
    css_div_class = models.CharField(max_length=100, null=True, blank=True)
    css_ahref_class = models.CharField(max_length=100, null=True, blank=True)
    datacategory_choix =  (
    ('products','products'),
    ('help','help'),    
    ('documentation','documentation'), 
    ('use-cases','use-cases'),
    ('','aucun')
    )
    css_datacategory = models.CharField(max_length=50,
        choices=datacategory_choix,
        default=''
        )
    actif = models.BooleanField(default=True)

    def __str__(self):
    	return self.nom_section


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=30)
    level = models.PositiveSmallIntegerField(blank=True, null=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif =  models.BooleanField(default=True)
    
    def __str__(self):
    	return self.nom_categorie

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

class Service(models.Model):
    nom_service = models.CharField(max_length=30)
    categorie_service = models.ForeignKey(Categorie, null=True, blank=True)    
    pitch = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)
    #secteur =  models.ManyToManyField(Secteur)

    def __str__(self):
    	return self.nom_service


class Software(models.Model): 
    nom_soft = models.CharField(max_length=15)
    pitch = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom_soft


class Formation(models.Model):
    nom_formation = models.CharField(max_length=15)   
    pitch = models.CharField(max_length=30, null=True, blank=True)
    contenu = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.CharField(max_length=15)
    prerequis = models.CharField(max_length=15)
    duree = models.CharField(max_length=15)
    tarif = models.CharField(max_length=15)
    logiciels =  models.ManyToManyField(Software, blank=True)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_formation

class CatFormation(models.Model):
    nom_categorie = models.CharField(max_length=15)
    pitch = models.CharField(max_length=30, null=True, blank=True)
    formations =  models.ManyToManyField(Formation, blank=True)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)


class Reference(models.Model):
    nom_reference = models.CharField(max_length=15)
    pitch = models.CharField(max_length=30, null=True, blank=True)
    image = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)


#class MyContact(models.Model):
#    nom_contact = models.CharField(max_length=15)
#    type_contact = models.CharField(max_length=15)
#    valeur = models.CharField(max_length=30)
#    css_icon = models.CharField(max_length=15, null=True, blank=True)
#   css_class = models.CharField(max_length=100, null=True, blank=True)


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