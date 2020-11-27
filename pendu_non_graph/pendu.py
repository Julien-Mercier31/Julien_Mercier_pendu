# c'est le main du projet
import detection as d

fich = open('mot.txt','r');
mot  = fich.read();
restart = "y"
while restart == "y":
	erreur =0
	while erreur < 5:
		print ("Vous jouer aux jeux du pendu")
		print ("Donner une lettre")
		lettre 	= input ()
		if (d.detection(lettre, mot, erreur)):
			print("la lettre existe dans le mot donner")
		else:
			print("la lettre n'existe pas dans le mot donner")
			erreur = erreur+1
		print (erreur)
	print ("voulez vous recommancer taper sur y")
	restart = input ()


