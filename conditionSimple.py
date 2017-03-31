from premisse import premisse
import fait

class conditionSimple (premisse): # heritage: 

	def __init__(self, fait):
		premisse.__init__(self, fait)

	#l'affichage
	def out(self):
		self.fait.out()
	