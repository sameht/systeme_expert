import premisse
import conclusion

class regle:

	def __init__(self, nom, condition, production):
		self.nom=nom
		self.condition=condition #premisse
		self.production=production #conclusion

	#pour l'affichage
	#pour l'affichage
	def out(self):
		print(str(self.nom)+": ",end='')
		self.condition.out()
		print(" ===> ",end='')
		self.production.out()