import regle

class baseRegle:

	def __init__(self):
		self.listeRegle=[]

	#l'affichage
	def out(self):
		print("\n-------------BR------------")
		for element in self.listeRegle:
			element.out()

		#print("\n-------------------")

	#Ajouter une regle a la base
	def chargerBR(self, regle): 
		self.listeRegle.append(regle)