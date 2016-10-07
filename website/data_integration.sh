from website.models import Service, Categorie, Secteur, Section

#================================================

secteur = Secteur(
	nom_secteur = "Foresterie",
	)
secteur.save()

secteur = Secteur(
	nom_secteur = "Archéologie",
	)
secteur.save()


secteur = Secteur(
	nom_secteur = "Environnement",
	)
secteur.save()


secteur = Secteur(
	nom_secteur = "Agriculture",
	)
secteur.save()

#================================================


section = Section(
	nom_section = "Services",
	)
section.save()

section = Section(
	nom_section = "Secteurs",
	)
section.save()


section = Section(
	nom_section = "Assistances & Support",
	)
section.save()


section = Section(
	nom_section = "Blog",
	css_class = "quite",
	)
section.save()


#================================================

categorie = Categorie(
	nom_categorie = "Accompagnement",
	)
categorie.save()

#================================================

#---------------------------CAT 1
service = Service(
   nom_service = "Formation",
   categorie_service = categorie,
   )
service.save()

service = Service(
   nom_service = "Conseil",
   categorie_service = categorie,
   )
service.save()

service = Service(
   nom_service = "Maintenace",
   categorie_service = categorie,
   )
service.save()

#================================================
#---------------------------CAT 2

categorie = Categorie(
	nom_categorie = "Outils",
	)
categorie.save()



service = Service(
   nom_service = "Cartographie spécialisée",
   categorie_service = categorie,
   nom_icon = "map",
   )
service.save()

service = Service(
   nom_service = "SIG",
   categorie_service = categorie,
   )
service.save()

service = Service(
   nom_service = "Télédétection",
   categorie_service = categorie,
   )
service.save()


service = Service(
   nom_service = "Programmation",
   categorie_service = categorie,
   nom_icon = "",
   )
service.save()

service = Service(
   nom_service = "Analyse spatiale",
   categorie_service = categorie,
   nom_icon ="" ,
   )
service.save()
#================================================
#---------------------------CAT 3

categorie = Categorie(
	nom_categorie = "Data",
	)
categorie.save()

service = Service(
   nom_service = "Photogrammetrie",
   categorie_service = categorie,
   nom_icon = "",
   )
service.save()

service = Service(
   nom_service = "DataPack Open data",
   categorie_service = categorie,
   nom_icon = "",
   )
service.save()

service = Service(
   nom_service = "DataPack IGN",
   categorie_service = categorie,
   nom_icon ="" ,
   )
service.save()


#---------------------------