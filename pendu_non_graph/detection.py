# permet de vérifier qu'une lettre existe dans le mot rechercher sinon incrémente l'érreur
def detection (lettre, mot, erreur):
	det = False
	for let in (mot):
		if (ord(lettre)>140):
			print(lettre.upper(),"maj")
			if ((let == lettre) or (let == lettre.upper())):
				return True
		else:
			print(lettre.lower(),"min")
			if ((let == lettre) or (let == lettre.lower())):
				return True
	return False