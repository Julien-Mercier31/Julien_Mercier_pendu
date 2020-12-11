# detecte la victoire

def win (nouv_mot):
	win = True
	for lettre in nouv_mot:
		if lettre =="_":
			win = False
	return win
