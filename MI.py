import baseRegle
import baseFait
#// comments
class MI:

	def __init__(self, nom, BF, BR):
		self.nom=nom
		self.BF=BF
		self.BR=BR
		self.Resultat=[]

	#determiner tout les règles applicables
	def reglesApplicables(self):
		RA=[]
		i=0
		for element in self.BR.listeRegle:
		
			if(element.condition.regleValide(self.BF)):
				RA.append(element)
		return RA


	def deduction(self):
		RA=self.reglesApplicables()    # determiner les régles applicables
		while (len(RA)>0):
			R1=RA[0]         #choisir la première regle applicable
			for elt in R1.production.listeFait:
				self.BF.listeFait.append(elt ) # ajouter la conclusion a la bF et resultat
				self.Resultat.append(elt )
			
			self.BR.listeRegle.remove(R1)         # supprimer R1 de BR
			RA=self.reglesApplicables()       # determiner les régles applicables

		return self.Resultat