import fait
import baseFait


class premisse :

	def __init__(self,fait):
		self.fait=fait
	
	def regleValide(self,BF):
		i=0
		bobol=True
		
		while  i < len(BF.listeFait) and (bobol==True):
			F1=BF.listeFait[i]
			
			if(self.fait.valeur==F1.valeur):
				bobol=False
			
			i=i+1
		if (bobol==True):
			return False
		else:
			return True

		

	
