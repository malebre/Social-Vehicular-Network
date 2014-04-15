import libxml2
from libxml2 import xmlAttr
from fonctionLocal2 import intersect


#recuperation des infos des vehicules
##################################################################################

#Avec connaissance locale

##################################################################################

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs "))
identite= map(xmlAttr.getContent,ctxt.xpathEval("//@id"))

##################################################################################

#Sans connaissance

##################################################################################

doc2=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt2=doc2.xpathNewContext()
durationWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@duration"))
fuelWO=map(xmlAttr.getContent,ctxt2.xpathEval("//@fuel_abs "))
identiteWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@id"))

##################################################################################

#Avec toute ka connaissance

##################################################################################

doc3=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt3=doc3.xpathNewContext()
durationAll= map(xmlAttr.getContent,ctxt3.xpathEval("//@duration"))
fuelAll=map(xmlAttr.getContent,ctxt3.xpathEval("//@fuel_abs "))
identiteAll= map(xmlAttr.getContent,ctxt3.xpathEval("//@id"))

##################################################################################

#Initialisation

##################################################################################

#Liste des vehicules ayant ete reroutes 

ListVehicleGreen=sys.argv[1]
ListVehicleQuick=sys.argv[2]
ListVehicleSmooth=sys.argv[3]
Compromis=sys.argv[4]

#energistrement de leur satisfaction (rapport des valeurs sans et avec toute l'information)

SatisfactionDurationQuick=[]
SatisfactionFuelGreen=[]
SatisfactionSmooth=[]


SatisfactionDurationQuickAll=[]
SatisfactionFuelGreenAll=[]
SatisfactionSmoothAll=[]

#Local = connaissance local
#Sans = sans connaissance
#Avec= avec toute la connaissance


##################################################################################

#Receuil des donnees

##################################################################################

for vehID in identite :
	
	#Green
	if (vehID in intersect(ListVehicleGreen,identiteAll)) :
		#Conso Local
		i=identite.index(vehID)		
		fuel[i]=float(fuel[i])
		#Conso Sans
		j=identiteWO.index(vehID)	
		fuelWO[j]=float(fuelWO[j])
		#Conso Avec
		k=identiteAll.index(vehID)	
		fuelAll[k]=float(fuelAll[k])
		#Satisfaction Conso   Sans / Local
		SatisfactionFuelGreen.append(fuelWO[j]/fuel[i])
		#Satisfaction Conso   Sans / Avec
		SatisfactionFuelGreenAll.append(fuelWO[j]/fuelAll[k])

	#Quick
	if (vehID in intersect(ListVehicleQuick,identiteAll)) :
		#Temps Local
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		#Temps Sans
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		#Temps Avec
		k=identiteAll.index(vehID)
		durationAll[k]=float(durationAll[k])	
		#Satisfaction Temps   Sans / Local
		SatisfactionDurationQuick.append(durationWO[j]/duration[i])
		#Satisfaction Temps   Sans / Avec
		SatisfactionDurationQuickAll.append(durationWO[j]/durationAll[k])	

	#Smooth	
	if (vehID in intersect(ListVehicleSmooth,identiteAll)) :
		#Conso et Temps Local
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		fuel[i]=float(fuel[i])
		#Conso et Temps Sans
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		fuelWO[j]=float(fuelWO[j])
		#Conso et Temps Avec
		k=identiteAll.index(vehID)	
		durationAll[k]=float(durationAll[k])
		fuelAll[k]=float(fuelAll[k])
		#Satisfaction Conso et Temps   Sans / Local
		#Satisfaction Conso et Temps   Sans / Avec
		r=Compromis[ListVehicleSmooth.index(vehID)]
		coeffWO=((r*durationWO[j]+(1-r)*fuelWO[j])/(r*duration[i]+(1-r)*fuel[i]))
		coeffAll=((r*durationWO[j]+(1-r)*fuelWO[j])/(r*durationAll[k]+(1-r)*fuelAll[k]))
		SatisfactionSmooth.append(coeffWO)
		SatisfactionSmoothAll.append(coeffAll)	


