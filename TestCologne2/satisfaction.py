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

#Liste des vehicules ayant ete reroutes 

ListVehicleGreen=sys.argv[1]
ListVehicleQuick=sys.argv[2]
ListVehicleSmooth=sys.argv[3]
Compromis=sys.argv[4]




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
		r=Compromis[ListVehicleSmooth.index(vehID)]
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
else:
	MeanSatisfactionGreen=0
resultQuick=1
for satisf in SatisfactionDurationQuick:
	resultQuick=satisf*resultQuick
MeanSatisfactionQuick=1
if len(SatisfactionDurationQuick)!=0:
	MeanSatisfactionQuick=pow(resultQuick,1.0/float(len(SatisfactionDurationQuick)))
else:
	MeanSatisfactionQuick=0

resultSmooth=1
for satisf in SatisfactionSmooth:
	resultSmooth=satisf*resultSmooth
MeanSatisfactionSmooth=1
if len(SatisfactionSmooth)!=0:
	MeanSatisfactionSmooth=pow(resultSmooth,1.0/float(len(SatisfactionSmooth)))
else:
	MeanSatisfactionSmooth=0





resultGreenAll=1
for satisf in SatisfactionFuelGreenAll:
	resultGreenAll=satisf*resultGreenAll
MeanSatisfactionGreenAll=1
if len(SatisfactionFuelGreenAll)!=0:
	MeanSatisfactionGreenAll=pow(resultGreenAll,1.0/float(len(SatisfactionFuelGreenAll)))
else:
	MeanSatisfactionGreenAll=0

resultQuickAll=1
for satisf in SatisfactionDurationQuickAll:
	resultQuickAll=satisf*resultQuickAll
MeanSatisfactionQuickAll=1
if len(SatisfactionDurationQuickAll)!=0:
	MeanSatisfactionQuickAll=pow(resultQuickAll,1.0/float(len(SatisfactionDurationQuickAll)))
else:
	MeanSatisfactionQuickAll=0

resultSmoothAll=1
for satisf in SatisfactionSmoothAll:
	resultSmoothAll=satisf*resultSmoothAll
MeanSatisfactionSmoothAll=1
if len(SatisfactionSmoothAll)!=0:
	MeanSatisfactionSmoothAll=pow(resultSmoothAll,1.0/float(len(SatisfactionSmoothAll)))
else:
	MeanSatisfactionSmoothAll=0



result=1
for satisf in Satisfaction:
	result=satisf*result
MeanSatisfaction=1
if len(Satisfaction)!=0:
	MeanSatisfaction=pow(result,1.0/float(len(Satisfaction)))

resultAll=1
for satisf in SatisfactionAll:
	resultAll=satisf*resultAll
MeanSatisfactionAll=1
if len(SatisfactionAll)!=0:
	MeanSatisfactionAll=pow(resultAll,1.0/float(len(SatisfactionAll)))




