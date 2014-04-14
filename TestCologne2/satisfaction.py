import libxml2
from libxml2 import xmlAttr
from fonctionLocal2 import intersect

#recuperation des temps de trajet des vehicules arrivees avec information partielle

doc=libxml2.parseFile("data/maptripinfoLocal.out.xml")
ctxt=doc.xpathNewContext()
duration= map(xmlAttr.getContent,ctxt.xpathEval("//@duration"))
fuel=map(xmlAttr.getContent,ctxt.xpathEval("//@fuel_abs "))
identite= map(xmlAttr.getContent,ctxt.xpathEval("//@id"))

#recuperation des temps de trajet des memes vehicules sans information

doc2=libxml2.parseFile("data/maptripinfoWO.out.xml")
ctxt2=doc2.xpathNewContext()
durationWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@duration"))
fuelWO=map(xmlAttr.getContent,ctxt2.xpathEval("//@fuel_abs "))
identiteWO= map(xmlAttr.getContent,ctxt2.xpathEval("//@id"))


#recuperation des temps de trajet des memes vehicules avec toute l'info

doc3=libxml2.parseFile("data/maptripinfo.out.xml")
ctxt3=doc3.xpathNewContext()
durationAll= map(xmlAttr.getContent,ctxt3.xpathEval("//@duration"))
fuelAll=map(xmlAttr.getContent,ctxt3.xpathEval("//@fuel_abs "))
identiteAll= map(xmlAttr.getContent,ctxt3.xpathEval("//@id"))

#Liste des vehicules ayant ete reroutes 

ListVehicleGreen=sys.argv[1]
ListVehicleQuick=sys.argv[2]
ListSmooth=sys.argv[3]

ListVehicleSmooth=[]
ListVehicleSmoothChoice=[]
for s in ListSmooth:
	ListVehicleSmooth.append(s[0])
	ListVehicleSmoothChoice.append(s[1])


#energistrement de leur satisfaction (rapport des temps sans et avec information)


SatisfactionDurationQuick=[]
SatisfactionFuelGreen=[]
SatisfactionSmooth=[]


SatisfactionDurationQuickAll=[]
SatisfactionFuelGreenAll=[]
SatisfactionSmoothAll=[]



for vehID in identite :
	if (vehID in intersect(ListVehicleGreen,identiteAll)) :
		i=identite.index(vehID)		
		fuel[i]=float(fuel[i])
		j=identiteWO.index(vehID)	
		fuelWO[j]=float(fuelWO[j])
		k=identiteAll.index(vehID)	
		fuelAll[k]=float(fuelAll[k])
		SatisfactionFuelGreen.append(fuelWO[j]/fuel[i])
		SatisfactionFuelGreenAll.append(fuelWO[j]/fuelAll[k])
	if (vehID in intersect(ListVehicleQuick,identiteAll)) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		k=identiteAll.index(vehID)
		durationAll[k]=float(durationAll[k])	
		SatisfactionDurationQuick.append(durationWO[j]/duration[i])
		SatisfactionDurationQuickAll.append(durationWO[j]/durationAll[k])		
	if (vehID in intersect(ListVehicleSmooth,identiteAll)) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		fuel[i]=float(fuel[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		fuelWO[j]=float(fuelWO[j])
		k=identiteAll.index(vehID)	
		durationAll[k]=float(durationAll[k])
		fuelAll[k]=float(fuelAll[k])
		r=ListVehicleSmoothChoice[ListVehicleSmooth.index(vehID)]
		coeffWO=((r*durationWO[j]+(1-r)*fuelWO[j])/(r*duration[i]+(1-r)*fuel[i]))
		coeffAll=((r*durationWO[j]+(1-r)*fuelWO[j])/(r*durationAll[k]+(1-r)*fuelAll[k]))
		SatisfactionSmooth.append(coeffWO)
		SatisfactionSmoothAll.append(coeffAll)	

#on calcule la moyenne geometrique des satisfactions
Satisfaction=SatisfactionFuelGreen+SatisfactionDurationQuick+SatisfactionSmooth
SatisfactionAll=SatisfactionFuelGreenAll+SatisfactionDurationQuickAll+SatisfactionSmoothAll

resultGreen=1
for satisf in SatisfactionFuelGreen:
	resultGreen=satisf*resultGreen
MeanSatisfactionGreen=1
if len(SatisfactionFuelGreen)!=0:
	MeanSatisfactionGreen=pow(resultGreen,1.0/float(len(SatisfactionFuelGreen)))

resultQuick=1
for satisf in SatisfactionDurationQuick:
	resultQuick=satisf*resultQuick
MeanSatisfactionQuick=1
if len(SatisfactionDurationQuick)!=0:
	MeanSatisfactionQuick=pow(resultQuick,1.0/float(len(SatisfactionDurationQuick)))

resultSmooth=1
for satisf in SatisfactionSmooth:
	resultSmooth=satisf*resultSmooth
MeanSatisfactionSmooth=1
if len(SatisfactionSmooth)!=0:
	MeanSatisfactionSmooth=pow(resultSmooth,1.0/float(len(SatisfactionSmooth)))





resultGreenAll=1
for satisf in SatisfactionFuelGreenAll:
	resultGreenAll=satisf*resultGreenAll
MeanSatisfactionGreenAll=1
if len(SatisfactionFuelGreenAll)!=0:
	MeanSatisfactionGreenAll=pow(resultGreenAll,1.0/float(len(SatisfactionFuelGreenAll)))

resultQuickAll=1
for satisf in SatisfactionDurationQuickAll:
	resultQuickAll=satisf*resultQuickAll
MeanSatisfactionQuickAll=1
if len(SatisfactionDurationQuickAll)!=0:
	MeanSatisfactionQuickAll=pow(resultQuickAll,1.0/float(len(SatisfactionDurationQuickAll)))

resultSmoothAll=1
for satisf in SatisfactionSmoothAll:
	resultSmoothAll=satisf*resultSmoothAll
MeanSatisfactionSmoothAll=1
if len(SatisfactionSmoothAll)!=0:
	MeanSatisfactionSmoothAll=pow(resultSmoothAll,1.0/float(len(SatisfactionSmoothAll)))









