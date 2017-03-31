class fait:

	def __init__(self, ident, valeur):# continue pre defini non acceptable , de meme pr id 
		self.ident=ident
		self.valeur=valeur

	#pour l'affichage
	def out(self):
		print("("+str(self.ident)+","+str(self.valeur)+")",end='')
	