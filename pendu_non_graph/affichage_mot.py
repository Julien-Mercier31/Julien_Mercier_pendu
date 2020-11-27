# permet d'afficher le mot avec des underscor
def affichage (lettre,mot, affichage):
	nouv_mot = ""
	for lettre_init in mot:
		if lettre_init in lettre:
			nouv_mot += lettre_init
		else:
			nouv_mot += "_"
	if (affichage):
		print (nouv_mot)
	return nouv_mot
