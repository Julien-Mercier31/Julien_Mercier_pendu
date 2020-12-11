# permet de choisir un mot random
import random

def mot_random (mots):
	liste_mot = mots.split(",")
	print (liste_mot)
	rand = random.randint (0,(len(liste_mot)-1))
	print (rand)
	return liste_mot[rand]
