# permet de vérifier qu'une lettre existe dans le mot rechercher sinon incrémente l'érreur
def detection (lettre, mot):
	for let in (mot):
		if (let == lettre):
			return True
	return False