##################################################################################

#Moyenne geometrique des satisfactions pour la connaissance Locale

##################################################################################

#satisfaction Green Local
resultGreen=1
for satisf in SatisfactionFuelGreen:
	resultGreen=satisf*resultGreen
MeanSatisfactionGreen=1
if len(SatisfactionFuelGreen)!=0:
	MeanSatisfactionGreen=pow(resultGreen,1.0/float(len(SatisfactionFuelGreen)))
else:
	MeanSatisfactionGreen=0

#satisfaction Quick Local
resultQuick=1
for satisf in SatisfactionDurationQuick:
	resultQuick=satisf*resultQuick
MeanSatisfactionQuick=1
if len(SatisfactionDurationQuick)!=0:
	MeanSatisfactionQuick=pow(resultQuick,1.0/float(len(SatisfactionDurationQuick)))
else:
	MeanSatisfactionQuick=0

#satisfaction Smooth Local
resultSmooth=1
for satisf in SatisfactionSmooth:
	resultSmooth=satisf*resultSmooth
MeanSatisfactionSmooth=1
if len(SatisfactionSmooth)!=0:
	MeanSatisfactionSmooth=pow(resultSmooth,1.0/float(len(SatisfactionSmooth)))
else:
	MeanSatisfactionSmooth=0

##################################################################################

#Moyenne geometrique des satisfactions avec toute la connaissance

##################################################################################


#satisfaction Green Avec
resultGreenAll=1
for satisf in SatisfactionFuelGreenAll:
	resultGreenAll=satisf*resultGreenAll
MeanSatisfactionGreenAll=1
if len(SatisfactionFuelGreenAll)!=0:
	MeanSatisfactionGreenAll=pow(resultGreenAll,1.0/float(len(SatisfactionFuelGreenAll)))
else:
	MeanSatisfactionGreenAll=0

#satisfaction Quick Avec
resultQuickAll=1
for satisf in SatisfactionDurationQuickAll:
	resultQuickAll=satisf*resultQuickAll
MeanSatisfactionQuickAll=1
if len(SatisfactionDurationQuickAll)!=0:
	MeanSatisfactionQuickAll=pow(resultQuickAll,1.0/float(len(SatisfactionDurationQuickAll)))
else:
	MeanSatisfactionQuickAll=0

#satisfaction Smooth Avec
resultSmoothAll=1
for satisf in SatisfactionSmoothAll:
	resultSmoothAll=satisf*resultSmoothAll
MeanSatisfactionSmoothAll=1
if len(SatisfactionSmoothAll)!=0:
	MeanSatisfactionSmoothAll=pow(resultSmoothAll,1.0/float(len(SatisfactionSmoothAll)))
else:
	MeanSatisfactionSmoothAll=0

##################################################################################

#Moyenne geometrique des satisfactions tous les vehicules pour la connaissance Locale

##################################################################################


#satisfaction total avec la connaissance Local
Satisfaction=SatisfactionFuelGreen+SatisfactionDurationQuick+SatisfactionSmooth

result=1
for satisf in Satisfaction:
	result=satisf*result
MeanSatisfaction=1
if len(Satisfaction)!=0:
	MeanSatisfaction=pow(result,1.0/float(len(Satisfaction)))

##################################################################################

#Moyenne geometrique des satisfactions tous les vehicules avec toute la connaissance

##################################################################################


#satisfaction total avec toute la connaissance
SatisfactionAll=SatisfactionFuelGreenAll+SatisfactionDurationQuickAll+SatisfactionSmoothAll

resultAll=1
for satisf in SatisfactionAll:
	resultAll=satisf*resultAll
MeanSatisfactionAll=1
if len(SatisfactionAll)!=0:
	MeanSatisfactionAll=pow(resultAll,1.0/float(len(SatisfactionAll)))




