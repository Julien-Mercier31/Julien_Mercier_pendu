# permet d'afficher le mot avec des underscor
from tkinter import Tk, Label, Button, Canvas, Entry

def affichage (lettre,mot):
	nouv_mot = ""
	for lettre_init in mot:
		if lettre_init in lettre:
			nouv_mot += lettre_init
		else:
			nouv_mot += "_"
	return nouv_mot
