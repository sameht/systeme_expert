import fait

class baseFait:

	def __init__(self):
		self.listeFait=[]

	#pour l'affichage
	def out(self):
		print("-------------------")
		for element in self.listeFait:
			element.out()

		print("\n-------------------")
			

	#Ajouter un fait a la base
	def chargerBF(self, fait): 
		self.listeFait.append(fait)
