import fait

class conclusion:

	def __init__(self, listeFait):
		self.listeFait=listeFait

	#pour l'affichage
	def out(self):
		
		for element in self.listeFait:
			element.out()
			#print(" et ",end='')

		print("\n------------------------------------")
			