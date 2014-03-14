import libxml2
from libxml2 import xmlAttr

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

#Liste des vehicules ayant ete reroutes 

ListVehicleGreen=sys.argv[1]
ListVehicleQuick=sys.argv[2]
ListSmooth=sys.argv[3]

ListVehicleSmooth=[]
ListVehicleSmoothChoice=[]
for smooth in ListSmooth:
	ListVehicleSmooth.append(smooth[0])
	ListVehicleSmoothChoice.append(smooth[1])


#energistrement de leur satisfaction (rapport des temps sans et avec information)


SatisfactionDurationQuick=[]
SatisfactionFuelGreen=[]
SatisfactionSmooth=[]



for vehID in identite :
	if (vehID in ListVehicleGreen) :
		i=identite.index(vehID)		
		fuel[i]=float(fuel[i])
		j=identiteWO.index(vehID)	
		fuelWO[j]=float(fuelWO[j])
		SatisfactionFuelGreen.append(fuelWO[j]/fuel[i])
	if (vehID in ListVehicleQuick) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		SatisfactionDurationQuick.append(durationWO[j]/duration[i])	
	if (vehID in ListVehicleSmooth) :
		i=identite.index(vehID)		
		duration[i]=float(duration[i])
		fuel[i]=float(fuel[i])
		j=identiteWO.index(vehID)	
		durationWO[j]=float(durationWO[j])
		fuelWO[j]=float(fuelWO[j])
		r=ListVehicleSmoothChoice[ListVehicleSmooth.index(vehID)]
		coeff=((r*durationWO[j]+(1-r)*fuelWO[j])/(r*duration[i]+(1-r)*fuel[i]))
		SatisfactionSmooth.append(coeff)	

#on calcule la moyenne geometrique des satisfactions
Satisfaction=SatisfactionFuelGreen+SatisfactionDurationQuick+SatisfactionSmooth
result=1
for satisf in Satisfaction:
	result=satisf*result

MeanSatisfaction=pow(result,1.0/float(len(Satisfaction)))





