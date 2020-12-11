# perme de vérifier si il y a une erreur et si il une victoire 
import detection as d
import affichage_mot as a
import victoire as v

def pendu (liste,erreur,mot):
	er_max = 8
	lettre = liste[len(liste)-1]
	if (d.detection(lettre, mot) == False):
		erreur = erreur+1
	nouv_mot = a.affichage(liste,mot)
	print(nouv_mot)
	victoire = v.win(nouv_mot)
	return erreur


