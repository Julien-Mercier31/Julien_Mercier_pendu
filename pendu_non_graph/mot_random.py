# permet de choisir un mot random
import random

def mot_random (mots):
	liste_mot = mots.split(",")
	rand = random.randint (0,(len(liste_mot)-1))
	return liste_mot[rand]
