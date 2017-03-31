from MI import MI
import fait
import baseFait
from conclusion import conclusion
import regle
from baseRegle import baseRegle
from conditionSimple import conditionSimple

##########la classe Fait ############
# instancier les faits
f1=fait.fait("F1","A")
f2=fait.fait("F2","B")
f3=fait.fait("F3","C")
f4=fait.fait("F4","D")
f5=fait.fait("F5","E")

#afficher un fait
f1.out()

##########la classe baseFait ############
#insctancier la base des faits
BF=baseFait.baseFait()

#ajouter des faits a la base
BF.chargerBF(f1)
BF.chargerBF(f2)

#afficher la base
print("la base des faits: ")
BF.out()
###########la classe Premisse ############ 

#instancier une premisee
prem1=conditionSimple(f1)
prem2=conditionSimple(f3)
prem1.out()

#reglevalide
res=prem1.regleValide(BF)
print()
print(res)

###########la classe conclusion ############ 

#instancier une premisee
cl1=conclusion([f3,f2])
cl2=conclusion([f5])
cl1.out()

############la classe regle #############
R1=regle.regle("R1", prem1 , cl1)
R2=regle.regle("R2", prem2 , cl2)
print("une regle R1:")
R1.out()

############la classe base des regles #############
BR=baseRegle()
BR.chargerBR(R1)
BR.chargerBR(R2)

print("la base des regles")
BR.out()

############# MI ########################
proj=MI("monProj", BF, BR)
RA=proj.reglesApplicables()

print("les régles applicables: ")
for element in RA:
	element.out()


resultat=proj.deduction()
print("resultat: ")

for element in resultat:
	element.out()