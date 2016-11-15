
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
    css_icon = models.CharField(max_length=30, null=True, blank=True)
    css_color = models.CharField(max_length=30, null=True, blank=True)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

    #@permalink
    def get_absolute_url(self):
        return reverse('website:secteurDetail', kwargs={'slug': self.slug, })
    
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
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)
    actif = models.BooleanField(default=True)
     #@permalink
    def get_absolute_url(self):
        return reverse('website:sectionDetail', kwargs={'slug': self.slug, })
    
    def __str__(self):
    	return self.nom_section


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=30)
    pitch = models.CharField(max_length=500, null=True, blank=True)

    level = models.PositiveSmallIntegerField(blank=False, null=False, unique=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    css_color = models.CharField(max_length=15, null=True, blank=True)

    actif =  models.BooleanField(default=True)
    
    def __str__(self):
    	return self.nom_categorie

class Service(models.Model):
    nom_service = models.CharField(max_length=30)
    categorie_service = models.ForeignKey(Categorie, null=True, blank=True)    
    pitch = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    css_color = models.CharField(max_length=15, null=True, blank=True)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)
    landpage = models.BooleanField(default=False)
    html_page = models.CharField(max_length=10000, default='<p></p>')
    #secteur =  models.ManyToManyField(Secteur)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

    #@permalink
    def get_absolute_url(self):
        return reverse('website:serviceDetail', kwargs={'slug': self.slug, })


    def __str__(self):
    	return self.nom_service


class Software(models.Model): 
    nom_soft = models.CharField(max_length=15)
    pitch = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_soft



class ModuleFormation(models.Model):
    nom_module = models.CharField(max_length=100)
    objectif = models.CharField(max_length=300, null=True, blank=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    #chapitre = models.ManyToManyField(ChapitreFormation, blank=True)
    #test = models.ManyToManyField(PretestFormation, blank=True)
    #evaluation = 
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)
    
    def get_chapitre_ordered(self):
        return self.chapitreformation_set.order_by('order')

    def get_absolute_url(self):
        return reverse('website:contenuFormationDetail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.nom_module

class ChapitreFormation(models.Model):
    nom_chapitre = models.CharField(max_length=100)
    module = models.ForeignKey(ModuleFormation, null=True, blank=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    #logiciels =  models.ForeignKey(Software, null=True, blank=True)
    documentation_url = models.URLField(null=True, blank=True)   
    
    def __str__(self):
        return self.nom_chapitre

class Formation(models.Model):
    nom_formation = models.CharField(max_length=50)   
    pitch = models.CharField(max_length=300, null=True, blank=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True) 
    niveau_choix =  (
    ('Débutant','0'),
    ('Avancé','1'),    
    ('Expert','2')
    )
    niveau = models.CharField(max_length=50,
        choices=niveau_choix,
        default='0'
        )
    public = models.CharField(max_length=100)
    prerequis = models.ManyToManyField('self', blank=True, symmetrical=False)
    objectif = models.CharField(max_length=300, null=True, blank=True)
    formateur = models.CharField(max_length=50, default='Hugo Roussaffa', blank=True)
    methode = models.CharField(max_length=100)
    programme = models.ManyToManyField(ModuleFormation, blank=True)
    duree_choix =  (
    ('une demi journée','1/2j'),
    ('une journée','1j'),    
    ('2 jours','2j'),
    ('3 jours','3j')
    )
    duree = models.CharField(max_length=50,
        choices=duree_choix,
        default=''
        )
    tarif = models.CharField(max_length=15)
    logiciels =  models.ManyToManyField(Software, blank=True)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    css_color = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)
    
    def get_module_ordered(self):
        return self.programme.order_by('order')

 
    def get_absolute_url(self):
        return reverse('website:formationDetail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.nom_formation

class CatFormation(models.Model):
    nom_catformation = models.CharField(max_length=30)
    pitch = models.CharField(max_length=300, null=True, blank=True)
    formations =  models.ManyToManyField(Formation, blank=True)
    css_icon = models.CharField(max_length=100, null=True, blank=True)
    css_class = models.CharField(max_length=200, null=True, blank=True)
    css_color = models.CharField(max_length=30, null=True, blank=True)
    urlimage = models.URLField(null=True, blank=True)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

    def get_formation_ordered(self):
        return self.formations.order_by('order')

    def __str__(self):
        return self.nom_catformation

    #@permalink
    def get_absolute_url(self):
        return reverse('website:catformationDetail', kwargs={'slug': self.slug, })



class Reference(models.Model):
    nom_reference = models.CharField(max_length=15)
    pitch = models.CharField(max_length=30, null=True, blank=True)
    image = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
    css_icon = models.CharField(max_length=15, null=True, blank=True)
    css_class = models.CharField(max_length=100, null=True, blank=True)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)
    
    def __str__(self):
        return self.nom_reference

    
class Personne(models.Model):
     nom_personne = models.CharField(max_length=30)
     personne_choix =  (
         ('equipe','equipe'),
         ('client','client'),
         ('fournisseur','fournisseur'),
         ('aucun','aucun'),
         )
     type_personne = models.CharField(max_length=50,
        choices=personne_choix,
        default='equipe'
        )
     position_choix =   (
         ('Associé','associé'),
         ('Prestataire','prestataire'),
         ('Salarié','salarié'),
         ('aucun','aucun'),
         )
     position = models.CharField(max_length=50,
        choices=position_choix,
        default='associé'
        )
     fonction = models.CharField(max_length=60, null=True, blank=True)
     description = models.CharField(max_length=100, null=True, blank=True)

     photo = FilerImageField(blank=True, null=True,on_delete=models.SET_NULL,)
     css_icon = models.CharField(max_length=15, null=True, blank=True)
     css_class = models.CharField(max_length=100, null=True, blank=True)
     actif = models.BooleanField(default=True)
     slug = models.SlugField(u'slug',blank=False, default='',help_text='indiquer un nom unique pour url', max_length=64)

     def get_absolute_url(self):
        return reverse('website:personneDetail', kwargs={'slug': self.slug, })

     def __str__(self):
        return self.nom_personne