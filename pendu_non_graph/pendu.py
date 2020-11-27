# c'est le main du projet
import detection as d
import affichage_mot as a
import mot_random as r
import victoire as v
er_max = 8

fich = open('mot.txt','r');
mots  = fich.read();
restart = "r"
liste = []
higt_score = 0

while restart == "r":
	victoire = False
	erreur =0
	mot = r.mot_random(mots)
	print ("Vous jouer aux jeux du pendu.")
	while erreur < er_max and victoire == False:
		print ("Donner une lettre.")
		nouv_mot = a.affichage(liste,mot,True)
		print ("vous avez deja essayer les lettre ", liste)
		lettre 	= input ()
		while lettre in liste:
			print ("vous avez deja taper ce chiffre taper en un autre.")
			lettre 	= input ()  
		liste.append (lettre)
		if (d.detection(lettre, mot)):
			print("la lettre existe dans le mot donner.")
		else:
			print("la lettre n'existe pas dans le mot donner.")
			erreur = erreur+1
		print("il vous reste ",er_max-erreur," erreur aux total.")
		nouv_mot = a.affichage(liste,mot,False)
		print(nouv_mot)
		victoire = v.win(nouv_mot)

	if higt_score < er_max - erreur:
		higt_score = er_max - erreur
		print ("vous avez battu votre ancine Hight_score le nouveaux est de ", higt_score)	
	else:
		print ("votre ancient higt-score et de  ", higt_score)	
	if (victoire):
		print("bravo tu est un monstre ")
	else:
		print ("bouhou ta perdu t'est nul") 
	print ("voulez vous recommancer taper sur r")
	restart = input ()
	cpt=0
	longe = len(liste)
	while longe > cpt:
		liste.remove (liste[0])
		cpt = cpt+1


